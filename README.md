### Hi, I'm Riko

I write [Kardamow](https://kardamow.com), an independent research publication on energy markets, and I build the data tools I need to do it. Mostly oil and gas, some power, and the geopolitics that moves both.

What I forecast is frozen and hashed before the number comes out, scored against the first print, and kept when it misses.

<details>
<summary>How I came to this</summary>

<br>

I came to this from finance and data work, where much of the job was cleaning numbers. That taught me to trust a number only once I have seen where it came from. I studied management at UCD Smurfit and I am now doing a part-time MSc in Energy Economics and Finance at the University of Aberdeen. In the evenings I turn public data into something I can test.

</details>

<!-- stocks:chart -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stocks-dark.svg">
  <img alt="US commercial crude stocks are 19 mb below the five-year average: 414.4 mb in the week ending 6 Nov 2026, under the whole 2021 to 2025 range for the week." src="assets/stocks-light.svg" width="100%">
</picture>

*Figure: US commercial crude stocks are 19 mb below the five-year average. Stocks by ISO week excluding the Strategic Petroleum Reserve: 2026 so far, 2025, and the 2021 to 2025 range and average. Units: mb; weekly. Source: US Energy Information Administration, Weekly Petroleum Status Report, series WCESTUS1; public domain; as of 2026-11-06.*
<!-- /stocks:chart -->

<details>
<summary>The numbers behind the chart</summary>

<br>

<!-- stocks:table -->
| | mb |
|:--|--:|
| Stocks, week ending 6 Nov 2026 | 414.4 |
| Change on the week | +4.7 |
| Same week of 2025 | 427.6 |
| 2021 to 2025 average | 433.0 |
| Gap to that average | −18.6 |
| 2021 to 2025 range | 427.6 to 439.4 |
<!-- /stocks:table -->

</details>

This is the series behind my weekly forecasting record for US crude stocks, with gas storage to follow. The record goes public once there are enough weeks to judge it.

#### From the weekly chart book

Pages from the public edition of the chart book I build on each EIA weekly release. Click one to open it full size.

<p>
<a href="assets/gallery/balance-waterfall.png"><img src="assets/gallery/balance-waterfall.png" width="49%" alt="Weekly US crude balance: production, imports, exports, refinery runs and the SPR, and what moved on the week"></a>
<a href="assets/gallery/regional-stocks.png"><img src="assets/gallery/regional-stocks.png" width="49%" alt="US commercial crude stocks by region, PADD 1 to 5 and Cushing, against each one's five-year range"></a>
</p>

<p>
<a href="assets/gallery/inventory-clock.png"><img src="assets/gallery/inventory-clock.png" width="49%" alt="Inventory clock: distillate days of cover against refinery utilisation over the last twelve weeks"></a>
<a href="assets/gallery/abnormal-weeks.png"><img src="assets/gallery/abnormal-weeks.png" width="49%" alt="Abnormal-week calendar: each weekly series against its same-week norm, as a z-score heatmap"></a>
</p>

<p>
<a href="assets/gallery/hidden-balance.png"><img src="assets/gallery/hidden-balance.png" width="49%" alt="The implied crude adjustment as a slow-moving level plus noise, filtered with a Kalman model"></a>
<a href="assets/gallery/wti-positioning.png"><img src="assets/gallery/wti-positioning.png" width="49%" alt="Money managers' net position in NYMEX WTI futures, from the CFTC, with open interest"></a>
</p>

<details>
<summary>Two more: Cushing, and heating demand</summary>

<br>

<p>
<a href="assets/gallery/cushing.png"><img src="assets/gallery/cushing.png" width="49%" alt="Crude stocks at Cushing, Oklahoma, against the lowest weekly level since 2015 and working capacity"></a>
<a href="assets/gallery/heating-degree-days.png"><img src="assets/gallery/heating-degree-days.png" width="49%" alt="Heating degree days by state against normal for the latest week, from NOAA"></a>
</p>

</details>

#### Projects

**[nordcast](https://github.com/rikokardamow/nordcast)** forecasts the electricity imbalance in western Denmark every quarter-hour, 15, 30 and 60 minutes ahead: which way the grid operator will have to balance, and by how many megawatts.

<p>
<a href="assets/gallery/dk1-imbalance.png"><img src="assets/gallery/dk1-imbalance.png" width="42%" alt="DK1 system imbalance and wind forecast error, one week, quarter-hourly"></a>
<a href="assets/gallery/dk1-replay.png"><img src="assets/gallery/dk1-replay.png" width="56%" alt="Replay: mean absolute error of the 15-minute call by method and round"></a>
</p>

<sub>Source: Energinet, Energi Data Service; CC BY 4.0. The replay runs on estimated data vintages and is not the live record.</sub>

<details>
<summary>How each forecast is kept</summary>

<br>

1. Written to a file before its deadline and hashed.
2. The day's hashes are timestamped with OpenTimestamps.
3. Scored against the first figure Energinet publishes.
4. Never revised, so the misses and the missed deadlines stay in the table.

Persistence is the forecast on the record. A LightGBM challenger is frozen and scored on the same terms, and it can only take over by passing a test set out in advance, not before 1 April 2027. The record started on 28 October 2026.

</details>

**[ie-grid-pipeline](https://github.com/rikokardamow/ie-grid-pipeline)** keeps a record of Ireland's grid connection queue, read from every list EirGrid and ESB Networks have published since 2015. Each new list replaces the last, so without a record the history disappears.

<p>
<a href="assets/gallery/ie-technology.png"><img src="assets/gallery/ie-technology.png" width="49%" alt="Irish generation contracted to connect, by technology, transmission and distribution"></a>
<a href="assets/gallery/ie-history.png"><img src="assets/gallery/ie-history.png" width="49%" alt="Contracted capacity on Ireland's transmission grid, every list since 2015, wind and non-wind"></a>
</p>

<sub>Source: EirGrid contracted lists, Supported by EirGrid Group Data; ESB Networks DSO lists, © ESB Networks, used with their permission.</sub>

<details>
<summary>What the record shows, and where the queue sits</summary>

<br>

- 16.57 GW has signed to connect but is not connected yet. Solar is a third of it.
- 15 of the 16 wind projects that could be checked connected after their target date.
- Under the capacity auction's rules, 2.0 to 2.1 GW of the 12.0 GW with a published rating counts towards keeping the lights on, and more than half of that is gas.

Figures from the report of 30 October 2026.

<a href="assets/gallery/ie-map.png"><img src="assets/gallery/ie-map.png" width="70%" alt="Map of Ireland: contracted capacity waiting at each substation, against the 220 to 400 kV backbone"></a>

<sub>Source: EirGrid contracted lists, Supported by EirGrid Group Data; ESB Networks DSO lists, © ESB Networks, used with their permission; lines and substations © OpenStreetMap contributors (ODbL).</sub>

</details>

#### Where the work is

Click a point or a line to see what it is.

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "Project": "nordcast",
        "Forecasts": "DK1 power imbalance",
        "How often": "Every quarter-hour",
        "Horizons": "15, 30 and 60 minutes",
        "Scored on": "Energinet's first figure",
        "Since": "28 October 2026"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [9.74, 55.56]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "ie-grid-pipeline",
        "Records": "Ireland's grid connection queue",
        "Lists kept": "EirGrid and ESB Networks",
        "Since": "2015",
        "Waiting": "16.57 GW, at 30 October 2026"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-6.23, 53.33]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "US crude stocks record",
        "Forecasts": "Weekly change in crude stocks",
        "Frozen": "Before each EIA release",
        "Why Cushing": "Delivery point for WTI",
        "Status": "Private until enough weeks"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-96.77, 35.99]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "US gas storage record",
        "Status": "Next, built the same way",
        "Why Henry Hub": "Delivery point for NYMEX gas"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-92.04, 29.96]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "East West (EWIC)",
        "Links": "Co. Meath to Deeside, Wales",
        "Capacity": "500 MW, in service",
        "Line": "Straight, not the cable route"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-6.53, 53.47],
          [-3.06, 53.23]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Moyle",
        "Links": "Co. Antrim to Ayrshire",
        "Capacity": "500 MW, in service",
        "Line": "Straight, not the cable route"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-5.77, 54.83],
          [-4.95, 55.07]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Greenlink",
        "Links": "Co. Wexford to Pembroke, Wales",
        "Capacity": "500 MW, in service since 2025",
        "Line": "Straight, not the cable route"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-6.98, 52.35],
          [-4.99, 51.68]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Celtic",
        "Links": "East Cork to Brittany",
        "Capacity": "700 MW, being built",
        "Due": "Q4 2028, per EirGrid",
        "Line": "Straight, not the cable route"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-8.25, 51.93],
          [-4.16, 48.45]
        ]
      }
    }
  ]
}
```

#### What I keep coming back to

- The shape of the futures curve, and the moments when the price of physical barrels and the price of paper contracts disagree
- Sanctions, and the gap between when a policy is announced and when barrels actually move
- Pipelines, terminals and refineries as the real limit on how fast anything changes

**Tools:** Python, SQL, DuckDB, Postgres, pandas, matplotlib, Next.js. Public data from the EIA, Energinet, EirGrid, GIE, ENTSO-E and the CFTC.

**Find me** at [kardamow.com](https://kardamow.com) and [@kardamow on X](https://x.com/kardamow).

<!-- built -->
<sub>Stocks chart drawn by <code>build/build.py</code> from EIA data, last built for the week ending 6 Nov 2026. The other charts come from the repositories named beside them.</sub>
<!-- /built -->
