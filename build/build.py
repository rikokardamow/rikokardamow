"""Draw the profile's crude stocks chart and 3D model from EIA weekly data.

Run from anywhere after a Weekly Petroleum Status Report:

    EIA_API_KEY=... python3 build/build.py

Without a key it rebuilds from the cached CSV in build/data/. It writes
assets/stocks-light.svg, assets/stocks-dark.svg and assets/us-crude-stocks.stl,
and rewrites the blocks between <!-- name --> and <!-- /name --> in README.md.
Standard library only, so it runs on any Python 3.10 or later.

Data: EIA series WCESTUS1, US ending stocks of crude oil excluding the SPR,
thousand barrels, weekly. Public domain.
"""

import csv
import itertools
import json
import math
import os
import re
import struct
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "build" / "data" / "wcestus1.csv"
ASSETS = ROOT / "assets"
README = ROOT / "README.md"
URL = "https://api.eia.gov/v2/petroleum/stoc/wstk/data/"
SERIES = "WCESTUS1"

MODEL_YEARS = (2010, 2025)  # full years only, so the model is a closed solid
MODEL_FLOOR = 250  # mb; height in the model is stocks above this
MINUS = "−"

# Kardamow house style (energy-forecasting house_style.TOKENS), with dark steps
# chosen for GitHub's dark page. No red or green; text never wears a series colour.
THEMES = {
    "light": {
        "page": "#FFFFFF",
        "text": "#0B1F3A",
        "muted": "#5B6878",
        "grid": "#DCE3EC",
        "band": "#E6ECF4",
        "average": "#93A5BB",
        "last_year": "#5B6878",
        "current": "#1F5FBF",
    },
    "dark": {
        "page": "#0D1117",
        "text": "#E6EDF3",
        "muted": "#9198A1",
        "grid": "#262C36",
        "band": "#17243A",
        "average": "#4A6489",
        "last_year": "#8B949E",
        "current": "#6CA0F0",
    },
}
FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"


# ---------------------------------------------------------------- data


def fetch(key):
    """Every weekly print of WCESTUS1 as [(date, thousand barrels)], oldest first."""
    rows, offset = [], 0
    while True:
        query = urllib.parse.urlencode(
            {
                "api_key": key,
                "frequency": "weekly",
                "data[0]": "value",
                "facets[series][]": SERIES,
                "sort[0][column]": "period",
                "sort[0][direction]": "asc",
                "offset": offset,
                "length": 5000,
            }
        )
        with urllib.request.urlopen(URL + "?" + query, timeout=60) as resp:
            body = json.load(resp)["response"]
        page = body["data"]
        rows += page
        offset += len(page)
        if not page or offset >= int(body["total"]):
            break
    return sorted((date.fromisoformat(r["period"]), int(r["value"])) for r in rows if r.get("value") is not None)


def load():
    key = os.environ.get("EIA_API_KEY")
    if key:
        series = fetch(key)
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        with CACHE.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["period", "thousand_barrels"])
            w.writerows((d.isoformat(), v) for d, v in series)
        return series
    if not CACHE.exists():
        sys.exit("No EIA_API_KEY and no cached data in build/data/; set the key and rerun.")
    with CACHE.open() as f:
        return [(date.fromisoformat(r["period"]), int(r["thousand_barrels"])) for r in csv.DictReader(f)]


def by_week(series):
    """{iso_year: {iso_week: mb}} for ISO weeks 1 to 52. Week 53 is dropped."""
    out = {}
    for d, kb in series:
        year, week, _ = d.isocalendar()
        if week <= 52:
            out.setdefault(year, {})[week] = kb / 1000
    return out


