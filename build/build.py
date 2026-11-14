"""Draw the profile's crude stocks chart from EIA weekly data, and refresh the gallery.

Run from anywhere after a Weekly Petroleum Status Report:

    EIA_API_KEY=... python3 build/build.py             # the stocks chart and its table
    EIA_API_KEY=... python3 build/build.py --gallery   # also copy the gallery charts in

Without a key it rebuilds from the cached CSV in build/data/. It writes
assets/stocks-light.svg and assets/stocks-dark.svg, and rewrites the blocks between
<!-- name --> and <!-- /name --> in README.md. The gallery charts are drawn in the
other repositories (see GALLERY); --gallery copies the current ones into
assets/gallery/. Standard library only, so it runs on any Python 3.10 or later.

Data: EIA series WCESTUS1, US ending stocks of crude oil excluding the SPR,
thousand barrels, weekly. Public domain.
"""

import csv
import itertools
import json
import math
import os
import re
import shutil
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


# ---------------------------------------------------------------- gallery

# Each gallery chart, where it is drawn, and its data licence. The private
# energy-forecasting charts are copied from disk; the public repos from GitHub.
EF = Path(os.environ.get("ENERGY_FORECASTING", Path.home() / "energy-forecasting"))
REF = EF / "docs" / "chartbook" / "reference"
RAW = "https://raw.githubusercontent.com/rikokardamow"
GALLERY = {
    "balance-waterfall.png": (REF / "A32_weekly_balance_waterfall.png", "EIA, public domain"),
    "regional-stocks.png": (REF / "A08_padd_cushing_small_multiples.png", "EIA, public domain"),
    "inventory-clock.png": ("chartbook:E5", "EIA, public domain"),
    "abnormal-weeks.png": ("chartbook:E6", "EIA, public domain"),
    "hidden-balance.png": ("chartbook:E7", "EIA, public domain"),
    "wti-positioning.png": (REF / "A17_wti_positioning_public.png", "CFTC, public domain"),
    "cushing.png": (REF / "A44_cushing_vs_recent_low.png", "EIA, public domain"),
    "heating-degree-days.png": (REF / "A45_hdd_anomaly_map.png", "NOAA, public domain"),
    "dk1-imbalance.png": (f"{RAW}/nordcast/main/notebooks/01_look.png", "Energinet, CC BY 4.0"),
    "dk1-replay.png": (f"{RAW}/nordcast/main/replay/mae_by_round.png", "Energinet, CC BY 4.0"),
    "ie-technology.png": (
        f"{RAW}/ie-grid-pipeline/main/docs/img/technology.png",
        "EirGrid and ESB Networks, with permission",
    ),
    "ie-history.png": (f"{RAW}/ie-grid-pipeline/main/docs/img/history.png", "EirGrid, with permission"),
    "ie-map.png": (f"{RAW}/ie-grid-pipeline/main/docs/img/map.png", "EirGrid, ESB Networks and OpenStreetMap"),
}


def chartbook(exhibit):
    """The newest public chart book page for an exhibit, e.g. E5."""
    pages = sorted((EF / ".local" / "chartbook" / "book").glob(f"*/public/{exhibit}.png"))
    return pages[-1] if pages else None


def gallery():
    out = ASSETS / "gallery"
    out.mkdir(parents=True, exist_ok=True)
    for name, (source, licence) in GALLERY.items():
        if isinstance(source, str) and source.startswith("chartbook:"):
            source = chartbook(source.split(":", 1)[1])
        if isinstance(source, str):
            with urllib.request.urlopen(source, timeout=60) as resp:
                (out / name).write_bytes(resp.read())
        elif source and source.exists():
            shutil.copyfile(source, out / name)
        else:
            print(f"kept the old {name}: no source on this machine")
            continue
        print(f"{name:<24} {licence}")


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


def main():
    series = load()
    weeks = by_week(series)
    s = stats(series, weeks)

    ASSETS.mkdir(exist_ok=True)
    for theme in THEMES:
        (ASSETS / f"stocks-{theme}.svg").write_text(chart(s, weeks, theme))
    if "--gallery" in sys.argv[1:]:
        gallery()

    text = README.read_text()
    text = splice(text, "stocks:chart", picture(s))
    text = splice(text, "stocks:table", table(s))
    text = splice(
        text,
        "built",
        f"<sub>Stocks chart drawn by <code>build/build.py</code> from EIA data, last built for the "
        f"week ending {day(s['date'])}. The other charts come from the repositories named beside them.</sub>",
    )
    README.write_text(text)
    print(f"{headline(s)}. {s['value']:.1f} mb, week ending {day(s['date'])}.")


if __name__ == "__main__":
    main()
