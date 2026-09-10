## Supply or Demand? You build.

Independent research on the seam where energy, finance and geopolitics meet — and the data platform underneath it.

Most energy commentary is either a seminar with no contact with the molecule, or a price feed with no memory. The work sits at the join: close enough to know how a barrel actually moves, far enough back to see the belief that is moving it.

[**The code**](https://github.com/rikokardamow/supply-or-demand)

---

### supply-or-demand

The platform behind the publication, open-sourced.

Roughly 1,600 series from twenty-odd primary sources — EIA, GIE, ENTSO-E, ENTSOG, CFTC, OPEC, JODI, Baker Hughes, OFAC, AIS — land in a DuckDB and Parquet lake on one laptop. A publish step promotes a serving copy to Postgres under row-level security. Two Next.js sites and a Streamlit app read it. The serving layer is a read-only API with no write path, which is why its key sits openly in the browser bundle.

[![The weekly US crude balance, and where it fails to close](https://raw.githubusercontent.com/rikokardamow/supply-or-demand/main/docs/screenshots/data-oil-math.png)](https://github.com/rikokardamow/supply-or-demand)

*The weekly crude balance and its residual. The identity is `Δ(commercial + SPR stocks) = production + imports − exports − runs + adjustment`. The adjustment is not a rounding error — EIA publishes it because the components come from different surveys — so it gets its own line rather than being absorbed silently.*

It is opinionated about correctness in ways most dashboards are not, and that is the part worth reading:

- **Seasonal maths always excludes 2020**, by rule, in one shared module — never reimplemented per page.
- **`as_of` is the data's own date, never the time the job ran.** A source that has stopped updating keeps its old `as_of` however recently it was refreshed. Both are recorded, because the difference between them is the whole signal.
- **Gaps are never bridged.** A series with no observation genuinely has none. Joining across the hole would draw a straight line through missing data as though it had been measured.
- **Colour never carries meaning alone.** Direction shows a sign as well as a hue, and the heat wash is balanced by measurement rather than by eye — so a build is exactly as visible as a draw.
- **Failures are loud.** A partial run exits non-zero instead of reporting success, and credentials are redacted from exception text before it is ever printed.

MIT for the code. The data is not the project's to relicense — every source keeps its own terms, and several restrict commercial use.

---

### The three questions

**Crude and gas structure.** Backwardation, contango, and the term-structure dislocations that mark where the physical market disagrees with paper. Crack spreads tell you what the market expects; run cuts tell you what refiners actually believe. When the two detach, take the run cut — a refiner who pulls throughput has voted with a plant, not a forecast.

**Sanctions and the enforcement gap.** Policy moves the molecule on a lag and the market prices the policy on the day. The distance between those two clocks is where a regime is either enforced or quietly routed around, so track the workaround rather than the designation.

**Infrastructure as the binding constraint.** Pipeline and export-terminal capacity, and the basis differentials that appear when ambition outruns steel. Steel is slower than capital and capital is slower than belief, so every transition story eventually becomes a bottleneck story — and the bottleneck, once it binds, sets the price for everything queued behind it.

---

Reachable through [the repository](https://github.com/rikokardamow/supply-or-demand/issues).