def stats(series, weeks):
    (latest, kb), (_, prev_kb) = series[-1], series[-2]
    year, week, _ = latest.isocalendar()
    week = min(week, 52)
    five = [weeks[y][week] for y in range(year - 5, year) if week in weeks.get(y, {})]
    value = kb / 1000
    return {
        "date": latest,
        "year": year,
        "week": week,
        "value": value,
        "change": value - prev_kb / 1000,
        "last_year": weeks.get(year - 1, {}).get(week),
        "avg": sum(five) / len(five),
        "lo": min(five),
        "hi": max(five),
        "first": year - 5,
        "last": year - 1,
    }


# ---------------------------------------------------------------- words


def signed(v, digits=1):
    s = f"{abs(v):,.{digits}f}"
    return ("+" if v > 0 else MINUS if v < 0 else "") + s if round(v, digits) else f"{0:.{digits}f}"


def day(d):
    return f"{d.day} {d:%b %Y}"


def headline(s):
    gap = s["value"] - s["avg"]
    if abs(gap) < 1.5:
        return "US commercial crude stocks are in line with the five-year average"
    side = "below" if gap < 0 else "above"
    return f"US commercial crude stocks are {abs(gap):.0f} mb {side} the five-year average"


def where_in_range(s):
    if s["value"] < s["lo"]:
        return f"under the whole {s['first']} to {s['last']} range for the week"
    if s["value"] > s["hi"]:
        return f"over the whole {s['first']} to {s['last']} range for the week"
    return f"inside the {s['first']} to {s['last']} range for the week"


# ---------------------------------------------------------------- chart


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path(points):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)


def dodge(labels, gap=15, top=0, bottom=10_000):
    """Push label y positions apart, keeping order, so no two are closer than `gap`."""
    labels.sort(key=lambda lab: lab["y"])
    for a, b in itertools.pairwise(labels):
        if b["y"] - a["y"] < gap:
            b["y"] = a["y"] + gap
    overflow = labels[-1]["y"] - bottom if labels else 0
    if overflow > 0:
        for lab in labels:
            lab["y"] -= overflow
    for lab in labels:
        lab["y"] = max(lab["y"], top)
    return labels


def chart(s, weeks, theme):
    c = THEMES[theme]
    W, H = 880, 448
    x0, x1, y0, y1 = 64, 716, 104, 356
    year, last = s["year"], s["year"] - 1
    span = range(s["first"], s["last"] + 1)

    band = []
    for w in range(1, 53):
        vals = [weeks[y][w] for y in span if w in weeks.get(y, {})]
        if len(vals) == len(span):
            band.append((w, min(vals), max(vals), sum(vals) / len(vals)))
    this = sorted(weeks.get(year, {}).items())
    prior = sorted(weeks.get(last, {}).items())

    every = [v for _, lo, hi, _ in band for v in (lo, hi)] + [v for _, v in this + prior]
    step = 25 if max(every) - min(every) < 160 else 50
    vmin = math.floor((min(every) - 12) / step) * step
    vmax = math.ceil((max(every) + 6) / step) * step

    def X(w):
        return x0 + (w - 1) / 51 * (x1 - x0)

    def Y(v):
        return y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)

    out = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'role="img" aria-labelledby="t d">'
        ),
        f'<title id="t">{esc(headline(s))}</title>',
        (
            f'<desc id="d">US commercial crude stocks by week of the year: {year} so far, {last}, and the '
            f"{s['first']} to {s['last']} range and average. Week ending {day(s['date'])}: "
            f"{s['value']:.1f} mb, {where_in_range(s)}.</desc>"
        ),
        "<style>",
        f"text{{font-family:{FONT};font-variant-numeric:tabular-nums;fill:{c['muted']}}}",
        f".title{{font-size:20px;font-weight:600;fill:{c['text']};letter-spacing:-.01em}}",
        ".sub{font-size:13px}",
        ".tick{font-size:11.5px}",
        ".lab{font-size:12px}",
        f".strong{{font-weight:600;fill:{c['text']}}}",
        ".foot{font-size:11px}",
        "</style>",
        f'<text class="title" x="24" y="40">{esc(headline(s))}</text>',
        (
            f'<text class="sub" x="24" y="64">mb, weekly, excluding the Strategic Petroleum Reserve. '
            f"Latest: week ending {day(s['date'])}.</text>"
        ),
    ]

    for v in range(int(vmin), int(vmax) + 1, step):
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{c["grid"]}" stroke-width="1"/>')
        out.append(f'<text class="tick" x="{x0 - 10}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    for m in range(1, 13):
        mid = date(year, m, 15).timetuple().tm_yday / 7 + 0.5
        out.append(
            f'<text class="tick" x="{X(mid):.1f}" y="{y1 + 22}" text-anchor="middle">{date(year, m, 1):%b}</text>'
        )

    upper = [(X(w), Y(hi)) for w, _, hi, _ in band]
    lower = [(X(w), Y(lo)) for w, lo, _, _ in reversed(band)]
    out.append(f'<path d="{path(upper + lower)} Z" fill="{c["band"]}"/>')
    out.append(
        f'<path d="{path([(X(w), Y(a)) for w, _, _, a in band])}" fill="none" stroke="{c["average"]}" stroke-width="1.5"/>'
    )
    out.append(
        f'<path d="{path([(X(w), Y(v)) for w, v in prior])}" fill="none" stroke="{c["last_year"]}" '
        f'stroke-width="1.4" stroke-linejoin="round"/>'
    )
    out.append(
        f'<path d="{path([(X(w), Y(v)) for w, v in this])}" fill="none" '
        f'stroke="{c["current"]}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>'
    )

    # The latest print: a dot at the end of the line, its value and year beneath.
    dx, dy = X(this[-1][0]), Y(this[-1][1])
    below = s["value"] < s["avg"]
    ly = dy + 30 if below else dy - 26
    out.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="4.5" fill="{c["current"]}"/>')
    out.append(f'<text class="lab strong" x="{dx:.1f}" y="{ly:.1f}" text-anchor="middle">{s["value"]:.1f}</text>')
    out.append(f'<text class="lab" x="{dx:.1f}" y="{ly + 15:.1f}" text-anchor="middle">{year}</text>')

    # The range is named inside the band, where it is widest in the first half of the year.
    bw, _, bhi, _ = max(band[2:26], key=lambda b: b[2] - b[1])
    out.append(
        f'<text class="lab" x="{X(bw):.1f}" y="{Y(bhi) + 20:.1f}" text-anchor="middle">{s["first"]} to {s["last"]} range</text>'
    )

    # End labels at the right edge, nudged apart; none is a legend box.
    _w_end, _lo_end, _hi_end, avg_end = band[-1]
    ends = dodge(
        [
            {"y": Y(prior[-1][1]), "text": str(last), "cls": "lab strong"},
            {"y": Y(avg_end), "text": "Five-year average", "cls": "lab"},
        ],
        top=y0,
        bottom=y1,
    )
    for lab in ends:
        out.append(f'<text class="{lab["cls"]}" x="{x1 + 12}" y="{lab["y"] + 4:.1f}">{esc(lab["text"])}</text>')

    out.append(
        f'<text class="foot" x="24" y="{H - 34}">Source: US Energy Information Administration, Weekly Petroleum '
        f"Status Report, series {SERIES}. Public domain.</text>"
    )
    out.append(
        f'<text class="foot" x="24" y="{H - 16}">Range and average over {s["first"]} to {s["last"]}, '
        f"by ISO week. Drawn by build/build.py in github.com/rikokardamow/rikokardamow.</text>"
    )
    out.append("</svg>")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- model


def grid(weeks, years, bin_weeks):
    """Mean stocks (mb) per bin of weeks, one row per year; gaps filled from neighbours."""
    rows = []
    for y in years:
        row = []
        for b in range(52 // bin_weeks):
            vals = [weeks[y][w] for w in range(b * bin_weeks + 1, (b + 1) * bin_weeks + 1) if w in weeks.get(y, {})]
            row.append(sum(vals) / len(vals) if vals else None)
        for j, v in enumerate(row):
            if v is None:
                near = [u for u in row[max(0, j - 1) : j + 2] if u is not None]
                row[j] = sum(near) / len(near)
        rows.append(row)
    return rows


def solid(rows, dx, dy, kz, base):
    """Closed triangle mesh: a surface over the grid, four walls and a floor.

    x runs along the weeks, y along the years, z up. Every facet is wound so its
    normal points out of the solid.
    """
    ny, nx = len(rows), len(rows[0])
    z = [[(v - MODEL_FLOOR) * kz for v in row] for row in rows]
    X, Y = (nx - 1) * dx, (ny - 1) * dy
    cx, cy = X / 2, Y / 2
    facets = []

    def add(a, b, c, out):
        n = cross(sub(b, a), sub(c, a))
        if sum(n[k] * out[k] for k in range(3)) < 0:
            b, c = c, b
            n = [-v for v in n]
        length = math.sqrt(sum(v * v for v in n)) or 1
        facets.append(([v / length for v in n], a, b, c))

    for i in range(ny - 1):
        for j in range(nx - 1):
            p00 = (j * dx, i * dy, z[i][j])
            p10 = ((j + 1) * dx, i * dy, z[i][j + 1])
            p01 = (j * dx, (i + 1) * dy, z[i + 1][j])
            p11 = ((j + 1) * dx, (i + 1) * dy, z[i + 1][j + 1])
            add(p00, p10, p11, (0, 0, 1))
            add(p00, p11, p01, (0, 0, 1))

    def wall(edge, out):
        for a, b in itertools.pairwise(edge):
            a0, b0 = (a[0], a[1], -base), (b[0], b[1], -base)
            add(a0, b0, b, out)
            add(a0, b, a, out)

    wall([(j * dx, 0, z[0][j]) for j in range(nx)], (0, -1, 0))
    wall([(j * dx, Y, z[-1][j]) for j in range(nx)], (0, 1, 0))
    wall([(0, i * dy, z[i][0]) for i in range(ny)], (-1, 0, 0))
    wall([(X, i * dy, z[i][-1]) for i in range(ny)], (1, 0, 0))
    # The floor is a fan from its centre to every point on the walls' lower edge,
    # so each edge is shared by exactly two facets and the mesh is watertight.
    rim = (
        [(j * dx, 0) for j in range(nx)]
        + [(X, i * dy) for i in range(1, ny)]
        + [(j * dx, Y) for j in range(nx - 2, -1, -1)]
        + [(0, i * dy) for i in range(ny - 2, -1, -1)]
    )
    for (ax, ay), (bx, by) in itertools.pairwise(rim):
        add((cx, cy, -base), (ax, ay, -base), (bx, by, -base), (0, 0, -1))

    # Centre on the origin so viewers orbit the middle of the model.
    return [(n, *[(p[0] - cx, p[1] - cy, p[2]) for p in tri]) for n, *tri in facets]


def sub(a, b):
    return [a[k] - b[k] for k in range(3)]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def num(v, digits):
    s = f"{v:.{digits}f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def ascii_stl(facets, name):
    lines = [f"solid {name}"]
    for n, *tri in facets:
        lines.append("facet normal " + " ".join(num(v, 3) for v in n))
        lines.append("outer loop")
        lines += ["vertex " + " ".join(num(v, 2) for v in p) for p in tri]
        lines.append("endloop")
        lines.append("endfacet")
    lines.append(f"endsolid {name}")
    return "\n".join(lines)


def binary_stl(facets, header):
    out = bytearray(header.encode().ljust(80, b" ")[:80])
    out += struct.pack("<I", len(facets))
    for n, *tri in facets:
        out += struct.pack("<12fH", *n, *[v for p in tri for v in p], 0)
    return bytes(out)


# ---------------------------------------------------------------- README


def splice(text, name, body):
    pattern = re.compile(rf"(<!-- {name} -->\n).*?(<!-- /{name} -->)", re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"README.md has no <!-- {name} --> block")
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text, count=1)


def picture(s):
    alt = f"{headline(s)}: {s['value']:.1f} mb in the week ending {day(s['date'])}, {where_in_range(s)}."
    return (
        "<picture>\n"
        '  <source media="(prefers-color-scheme: dark)" srcset="assets/stocks-dark.svg">\n'
        f'  <img alt="{esc(alt)}" src="assets/stocks-light.svg" width="100%">\n'
        "</picture>"
    )


def table(s):
    ly = s["last_year"]
    rows = [
        ("Stocks, week ending " + day(s["date"]), f"{s['value']:.1f}"),
        ("Change on the week", signed(s["change"])),
        (f"Same week of {s['year'] - 1}", f"{ly:.1f}" if ly else "n/a"),
        (f"{s['first']} to {s['last']} average", f"{s['avg']:.1f}"),
        ("Gap to that average", signed(s["value"] - s["avg"])),
        (f"{s['first']} to {s['last']} range", f"{s['lo']:.1f} to {s['hi']:.1f}"),
    ]
    return "\n".join(["| | mb |", "|:--|--:|"] + [f"| {a} | {b} |" for a, b in rows])


def caption(series):
    """How to read the model, with its two big moves measured from the data."""
    first, last = MODEL_YEARS
    inside = [(d, kb / 1000) for d, kb in series if first <= d.year <= last]
    peak_d, peak = max(inside, key=lambda r: r[1])
    record = peak_d == max(series, key=lambda r: r[1])[0]

    def mean(year):
        vals = [v for d, v in inside if d.year == year]
        return sum(vals) / len(vals)

    return (
        f"Drag to turn it and scroll to zoom. Weeks run along the long side, January to December, "
        f"and years run across it from {first} to {last}. Height is stocks above {MODEL_FLOOR} mb. "
        f"The step up from 2014 to 2016 is the shale glut, {mean(2016) - mean(2014):.0f} mb on the yearly "
        f"average. The highest point is the week ending {day(peak_d)}, at {peak:.1f} mb"
        + (f", the most since the series began in {series[0][0].year}." if record else ".")
    )


def main():
    series = load()
    weeks = by_week(series)
    s = stats(series, weeks)

    ASSETS.mkdir(exist_ok=True)
    for theme in THEMES:
        (ASSETS / f"stocks-{theme}.svg").write_text(chart(s, weeks, theme))

    years = range(MODEL_YEARS[0], MODEL_YEARS[1] + 1)
    # Inline model: two-week bins keep the README light. File: every week.
    inline = solid(grid(weeks, years, 2), dx=6.0, dy=7.2, kz=0.33, base=9)
    full = solid(grid(weeks, years, 1), dx=3.0, dy=7.2, kz=0.33, base=9)
    name = f"us_crude_stocks_{MODEL_YEARS[0]}_{MODEL_YEARS[1]}"
    (ASSETS / "us-crude-stocks.stl").write_bytes(
        binary_stl(full, f"US crude stocks ex SPR, EIA {SERIES}, weekly {MODEL_YEARS[0]}-{MODEL_YEARS[1]}")
    )

    text = README.read_text()
    text = splice(text, "stocks:chart", picture(s))
    text = splice(text, "stocks:table", table(s))
    text = splice(text, "stocks:model", caption(series) + "\n\n```stl\n" + ascii_stl(inline, name) + "\n```")
    text = splice(
        text,
        "built",
        f"<sub>Chart and model drawn by <code>build/build.py</code> from EIA data, last built for the "
        f"week ending {day(s['date'])}.</sub>",
    )
    README.write_text(text)
    print(f"{headline(s)}. {s['value']:.1f} mb, week ending {day(s['date'])}; {len(inline)} facets inline.")


if __name__ == "__main__":
    main()
