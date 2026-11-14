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

#### Projects

**[nordcast](https://github.com/rikokardamow/nordcast)** forecasts the electricity imbalance in western Denmark every quarter-hour, 15, 30 and 60 minutes ahead: which way the grid operator will have to balance, and by how many megawatts.

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

<details>
<summary>What the record shows</summary>

<br>

- 16.57 GW has signed to connect but is not connected yet. Solar is a third of it.
- 15 of the 16 wind projects that could be checked connected after their target date.
- Under the capacity auction's rules, 2.0 to 2.1 GW of the 12.0 GW with a published rating counts towards keeping the lights on, and more than half of that is gas.

Figures from the report of 30 October 2026.

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
        "Forecast": "DK1 power imbalance, every quarter-hour, 15, 30 and 60 minutes ahead",
        "Scored against": "Energinet's first published figure",
        "Record since": "28 October 2026",
        "marker-color": "#1F5FBF"
      },
      "geometry": { "type": "Point", "coordinates": [9.74, 55.56] }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "ie-grid-pipeline",
        "Record": "Every EirGrid and ESB Networks connection list since 2015",
        "Waiting to connect": "16.57 GW (report of 30 October 2026)",
        "marker-color": "#1F5FBF"
      },
      "geometry": { "type": "Point", "coordinates": [-6.23, 53.33] }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "US crude stocks record",
        "Forecast": "Weekly change in US commercial crude stocks, frozen before the EIA release",
        "Why Cushing": "The delivery point for WTI; the record covers all US commercial stocks",
        "Status": "Private until there are enough weeks to judge it",
        "marker-color": "#0F2A4A"
      },
      "geometry": { "type": "Point", "coordinates": [-96.77, 35.99] }
    },
    {
      "type": "Feature",
      "properties": {
        "Project": "US gas storage record",
        "Status": "Next, built the same way",
        "Why Henry Hub": "The delivery point for NYMEX natural gas, at Erath, Louisiana",
        "marker-color": "#7D8996"
      },
      "geometry": { "type": "Point", "coordinates": [-92.04, 29.96] }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "East West (EWIC)",
        "Links": "Woodland, Co. Meath to Deeside, Wales",
        "Capacity": "500 MW, in service",
        "Drawn as": "A straight line between converter stations, not the cable route",
        "stroke": "#5B6878",
        "stroke-width": 2
      },
      "geometry": { "type": "LineString", "coordinates": [[-6.53, 53.47], [-3.06, 53.23]] }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Moyle",
        "Links": "Islandmagee, Co. Antrim to Auchencrosh, Ayrshire",
        "Capacity": "500 MW, in service",
        "Drawn as": "A straight line between converter stations, not the cable route",
        "stroke": "#5B6878",
        "stroke-width": 2
      },
      "geometry": { "type": "LineString", "coordinates": [[-5.77, 54.83], [-4.95, 55.07]] }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Greenlink",
        "Links": "Great Island, Co. Wexford to Pembroke, Wales",
        "Capacity": "500 MW, in commercial operation since early 2025",
        "Drawn as": "A straight line between converter stations, not the cable route",
        "stroke": "#5B6878",
        "stroke-width": 2
      },
      "geometry": { "type": "LineString", "coordinates": [[-6.98, 52.35], [-4.99, 51.68]] }
    },
    {
      "type": "Feature",
      "properties": {
        "Interconnector": "Celtic",
        "Links": "Ballyadam, east Cork to La Martyre, Brittany",
        "Capacity": "700 MW, under construction; EirGrid expects commissioning in Q4 2028",
        "Drawn as": "A straight line between converter stations, not the cable route",
        "stroke": "#93A5BB",
        "stroke-width": 2
      },
      "geometry": { "type": "LineString", "coordinates": [[-8.25, 51.93], [-4.16, 48.45]] }
    }
  ]
}
```

#### US crude stocks, 2010 to 2025, as an object

<!-- stocks:model -->
Drag to turn it and scroll to zoom. Weeks run along the long side, January to December, and years run across it from 2010 to 2025. Height is stocks above 250 mb. The step up from 2014 to 2016 is the shale glut, 144 mb on the yearly average. The highest point is the week ending 19 Jun 2020, at 540.7 mb, the most since the series began in 1982.

```stl
solid us_crude_stocks_2010_2025
facet normal -0.048 -0.348 0.936
outer loop
vertex -48 -30 7.21
vertex -41.6 -30 7.54
vertex -41.6 -27.6 8.43
endloop
endfacet
facet normal -0.237 0.142 0.961
outer loop
vertex -48 -30 7.21
vertex -41.6 -27.6 8.43
vertex -48 -27.6 6.85
endloop
endfacet
facet normal 0.101 -0.192 0.976
outer loop
vertex -41.6 -30 7.54
vertex -35.2 -30 6.88
vertex -35.2 -27.6 7.35
endloop
endfacet
facet normal 0.156 -0.344 0.926
outer loop
vertex -41.6 -30 7.54
vertex -35.2 -27.6 7.35
vertex -41.6 -27.6 8.43
endloop
endfacet
facet normal -0.417 -0.233 0.878
outer loop
vertex -35.2 -30 6.88
vertex -28.8 -30 9.92
vertex -28.8 -27.6 10.56
endloop
endfacet
facet normal -0.441 -0.173 0.881
outer loop
vertex -35.2 -30 6.88
vertex -28.8 -27.6 10.56
vertex -35.2 -27.6 7.35
endloop
endfacet
facet normal 0.18 -0.018 0.984
outer loop
vertex -28.8 -30 9.92
vertex -22.4 -30 8.75
vertex -22.4 -27.6 8.79
endloop
endfacet
facet normal 0.257 -0.248 0.934
outer loop
vertex -28.8 -30 9.92
vertex -22.4 -27.6 8.79
vertex -28.8 -27.6 10.56
endloop
endfacet
facet normal -0.377 -0.604 0.702
outer loop
vertex -22.4 -30 8.75
vertex -16 -30 12.18
vertex -16 -27.6 14.24
endloop
endfacet
facet normal -0.648 -0.014 0.761
outer loop
vertex -22.4 -30 8.75
vertex -16 -27.6 14.24
vertex -22.4 -27.6 8.79
endloop
endfacet
facet normal -0.841 -0.315 0.441
outer loop
vertex -16 -30 12.18
vertex -9.6 -30 24.38
vertex -9.6 -27.6 26.09
endloop
endfacet
facet normal -0.814 -0.378 0.44
outer loop
vertex -16 -30 12.18
vertex -9.6 -27.6 26.09
vertex -16 -27.6 14.24
endloop
endfacet
facet normal -0.481 -0.299 0.824
outer loop
vertex -9.6 -30 24.38
vertex -3.2 -30 28.11
vertex -3.2 -27.6 28.98
endloop
endfacet
facet normal -0.345 -0.545 0.764
outer loop
vertex -9.6 -30 24.38
vertex -3.2 -27.6 28.98
vertex -9.6 -27.6 26.09
endloop
endfacet
facet normal 0.787 0.034 0.616
outer loop
vertex -3.2 -30 28.11
vertex 3.2 -30 19.93
vertex 3.2 -27.6 19.8
endloop
endfacet
facet normal 0.803 -0.203 0.56
outer loop
vertex -3.2 -30 28.11
vertex 3.2 -27.6 19.8
vertex -3.2 -27.6 28.98
endloop
endfacet
facet normal -0.367 -0.311 0.877
outer loop
vertex 3.2 -30 19.93
vertex 9.6 -30 22.61
vertex 9.6 -27.6 23.46
endloop
endfacet
facet normal -0.496 0.048 0.867
outer loop
vertex 3.2 -30 19.93
vertex 9.6 -27.6 23.46
vertex 3.2 -27.6 19.8
endloop
endfacet
facet normal 0.159 -0.005 0.987
outer loop
vertex 9.6 -30 22.61
vertex 16 -30 21.57
vertex 16 -27.6 21.59
endloop
endfacet
facet normal 0.266 -0.322 0.909
outer loop
vertex 9.6 -30 22.61
vertex 16 -27.6 21.59
vertex 9.6 -27.6 23.46
endloop
endfacet
facet normal -0.688 0.276 0.672
outer loop
vertex 16 -30 21.57
vertex 22.4 -30 28.13
vertex 22.4 -27.6 27.14
endloop
endfacet
facet normal -0.655 -0.004 0.755
outer loop
vertex 16 -30 21.57
vertex 22.4 -27.6 27.14
vertex 16 -27.6 21.59
endloop
endfacet
facet normal 0.797 -0.063 0.6
outer loop
vertex 22.4 -30 28.13
vertex 28.8 -30 19.63
vertex 28.8 -27.6 19.88
endloop
endfacet
facet normal 0.724 0.263 0.638
outer loop
vertex 22.4 -30 28.13
vertex 28.8 -27.6 19.88
vertex 22.4 -27.6 27.14
endloop
endfacet
facet normal -0.473 -0.284 0.834
outer loop
vertex 28.8 -30 19.63
vertex 35.2 -30 23.26
vertex 35.2 -27.6 24.07
endloop
endfacet
facet normal -0.546 -0.088 0.833
outer loop
vertex 28.8 -30 19.63
vertex 35.2 -27.6 24.07
vertex 28.8 -27.6 19.88
endloop
endfacet
facet normal 0.208 0.433 0.877
outer loop
vertex 35.2 -30 23.26
vertex 41.6 -30 21.74
vertex 41.6 -27.6 20.56
endloop
endfacet
facet normal 0.462 -0.286 0.84
outer loop
vertex 35.2 -30 23.26
vertex 41.6 -27.6 20.56
vertex 35.2 -27.6 24.07
endloop
endfacet
facet normal 0.312 0.013 0.95
outer loop
vertex 41.6 -30 21.74
vertex 48 -30 19.64
vertex 48 -27.6 19.61
endloop
endfacet
facet normal 0.132 0.438 0.889
outer loop
vertex 41.6 -30 21.74
vertex 48 -27.6 19.61
vertex 41.6 -27.6 20.56
endloop
endfacet
facet normal -0.236 -0.17 0.957
outer loop
vertex -48 -27.6 6.85
vertex -41.6 -27.6 8.43
vertex -41.6 -25.2 8.86
endloop
endfacet
facet normal -0.208 -0.237 0.949
outer loop
vertex -48 -27.6 6.85
vertex -41.6 -25.2 8.86
vertex -48 -25.2 7.45
endloop
endfacet
facet normal 0.166 -0.112 0.98
outer loop
vertex -41.6 -27.6 8.43
vertex -35.2 -27.6 7.35
vertex -35.2 -25.2 7.63
endloop
endfacet
facet normal 0.186 -0.172 0.967
outer loop
vertex -41.6 -27.6 8.43
vertex -35.2 -25.2 7.63
vertex -41.6 -25.2 8.86
endloop
endfacet
facet normal -0.434 -0.242 0.868
outer loop
vertex -35.2 -27.6 7.35
vertex -28.8 -27.6 10.56
vertex -28.8 -25.2 11.23
endloop
endfacet
facet normal -0.488 -0.099 0.867
outer loop
vertex -35.2 -27.6 7.35
vertex -28.8 -25.2 11.23
vertex -35.2 -25.2 7.63
endloop
endfacet
facet normal 0.258 -0.242 0.935
outer loop
vertex -28.8 -27.6 10.56
vertex -22.4 -27.6 8.79
vertex -22.4 -25.2 9.41
endloop
endfacet
facet normal 0.263 -0.26 0.929
outer loop
vertex -28.8 -27.6 10.56
vertex -22.4 -25.2 9.41
vertex -28.8 -25.2 11.23
endloop
endfacet
facet normal -0.582 -0.442 0.683
outer loop
vertex -22.4 -27.6 8.79
vertex -16 -27.6 14.24
vertex -16 -25.2 15.8
endloop
endfacet
facet normal -0.695 -0.18 0.697
outer loop
vertex -22.4 -27.6 8.79
vertex -16 -25.2 15.8
vertex -22.4 -25.2 9.41
endloop
endfacet
facet normal -0.875 -0.102 0.473
outer loop
vertex -16 -27.6 14.24
vertex -9.6 -27.6 26.09
vertex -9.6 -25.2 26.61
endloop
endfacet
facet normal -0.817 -0.313 0.484
outer loop
vertex -16 -27.6 14.24
vertex -9.6 -25.2 26.61
vertex -16 -25.2 15.8
endloop
endfacet
facet normal -0.292 -0.705 0.646
outer loop
vertex -9.6 -27.6 26.09
vertex -3.2 -27.6 28.98
vertex -3.2 -25.2 31.6
endloop
endfacet
facet normal -0.606 -0.167 0.777
outer loop
vertex -9.6 -27.6 26.09
vertex -3.2 -25.2 31.6
vertex -9.6 -25.2 26.61
endloop
endfacet
facet normal 0.808 -0.175 0.563
outer loop
vertex -3.2 -27.6 28.98
vertex 3.2 -27.6 19.8
vertex 3.2 -25.2 20.54
endloop
endfacet
facet normal 0.76 -0.48 0.439
outer loop
vertex -3.2 -27.6 28.98
vertex 3.2 -25.2 20.54
vertex -3.2 -25.2 31.6
endloop
endfacet
facet normal -0.491 -0.152 0.858
outer loop
vertex 3.2 -27.6 19.8
vertex 9.6 -27.6 23.46
vertex 9.6 -25.2 23.88
endloop
endfacet
facet normal -0.446 -0.265 0.855
outer loop
vertex 3.2 -27.6 19.8
vertex 9.6 -25.2 23.88
vertex 3.2 -25.2 20.54
endloop
endfacet
facet normal 0.258 -0.391 0.883
outer loop
vertex 9.6 -27.6 23.46
vertex 16 -27.6 21.59
vertex 16 -25.2 22.65
endloop
endfacet
facet normal 0.187 -0.171 0.967
outer loop
vertex 9.6 -27.6 23.46
vertex 16 -25.2 22.65
vertex 9.6 -25.2 23.88
endloop
endfacet
facet normal -0.607 0.377 0.7
outer loop
vertex 16 -27.6 21.59
vertex 22.4 -27.6 27.14
vertex 22.4 -25.2 25.85
endloop
endfacet
facet normal -0.416 -0.368 0.832
outer loop
vertex 16 -27.6 21.59
vertex 22.4 -25.2 25.85
vertex 16 -25.2 22.65
endloop
endfacet
facet normal 0.741 0.154 0.653
outer loop
vertex 22.4 -27.6 27.14
vertex 28.8 -27.6 19.88
vertex 28.8 -25.2 19.31
endloop
endfacet
facet normal 0.668 0.353 0.655
outer loop
vertex 22.4 -27.6 27.14
vertex 28.8 -25.2 19.31
vertex 22.4 -25.2 25.85
endloop
endfacet
facet normal -0.485 -0.467 0.74
outer loop
vertex 28.8 -27.6 19.88
vertex 35.2 -27.6 24.07
vertex 35.2 -25.2 25.59
endloop
endfacet
facet normal -0.69 0.166 0.704
outer loop
vertex 28.8 -27.6 19.88
vertex 35.2 -25.2 25.59
vertex 28.8 -25.2 19.31
endloop
endfacet
facet normal 0.425 -0.47 0.774
outer loop
vertex 35.2 -27.6 24.07
vertex 41.6 -27.6 20.56
vertex 41.6 -25.2 22.01
endloop
endfacet
facet normal 0.427 -0.483 0.764
outer loop
vertex 35.2 -27.6 24.07
vertex 41.6 -25.2 22.01
vertex 35.2 -25.2 25.59
endloop
endfacet
facet normal 0.125 -0.524 0.843
outer loop
vertex 41.6 -27.6 20.56
vertex 48 -27.6 19.61
vertex 48 -25.2 21.1
endloop
endfacet
facet normal 0.121 -0.515 0.848
outer loop
vertex 41.6 -27.6 20.56
vertex 48 -25.2 21.1
vertex 41.6 -25.2 22.01
endloop
endfacet
facet normal -0.214 -0.052 0.975
outer loop
vertex -48 -25.2 7.45
vertex -41.6 -25.2 8.86
vertex -41.6 -22.8 8.99
endloop
endfacet
facet normal -0.11 -0.311 0.944
outer loop
vertex -48 -25.2 7.45
vertex -41.6 -22.8 8.99
vertex -48 -22.8 8.25
endloop
endfacet
facet normal 0.186 -0.175 0.967
outer loop
vertex -41.6 -25.2 8.86
vertex -35.2 -25.2 7.63
vertex -35.2 -22.8 8.06
endloop
endfacet
facet normal 0.143 -0.053 0.988
outer loop
vertex -41.6 -25.2 8.86
vertex -35.2 -22.8 8.06
vertex -41.6 -22.8 8.99
endloop
endfacet
facet normal -0.479 -0.212 0.852
outer loop
vertex -35.2 -25.2 7.63
vertex -28.8 -25.2 11.23
vertex -28.8 -22.8 11.83
endloop
endfacet
facet normal -0.501 -0.154 0.852
outer loop
vertex -35.2 -25.2 7.63
vertex -28.8 -22.8 11.83
vertex -35.2 -22.8 8.06
endloop
endfacet
facet normal 0.27 -0.121 0.955
outer loop
vertex -28.8 -25.2 11.23
vertex -22.4 -25.2 9.41
vertex -22.4 -22.8 9.72
endloop
endfacet
facet normal 0.304 -0.231 0.924
outer loop
vertex -28.8 -25.2 11.23
vertex -22.4 -22.8 9.72
vertex -28.8 -22.8 11.83
endloop
endfacet
facet normal -0.632 -0.446 0.634
outer loop
vertex -22.4 -25.2 9.41
vertex -16 -25.2 15.8
vertex -16 -22.8 17.49
endloop
endfacet
facet normal -0.769 -0.08 0.634
outer loop
vertex -22.4 -25.2 9.41
vertex -16 -22.8 17.49
vertex -22.4 -22.8 9.72
endloop
endfacet
facet normal -0.835 -0.241 0.494
outer loop
vertex -16 -25.2 15.8
vertex -9.6 -25.2 26.61
vertex -9.6 -22.8 27.78
endloop
endfacet
facet normal -0.796 -0.349 0.495
outer loop
vertex -16 -25.2 15.8
vertex -9.6 -22.8 27.78
vertex -16 -22.8 17.49
endloop
endfacet
facet normal -0.598 -0.233 0.767
outer loop
vertex -9.6 -25.2 26.61
vertex -3.2 -25.2 31.6
vertex -3.2 -22.8 32.33
endloop
endfacet
facet normal -0.538 -0.37 0.757
outer loop
vertex -9.6 -25.2 26.61
vertex -3.2 -22.8 32.33
vertex -9.6 -22.8 27.78
endloop
endfacet
facet normal 0.865 -0.02 0.501
outer loop
vertex -3.2 -25.2 31.6
vertex 3.2 -25.2 20.54
vertex 3.2 -22.8 20.64
endloop
endfacet
facet normal 0.868 -0.144 0.475
outer loop
vertex -3.2 -25.2 31.6
vertex 3.2 -22.8 20.64
vertex -3.2 -22.8 32.33
endloop
endfacet
facet normal -0.462 -0.052 0.885
outer loop
vertex 3.2 -25.2 20.54
vertex 9.6 -25.2 23.88
vertex 9.6 -22.8 24.02
endloop
endfacet
facet normal -0.467 -0.036 0.883
outer loop
vertex 3.2 -25.2 20.54
vertex 9.6 -22.8 24.02
vertex 3.2 -22.8 20.64
endloop
endfacet
facet normal 0.185 -0.21 0.96
outer loop
vertex 9.6 -25.2 23.88
vertex 16 -25.2 22.65
vertex 16 -22.8 23.17
endloop
endfacet
facet normal 0.131 -0.058 0.99
outer loop
vertex 9.6 -25.2 23.88
vertex 16 -22.8 23.17
vertex 9.6 -22.8 24.02
endloop
endfacet
facet normal -0.418 -0.353 0.837
outer loop
vertex 16 -25.2 22.65
vertex 22.4 -25.2 25.85
vertex 22.4 -22.8 26.86
endloop
endfacet
facet normal -0.49 -0.186 0.851
outer loop
vertex 16 -25.2 22.65
vertex 22.4 -22.8 26.86
vertex 16 -22.8 23.17
endloop
endfacet
facet normal 0.708 -0.131 0.694
outer loop
vertex 22.4 -25.2 25.85
vertex 28.8 -25.2 19.31
vertex 28.8 -22.8 19.77
endloop
endfacet
facet normal 0.714 -0.272 0.645
outer loop
vertex 22.4 -25.2 25.85
vertex 28.8 -22.8 19.77
vertex 22.4 -22.8 26.86
endloop
endfacet
facet normal -0.605 -0.505 0.616
outer loop
vertex 28.8 -25.2 19.31
vertex 35.2 -25.2 25.59
vertex 35.2 -22.8 27.55
endloop
endfacet
facet normal -0.767 -0.119 0.63
outer loop
vertex 28.8 -25.2 19.31
vertex 35.2 -22.8 27.55
vertex 28.8 -22.8 19.77
endloop
endfacet
facet normal 0.435 -0.452 0.778
outer loop
vertex 35.2 -25.2 25.59
vertex 41.6 -25.2 22.01
vertex 41.6 -22.8 23.41
endloop
endfacet
facet normal 0.448 -0.566 0.692
outer loop
vertex 35.2 -25.2 25.59
vertex 41.6 -22.8 23.41
vertex 35.2 -22.8 27.55
endloop
endfacet
facet normal 0.136 -0.263 0.955
outer loop
vertex 41.6 -25.2 22.01
vertex 48 -25.2 21.1
vertex 48 -22.8 21.76
endloop
endfacet
facet normal 0.217 -0.49 0.844
outer loop
vertex 41.6 -25.2 22.01
vertex 48 -22.8 21.76
vertex 41.6 -22.8 23.41
endloop
endfacet
facet normal -0.114 -0.151 0.982
outer loop
vertex -48 -22.8 8.25
vertex -41.6 -22.8 8.99
vertex -41.6 -20.4 9.36
endloop
endfacet
facet normal -0.096 -0.195 0.976
outer loop
vertex -48 -22.8 8.25
vertex -41.6 -20.4 9.36
vertex -48 -20.4 8.72
endloop
endfacet
facet normal 0.141 -0.185 0.973
outer loop
vertex -41.6 -22.8 8.99
vertex -35.2 -22.8 8.06
vertex -35.2 -20.4 8.52
endloop
endfacet
facet normal 0.128 -0.15 0.98
outer loop
vertex -41.6 -22.8 8.99
vertex -35.2 -20.4 8.52
vertex -41.6 -20.4 9.36
endloop
endfacet
facet normal -0.493 -0.235 0.838
outer loop
vertex -35.2 -22.8 8.06
vertex -28.8 -22.8 11.83
vertex -28.8 -20.4 12.5
endloop
endfacet
facet normal -0.521 -0.159 0.838
outer loop
vertex -35.2 -22.8 8.06
vertex -28.8 -20.4 12.5
vertex -35.2 -20.4 8.52
endloop
endfacet
facet normal 0.306 -0.205 0.93
outer loop
vertex -28.8 -22.8 11.83
vertex -22.4 -22.8 9.72
vertex -22.4 -20.4 10.25
endloop
endfacet
facet normal 0.321 -0.256 0.912
outer loop
vertex -28.8 -22.8 11.83
vertex -22.4 -20.4 10.25
vertex -28.8 -20.4 12.5
endloop
endfacet
facet normal -0.678 -0.478 0.559
outer loop
vertex -22.4 -22.8 9.72
vertex -16 -22.8 17.49
vertex -16 -20.4 19.54
endloop
endfacet
facet normal -0.817 -0.124 0.563
outer loop
vertex -22.4 -22.8 9.72
vertex -16 -20.4 19.54
vertex -22.4 -20.4 10.25
endloop
endfacet
facet normal -0.821 -0.255 0.511
outer loop
vertex -16 -22.8 17.49
vertex -9.6 -22.8 27.78
vertex -9.6 -20.4 28.98
endloop
endfacet
facet normal -0.746 -0.433 0.506
outer loop
vertex -16 -22.8 17.49
vertex -9.6 -20.4 28.98
vertex -16 -20.4 19.54
endloop
endfacet
facet normal -0.545 -0.339 0.767
outer loop
vertex -9.6 -22.8 27.78
vertex -3.2 -22.8 32.33
vertex -3.2 -20.4 33.39
endloop
endfacet
facet normal -0.525 -0.38 0.761
outer loop
vertex -9.6 -22.8 27.78
vertex -3.2 -20.4 33.39
vertex -9.6 -20.4 28.98
endloop
endfacet
facet normal 0.867 -0.153 0.474
outer loop
vertex -3.2 -22.8 32.33
vertex 3.2 -22.8 20.64
vertex 3.2 -20.4 21.41
endloop
endfacet
facet normal 0.864 -0.204 0.461
outer loop
vertex -3.2 -22.8 32.33
vertex 3.2 -20.4 21.41
vertex -3.2 -20.4 33.39
endloop
endfacet
facet normal -0.467 -0.036 0.883
outer loop
vertex 3.2 -22.8 20.64
vertex 9.6 -22.8 24.02
vertex 9.6 -20.4 24.12
endloop
endfacet
facet normal -0.374 -0.284 0.883
outer loop
vertex 3.2 -22.8 20.64
vertex 9.6 -20.4 24.12
vertex 3.2 -20.4 21.41
endloop
endfacet
facet normal 0.128 -0.233 0.964
outer loop
vertex 9.6 -22.8 24.02
vertex 16 -22.8 23.17
vertex 16 -20.4 23.75
endloop
endfacet
facet normal 0.057 -0.041 0.998
outer loop
vertex 9.6 -22.8 24.02
vertex 16 -20.4 23.75
vertex 9.6 -20.4 24.12
endloop
endfacet
facet normal -0.333 -0.745 0.578
outer loop
vertex 16 -22.8 23.17
vertex 22.4 -22.8 26.86
vertex 22.4 -20.4 29.95
endloop
endfacet
facet normal -0.685 -0.171 0.708
outer loop
vertex 16 -22.8 23.17
vertex 22.4 -20.4 29.95
vertex 16 -20.4 23.75
endloop
endfacet
facet normal 0.742 0.033 0.67
outer loop
vertex 22.4 -22.8 26.86
vertex 28.8 -22.8 19.77
vertex 28.8 -20.4 19.65
endloop
endfacet
facet normal 0.702 -0.562 0.436
outer loop
vertex 22.4 -22.8 26.86
vertex 28.8 -20.4 19.65
vertex 22.4 -20.4 29.95
endloop
endfacet
facet normal -0.773 0.011 0.635
outer loop
vertex 28.8 -22.8 19.77
vertex 35.2 -22.8 27.55
vertex 35.2 -20.4 27.51
endloop
endfacet
facet normal -0.775 0.031 0.631
outer loop
vertex 28.8 -22.8 19.77
vertex 35.2 -20.4 27.51
vertex 28.8 -20.4 19.65
endloop
endfacet
facet normal 0.54 -0.113 0.834
outer loop
vertex 35.2 -22.8 27.55
vertex 41.6 -22.8 23.41
vertex 41.6 -20.4 23.73
endloop
endfacet
facet normal 0.509 0.014 0.861
outer loop
vertex 35.2 -22.8 27.55
vertex 41.6 -20.4 23.73
vertex 35.2 -20.4 27.51
endloop
endfacet
facet normal 0.247 -0.152 0.957
outer loop
vertex 41.6 -22.8 23.41
vertex 48 -22.8 21.76
vertex 48 -20.4 22.14
endloop
endfacet
facet normal 0.239 -0.13 0.962
outer loop
vertex 41.6 -22.8 23.41
vertex 48 -20.4 22.14
vertex 41.6 -20.4 23.73
endloop
endfacet
facet normal -0.096 -0.217 0.971
outer loop
vertex -48 -20.4 8.72
vertex -41.6 -20.4 9.36
vertex -41.6 -18 9.89
endloop
endfacet
facet normal -0.009 -0.418 0.908
outer loop
vertex -48 -20.4 8.72
vertex -41.6 -18 9.89
vertex -48 -18 9.83
endloop
endfacet
facet normal 0.128 -0.16 0.979
outer loop
vertex -41.6 -20.4 9.36
vertex -35.2 -20.4 8.52
vertex -35.2 -18 8.91
endloop
endfacet
facet normal 0.148 -0.216 0.965
outer loop
vertex -41.6 -20.4 9.36
vertex -35.2 -18 8.91
vertex -41.6 -18 9.89
endloop
endfacet
facet normal -0.527 -0.069 0.847
outer loop
vertex -35.2 -20.4 8.52
vertex -28.8 -20.4 12.5
vertex -28.8 -18 12.69
endloop
endfacet
facet normal -0.504 -0.139 0.852
outer loop
vertex -35.2 -20.4 8.52
vertex -28.8 -18 12.69
vertex -35.2 -18 8.91
endloop
endfacet
facet normal 0.288 -0.496 0.819
outer loop
vertex -28.8 -20.4 12.5
vertex -22.4 -20.4 10.25
vertex -22.4 -18 11.7
endloop
endfacet
facet normal 0.153 -0.08 0.985
outer loop
vertex -28.8 -20.4 12.5
vertex -22.4 -18 11.7
vertex -28.8 -18 12.69
endloop
endfacet
facet normal -0.748 -0.42 0.515
outer loop
vertex -22.4 -20.4 10.25
vertex -16 -20.4 19.54
vertex -16 -18 21.5
endloop
endfacet
facet normal -0.795 -0.314 0.519
outer loop
vertex -22.4 -20.4 10.25
vertex -16 -18 21.5
vertex -22.4 -18 11.7
endloop
endfacet
facet normal -0.79 -0.299 0.536
outer loop
vertex -16 -20.4 19.54
vertex -9.6 -20.4 28.98
vertex -9.6 -18 30.32
endloop
endfacet
facet normal -0.73 -0.432 0.53
outer loop
vertex -16 -20.4 19.54
vertex -9.6 -18 30.32
vertex -16 -18 21.5
endloop
endfacet
facet normal -0.555 -0.212 0.805
outer loop
vertex -9.6 -20.4 28.98
vertex -3.2 -20.4 33.39
vertex -3.2 -18 34.03
endloop
endfacet
facet normal -0.451 -0.435 0.779
outer loop
vertex -9.6 -20.4 28.98
vertex -3.2 -18 34.03
vertex -9.6 -18 30.32
endloop
endfacet
facet normal 0.882 -0.017 0.471
outer loop
vertex -3.2 -20.4 33.39
vertex 3.2 -20.4 21.41
vertex 3.2 -18 21.5
endloop
endfacet
facet normal 0.884 -0.119 0.452
outer loop
vertex -3.2 -20.4 33.39
vertex 3.2 -18 21.5
vertex -3.2 -18 34.03
endloop
endfacet
facet normal -0.353 0.422 0.835
outer loop
vertex 3.2 -20.4 21.41
vertex 9.6 -20.4 24.12
vertex 9.6 -18 22.91
endloop
endfacet
facet normal -0.215 -0.035 0.976
outer loop
vertex 3.2 -20.4 21.41
vertex 9.6 -18 22.91
vertex 3.2 -18 21.5
endloop
endfacet
facet normal 0.054 -0.313 0.948
outer loop
vertex 9.6 -20.4 24.12
vertex 16 -20.4 23.75
vertex 16 -18 24.55
endloop
endfacet
facet normal -0.223 0.44 0.87
outer loop
vertex 9.6 -20.4 24.12
vertex 16 -18 24.55
vertex 9.6 -18 22.91
endloop
endfacet
facet normal -0.692 -0.096 0.715
outer loop
vertex 16 -20.4 23.75
vertex 22.4 -20.4 29.95
vertex 22.4 -18 30.27
endloop
endfacet
facet normal -0.648 -0.239 0.724
outer loop
vertex 16 -20.4 23.75
vertex 22.4 -18 30.27
vertex 16 -18 24.55
endloop
endfacet
facet normal 0.848 0.054 0.527
outer loop
vertex 22.4 -20.4 29.95
vertex 28.8 -20.4 19.65
vertex 28.8 -18 19.4
endloop
endfacet
facet normal 0.86 -0.068 0.506
outer loop
vertex 22.4 -20.4 29.95
vertex 28.8 -18 19.4
vertex 22.4 -18 30.27
endloop
endfacet
facet normal -0.774 0.058 0.63
outer loop
vertex 28.8 -20.4 19.65
vertex 35.2 -20.4 27.51
vertex 35.2 -18 27.29
endloop
endfacet
facet normal -0.775 0.065 0.629
outer loop
vertex 28.8 -20.4 19.65
vertex 35.2 -18 27.29
vertex 28.8 -18 19.4
endloop
endfacet
facet normal 0.508 0.049 0.86
outer loop
vertex 35.2 -20.4 27.51
vertex 41.6 -20.4 23.73
vertex 41.6 -18 23.59
endloop
endfacet
facet normal 0.499 0.08 0.863
outer loop
vertex 35.2 -20.4 27.51
vertex 41.6 -18 23.59
vertex 35.2 -18 27.29
endloop
endfacet
facet normal 0.241 -0.039 0.97
outer loop
vertex 41.6 -20.4 23.73
vertex 48 -20.4 22.14
vertex 48 -18 22.24
endloop
endfacet
facet normal 0.207 0.056 0.977
outer loop
vertex 41.6 -20.4 23.73
vertex 48 -18 22.24
vertex 41.6 -18 23.59
endloop
endfacet
facet normal -0.01 -0.191 0.981
outer loop
vertex -48 -18 9.83
vertex -41.6 -18 9.89
vertex -41.6 -15.6 10.36
endloop
endfacet
facet normal -0.036 -0.124 0.992
outer loop
vertex -48 -18 9.83
vertex -41.6 -15.6 10.36
vertex -48 -15.6 10.13
endloop
endfacet
facet normal 0.125 -0.565 0.816
outer loop
vertex -41.6 -18 9.89
vertex -35.2 -18 8.91
vertex -35.2 -15.6 10.57
endloop
endfacet
facet normal -0.032 -0.191 0.981
outer loop
vertex -41.6 -18 9.89
vertex -35.2 -15.6 10.57
vertex -41.6 -15.6 10.36
endloop
endfacet
facet normal -0.501 -0.181 0.847
outer loop
vertex -35.2 -18 8.91
vertex -28.8 -18 12.69
vertex -28.8 -15.6 13.21
endloop
endfacet
facet normal -0.321 -0.539 0.779
outer loop
vertex -35.2 -18 8.91
vertex -28.8 -15.6 13.21
vertex -35.2 -15.6 10.57
endloop
endfacet
facet normal 0.152 -0.141 0.978
outer loop
vertex -28.8 -18 12.69
vertex -22.4 -18 11.7
vertex -22.4 -15.6 12.05
endloop
endfacet
facet normal 0.175 -0.206 0.963
outer loop
vertex -28.8 -18 12.69
vertex -22.4 -15.6 12.05
vertex -28.8 -15.6 13.21
endloop
endfacet
facet normal -0.777 -0.373 0.507
outer loop
vertex -22.4 -18 11.7
vertex -16 -18 21.5
vertex -16 -15.6 23.26
endloop
endfacet
facet normal -0.866 -0.071 0.494
outer loop
vertex -22.4 -18 11.7
vertex -16 -15.6 23.26
vertex -22.4 -15.6 12.05
endloop
endfacet
facet normal -0.809 0.022 0.587
outer loop
vertex -16 -18 21.5
vertex -9.6 -18 30.32
vertex -9.6 -15.6 30.23
endloop
endfacet
facet normal -0.66 -0.445 0.606
outer loop
vertex -16 -18 21.5
vertex -9.6 -15.6 30.23
vertex -16 -15.6 23.26
endloop
endfacet
facet normal -0.501 -0.04 0.865
outer loop
vertex -9.6 -18 30.32
vertex -3.2 -18 34.03
vertex -3.2 -15.6 34.14
endloop
endfacet
facet normal -0.521 0.032 0.853
outer loop
vertex -9.6 -18 30.32
vertex -3.2 -15.6 34.14
vertex -9.6 -15.6 30.23
endloop
endfacet
facet normal 0.889 0.049 0.454
outer loop
vertex -3.2 -18 34.03
vertex 3.2 -18 21.5
vertex 3.2 -15.6 21.24
endloop
endfacet
facet normal 0.896 -0.02 0.444
outer loop
vertex -3.2 -18 34.03
vertex 3.2 -15.6 21.24
vertex -3.2 -15.6 34.14
endloop
endfacet
facet normal -0.185 -0.51 0.84
outer loop
vertex 3.2 -18 21.5
vertex 9.6 -18 22.91
vertex 9.6 -15.6 24.36
endloop
endfacet
facet normal -0.437 0.096 0.894
outer loop
vertex 3.2 -18 21.5
vertex 9.6 -15.6 24.36
vertex 3.2 -15.6 21.24
endloop
endfacet
facet normal -0.169 -0.733 0.659
outer loop
vertex 9.6 -18 22.91
vertex 16 -18 24.55
vertex 16 -15.6 27.21
endloop
endfacet
facet normal -0.356 -0.485 0.799
outer loop
vertex 9.6 -18 22.91
vertex 16 -15.6 27.21
vertex 9.6 -15.6 24.36
endloop
endfacet
facet normal -0.646 0.249 0.722
outer loop
vertex 16 -18 24.55
vertex 22.4 -18 30.27
vertex 22.4 -15.6 29.44
endloop
endfacet
facet normal -0.227 -0.724 0.651
outer loop
vertex 16 -18 24.55
vertex 22.4 -15.6 29.44
vertex 16 -15.6 27.21
endloop
endfacet
facet normal 0.854 -0.135 0.503
outer loop
vertex 22.4 -18 30.27
vertex 28.8 -18 19.4
vertex 28.8 -15.6 20.05
endloop
endfacet
facet normal 0.811 0.191 0.553
outer loop
vertex 22.4 -18 30.27
vertex 28.8 -15.6 20.05
vertex 22.4 -15.6 29.44
endloop
endfacet
facet normal -0.758 0.221 0.614
outer loop
vertex 28.8 -18 19.4
vertex 35.2 -18 27.29
vertex 35.2 -15.6 26.43
endloop
endfacet
facet normal -0.694 -0.187 0.696
outer loop
vertex 28.8 -18 19.4
vertex 35.2 -15.6 26.43
vertex 28.8 -15.6 20.05
endloop
endfacet
facet normal 0.474 -0.317 0.821
outer loop
vertex 35.2 -18 27.29
vertex 41.6 -18 23.59
vertex 41.6 -15.6 24.52
endloop
endfacet
facet normal 0.27 0.326 0.906
outer loop
vertex 35.2 -18 27.29
vertex 41.6 -15.6 24.52
vertex 35.2 -15.6 26.43
endloop
endfacet
facet normal 0.2 -0.272 0.941
outer loop
vertex 41.6 -18 23.59
vertex 48 -18 22.24
vertex 48 -15.6 22.93
endloop
endfacet
facet normal 0.226 -0.351 0.909
outer loop
vertex 41.6 -18 23.59
vertex 48 -15.6 22.93
vertex 41.6 -15.6 24.52
endloop
endfacet
facet normal -0.036 -0.078 0.996
outer loop
vertex -48 -15.6 10.13
vertex -41.6 -15.6 10.36
vertex -41.6 -13.2 10.55
endloop
endfacet
facet normal -0.032 -0.088 0.996
outer loop
vertex -48 -15.6 10.13
vertex -41.6 -13.2 10.55
vertex -48 -13.2 10.34
endloop
endfacet
facet normal -0.031 -0.336 0.942
outer loop
vertex -41.6 -15.6 10.36
vertex -35.2 -15.6 10.57
vertex -35.2 -13.2 11.43
endloop
endfacet
facet normal -0.135 -0.078 0.988
outer loop
vertex -41.6 -15.6 10.36
vertex -35.2 -13.2 11.43
vertex -41.6 -13.2 10.55
endloop
endfacet
facet normal -0.381 0.038 0.924
outer loop
vertex -35.2 -15.6 10.57
vertex -28.8 -15.6 13.21
vertex -28.8 -13.2 13.11
endloop
endfacet
facet normal -0.24 -0.326 0.914
outer loop
vertex -35.2 -15.6 10.57
vertex -28.8 -13.2 13.11
vertex -35.2 -13.2 11.43
endloop
endfacet
facet normal 0.148 -0.56 0.815
outer loop
vertex -28.8 -15.6 13.21
vertex -22.4 -15.6 12.05
vertex -22.4 -13.2 13.69
endloop
endfacet
facet normal -0.091 0.041 0.995
outer loop
vertex -28.8 -15.6 13.21
vertex -22.4 -13.2 13.69
vertex -28.8 -13.2 13.11
endloop
endfacet
facet normal -0.844 -0.236 0.482
outer loop
vertex -22.4 -15.6 12.05
vertex -16 -15.6 23.26
vertex -16 -13.2 24.43
endloop
endfacet
facet normal -0.81 -0.332 0.483
outer loop
vertex -22.4 -15.6 12.05
vertex -16 -13.2 24.43
vertex -22.4 -13.2 13.69
endloop
endfacet
facet normal -0.72 -0.211 0.661
outer loop
vertex -16 -15.6 23.26
vertex -9.6 -15.6 30.23
vertex -9.6 -13.2 31
endloop
endfacet
facet normal -0.678 -0.323 0.661
outer loop
vertex -16 -15.6 23.26
vertex -9.6 -13.2 31
vertex -16 -13.2 24.43
endloop
endfacet
facet normal -0.514 0.166 0.842
outer loop
vertex -9.6 -15.6 30.23
vertex -3.2 -15.6 34.14
vertex -3.2 -13.2 33.66
endloop
endfacet
facet normal -0.369 -0.283 0.885
outer loop
vertex -9.6 -15.6 30.23
vertex -3.2 -13.2 33.66
vertex -9.6 -13.2 31
endloop
endfacet
facet normal 0.895 -0.037 0.444
outer loop
vertex -3.2 -15.6 34.14
vertex 3.2 -15.6 21.24
vertex 3.2 -13.2 21.44
endloop
endfacet
facet normal 0.882 0.091 0.462
outer loop
vertex -3.2 -15.6 34.14
vertex 3.2 -13.2 21.44
vertex -3.2 -13.2 33.66
endloop
endfacet
facet normal -0.429 -0.213 0.878
outer loop
vertex 3.2 -15.6 21.24
vertex 9.6 -15.6 24.36
vertex 9.6 -13.2 24.95
endloop
endfacet
facet normal -0.479 -0.073 0.875
outer loop
vertex 3.2 -15.6 21.24
vertex 9.6 -13.2 24.95
vertex 3.2 -13.2 21.44
endloop
endfacet
facet normal -0.219 -0.843 0.491
outer loop
vertex 9.6 -15.6 24.36
vertex 16 -15.6 27.21
vertex 16 -13.2 31.34
endloop
endfacet
facet normal -0.696 -0.169 0.698
outer loop
vertex 9.6 -15.6 24.36
vertex 16 -13.2 31.34
vertex 9.6 -13.2 24.95
endloop
endfacet
facet normal -0.327 0.108 0.939
outer loop
vertex 16 -15.6 27.21
vertex 22.4 -15.6 29.44
vertex 22.4 -13.2 29.17
endloop
endfacet
facet normal 0.168 -0.852 0.496
outer loop
vertex 16 -15.6 27.21
vertex 22.4 -13.2 29.17
vertex 16 -13.2 31.34
endloop
endfacet
facet normal 0.824 0.084 0.561
outer loop
vertex 22.4 -15.6 29.44
vertex 28.8 -15.6 20.05
vertex 28.8 -13.2 19.69
endloop
endfacet
facet normal 0.827 0.064 0.558
outer loop
vertex 22.4 -15.6 29.44
vertex 28.8 -13.2 19.69
vertex 22.4 -13.2 29.17
endloop
endfacet
facet normal -0.686 0.234 0.688
outer loop
vertex 28.8 -15.6 20.05
vertex 35.2 -15.6 26.43
vertex 35.2 -13.2 25.61
endloop
endfacet
facet normal -0.675 0.109 0.73
outer loop
vertex 28.8 -15.6 20.05
vertex 35.2 -13.2 25.61
vertex 28.8 -13.2 19.69
endloop
endfacet
facet normal 0.284 -0.118 0.952
outer loop
vertex 35.2 -15.6 26.43
vertex 41.6 -15.6 24.52
vertex 41.6 -13.2 24.82
endloop
endfacet
facet normal 0.117 0.32 0.94
outer loop
vertex 35.2 -15.6 26.43
vertex 41.6 -13.2 24.82
vertex 35.2 -13.2 25.61
endloop
endfacet
facet normal 0.24 -0.092 0.966
outer loop
vertex 41.6 -15.6 24.52
vertex 48 -15.6 22.93
vertex 48 -13.2 23.16
endloop
endfacet
facet normal 0.249 -0.119 0.961
outer loop
vertex 41.6 -15.6 24.52
vertex 48 -13.2 23.16
vertex 41.6 -13.2 24.82
endloop
endfacet
facet normal -0.03 -0.384 0.923
outer loop
vertex -48 -13.2 10.34
vertex -41.6 -13.2 10.55
vertex -41.6 -10.8 11.55
endloop
endfacet
facet normal -0.097 -0.228 0.969
outer loop
vertex -48 -13.2 10.34
vertex -41.6 -10.8 11.55
vertex -48 -10.8 10.91
endloop
endfacet
facet normal -0.127 -0.347 0.929
outer loop
vertex -41.6 -13.2 10.55
vertex -35.2 -13.2 11.43
vertex -35.2 -10.8 12.32
endloop
endfacet
facet normal -0.111 -0.382 0.918
outer loop
vertex -41.6 -13.2 10.55
vertex -35.2 -10.8 12.32
vertex -41.6 -10.8 11.55
endloop
endfacet
facet normal -0.239 -0.335 0.911
outer loop
vertex -35.2 -13.2 11.43
vertex -28.8 -13.2 13.11
vertex -28.8 -10.8 13.99
endloop
endfacet
facet normal -0.237 -0.34 0.91
outer loop
vertex -35.2 -13.2 11.43
vertex -28.8 -10.8 13.99
vertex -35.2 -10.8 12.32
endloop
endfacet
facet normal -0.09 -0.132 0.987
outer loop
vertex -28.8 -13.2 13.11
vertex -22.4 -13.2 13.69
vertex -22.4 -10.8 14.01
endloop
endfacet
facet normal -0.003 -0.345 0.939
outer loop
vertex -28.8 -13.2 13.11
vertex -22.4 -10.8 14.01
vertex -28.8 -10.8 13.99
endloop
endfacet
facet normal -0.857 -0.064 0.511
outer loop
vertex -22.4 -13.2 13.69
vertex -16 -13.2 24.43
vertex -16 -10.8 24.74
endloop
endfacet
facet normal -0.857 -0.068 0.511
outer loop
vertex -22.4 -13.2 13.69
vertex -16 -10.8 24.74
vertex -22.4 -10.8 14.01
endloop
endfacet
facet normal -0.714 -0.069 0.696
outer loop
vertex -16 -13.2 24.43
vertex -9.6 -13.2 31
vertex -9.6 -10.8 31.23
endloop
endfacet
facet normal -0.71 -0.088 0.699
outer loop
vertex -16 -13.2 24.43
vertex -9.6 -10.8 31.23
vertex -16 -10.8 24.74
endloop
endfacet
facet normal -0.373 0.241 0.896
outer loop
vertex -9.6 -13.2 31
vertex -3.2 -13.2 33.66
vertex -3.2 -10.8 33.02
endloop
endfacet
facet normal -0.267 -0.095 0.959
outer loop
vertex -9.6 -13.2 31
vertex -3.2 -10.8 33.02
vertex -9.6 -10.8 31.23
endloop
endfacet
facet normal 0.877 -0.142 0.459
outer loop
vertex -3.2 -13.2 33.66
vertex 3.2 -13.2 21.44
vertex 3.2 -10.8 22.18
endloop
endfacet
facet normal 0.853 0.135 0.504
outer loop
vertex -3.2 -13.2 33.66
vertex 3.2 -10.8 22.18
vertex -3.2 -10.8 33.02
endloop
endfacet
facet normal -0.435 -0.424 0.794
outer loop
vertex 3.2 -13.2 21.44
vertex 9.6 -13.2 24.95
vertex 9.6 -10.8 26.23
endloop
endfacet
facet normal -0.517 -0.254 0.818
outer loop
vertex 3.2 -13.2 21.44
vertex 9.6 -10.8 26.23
vertex 3.2 -10.8 22.18
endloop
endfacet
facet normal -0.588 -0.554 0.589
outer loop
vertex 9.6 -13.2 24.95
vertex 16 -13.2 31.34
vertex 16 -10.8 33.59
endloop
endfacet
facet normal -0.712 -0.331 0.619
outer loop
vertex 9.6 -13.2 24.95
vertex 16 -10.8 33.59
vertex 9.6 -10.8 26.23
endloop
endfacet
facet normal 0.299 0.36 0.883
outer loop
vertex 16 -13.2 31.34
vertex 22.4 -13.2 29.17
vertex 22.4 -10.8 28.19
endloop
endfacet
facet normal 0.524 -0.583 0.621
outer loop
vertex 16 -13.2 31.34
vertex 22.4 -10.8 28.19
vertex 16 -10.8 33.59
endloop
endfacet
facet normal 0.818 -0.163 0.552
outer loop
vertex 22.4 -13.2 29.17
vertex 28.8 -13.2 19.69
vertex 28.8 -10.8 20.4
endloop
endfacet
facet normal 0.748 0.251 0.614
outer loop
vertex 22.4 -13.2 29.17
vertex 28.8 -10.8 20.4
vertex 22.4 -10.8 28.19
endloop
endfacet
facet normal -0.677 0.085 0.731
outer loop
vertex 28.8 -13.2 19.69
vertex 35.2 -13.2 25.61
vertex 35.2 -10.8 25.33
endloop
endfacet
facet normal -0.595 -0.227 0.771
outer loop
vertex 28.8 -13.2 19.69
vertex 35.2 -10.8 25.33
vertex 28.8 -10.8 20.4
endloop
endfacet
facet normal 0.122 -0.166 0.979
outer loop
vertex 35.2 -13.2 25.61
vertex 41.6 -13.2 24.82
vertex 41.6 -10.8 25.23
endloop
endfacet
facet normal 0.017 0.116 0.993
outer loop
vertex 35.2 -13.2 25.61
vertex 41.6 -10.8 25.23
vertex 35.2 -10.8 25.33
endloop
endfacet
facet normal 0.247 0.171 0.954
outer loop
vertex 41.6 -13.2 24.82
vertex 48 -13.2 23.16
vertex 48 -10.8 22.73
endloop
endfacet
facet normal 0.359 -0.156 0.92
outer loop
vertex 41.6 -13.2 24.82
vertex 48 -10.8 22.73
vertex 41.6 -10.8 25.23
endloop
endfacet
facet normal -0.099 -0.104 0.99
outer loop
vertex -48 -10.8 10.91
vertex -41.6 -10.8 11.55
vertex -41.6 -8.4 11.8
endloop
endfacet
facet normal -0.094 -0.116 0.989
outer loop
vertex -48 -10.8 10.91
vertex -41.6 -8.4 11.8
vertex -48 -8.4 11.19
endloop
endfacet
facet normal -0.116 -0.251 0.961
outer loop
vertex -41.6 -10.8 11.55
vertex -35.2 -10.8 12.32
vertex -35.2 -8.4 12.95
endloop
endfacet
facet normal -0.176 -0.103 0.979
outer loop
vertex -41.6 -10.8 11.55
vertex -35.2 -8.4 12.95
vertex -41.6 -8.4 11.8
endloop
endfacet
facet normal -0.252 0.029 0.967
outer loop
vertex -35.2 -10.8 12.32
vertex -28.8 -10.8 13.99
vertex -28.8 -8.4 13.92
endloop
endfacet
facet normal -0.145 -0.25 0.957
outer loop
vertex -35.2 -10.8 12.32
vertex -28.8 -8.4 13.92
vertex -35.2 -8.4 12.95
endloop
endfacet
facet normal -0.004 0.17 0.985
outer loop
vertex -28.8 -10.8 13.99
vertex -22.4 -10.8 14.01
vertex -22.4 -8.4 13.6
endloop
endfacet
facet normal 0.05 0.03 0.998
outer loop
vertex -28.8 -10.8 13.99
vertex -22.4 -8.4 13.6
vertex -28.8 -8.4 13.92
endloop
endfacet
facet normal -0.85 0.142 0.507
outer loop
vertex -22.4 -10.8 14.01
vertex -16 -10.8 24.74
vertex -16 -8.4 24.07
endloop
endfacet
facet normal -0.85 0.09 0.52
outer loop
vertex -22.4 -10.8 14.01
vertex -16 -8.4 24.07
vertex -22.4 -8.4 13.6
endloop
endfacet
facet normal -0.71 0.091 0.699
outer loop
vertex -16 -10.8 24.74
vertex -9.6 -10.8 31.23
vertex -9.6 -8.4 30.92
endloop
endfacet
facet normal -0.718 0.187 0.67
outer loop
vertex -16 -10.8 24.74
vertex -9.6 -8.4 30.92
vertex -16 -8.4 24.07
endloop
endfacet
facet normal -0.256 0.303 0.918
outer loop
vertex -9.6 -10.8 31.23
vertex -3.2 -10.8 33.02
vertex -3.2 -8.4 32.23
endloop
endfacet
facet normal -0.198 0.127 0.972
outer loop
vertex -9.6 -10.8 31.23
vertex -3.2 -8.4 32.23
vertex -9.6 -8.4 30.92
endloop
endfacet
facet normal 0.861 -0.01 0.509
outer loop
vertex -3.2 -10.8 33.02
vertex 3.2 -10.8 22.18
vertex 3.2 -8.4 22.23
endloop
endfacet
facet normal 0.829 0.175 0.531
outer loop
vertex -3.2 -10.8 33.02
vertex 3.2 -8.4 22.23
vertex -3.2 -8.4 32.23
endloop
endfacet
facet normal -0.519 -0.239 0.821
outer loop
vertex 3.2 -10.8 22.18
vertex 9.6 -10.8 26.23
vertex 9.6 -8.4 26.93
endloop
endfacet
facet normal -0.592 -0.016 0.806
outer loop
vertex 3.2 -10.8 22.18
vertex 9.6 -8.4 26.93
vertex 3.2 -8.4 22.23
endloop
endfacet
facet normal -0.754 0.031 0.656
outer loop
vertex 9.6 -10.8 26.23
vertex 16 -10.8 33.59
vertex 16 -8.4 33.48
endloop
endfacet
facet normal -0.701 -0.199 0.685
outer loop
vertex 9.6 -10.8 26.23
vertex 16 -8.4 33.48
vertex 9.6 -8.4 26.93
endloop
endfacet
facet normal 0.645 -0.011 0.764
outer loop
vertex 16 -10.8 33.59
vertex 22.4 -10.8 28.19
vertex 22.4 -8.4 28.22
endloop
endfacet
facet normal 0.634 0.036 0.772
outer loop
vertex 16 -10.8 33.59
vertex 22.4 -8.4 28.22
vertex 16 -8.4 33.48
endloop
endfacet
facet normal 0.773 -0.011 0.635
outer loop
vertex 22.4 -10.8 28.19
vertex 28.8 -10.8 20.4
vertex 28.8 -8.4 20.44
endloop
endfacet
facet normal 0.772 -0.009 0.635
outer loop
vertex 22.4 -10.8 28.19
vertex 28.8 -8.4 20.44
vertex 22.4 -8.4 28.22
endloop
endfacet
facet normal -0.611 -0.011 0.792
outer loop
vertex 28.8 -10.8 20.4
vertex 35.2 -10.8 25.33
vertex 35.2 -8.4 25.37
endloop
endfacet
facet normal -0.61 -0.013 0.792
outer loop
vertex 28.8 -10.8 20.4
vertex 35.2 -8.4 25.37
vertex 28.8 -8.4 20.44
endloop
endfacet
facet normal 0.017 0.113 0.993
outer loop
vertex 35.2 -10.8 25.33
vertex 41.6 -10.8 25.23
vertex 41.6 -8.4 24.95
endloop
endfacet
facet normal 0.065 -0.014 0.998
outer loop
vertex 35.2 -10.8 25.33
vertex 41.6 -8.4 24.95
vertex 35.2 -8.4 25.37
endloop
endfacet
facet normal 0.36 -0.143 0.922
outer loop
vertex 41.6 -10.8 25.23
vertex 48 -10.8 22.73
vertex 48 -8.4 23.1
endloop
endfacet
facet normal 0.276 0.109 0.955
outer loop
vertex 41.6 -10.8 25.23
vertex 48 -8.4 23.1
vertex 41.6 -8.4 24.95
endloop
endfacet
facet normal -0.095 -0.043 0.995
outer loop
vertex -48 -8.4 11.19
vertex -41.6 -8.4 11.8
vertex -41.6 -6 11.91
endloop
endfacet
facet normal -0.138 0.075 0.988
outer loop
vertex -48 -8.4 11.19
vertex -41.6 -6 11.91
vertex -48 -6 11.01
endloop
endfacet
facet normal -0.176 -0.087 0.981
outer loop
vertex -41.6 -8.4 11.8
vertex -35.2 -8.4 12.95
vertex -35.2 -6 13.16
endloop
endfacet
facet normal -0.192 -0.043 0.98
outer loop
vertex -41.6 -8.4 11.8
vertex -35.2 -6 13.16
vertex -41.6 -6 11.91
endloop
endfacet
facet normal -0.15 0.015 0.989
outer loop
vertex -35.2 -8.4 12.95
vertex -28.8 -8.4 13.92
vertex -28.8 -6 13.88
endloop
endfacet
facet normal -0.111 -0.088 0.99
outer loop
vertex -35.2 -8.4 12.95
vertex -28.8 -6 13.88
vertex -35.2 -6 13.16
endloop
endfacet
facet normal 0.049 0.18 0.982
outer loop
vertex -28.8 -8.4 13.92
vertex -22.4 -8.4 13.6
vertex -22.4 -6 13.16
endloop
endfacet
facet normal 0.112 0.015 0.994
outer loop
vertex -28.8 -8.4 13.92
vertex -22.4 -6 13.16
vertex -28.8 -6 13.88
endloop
endfacet
facet normal -0.846 0.132 0.517
outer loop
vertex -22.4 -8.4 13.6
vertex -16 -8.4 24.07
vertex -16 -6 23.45
endloop
endfacet
facet normal -0.845 0.096 0.526
outer loop
vertex -22.4 -8.4 13.6
vertex -16 -6 23.45
vertex -22.4 -6 13.16
endloop
endfacet
facet normal -0.722 0.157 0.674
outer loop
vertex -16 -8.4 24.07
vertex -9.6 -8.4 30.92
vertex -9.6 -6 30.36
endloop
endfacet
facet normal -0.723 0.171 0.669
outer loop
vertex -16 -8.4 24.07
vertex -9.6 -6 30.36
vertex -16 -6 23.45
endloop
endfacet
facet normal -0.189 0.324 0.927
outer loop
vertex -9.6 -8.4 30.92
vertex -3.2 -8.4 32.23
vertex -3.2 -6 31.39
endloop
endfacet
facet normal -0.154 0.224 0.962
outer loop
vertex -9.6 -8.4 30.92
vertex -3.2 -6 31.39
vertex -9.6 -6 30.36
endloop
endfacet
facet normal 0.842 -0.008 0.539
outer loop
vertex -3.2 -8.4 32.23
vertex 3.2 -8.4 22.23
vertex 3.2 -6 22.27
endloop
endfacet
facet normal 0.803 0.197 0.563
outer loop
vertex -3.2 -8.4 32.23
vertex 3.2 -6 22.27
vertex -3.2 -6 31.39
endloop
endfacet
facet normal -0.578 -0.215 0.787
outer loop
vertex 3.2 -8.4 22.23
vertex 9.6 -8.4 26.93
vertex 9.6 -6 27.59
endloop
endfacet
facet normal -0.639 -0.012 0.769
outer loop
vertex 3.2 -8.4 22.23
vertex 9.6 -6 27.59
vertex 3.2 -6 22.27
endloop
endfacet
facet normal -0.707 -0.152 0.691
outer loop
vertex 9.6 -8.4 26.93
vertex 16 -8.4 33.48
vertex 16 -6 34.01
endloop
endfacet
facet normal -0.695 -0.19 0.693
outer loop
vertex 9.6 -8.4 26.93
vertex 16 -6 34.01
vertex 9.6 -6 27.59
endloop
endfacet
facet normal 0.603 0.313 0.734
outer loop
vertex 16 -8.4 33.48
vertex 22.4 -8.4 28.22
vertex 22.4 -6 27.2
endloop
endfacet
facet normal 0.72 -0.149 0.677
outer loop
vertex 16 -8.4 33.48
vertex 22.4 -6 27.2
vertex 16 -6 34.01
endloop
endfacet
facet normal 0.764 0.143 0.629
outer loop
vertex 22.4 -8.4 28.22
vertex 28.8 -8.4 20.44
vertex 28.8 -6 19.89
endloop
endfacet
facet normal 0.724 0.271 0.634
outer loop
vertex 22.4 -8.4 28.22
vertex 28.8 -6 19.89
vertex 22.4 -6 27.2
endloop
endfacet
facet normal -0.608 0.078 0.79
outer loop
vertex 28.8 -8.4 20.44
vertex 35.2 -8.4 25.37
vertex 35.2 -6 25.13
endloop
endfacet
facet normal -0.624 0.174 0.762
outer loop
vertex 28.8 -8.4 20.44
vertex 35.2 -6 25.13
vertex 28.8 -6 19.89
endloop
endfacet
facet normal 0.064 0.13 0.989
outer loop
vertex 35.2 -8.4 25.37
vertex 41.6 -8.4 24.95
vertex 41.6 -6 24.64
endloop
endfacet
facet normal 0.077 0.097 0.992
outer loop
vertex 35.2 -8.4 25.37
vertex 41.6 -6 24.64
vertex 35.2 -6 25.13
endloop
endfacet
facet normal 0.272 0.201 0.941
outer loop
vertex 41.6 -8.4 24.95
vertex 48 -8.4 23.1
vertex 48 -6 22.59
endloop
endfacet
facet normal 0.303 0.124 0.945
outer loop
vertex 41.6 -8.4 24.95
vertex 48 -6 22.59
vertex 41.6 -6 24.64
endloop
endfacet
facet normal -0.132 0.31 0.942
outer loop
vertex -48 -6 11.01
vertex -41.6 -6 11.91
vertex -41.6 -3.6 11.12
endloop
endfacet
facet normal 0.018 -0.093 0.996
outer loop
vertex -48 -6 11.01
vertex -41.6 -3.6 11.12
vertex -48 -3.6 11.23
endloop
endfacet
facet normal -0.193 -0.018 0.981
outer loop
vertex -41.6 -6 11.91
vertex -35.2 -6 13.16
vertex -35.2 -3.6 13.2
endloop
endfacet
facet normal -0.296 0.298 0.907
outer loop
vertex -41.6 -6 11.91
vertex -35.2 -3.6 13.2
vertex -41.6 -3.6 11.12
endloop
endfacet
facet normal -0.112 0.017 0.994
outer loop
vertex -35.2 -6 13.16
vertex -28.8 -6 13.88
vertex -28.8 -3.6 13.84
endloop
endfacet
facet normal -0.099 -0.018 0.995
outer loop
vertex -35.2 -6 13.16
vertex -28.8 -3.6 13.84
vertex -35.2 -3.6 13.2
endloop
endfacet
facet normal 0.109 0.229 0.967
outer loop
vertex -28.8 -6 13.88
vertex -22.4 -6 13.16
vertex -22.4 -3.6 12.59
endloop
endfacet
facet normal 0.191 0.017 0.981
outer loop
vertex -28.8 -6 13.88
vertex -22.4 -3.6 12.59
vertex -28.8 -3.6 13.84
endloop
endfacet
facet normal -0.829 0.215 0.516
outer loop
vertex -22.4 -6 13.16
vertex -16 -6 23.45
vertex -16 -3.6 22.45
endloop
endfacet
facet normal -0.832 0.128 0.54
outer loop
vertex -22.4 -6 13.16
vertex -16 -3.6 22.45
vertex -22.4 -3.6 12.59
endloop
endfacet
facet normal -0.731 0.087 0.677
outer loop
vertex -16 -6 23.45
vertex -9.6 -6 30.36
vertex -9.6 -3.6 30.05
endloop
endfacet
facet normal -0.739 0.259 0.622
outer loop
vertex -16 -6 23.45
vertex -9.6 -3.6 30.05
vertex -16 -3.6 22.45
endloop
endfacet
facet normal -0.158 0.061 0.986
outer loop
vertex -9.6 -6 30.36
vertex -3.2 -6 31.39
vertex -3.2 -3.6 31.24
endloop
endfacet
facet normal -0.18 0.125 0.976
outer loop
vertex -9.6 -6 30.36
vertex -3.2 -3.6 31.24
vertex -9.6 -3.6 30.05
endloop
endfacet
facet normal 0.806 0.172 0.566
outer loop
vertex -3.2 -6 31.39
vertex 3.2 -6 22.27
vertex 3.2 -3.6 21.54
endloop
endfacet
facet normal 0.834 0.034 0.55
outer loop
vertex -3.2 -6 31.39
vertex 3.2 -3.6 21.54
vertex -3.2 -3.6 31.24
endloop
endfacet
facet normal -0.632 -0.153 0.76
outer loop
vertex 3.2 -6 22.27
vertex 9.6 -6 27.59
vertex 9.6 -3.6 28.07
endloop
endfacet
facet normal -0.699 0.208 0.685
outer loop
vertex 3.2 -6 22.27
vertex 9.6 -3.6 28.07
vertex 3.2 -3.6 21.54
endloop
endfacet
facet normal -0.696 -0.184 0.694
outer loop
vertex 9.6 -6 27.59
vertex 16 -6 34.01
vertex 16 -3.6 34.64
endloop
endfacet
facet normal -0.709 -0.14 0.691
outer loop
vertex 9.6 -6 27.59
vertex 16 -3.6 34.64
vertex 9.6 -3.6 28.07
endloop
endfacet
facet normal 0.659 0.427 0.619
outer loop
vertex 16 -6 34.01
vertex 22.4 -6 27.2
vertex 22.4 -3.6 25.54
endloop
endfacet
facet normal 0.809 -0.15 0.569
outer loop
vertex 16 -6 34.01
vertex 22.4 -3.6 25.54
vertex 16 -3.6 34.64
endloop
endfacet
facet normal 0.749 -0.091 0.656
outer loop
vertex 22.4 -6 27.2
vertex 28.8 -6 19.89
vertex 28.8 -3.6 20.22
endloop
endfacet
facet normal 0.565 0.468 0.679
outer loop
vertex 22.4 -6 27.2
vertex 28.8 -3.6 20.22
vertex 22.4 -3.6 25.54
endloop
endfacet
facet normal -0.618 -0.218 0.755
outer loop
vertex 28.8 -6 19.89
vertex 35.2 -6 25.13
vertex 35.2 -3.6 25.83
endloop
endfacet
facet normal -0.655 -0.104 0.748
outer loop
vertex 28.8 -6 19.89
vertex 35.2 -3.6 25.83
vertex 28.8 -3.6 20.22
endloop
endfacet
facet normal 0.076 -0.151 0.986
outer loop
vertex 35.2 -6 25.13
vertex 41.6 -6 24.64
vertex 41.6 -3.6 25.01
endloop
endfacet
facet normal 0.122 -0.275 0.954
outer loop
vertex 35.2 -6 25.13
vertex 41.6 -3.6 25.01
vertex 35.2 -3.6 25.83
endloop
endfacet
facet normal 0.268 0.481 0.835
outer loop
vertex 41.6 -6 24.64
vertex 48 -6 22.59
vertex 48 -3.6 21.2
endloop
endfacet
facet normal 0.507 -0.131 0.852
outer loop
vertex 41.6 -6 24.64
vertex 48 -3.6 21.2
vertex 41.6 -3.6 25.01
endloop
endfacet
facet normal 0.017 0.273 0.962
outer loop
vertex -48 -3.6 11.23
vertex -41.6 -3.6 11.12
vertex -41.6 -1.2 10.44
endloop
endfacet
facet normal 0.057 0.173 0.983
outer loop
vertex -48 -3.6 11.23
vertex -41.6 -1.2 10.44
vertex -48 -1.2 10.81
endloop
endfacet
facet normal -0.31 0.04 0.95
outer loop
vertex -41.6 -3.6 11.12
vertex -35.2 -3.6 13.2
vertex -35.2 -1.2 13.1
endloop
endfacet
facet normal -0.372 0.253 0.893
outer loop
vertex -41.6 -3.6 11.12
vertex -35.2 -1.2 13.1
vertex -41.6 -1.2 10.44
endloop
endfacet
facet normal -0.096 0.241 0.966
outer loop
vertex -35.2 -3.6 13.2
vertex -28.8 -3.6 13.84
vertex -28.8 -1.2 13.24
endloop
endfacet
facet normal -0.021 0.042 0.999
outer loop
vertex -35.2 -3.6 13.2
vertex -28.8 -1.2 13.24
vertex -35.2 -1.2 13.1
endloop
endfacet
facet normal 0.191 0.006 0.981
outer loop
vertex -28.8 -3.6 13.84
vertex -22.4 -3.6 12.59
vertex -22.4 -1.2 12.58
endloop
endfacet
facet normal 0.1 0.241 0.965
outer loop
vertex -28.8 -3.6 13.84
vertex -22.4 -1.2 12.58
vertex -28.8 -1.2 13.24
endloop
endfacet
facet normal -0.831 0.137 0.539
outer loop
vertex -22.4 -3.6 12.59
vertex -16 -3.6 22.45
vertex -16 -1.2 21.84
endloop
endfacet
facet normal -0.823 0.004 0.568
outer loop
vertex -22.4 -3.6 12.59
vertex -16 -1.2 21.84
vertex -22.4 -1.2 12.58
endloop
endfacet
facet normal -0.753 0.178 0.634
outer loop
vertex -16 -3.6 22.45
vertex -9.6 -3.6 30.05
vertex -9.6 -1.2 29.38
endloop
endfacet
facet normal -0.752 0.162 0.639
outer loop
vertex -16 -3.6 22.45
vertex -9.6 -1.2 29.38
vertex -16 -1.2 21.84
endloop
endfacet
facet normal -0.178 0.205 0.962
outer loop
vertex -9.6 -3.6 30.05
vertex -3.2 -3.6 31.24
vertex -3.2 -1.2 30.73
endloop
endfacet
facet normal -0.199 0.265 0.943
outer loop
vertex -9.6 -3.6 30.05
vertex -3.2 -1.2 30.73
vertex -9.6 -1.2 29.38
endloop
endfacet
facet normal 0.791 0.319 0.522
outer loop
vertex -3.2 -3.6 31.24
vertex 3.2 -3.6 21.54
vertex 3.2 -1.2 20.07
endloop
endfacet
facet normal 0.852 0.109 0.512
outer loop
vertex -3.2 -3.6 31.24
vertex 3.2 -1.2 20.07
vertex -3.2 -1.2 30.73
endloop
endfacet
facet normal -0.634 0.462 0.621
outer loop
vertex 3.2 -3.6 21.54
vertex 9.6 -3.6 28.07
vertex 9.6 -1.2 26.28
endloop
endfacet
facet normal -0.638 0.402 0.657
outer loop
vertex 3.2 -3.6 21.54
vertex 9.6 -1.2 26.28
vertex 3.2 -1.2 20.07
endloop
endfacet
facet normal -0.715 0.054 0.697
outer loop
vertex 9.6 -3.6 28.07
vertex 16 -3.6 34.64
vertex 16 -1.2 34.45
endloop
endfacet
facet normal -0.716 0.417 0.56
outer loop
vertex 9.6 -3.6 28.07
vertex 16 -1.2 34.45
vertex 9.6 -1.2 26.28
endloop
endfacet
facet normal 0.759 0.373 0.534
outer loop
vertex 16 -3.6 34.64
vertex 22.4 -3.6 25.54
vertex 22.4 -1.2 23.87
endloop
endfacet
facet normal 0.855 0.04 0.517
outer loop
vertex 16 -3.6 34.64
vertex 22.4 -1.2 23.87
vertex 16 -1.2 34.45
endloop
endfacet
facet normal 0.639 -0.045 0.768
outer loop
vertex 22.4 -3.6 25.54
vertex 28.8 -3.6 20.22
vertex 28.8 -1.2 20.36
endloop
endfacet
facet normal 0.41 0.522 0.748
outer loop
vertex 22.4 -3.6 25.54
vertex 28.8 -1.2 20.36
vertex 22.4 -1.2 23.87
endloop
endfacet
facet normal -0.598 0.419 0.683
outer loop
vertex 28.8 -3.6 20.22
vertex 35.2 -3.6 25.83
vertex 35.2 -1.2 24.35
endloop
endfacet
facet normal -0.528 -0.049 0.848
outer loop
vertex 28.8 -3.6 20.22
vertex 35.2 -1.2 24.35
vertex 28.8 -1.2 20.36
endloop
endfacet
facet normal 0.125 0.183 0.975
outer loop
vertex 35.2 -3.6 25.83
vertex 41.6 -3.6 25.01
vertex 41.6 -1.2 24.55
endloop
endfacet
facet normal -0.027 0.523 0.852
outer loop
vertex 35.2 -3.6 25.83
vertex 41.6 -1.2 24.55
vertex 35.2 -1.2 24.35
endloop
endfacet
facet normal 0.472 0.383 0.794
outer loop
vertex 41.6 -3.6 25.01
vertex 48 -3.6 21.2
vertex 48 -1.2 20.04
endloop
endfacet
facet normal 0.569 0.152 0.808
outer loop
vertex 41.6 -3.6 25.01
vertex 48 -1.2 20.04
vertex 41.6 -1.2 24.55
endloop
endfacet
facet normal 0.056 0.261 0.964
outer loop
vertex -48 -1.2 10.81
vertex -41.6 -1.2 10.44
vertex -41.6 1.2 9.79
endloop
endfacet
facet normal 0.02 0.347 0.938
outer loop
vertex -48 -1.2 10.81
vertex -41.6 1.2 9.79
vertex -48 1.2 9.92
endloop
endfacet
facet normal -0.364 0.323 0.874
outer loop
vertex -41.6 -1.2 10.44
vertex -35.2 -1.2 13.1
vertex -35.2 1.2 12.22
endloop
endfacet
facet normal -0.344 0.246 0.906
outer loop
vertex -41.6 -1.2 10.44
vertex -35.2 1.2 12.22
vertex -41.6 1.2 9.79
endloop
endfacet
facet normal -0.016 0.676 0.737
outer loop
vertex -35.2 -1.2 13.1
vertex -28.8 -1.2 13.24
vertex -28.8 1.2 11.04
endloop
endfacet
facet normal 0.17 0.342 0.924
outer loop
vertex -35.2 -1.2 13.1
vertex -28.8 1.2 11.04
vertex -35.2 1.2 12.22
endloop
endfacet
facet normal 0.096 0.36 0.928
outer loop
vertex -28.8 -1.2 13.24
vertex -22.4 -1.2 12.58
vertex -22.4 1.2 11.65
endloop
endfacet
facet normal -0.07 0.675 0.735
outer loop
vertex -28.8 -1.2 13.24
vertex -22.4 1.2 11.65
vertex -28.8 1.2 11.04
endloop
endfacet
facet normal -0.823 0.014 0.568
outer loop
vertex -22.4 -1.2 12.58
vertex -16 -1.2 21.84
vertex -16 1.2 21.78
endloop
endfacet
facet normal -0.828 0.202 0.523
outer loop
vertex -22.4 -1.2 12.58
vertex -16 1.2 21.78
vertex -22.4 1.2 11.65
endloop
endfacet
facet normal -0.753 0.154 0.64
outer loop
vertex -16 -1.2 21.84
vertex -9.6 -1.2 29.38
vertex -9.6 1.2 28.8
endloop
endfacet
facet normal -0.739 0.016 0.674
outer loop
vertex -16 -1.2 21.84
vertex -9.6 1.2 28.8
vertex -16 1.2 21.78
endloop
endfacet
facet normal -0.174 0.539 0.824
outer loop
vertex -9.6 -1.2 29.38
vertex -3.2 -1.2 30.73
vertex -3.2 1.2 29.16
endloop
endfacet
facet normal -0.054 0.234 0.971
outer loop
vertex -9.6 -1.2 29.38
vertex -3.2 1.2 29.16
vertex -9.6 1.2 28.8
endloop
endfacet
facet normal 0.835 0.228 0.501
outer loop
vertex -3.2 -1.2 30.73
vertex 3.2 -1.2 20.07
vertex 3.2 1.2 18.98
endloop
endfacet
facet normal 0.8 0.329 0.503
outer loop
vertex -3.2 -1.2 30.73
vertex 3.2 1.2 18.98
vertex -3.2 1.2 29.16
endloop
endfacet
facet normal -0.643 0.384 0.662
outer loop
vertex 3.2 -1.2 20.07
vertex 9.6 -1.2 26.28
vertex 9.6 1.2 24.89
endloop
endfacet
facet normal -0.644 0.317 0.697
outer loop
vertex 3.2 -1.2 20.07
vertex 9.6 1.2 24.89
vertex 3.2 1.2 18.98
endloop
endfacet
facet normal -0.786 0.052 0.616
outer loop
vertex 9.6 -1.2 26.28
vertex 16 -1.2 34.45
vertex 16 1.2 34.25
endloop
endfacet
facet normal -0.785 0.311 0.536
outer loop
vertex 9.6 -1.2 26.28
vertex 16 1.2 34.25
vertex 9.6 1.2 24.89
endloop
endfacet
facet normal 0.827 0.257 0.5
outer loop
vertex 16 -1.2 34.45
vertex 22.4 -1.2 23.87
vertex 22.4 1.2 22.64
endloop
endfacet
facet normal 0.875 0.041 0.482
outer loop
vertex 16 -1.2 34.45
vertex 22.4 1.2 22.64
vertex 16 1.2 34.25
endloop
endfacet
facet normal 0.459 -0.299 0.837
outer loop
vertex 22.4 -1.2 23.87
vertex 28.8 -1.2 20.36
vertex 28.8 1.2 21.22
endloop
endfacet
facet normal 0.193 0.448 0.873
outer loop
vertex 22.4 -1.2 23.87
vertex 28.8 1.2 21.22
vertex 22.4 1.2 22.64
endloop
endfacet
facet normal -0.518 -0.201 0.831
outer loop
vertex 28.8 -1.2 20.36
vertex 35.2 -1.2 24.35
vertex 35.2 1.2 24.93
endloop
endfacet
facet normal -0.479 -0.295 0.826
outer loop
vertex 28.8 -1.2 20.36
vertex 35.2 1.2 24.93
vertex 28.8 1.2 21.22
endloop
endfacet
facet normal -0.027 0.513 0.858
outer loop
vertex 35.2 -1.2 24.35
vertex 41.6 -1.2 24.55
vertex 41.6 1.2 23.12
endloop
endfacet
facet normal 0.266 -0.227 0.937
outer loop
vertex 35.2 -1.2 24.35
vertex 41.6 1.2 23.12
vertex 35.2 1.2 24.93
endloop
endfacet
facet normal 0.553 -0.277 0.785
outer loop
vertex 41.6 -1.2 24.55
vertex 48 -1.2 20.04
vertex 48 1.2 20.89
endloop
endfacet
facet normal 0.286 0.492 0.822
outer loop
vertex 41.6 -1.2 24.55
vertex 48 1.2 20.89
vertex 41.6 1.2 23.12
endloop
endfacet
facet normal 0.021 -0.045 0.999
outer loop
vertex -48 1.2 9.92
vertex -41.6 1.2 9.79
vertex -41.6 3.6 9.89
endloop
endfacet
facet normal 0.113 -0.29 0.95
outer loop
vertex -48 1.2 9.92
vertex -41.6 3.6 9.89
vertex -48 3.6 10.65
endloop
endfacet
facet normal -0.355 0.044 0.934
outer loop
vertex -41.6 1.2 9.79
vertex -35.2 1.2 12.22
vertex -35.2 3.6 12.1
endloop
endfacet
facet normal -0.326 -0.043 0.944
outer loop
vertex -41.6 1.2 9.79
vertex -35.2 3.6 12.1
vertex -41.6 3.6 9.89
endloop
endfacet
facet normal 0.174 0.286 0.942
outer loop
vertex -35.2 1.2 12.22
vertex -28.8 1.2 11.04
vertex -28.8 3.6 10.31
endloop
endfacet
facet normal 0.27 0.046 0.962
outer loop
vertex -35.2 1.2 12.22
vertex -28.8 3.6 10.31
vertex -35.2 3.6 12.1
endloop
endfacet
facet normal -0.086 0.43 0.899
outer loop
vertex -28.8 1.2 11.04
vertex -22.4 1.2 11.65
vertex -22.4 3.6 10.5
endloop
endfacet
facet normal -0.028 0.29 0.957
outer loop
vertex -28.8 1.2 11.04
vertex -22.4 3.6 10.5
vertex -28.8 3.6 10.31
endloop
endfacet
facet normal -0.845 0.048 0.533
outer loop
vertex -22.4 1.2 11.65
vertex -16 1.2 21.78
vertex -16 3.6 21.57
endloop
endfacet
facet normal -0.842 0.233 0.487
outer loop
vertex -22.4 1.2 11.65
vertex -16 3.6 21.57
vertex -22.4 3.6 10.5
endloop
endfacet
facet normal -0.738 -0.041 0.673
outer loop
vertex -16 1.2 21.78
vertex -9.6 1.2 28.8
vertex -9.6 3.6 28.94
endloop
endfacet
facet normal -0.754 0.059 0.654
outer loop
vertex -16 1.2 21.78
vertex -9.6 3.6 28.94
vertex -16 3.6 21.57
endloop
endfacet
facet normal -0.05 0.459 0.887
outer loop
vertex -9.6 1.2 28.8
vertex -3.2 1.2 29.16
vertex -3.2 3.6 27.92
endloop
endfacet
facet normal 0.158 -0.059 0.986
outer loop
vertex -9.6 1.2 28.8
vertex -3.2 3.6 27.92
vertex -9.6 3.6 28.94
endloop
endfacet
facet normal 0.846 0.035 0.532
outer loop
vertex -3.2 1.2 29.16
vertex 3.2 1.2 18.98
vertex 3.2 3.6 18.82
endloop
endfacet
facet normal 0.784 0.285 0.552
outer loop
vertex -3.2 1.2 29.16
vertex 3.2 3.6 18.82
vertex -3.2 3.6 27.92
endloop
endfacet
facet normal -0.579 0.521 0.627
outer loop
vertex 3.2 1.2 18.98
vertex 9.6 1.2 24.89
vertex 9.6 3.6 22.9
endloop
endfacet
facet normal -0.536 0.056 0.842
outer loop
vertex 3.2 1.2 18.98
vertex 9.6 3.6 22.9
vertex 3.2 3.6 18.82
endloop
endfacet
facet normal -0.82 0.117 0.561
outer loop
vertex 9.6 1.2 24.89
vertex 16 1.2 34.25
vertex 16 3.6 33.75
endloop
endfacet
facet normal -0.794 0.389 0.468
outer loop
vertex 9.6 1.2 24.89
vertex 16 3.6 33.75
vertex 9.6 3.6 22.9
endloop
endfacet
facet normal 0.875 0.029 0.482
outer loop
vertex 16 1.2 34.25
vertex 22.4 1.2 22.64
vertex 22.4 3.6 22.49
endloop
endfacet
facet normal 0.865 0.102 0.491
outer loop
vertex 16 1.2 34.25
vertex 22.4 3.6 22.49
vertex 16 3.6 33.75
endloop
endfacet
facet normal 0.214 0.122 0.969
outer loop
vertex 22.4 1.2 22.64
vertex 28.8 1.2 21.22
vertex 28.8 3.6 20.92
endloop
endfacet
facet normal 0.238 0.059 0.969
outer loop
vertex 22.4 1.2 22.64
vertex 28.8 3.6 20.92
vertex 22.4 3.6 22.49
endloop
endfacet
facet normal -0.464 0.379 0.8
outer loop
vertex 28.8 1.2 21.22
vertex 35.2 1.2 24.93
vertex 35.2 3.6 23.8
endloop
endfacet
facet normal -0.407 0.114 0.906
outer loop
vertex 28.8 1.2 21.22
vertex 35.2 3.6 23.8
vertex 28.8 3.6 20.92
endloop
endfacet
facet normal 0.255 0.355 0.899
outer loop
vertex 35.2 1.2 24.93
vertex 41.6 1.2 23.12
vertex 41.6 3.6 22.17
endloop
endfacet
facet normal 0.223 0.417 0.881
outer loop
vertex 35.2 1.2 24.93
vertex 41.6 3.6 22.17
vertex 35.2 3.6 23.8
endloop
endfacet
facet normal 0.328 0.059 0.943
outer loop
vertex 41.6 1.2 23.12
vertex 48 1.2 20.89
vertex 48 3.6 20.74
endloop
endfacet
facet normal 0.204 0.359 0.911
outer loop
vertex 41.6 1.2 23.12
vertex 48 3.6 20.74
vertex 41.6 3.6 22.17
endloop
endfacet
facet normal 0.117 0.125 0.985
outer loop
vertex -48 3.6 10.65
vertex -41.6 3.6 9.89
vertex -41.6 6 9.59
endloop
endfacet
facet normal 0.074 0.233 0.97
outer loop
vertex -48 3.6 10.65
vertex -41.6 6 9.59
vertex -48 6 10.08
endloop
endfacet
facet normal -0.301 0.387 0.872
outer loop
vertex -41.6 3.6 9.89
vertex -35.2 3.6 12.1
vertex -35.2 6 11.04
endloop
endfacet
facet normal -0.219 0.122 0.968
outer loop
vertex -41.6 3.6 9.89
vertex -35.2 6 11.04
vertex -41.6 6 9.59
endloop
endfacet
facet normal 0.268 0.125 0.955
outer loop
vertex -35.2 3.6 12.1
vertex -28.8 3.6 10.31
vertex -28.8 6 10
endloop
endfacet
facet normal 0.147 0.402 0.904
outer loop
vertex -35.2 3.6 12.1
vertex -28.8 6 10
vertex -35.2 6 11.04
endloop
endfacet
facet normal -0.029 0.129 0.991
outer loop
vertex -28.8 3.6 10.31
vertex -22.4 3.6 10.5
vertex -22.4 6 10.18
endloop
endfacet
facet normal -0.029 0.13 0.991
outer loop
vertex -28.8 3.6 10.31
vertex -22.4 6 10.18
vertex -28.8 6 10
endloop
endfacet
facet normal -0.852 0.178 0.493
outer loop
vertex -22.4 3.6 10.5
vertex -16 3.6 21.57
vertex -16 6 20.7
endloop
endfacet
facet normal -0.852 0.068 0.519
outer loop
vertex -22.4 3.6 10.5
vertex -16 6 20.7
vertex -22.4 6 10.18
endloop
endfacet
facet normal -0.755 -0.017 0.655
outer loop
vertex -16 3.6 21.57
vertex -9.6 3.6 28.94
vertex -9.6 6 29.01
endloop
endfacet
facet normal -0.774 0.215 0.596
outer loop
vertex -16 3.6 21.57
vertex -9.6 6 29.01
vertex -16 6 20.7
endloop
endfacet
facet normal 0.137 0.5 0.855
outer loop
vertex -9.6 3.6 28.94
vertex -3.2 3.6 27.92
vertex -3.2 6 26.52
endloop
endfacet
facet normal 0.362 -0.024 0.932
outer loop
vertex -9.6 3.6 28.94
vertex -3.2 6 26.52
vertex -9.6 6 29.01
endloop
endfacet
facet normal 0.813 -0.113 0.572
outer loop
vertex -3.2 3.6 27.92
vertex 3.2 3.6 18.82
vertex 3.2 6 19.29
endloop
endfacet
facet normal 0.698 0.361 0.618
outer loop
vertex -3.2 3.6 27.92
vertex 3.2 6 19.29
vertex -3.2 6 26.52
endloop
endfacet
facet normal -0.536 0.045 0.843
outer loop
vertex 3.2 3.6 18.82
vertex 9.6 3.6 22.9
vertex 9.6 6 22.77
endloop
endfacet
facet normal -0.47 -0.171 0.866
outer loop
vertex 3.2 3.6 18.82
vertex 9.6 6 22.77
vertex 3.2 6 19.29
endloop
endfacet
facet normal -0.806 0.355 0.475
outer loop
vertex 9.6 3.6 22.9
vertex 16 3.6 33.75
vertex 16 6 31.96
endloop
endfacet
facet normal -0.82 0.031 0.571
outer loop
vertex 9.6 3.6 22.9
vertex 16 6 31.96
vertex 9.6 6 22.77
endloop
endfacet
facet normal 0.869 0.006 0.494
outer loop
vertex 16 3.6 33.75
vertex 22.4 3.6 22.49
vertex 22.4 6 22.46
endloop
endfacet
facet normal 0.765 0.385 0.516
outer loop
vertex 16 3.6 33.75
vertex 22.4 6 22.46
vertex 16 6 31.96
endloop
endfacet
facet normal 0.234 -0.198 0.952
outer loop
vertex 22.4 3.6 22.49
vertex 28.8 3.6 20.92
vertex 28.8 6 21.42
endloop
endfacet
facet normal 0.161 0.012 0.987
outer loop
vertex 22.4 3.6 22.49
vertex 28.8 6 21.42
vertex 22.4 6 22.46
endloop
endfacet
facet normal -0.397 0.25 0.883
outer loop
vertex 28.8 3.6 20.92
vertex 35.2 3.6 23.8
vertex 35.2 6 23.12
endloop
endfacet
facet normal -0.252 -0.197 0.948
outer loop
vertex 28.8 3.6 20.92
vertex 35.2 6 23.12
vertex 28.8 6 21.42
endloop
endfacet
facet normal 0.24 0.225 0.944
outer loop
vertex 35.2 3.6 23.8
vertex 41.6 3.6 22.17
vertex 41.6 6 21.6
endloop
endfacet
facet normal 0.222 0.265 0.938
outer loop
vertex 35.2 3.6 23.8
vertex 41.6 6 21.6
vertex 35.2 6 23.12
endloop
endfacet
facet normal 0.217 -0.113 0.97
outer loop
vertex 41.6 3.6 22.17
vertex 48 3.6 20.74
vertex 48 6 21.02
endloop
endfacet
facet normal 0.088 0.231 0.969
outer loop
vertex 41.6 3.6 22.17
vertex 48 6 21.02
vertex 41.6 6 21.6
endloop
endfacet
facet normal 0.075 -0.126 0.989
outer loop
vertex -48 6 10.08
vertex -41.6 6 9.59
vertex -41.6 8.4 9.9
endloop
endfacet
facet normal 0.124 -0.259 0.958
outer loop
vertex -48 6 10.08
vertex -41.6 8.4 9.9
vertex -48 8.4 10.73
endloop
endfacet
facet normal -0.213 0.253 0.944
outer loop
vertex -41.6 6 9.59
vertex -35.2 6 11.04
vertex -35.2 8.4 10.39
endloop
endfacet
facet normal -0.077 -0.126 0.989
outer loop
vertex -41.6 6 9.59
vertex -35.2 8.4 10.39
vertex -41.6 8.4 9.9
endloop
endfacet
facet normal 0.16 0.066 0.985
outer loop
vertex -35.2 6 11.04
vertex -28.8 6 10
vertex -28.8 8.4 9.83
endloop
endfacet
facet normal 0.084 0.259 0.962
outer loop
vertex -35.2 6 11.04
vertex -28.8 8.4 9.83
vertex -35.2 8.4 10.39
endloop
endfacet
facet normal -0.029 0.234 0.972
outer loop
vertex -28.8 6 10
vertex -22.4 6 10.18
vertex -22.4 8.4 9.61
endloop
endfacet
facet normal 0.035 0.067 0.997
outer loop
vertex -28.8 6 10
vertex -22.4 8.4 9.61
vertex -28.8 8.4 9.83
endloop
endfacet
facet normal -0.854 0.021 0.52
outer loop
vertex -22.4 6 10.18
vertex -16 6 20.7
vertex -16 8.4 20.61
endloop
endfacet
facet normal -0.858 0.12 0.499
outer loop
vertex -22.4 6 10.18
vertex -16 8.4 20.61
vertex -22.4 8.4 9.61
endloop
endfacet
facet normal -0.79 -0.073 0.609
outer loop
vertex -16 6 20.7
vertex -9.6 6 29.01
vertex -9.6 8.4 29.29
endloop
endfacet
facet normal -0.805 0.024 0.593
outer loop
vertex -16 6 20.7
vertex -9.6 8.4 29.29
vertex -16 8.4 20.61
endloop
endfacet
facet normal 0.326 0.439 0.837
outer loop
vertex -9.6 6 29.01
vertex -3.2 6 26.52
vertex -3.2 8.4 25.26
endloop
endfacet
facet normal 0.531 -0.1 0.842
outer loop
vertex -9.6 6 29.01
vertex -3.2 8.4 25.26
vertex -9.6 8.4 29.29
endloop
endfacet
facet normal 0.743 0.122 0.658
outer loop
vertex -3.2 6 26.52
vertex 3.2 6 19.29
vertex 3.2 8.4 18.85
endloop
endfacet
facet normal 0.663 0.348 0.663
outer loop
vertex -3.2 6 26.52
vertex 3.2 8.4 18.85
vertex -3.2 8.4 25.26
endloop
endfacet
facet normal -0.456 0.292 0.841
outer loop
vertex 3.2 6 19.29
vertex 9.6 6 22.77
vertex 9.6 8.4 21.93
endloop
endfacet
facet normal -0.428 0.165 0.889
outer loop
vertex 3.2 6 19.29
vertex 9.6 8.4 21.93
vertex 3.2 8.4 18.85
endloop
endfacet
facet normal -0.808 0.175 0.562
outer loop
vertex 9.6 6 22.77
vertex 16 6 31.96
vertex 16 8.4 31.21
endloop
endfacet
facet normal -0.808 0.194 0.557
outer loop
vertex 9.6 6 22.77
vertex 16 8.4 31.21
vertex 9.6 8.4 21.93
endloop
endfacet
facet normal 0.809 0.223 0.545
outer loop
vertex 16 6 31.96
vertex 22.4 6 22.46
vertex 22.4 8.4 21.48
endloop
endfacet
facet normal 0.824 0.169 0.541
outer loop
vertex 16 6 31.96
vertex 22.4 8.4 21.48
vertex 16 8.4 31.21
endloop
endfacet
facet normal 0.148 0.386 0.911
outer loop
vertex 22.4 6 22.46
vertex 28.8 6 21.42
vertex 28.8 8.4 20.4
endloop
endfacet
facet normal 0.154 0.374 0.915
outer loop
vertex 22.4 6 22.46
vertex 28.8 8.4 20.4
vertex 22.4 8.4 21.48
endloop
endfacet
facet normal -0.211 0.571 0.793
outer loop
vertex 28.8 6 21.42
vertex 35.2 6 23.12
vertex 35.2 8.4 21.39
endloop
endfacet
facet normal -0.141 0.386 0.912
outer loop
vertex 28.8 6 21.42
vertex 35.2 8.4 21.39
vertex 28.8 8.4 20.4
endloop
endfacet
facet normal 0.226 0.209 0.952
outer loop
vertex 35.2 6 23.12
vertex 41.6 6 21.6
vertex 41.6 8.4 21.07
endloop
endfacet
facet normal 0.04 0.584 0.811
outer loop
vertex 35.2 6 23.12
vertex 41.6 8.4 21.07
vertex 35.2 8.4 21.39
endloop
endfacet
facet normal 0.087 0.273 0.958
outer loop
vertex 41.6 6 21.6
vertex 48 6 21.02
vertex 48 8.4 20.34
endloop
endfacet
facet normal 0.111 0.213 0.971
outer loop
vertex 41.6 6 21.6
vertex 48 8.4 20.34
vertex 41.6 8.4 21.07
endloop
endfacet
facet normal 0.125 0.226 0.966
outer loop
vertex -48 8.4 10.73
vertex -41.6 8.4 9.9
vertex -41.6 10.8 9.34
endloop
endfacet
facet normal 0.189 0.064 0.98
outer loop
vertex -48 8.4 10.73
vertex -41.6 10.8 9.34
vertex -48 10.8 10.57
endloop
endfacet
facet normal -0.075 0.234 0.969
outer loop
vertex -41.6 8.4 9.9
vertex -35.2 8.4 10.39
vertex -35.2 10.8 9.81
endloop
endfacet
facet normal -0.072 0.227 0.971
outer loop
vertex -41.6 8.4 9.9
vertex -35.2 10.8 9.81
vertex -41.6 10.8 9.34
endloop
endfacet
facet normal 0.087 0.032 0.996
outer loop
vertex -35.2 8.4 10.39
vertex -28.8 8.4 9.83
vertex -28.8 10.8 9.76
endloop
endfacet
facet normal 0.009 0.235 0.972
outer loop
vertex -35.2 8.4 10.39
vertex -28.8 10.8 9.76
vertex -35.2 10.8 9.81
endloop
endfacet
facet normal 0.035 0.113 0.993
outer loop
vertex -28.8 8.4 9.83
vertex -22.4 8.4 9.61
vertex -22.4 10.8 9.33
endloop
endfacet
facet normal 0.066 0.033 0.997
outer loop
vertex -28.8 8.4 9.83
vertex -22.4 10.8 9.33
vertex -28.8 10.8 9.76
endloop
endfacet
facet normal -0.862 -0.079 0.501
outer loop
vertex -22.4 8.4 9.61
vertex -16 8.4 20.61
vertex -16 10.8 20.98
endloop
endfacet
facet normal -0.875 0.055 0.481
outer loop
vertex -22.4 8.4 9.61
vertex -16 10.8 20.98
vertex -22.4 10.8 9.33
endloop
endfacet
facet normal -0.746 0.375 0.55
outer loop
vertex -16 8.4 20.61
vertex -9.6 8.4 29.29
vertex -9.6 10.8 27.65
endloop
endfacet
facet normal -0.717 -0.108 0.688
outer loop
vertex -16 8.4 20.61
vertex -9.6 10.8 27.65
vertex -16 10.8 20.98
endloop
endfacet
facet normal 0.523 -0.2 0.829
outer loop
vertex -9.6 8.4 29.29
vertex -3.2 8.4 25.26
vertex -3.2 10.8 25.84
endloop
endfacet
facet normal 0.228 0.549 0.804
outer loop
vertex -9.6 8.4 29.29
vertex -3.2 10.8 25.84
vertex -9.6 10.8 27.65
endloop
endfacet
facet normal 0.679 0.279 0.679
outer loop
vertex -3.2 8.4 25.26
vertex 3.2 8.4 18.85
vertex 3.2 10.8 17.86
endloop
endfacet
facet normal 0.771 -0.149 0.619
outer loop
vertex -3.2 8.4 25.26
vertex 3.2 10.8 17.86
vertex -3.2 10.8 25.84
endloop
endfacet
facet normal -0.373 0.512 0.774
outer loop
vertex 3.2 8.4 18.85
vertex 9.6 8.4 21.93
vertex 9.6 10.8 20.34
endloop
endfacet
facet normal -0.338 0.358 0.87
outer loop
vertex 3.2 8.4 18.85
vertex 9.6 10.8 20.34
vertex 3.2 10.8 17.86
endloop
endfacet
facet normal -0.788 0.29 0.543
outer loop
vertex 9.6 8.4 21.93
vertex 16 8.4 31.21
vertex 16 10.8 29.93
endloop
endfacet
facet normal -0.781 0.345 0.521
outer loop
vertex 9.6 8.4 21.93
vertex 16 10.8 29.93
vertex 9.6 10.8 20.34
endloop
endfacet
facet normal 0.815 0.223 0.536
outer loop
vertex 16 8.4 31.21
vertex 22.4 8.4 21.48
vertex 22.4 10.8 20.48
endloop
endfacet
facet normal 0.793 0.287 0.537
outer loop
vertex 16 8.4 31.21
vertex 22.4 10.8 20.48
vertex 16 10.8 29.93
endloop
endfacet
facet normal 0.153 -0.383 0.911
outer loop
vertex 22.4 8.4 21.48
vertex 28.8 8.4 20.4
vertex 28.8 10.8 21.41
endloop
endfacet
facet normal -0.133 0.381 0.915
outer loop
vertex 22.4 8.4 21.48
vertex 28.8 10.8 21.41
vertex 22.4 10.8 20.48
endloop
endfacet
facet normal -0.138 0.429 0.893
outer loop
vertex 28.8 8.4 20.4
vertex 35.2 8.4 21.39
vertex 35.2 10.8 20.23
endloop
endfacet
facet normal 0.167 -0.382 0.909
outer loop
vertex 28.8 8.4 20.4
vertex 35.2 10.8 20.23
vertex 28.8 10.8 21.41
endloop
endfacet
facet normal 0.047 0.325 0.945
outer loop
vertex 35.2 8.4 21.39
vertex 41.6 8.4 21.07
vertex 41.6 10.8 20.25
endloop
endfacet
facet normal -0.002 0.434 0.901
outer loop
vertex 35.2 8.4 21.39
vertex 41.6 10.8 20.25
vertex 35.2 10.8 20.23
endloop
endfacet
facet normal 0.113 -0.156 0.981
outer loop
vertex 41.6 8.4 21.07
vertex 48 8.4 20.34
vertex 48 10.8 20.72
endloop
endfacet
facet normal -0.07 0.324 0.943
outer loop
vertex 41.6 8.4 21.07
vertex 48 10.8 20.72
vertex 41.6 10.8 20.25
endloop
endfacet
facet normal 0.171 0.431 0.886
outer loop
vertex -48 10.8 10.57
vertex -41.6 10.8 9.34
vertex -41.6 13.2 8.17
endloop
endfacet
facet normal 0.344 0.024 0.939
outer loop
vertex -48 10.8 10.57
vertex -41.6 13.2 8.17
vertex -48 13.2 10.51
endloop
endfacet
facet normal -0.069 -0.371 0.926
outer loop
vertex -41.6 10.8 9.34
vertex -35.2 10.8 9.81
vertex -35.2 13.2 10.77
endloop
endfacet
facet normal -0.344 0.411 0.844
outer loop
vertex -41.6 10.8 9.34
vertex -35.2 13.2 10.77
vertex -41.6 13.2 8.17
endloop
endfacet
facet normal 0.009 0.166 0.986
outer loop
vertex -35.2 10.8 9.81
vertex -28.8 10.8 9.76
vertex -28.8 13.2 9.35
endloop
endfacet
facet normal 0.202 -0.364 0.909
outer loop
vertex -35.2 10.8 9.81
vertex -28.8 13.2 9.35
vertex -35.2 13.2 10.77
endloop
endfacet
facet normal 0.066 -0.059 0.996
outer loop
vertex -28.8 10.8 9.76
vertex -22.4 10.8 9.33
vertex -22.4 13.2 9.48
endloop
endfacet
facet normal -0.019 0.166 0.986
outer loop
vertex -28.8 10.8 9.76
vertex -22.4 13.2 9.48
vertex -28.8 13.2 9.35
endloop
endfacet
facet normal -0.876 0.045 0.481
outer loop
vertex -22.4 10.8 9.33
vertex -16 10.8 20.98
vertex -16 13.2 20.76
endloop
endfacet
facet normal -0.869 -0.029 0.493
outer loop
vertex -22.4 10.8 9.33
vertex -16 13.2 20.76
vertex -22.4 13.2 9.48
endloop
endfacet
facet normal -0.699 0.249 0.671
outer loop
vertex -16 10.8 20.98
vertex -9.6 10.8 27.65
vertex -9.6 13.2 26.76
endloop
endfacet
facet normal -0.683 0.068 0.728
outer loop
vertex -16 10.8 20.98
vertex -9.6 13.2 26.76
vertex -16 13.2 20.76
endloop
endfacet
facet normal 0.26 -0.303 0.917
outer loop
vertex -9.6 10.8 27.65
vertex -3.2 10.8 25.84
vertex -3.2 13.2 26.63
endloop
endfacet
facet normal 0.02 0.348 0.937
outer loop
vertex -9.6 10.8 27.65
vertex -3.2 13.2 26.63
vertex -9.6 13.2 26.76
endloop
endfacet
facet normal 0.775 0.117 0.622
outer loop
vertex -3.2 10.8 25.84
vertex 3.2 10.8 17.86
vertex 3.2 13.2 17.41
endloop
endfacet
facet normal 0.807 -0.185 0.56
outer loop
vertex -3.2 10.8 25.84
vertex 3.2 13.2 17.41
vertex -3.2 13.2 26.63
endloop
endfacet
facet normal -0.361 0.055 0.931
outer loop
vertex 3.2 10.8 17.86
vertex 9.6 10.8 20.34
vertex 9.6 13.2 20.2
endloop
endfacet
facet normal -0.394 0.171 0.903
outer loop
vertex 3.2 10.8 17.86
vertex 9.6 13.2 20.2
vertex 3.2 13.2 17.41
endloop
endfacet
facet normal -0.826 0.116 0.551
outer loop
vertex 9.6 10.8 20.34
vertex 16 10.8 29.93
vertex 16 13.2 29.43
endloop
endfacet
facet normal -0.821 0.034 0.57
outer loop
vertex 9.6 10.8 20.34
vertex 16 13.2 29.43
vertex 9.6 13.2 20.2
endloop
endfacet
facet normal 0.822 0.123 0.556
outer loop
vertex 16 10.8 29.93
vertex 22.4 10.8 20.48
vertex 22.4 13.2 19.95
endloop
endfacet
facet normal 0.823 0.117 0.556
outer loop
vertex 16 10.8 29.93
vertex 22.4 13.2 19.95
vertex 16 13.2 29.43
endloop
endfacet
facet normal -0.143 -0.111 0.983
outer loop
vertex 22.4 10.8 20.48
vertex 28.8 10.8 21.41
vertex 28.8 13.2 21.68
endloop
endfacet
facet normal -0.255 0.208 0.944
outer loop
vertex 22.4 10.8 20.48
vertex 28.8 13.2 21.68
vertex 22.4 13.2 19.95
endloop
endfacet
facet normal 0.18 0.061 0.982
outer loop
vertex 28.8 10.8 21.41
vertex 35.2 10.8 20.23
vertex 35.2 13.2 20.08
endloop
endfacet
facet normal 0.24 -0.109 0.965
outer loop
vertex 28.8 10.8 21.41
vertex 35.2 13.2 20.08
vertex 28.8 13.2 21.68
endloop
endfacet
facet normal -0.002 0.17 0.985
outer loop
vertex 35.2 10.8 20.23
vertex 41.6 10.8 20.25
vertex 41.6 13.2 19.83
endloop
endfacet
facet normal 0.039 0.062 0.997
outer loop
vertex 35.2 10.8 20.23
vertex 41.6 13.2 19.83
vertex 35.2 13.2 20.08
endloop
endfacet
facet normal -0.069 0.355 0.932
outer loop
vertex 41.6 10.8 20.25
vertex 48 10.8 20.72
vertex 48 13.2 19.81
endloop
endfacet
facet normal 0.004 0.17 0.985
outer loop
vertex 41.6 10.8 20.25
vertex 48 13.2 19.81
vertex 41.6 13.2 19.83
endloop
endfacet
facet normal 0.34 0.144 0.929
outer loop
vertex -48 13.2 10.51
vertex -41.6 13.2 8.17
vertex -41.6 15.6 7.8
endloop
endfacet
facet normal 0.422 -0.108 0.9
outer loop
vertex -48 13.2 10.51
vertex -41.6 15.6 7.8
vertex -48 15.6 10.8
endloop
endfacet
facet normal -0.377 0.044 0.925
outer loop
vertex -41.6 13.2 8.17
vertex -35.2 13.2 10.77
vertex -35.2 15.6 10.66
endloop
endfacet
facet normal -0.405 0.14 0.904
outer loop
vertex -41.6 13.2 8.17
vertex -35.2 15.6 10.66
vertex -41.6 15.6 7.8
endloop
endfacet
facet normal 0.194 -0.444 0.875
outer loop
vertex -35.2 13.2 10.77
vertex -28.8 13.2 9.35
vertex -28.8 15.6 10.57
endloop
endfacet
facet normal 0.014 0.047 0.999
outer loop
vertex -35.2 13.2 10.77
vertex -28.8 15.6 10.57
vertex -35.2 15.6 10.66
endloop
endfacet
facet normal -0.019 0.052 0.998
outer loop
vertex -28.8 13.2 9.35
vertex -22.4 13.2 9.48
vertex -22.4 15.6 9.35
endloop
endfacet
facet normal 0.168 -0.447 0.879
outer loop
vertex -28.8 13.2 9.35
vertex -22.4 15.6 9.35
vertex -28.8 15.6 10.57
endloop
endfacet
facet normal -0.864 -0.111 0.49
outer loop
vertex -22.4 13.2 9.48
vertex -16 13.2 20.76
vertex -16 15.6 21.3
endloop
endfacet
facet normal -0.881 0.025 0.472
outer loop
vertex -22.4 13.2 9.48
vertex -16 15.6 21.3
vertex -22.4 15.6 9.35
endloop
endfacet
facet normal -0.683 0.054 0.728
outer loop
vertex -16 13.2 20.76
vertex -9.6 13.2 26.76
vertex -9.6 15.6 26.58
endloop
endfacet
facet normal -0.627 -0.171 0.76
outer loop
vertex -16 13.2 20.76
vertex -9.6 15.6 26.58
vertex -16 15.6 21.3
endloop
endfacet
facet normal 0.019 0.384 0.923
outer loop
vertex -9.6 13.2 26.76
vertex -3.2 13.2 26.63
vertex -3.2 15.6 25.63
endloop
endfacet
facet normal 0.147 0.074 0.986
outer loop
vertex -9.6 13.2 26.76
vertex -3.2 15.6 25.63
vertex -9.6 15.6 26.58
endloop
endfacet
facet normal 0.778 -0.321 0.54
outer loop
vertex -3.2 13.2 26.63
vertex 3.2 13.2 17.41
vertex 3.2 15.6 18.83
endloop
endfacet
facet normal 0.7 0.274 0.659
outer loop
vertex -3.2 13.2 26.63
vertex 3.2 15.6 18.83
vertex -3.2 15.6 25.63
endloop
endfacet
facet normal -0.387 -0.256 0.886
outer loop
vertex 3.2 13.2 17.41
vertex 9.6 13.2 20.2
vertex 9.6 15.6 20.89
endloop
endfacet
facet normal -0.266 -0.493 0.828
outer loop
vertex 3.2 13.2 17.41
vertex 9.6 15.6 20.89
vertex 3.2 15.6 18.83
endloop
endfacet
facet normal -0.82 0.072 0.568
outer loop
vertex 9.6 13.2 20.2
vertex 16 13.2 29.43
vertex 16 15.6 29.12
endloop
endfacet
facet normal -0.777 -0.175 0.605
outer loop
vertex 9.6 13.2 20.2
vertex 16 15.6 29.12
vertex 9.6 15.6 20.89
endloop
endfacet
facet normal 0.81 -0.21 0.547
outer loop
vertex 16 13.2 29.43
vertex 22.4 13.2 19.95
vertex 22.4 15.6 20.87
endloop
endfacet
facet normal 0.788 0.078 0.611
outer loop
vertex 16 13.2 29.43
vertex 22.4 15.6 20.87
vertex 16 15.6 29.12
endloop
endfacet
facet normal -0.257 -0.165 0.952
outer loop
vertex 22.4 13.2 19.95
vertex 28.8 13.2 21.68
vertex 28.8 15.6 22.1
endloop
endfacet
facet normal -0.176 -0.353 0.919
outer loop
vertex 22.4 13.2 19.95
vertex 28.8 15.6 22.1
vertex 22.4 15.6 20.87
endloop
endfacet
facet normal 0.241 -0.086 0.967
outer loop
vertex 28.8 13.2 21.68
vertex 35.2 13.2 20.08
vertex 35.2 15.6 20.3
endloop
endfacet
facet normal 0.267 -0.165 0.949
outer loop
vertex 28.8 13.2 21.68
vertex 35.2 15.6 20.3
vertex 28.8 15.6 22.1
endloop
endfacet
facet normal 0.038 -0.222 0.974
outer loop
vertex 35.2 13.2 20.08
vertex 41.6 13.2 19.83
vertex 41.6 15.6 20.38
endloop
endfacet
facet normal -0.013 -0.089 0.996
outer loop
vertex 35.2 13.2 20.08
vertex 41.6 15.6 20.38
vertex 35.2 15.6 20.3
endloop
endfacet
facet normal 0.004 -0.165 0.986
outer loop
vertex 41.6 13.2 19.83
vertex 48 13.2 19.81
vertex 48 15.6 20.21
endloop
endfacet
facet normal 0.026 -0.222 0.975
outer loop
vertex 41.6 13.2 19.83
vertex 48 15.6 20.21
vertex 41.6 15.6 20.38
endloop
endfacet
facet normal 0.423 0.079 0.903
outer loop
vertex -48 15.6 10.8
vertex -41.6 15.6 7.8
vertex -41.6 18 7.59
endloop
endfacet
facet normal 0.483 -0.128 0.866
outer loop
vertex -48 15.6 10.8
vertex -41.6 18 7.59
vertex -48 18 11.15
endloop
endfacet
facet normal -0.391 -0.287 0.874
outer loop
vertex -41.6 15.6 7.8
vertex -35.2 15.6 10.66
vertex -35.2 18 11.45
endloop
endfacet
facet normal -0.515 0.074 0.854
outer loop
vertex -41.6 15.6 7.8
vertex -35.2 18 11.45
vertex -41.6 18 7.59
endloop
endfacet
facet normal 0.012 -0.447 0.894
outer loop
vertex -35.2 15.6 10.66
vertex -28.8 15.6 10.57
vertex -28.8 18 11.77
endloop
endfacet
facet normal -0.048 -0.311 0.949
outer loop
vertex -35.2 15.6 10.66
vertex -28.8 18 11.77
vertex -35.2 18 11.45
endloop
endfacet
facet normal 0.151 -0.591 0.792
outer loop
vertex -28.8 15.6 10.57
vertex -22.4 15.6 9.35
vertex -22.4 18 11.14
endloop
endfacet
facet normal 0.088 -0.445 0.891
outer loop
vertex -28.8 15.6 10.57
vertex -22.4 18 11.14
vertex -28.8 18 11.77
endloop
endfacet
facet normal -0.842 -0.295 0.451
outer loop
vertex -22.4 15.6 9.35
vertex -16 15.6 21.3
vertex -16 18 22.87
endloop
endfacet
facet normal -0.827 -0.337 0.451
outer loop
vertex -22.4 15.6 9.35
vertex -16 18 22.87
vertex -22.4 18 11.14
endloop
endfacet
facet normal -0.632 0.119 0.766
outer loop
vertex -16 15.6 21.3
vertex -9.6 15.6 26.58
vertex -9.6 18 26.21
endloop
endfacet
facet normal -0.4 -0.502 0.767
outer loop
vertex -16 15.6 21.3
vertex -9.6 18 26.21
vertex -16 18 22.87
endloop
endfacet
facet normal 0.14 0.314 0.939
outer loop
vertex -9.6 15.6 26.58
vertex -3.2 15.6 25.63
vertex -3.2 18 24.83
endloop
endfacet
facet normal 0.209 0.15 0.966
outer loop
vertex -9.6 15.6 26.58
vertex -3.2 18 24.83
vertex -9.6 18 26.21
endloop
endfacet
facet normal 0.668 -0.398 0.629
outer loop
vertex -3.2 15.6 25.63
vertex 3.2 15.6 18.83
vertex 3.2 18 20.35
endloop
endfacet
facet normal 0.553 0.264 0.79
outer loop
vertex -3.2 15.6 25.63
vertex 3.2 18 20.35
vertex -3.2 18 24.83
endloop
endfacet
facet normal -0.277 -0.426 0.861
outer loop
vertex 3.2 15.6 18.83
vertex 9.6 15.6 20.89
vertex 9.6 18 22.08
endloop
endfacet
facet normal -0.222 -0.521 0.824
outer loop
vertex 3.2 15.6 18.83
vertex 9.6 18 22.08
vertex 3.2 18 20.35
endloop
endfacet
facet normal -0.783 0.124 0.609
outer loop
vertex 9.6 15.6 20.89
vertex 16 15.6 29.12
vertex 16 18 28.63
endloop
endfacet
facet normal -0.676 -0.327 0.66
outer loop
vertex 9.6 15.6 20.89
vertex 16 18 28.63
vertex 9.6 18 22.08
endloop
endfacet
facet normal 0.782 -0.144 0.607
outer loop
vertex 16 15.6 29.12
vertex 22.4 15.6 20.87
vertex 22.4 18 21.44
endloop
endfacet
facet normal 0.74 0.134 0.659
outer loop
vertex 16 15.6 29.12
vertex 22.4 18 21.44
vertex 16 18 28.63
endloop
endfacet
facet normal -0.184 -0.216 0.959
outer loop
vertex 22.4 15.6 20.87
vertex 28.8 15.6 22.1
vertex 28.8 18 22.64
endloop
endfacet
facet normal -0.179 -0.227 0.957
outer loop
vertex 22.4 15.6 20.87
vertex 28.8 18 22.64
vertex 22.4 18 21.44
endloop
endfacet
facet normal 0.27 -0.062 0.961
outer loop
vertex 28.8 15.6 22.1
vertex 35.2 15.6 20.3
vertex 35.2 18 20.45
endloop
endfacet
facet normal 0.316 -0.209 0.925
outer loop
vertex 28.8 15.6 22.1
vertex 35.2 18 20.45
vertex 28.8 18 22.64
endloop
endfacet
facet normal -0.013 -0.17 0.985
outer loop
vertex 35.2 15.6 20.3
vertex 41.6 15.6 20.38
vertex 41.6 18 20.79
endloop
endfacet
facet normal -0.053 -0.064 0.997
outer loop
vertex 35.2 15.6 20.3
vertex 41.6 18 20.79
vertex 35.2 18 20.45
endloop
endfacet
facet normal 0.026 -0.238 0.971
outer loop
vertex 41.6 15.6 20.38
vertex 48 15.6 20.21
vertex 48 18 20.8
endloop
endfacet
facet normal 0 -0.17 0.985
outer loop
vertex 41.6 15.6 20.38
vertex 48 18 20.8
vertex 41.6 18 20.79
endloop
endfacet
facet normal 0.482 -0.147 0.864
outer loop
vertex -48 18 11.15
vertex -41.6 18 7.59
vertex -41.6 20.4 7.99
endloop
endfacet
facet normal 0.475 -0.117 0.872
outer loop
vertex -48 18 11.15
vertex -41.6 20.4 7.99
vertex -48 20.4 11.47
endloop
endfacet
facet normal -0.515 -0.072 0.854
outer loop
vertex -41.6 18 7.59
vertex -35.2 18 11.45
vertex -35.2 20.4 11.65
endloop
endfacet
facet normal -0.491 -0.146 0.859
outer loop
vertex -41.6 18 7.59
vertex -35.2 20.4 11.65
vertex -41.6 20.4 7.99
endloop
endfacet
facet normal -0.047 -0.343 0.938
outer loop
vertex -35.2 18 11.45
vertex -28.8 18 11.77
vertex -28.8 20.4 12.65
endloop
endfacet
facet normal -0.154 -0.083 0.985
outer loop
vertex -35.2 18 11.45
vertex -28.8 20.4 12.65
vertex -35.2 20.4 11.65
endloop
endfacet
facet normal 0.094 -0.279 0.956
outer loop
vertex -28.8 18 11.77
vertex -22.4 18 11.14
vertex -22.4 20.4 11.84
endloop
endfacet
facet normal 0.117 -0.341 0.933
outer loop
vertex -28.8 18 11.77
vertex -22.4 20.4 11.84
vertex -28.8 20.4 12.65
endloop
endfacet
facet normal -0.859 -0.207 0.469
outer loop
vertex -22.4 18 11.14
vertex -16 18 22.87
vertex -16 20.4 23.93
endloop
endfacet
facet normal -0.876 -0.136 0.464
outer loop
vertex -22.4 18 11.14
vertex -16 20.4 23.93
vertex -22.4 20.4 11.84
endloop
endfacet
facet normal -0.382 -0.563 0.733
outer loop
vertex -16 18 22.87
vertex -9.6 18 26.21
vertex -9.6 20.4 28.06
endloop
endfacet
facet normal -0.508 -0.347 0.788
outer loop
vertex -16 18 22.87
vertex -9.6 20.4 28.06
vertex -16 20.4 23.93
endloop
endfacet
facet normal 0.211 0.043 0.977
outer loop
vertex -9.6 18 26.21
vertex -3.2 18 24.83
vertex -3.2 20.4 24.72
endloop
endfacet
facet normal 0.382 -0.563 0.733
outer loop
vertex -9.6 18 26.21
vertex -3.2 20.4 24.72
vertex -9.6 20.4 28.06
endloop
endfacet
facet normal 0.536 -0.355 0.766
outer loop
vertex -3.2 18 24.83
vertex 3.2 18 20.35
vertex 3.2 20.4 21.47
endloop
endfacet
facet normal 0.453 0.04 0.891
outer loop
vertex -3.2 18 24.83
vertex 3.2 20.4 21.47
vertex -3.2 20.4 24.72
endloop
endfacet
facet normal -0.24 -0.392 0.888
outer loop
vertex 3.2 18 20.35
vertex 9.6 18 22.08
vertex 9.6 20.4 23.14
endloop
endfacet
facet normal -0.23 -0.41 0.883
outer loop
vertex 3.2 18 20.35
vertex 9.6 20.4 23.14
vertex 3.2 20.4 21.47
endloop
endfacet
facet normal -0.715 0.006 0.699
outer loop
vertex 9.6 18 22.08
vertex 16 18 28.63
vertex 16 20.4 28.61
endloop
endfacet
facet normal -0.616 -0.318 0.721
outer loop
vertex 9.6 18 22.08
vertex 16 20.4 28.61
vertex 9.6 20.4 23.14
endloop
endfacet
facet normal 0.733 -0.193 0.652
outer loop
vertex 16 18 28.63
vertex 22.4 18 21.44
vertex 22.4 20.4 22.15
endloop
endfacet
facet normal 0.71 0.006 0.704
outer loop
vertex 16 18 28.63
vertex 22.4 20.4 22.15
vertex 16 20.4 28.61
endloop
endfacet
facet normal -0.184 -0.007 0.983
outer loop
vertex 22.4 18 21.44
vertex 28.8 18 22.64
vertex 28.8 20.4 22.66
endloop
endfacet
facet normal -0.075 -0.283 0.956
outer loop
vertex 22.4 18 21.44
vertex 28.8 20.4 22.66
vertex 22.4 20.4 22.15
endloop
endfacet
facet normal 0.3 -0.369 0.879
outer loop
vertex 28.8 18 22.64
vertex 35.2 18 20.45
vertex 35.2 20.4 21.46
endloop
endfacet
facet normal 0.184 -0.007 0.983
outer loop
vertex 28.8 18 22.64
vertex 35.2 20.4 21.46
vertex 28.8 20.4 22.66
endloop
endfacet
facet normal -0.053 -0.162 0.985
outer loop
vertex 35.2 18 20.45
vertex 41.6 18 20.79
vertex 41.6 20.4 21.19
endloop
endfacet
facet normal 0.039 -0.387 0.921
outer loop
vertex 35.2 18 20.45
vertex 41.6 20.4 21.19
vertex 35.2 20.4 21.46
endloop
endfacet
facet normal 0 0.23 0.973
outer loop
vertex 41.6 18 20.79
vertex 48 18 20.8
vertex 48 20.4 20.23
endloop
endfacet
facet normal 0.147 -0.161 0.976
outer loop
vertex 41.6 18 20.79
vertex 48 20.4 20.23
vertex 41.6 20.4 21.19
endloop
endfacet
facet normal 0.467 0.213 0.858
outer loop
vertex -48 20.4 11.47
vertex -41.6 20.4 7.99
vertex -41.6 22.8 7.4
endloop
endfacet
facet normal 0.401 0.36 0.842
outer loop
vertex -48 20.4 11.47
vertex -41.6 22.8 7.4
vertex -48 22.8 10.45
endloop
endfacet
facet normal -0.495 -0.049 0.867
outer loop
vertex -41.6 20.4 7.99
vertex -35.2 20.4 11.65
vertex -35.2 22.8 11.78
endloop
endfacet
facet normal -0.554 0.2 0.808
outer loop
vertex -41.6 20.4 7.99
vertex -35.2 22.8 11.78
vertex -41.6 22.8 7.4
endloop
endfacet
facet normal -0.152 -0.167 0.974
outer loop
vertex -35.2 20.4 11.65
vertex -28.8 20.4 12.65
vertex -28.8 22.8 13.06
endloop
endfacet
facet normal -0.195 -0.055 0.979
outer loop
vertex -35.2 20.4 11.65
vertex -28.8 22.8 13.06
vertex -35.2 22.8 11.78
endloop
endfacet
facet normal 0.124 0.062 0.99
outer loop
vertex -28.8 20.4 12.65
vertex -22.4 20.4 11.84
vertex -22.4 22.8 11.69
endloop
endfacet
facet normal 0.206 -0.165 0.965
outer loop
vertex -28.8 20.4 12.65
vertex -22.4 22.8 11.69
vertex -28.8 22.8 13.06
endloop
endfacet
facet normal -0.876 -0.128 0.464
outer loop
vertex -22.4 20.4 11.84
vertex -16 20.4 23.93
vertex -16 22.8 24.59
endloop
endfacet
facet normal -0.895 0.028 0.444
outer loop
vertex -22.4 20.4 11.84
vertex -16 22.8 24.59
vertex -22.4 22.8 11.69
endloop
endfacet
facet normal -0.526 -0.239 0.816
outer loop
vertex -16 20.4 23.93
vertex -9.6 20.4 28.06
vertex -9.6 22.8 28.76
endloop
endfacet
facet normal -0.531 -0.226 0.817
outer loop
vertex -16 20.4 23.93
vertex -9.6 22.8 28.76
vertex -16 22.8 24.59
endloop
endfacet
facet normal 0.46 -0.09 0.883
outer loop
vertex -9.6 20.4 28.06
vertex -3.2 20.4 24.72
vertex -3.2 22.8 24.97
endloop
endfacet
facet normal 0.494 -0.245 0.834
outer loop
vertex -9.6 20.4 28.06
vertex -3.2 22.8 24.97
vertex -9.6 22.8 28.76
endloop
endfacet
facet normal 0.372 -0.571 0.732
outer loop
vertex -3.2 20.4 24.72
vertex 3.2 20.4 21.47
vertex 3.2 22.8 23.34
endloop
endfacet
facet normal 0.246 -0.099 0.964
outer loop
vertex -3.2 20.4 24.72
vertex 3.2 22.8 23.34
vertex -3.2 22.8 24.97
endloop
endfacet
facet normal -0.24 -0.316 0.918
outer loop
vertex 3.2 20.4 21.47
vertex 9.6 20.4 23.14
vertex 9.6 22.8 23.96
endloop
endfacet
facet normal -0.077 -0.613 0.786
outer loop
vertex 3.2 20.4 21.47
vertex 9.6 22.8 23.96
vertex 3.2 22.8 23.34
endloop
endfacet
facet normal -0.65 -0.025 0.76
outer loop
vertex 9.6 20.4 23.14
vertex 16 20.4 28.61
vertex 16 22.8 28.69
endloop
endfacet
facet normal -0.573 -0.266 0.775
outer loop
vertex 9.6 20.4 23.14
vertex 16 22.8 28.69
vertex 9.6 22.8 23.96
endloop
endfacet
facet normal 0.71 0.038 0.703
outer loop
vertex 16 20.4 28.61
vertex 22.4 20.4 22.15
vertex 22.4 22.8 22.02
endloop
endfacet
facet normal 0.721 -0.023 0.692
outer loop
vertex 16 20.4 28.61
vertex 22.4 22.8 22.02
vertex 16 22.8 28.69
endloop
endfacet
facet normal -0.076 0.255 0.964
outer loop
vertex 22.4 20.4 22.15
vertex 28.8 20.4 22.66
vertex 28.8 22.8 22.02
endloop
endfacet
facet normal 0 0.054 0.999
outer loop
vertex 22.4 20.4 22.15
vertex 28.8 22.8 22.02
vertex 22.4 22.8 22.02
endloop
endfacet
facet normal 0.148 -0.59 0.794
outer loop
vertex 28.8 20.4 22.66
vertex 35.2 20.4 21.46
vertex 35.2 22.8 23.24
endloop
endfacet
facet normal -0.182 0.251 0.951
outer loop
vertex 28.8 20.4 22.66
vertex 35.2 22.8 23.24
vertex 28.8 22.8 22.02
endloop
endfacet
facet normal 0.041 -0.169 0.985
outer loop
vertex 35.2 20.4 21.46
vertex 41.6 20.4 21.19
vertex 41.6 22.8 21.6
endloop
endfacet
facet normal 0.202 -0.585 0.786
outer loop
vertex 35.2 20.4 21.46
vertex 41.6 22.8 21.6
vertex 35.2 22.8 23.24
endloop
endfacet
facet normal 0.14 -0.34 0.93
outer loop
vertex 41.6 20.4 21.19
vertex 48 20.4 20.23
vertex 48 22.8 21.1
endloop
endfacet
facet normal 0.076 -0.169 0.983
outer loop
vertex 41.6 20.4 21.19
vertex 48 22.8 21.1
vertex 41.6 22.8 21.6
endloop
endfacet
facet normal 0.429 -0.063 0.901
outer loop
vertex -48 22.8 10.45
vertex -41.6 22.8 7.4
vertex -41.6 25.2 7.57
endloop
endfacet
facet normal 0.404 0.022 0.915
outer loop
vertex -48 22.8 10.45
vertex -41.6 25.2 7.57
vertex -48 25.2 10.39
endloop
endfacet
facet normal -0.563 0.093 0.821
outer loop
vertex -41.6 22.8 7.4
vertex -35.2 22.8 11.78
vertex -35.2 25.2 11.51
endloop
endfacet
facet normal -0.524 -0.059 0.85
outer loop
vertex -41.6 22.8 7.4
vertex -35.2 25.2 11.51
vertex -41.6 25.2 7.57
endloop
endfacet
facet normal -0.195 -0.017 0.981
outer loop
vertex -35.2 22.8 11.78
vertex -28.8 22.8 13.06
vertex -28.8 25.2 13.1
endloop
endfacet
facet normal -0.239 0.109 0.965
outer loop
vertex -35.2 22.8 11.78
vertex -28.8 25.2 13.1
vertex -35.2 25.2 11.51
endloop
endfacet
facet normal 0.208 -0.069 0.976
outer loop
vertex -28.8 22.8 13.06
vertex -22.4 22.8 11.69
vertex -22.4 25.2 11.86
endloop
endfacet
facet normal 0.19 -0.017 0.982
outer loop
vertex -28.8 22.8 13.06
vertex -22.4 25.2 11.86
vertex -28.8 25.2 13.1
endloop
endfacet
facet normal -0.895 -0.037 0.444
outer loop
vertex -22.4 22.8 11.69
vertex -16 22.8 24.59
vertex -16 25.2 24.79
endloop
endfacet
facet normal -0.896 -0.031 0.443
outer loop
vertex -22.4 22.8 11.69
vertex -16 25.2 24.79
vertex -22.4 25.2 11.86
endloop
endfacet
facet normal -0.542 0.113 0.833
outer loop
vertex -16 22.8 24.59
vertex -9.6 22.8 28.76
vertex -9.6 25.2 28.43
endloop
endfacet
facet normal -0.493 -0.073 0.867
outer loop
vertex -16 22.8 24.59
vertex -9.6 25.2 28.43
vertex -16 25.2 24.79
endloop
endfacet
facet normal 0.487 0.294 0.822
outer loop
vertex -9.6 22.8 28.76
vertex -3.2 22.8 24.97
vertex -3.2 25.2 24.11
endloop
endfacet
facet normal 0.556 0.111 0.823
outer loop
vertex -9.6 22.8 28.76
vertex -3.2 25.2 24.11
vertex -9.6 25.2 28.43
endloop
endfacet
facet normal 0.245 -0.113 0.963
outer loop
vertex -3.2 22.8 24.97
vertex 3.2 22.8 23.34
vertex 3.2 25.2 23.62
endloop
endfacet
facet normal 0.072 0.336 0.939
outer loop
vertex -3.2 22.8 24.97
vertex 3.2 25.2 23.62
vertex -3.2 25.2 24.11
endloop
endfacet
facet normal -0.097 0.008 0.995
outer loop
vertex 3.2 22.8 23.34
vertex 9.6 22.8 23.96
vertex 9.6 25.2 23.94
endloop
endfacet
facet normal -0.05 -0.116 0.992
outer loop
vertex 3.2 22.8 23.34
vertex 9.6 25.2 23.94
vertex 3.2 25.2 23.62
endloop
endfacet
facet normal -0.594 0.029 0.804
outer loop
vertex 9.6 22.8 23.96
vertex 16 22.8 28.69
vertex 16 25.2 28.61
endloop
endfacet
facet normal -0.589 0.007 0.808
outer loop
vertex 9.6 22.8 23.96
vertex 16 25.2 28.61
vertex 9.6 25.2 23.94
endloop
endfacet
facet normal 0.721 0.018 0.692
outer loop
vertex 16 22.8 28.69
vertex 22.4 22.8 22.02
vertex 22.4 25.2 21.96
endloop
endfacet
facet normal 0.72 0.025 0.693
outer loop
vertex 16 22.8 28.69
vertex 22.4 25.2 21.96
vertex 16 25.2 28.61
endloop
endfacet
facet normal 0 0.648 0.762
outer loop
vertex 22.4 22.8 22.02
vertex 28.8 22.8 22.02
vertex 28.8 25.2 19.98
endloop
endfacet
facet normal 0.295 0.025 0.955
outer loop
vertex 22.4 22.8 22.02
vertex 28.8 25.2 19.98
vertex 22.4 25.2 21.96
endloop
endfacet
facet normal -0.185 -0.176 0.967
outer loop
vertex 28.8 22.8 22.02
vertex 35.2 22.8 23.24
vertex 35.2 25.2 23.68
endloop
endfacet
facet normal -0.403 0.593 0.697
outer loop
vertex 28.8 22.8 22.02
vertex 35.2 25.2 23.68
vertex 28.8 25.2 19.98
endloop
endfacet
facet normal 0.244 0.195 0.95
outer loop
vertex 35.2 22.8 23.24
vertex 41.6 22.8 21.6
vertex 41.6 25.2 21.11
endloop
endfacet
facet normal 0.368 -0.167 0.915
outer loop
vertex 35.2 22.8 23.24
vertex 41.6 25.2 21.11
vertex 35.2 25.2 23.68
endloop
endfacet
facet normal 0.077 -0.067 0.995
outer loop
vertex 41.6 22.8 21.6
vertex 48 22.8 21.1
vertex 48 25.2 21.27
endloop
endfacet
facet normal -0.024 0.201 0.979
outer loop
vertex 41.6 22.8 21.6
vertex 48 25.2 21.27
vertex 41.6 25.2 21.11
endloop
endfacet
facet normal 0.386 0.291 0.875
outer loop
vertex -48 25.2 10.39
vertex -41.6 25.2 7.57
vertex -41.6 27.6 6.77
endloop
endfacet
facet normal 0.23 0.573 0.786
outer loop
vertex -48 25.2 10.39
vertex -41.6 27.6 6.77
vertex -48 27.6 8.64
endloop
endfacet
facet normal -0.524 0.065 0.849
outer loop
vertex -41.6 25.2 7.57
vertex -35.2 25.2 11.51
vertex -35.2 27.6 11.33
endloop
endfacet
facet normal -0.56 0.261 0.786
outer loop
vertex -41.6 25.2 7.57
vertex -35.2 27.6 11.33
vertex -41.6 27.6 6.77
endloop
endfacet
facet normal -0.193 0.595 0.78
outer loop
vertex -35.2 25.2 11.51
vertex -28.8 25.2 13.1
vertex -28.8 27.6 11.27
endloop
endfacet
facet normal 0.01 0.076 0.997
outer loop
vertex -35.2 25.2 11.51
vertex -28.8 27.6 11.27
vertex -35.2 27.6 11.33
endloop
endfacet
facet normal 0.19 0.048 0.981
outer loop
vertex -28.8 25.2 13.1
vertex -22.4 25.2 11.86
vertex -22.4 27.6 11.75
endloop
endfacet
facet normal -0.059 0.606 0.793
outer loop
vertex -28.8 25.2 13.1
vertex -22.4 27.6 11.75
vertex -28.8 27.6 11.27
endloop
endfacet
facet normal -0.896 0.015 0.444
outer loop
vertex -22.4 25.2 11.86
vertex -16 25.2 24.79
vertex -16 27.6 24.71
endloop
endfacet
facet normal -0.897 0.021 0.442
outer loop
vertex -22.4 25.2 11.86
vertex -16 27.6 24.71
vertex -22.4 27.6 11.75
endloop
endfacet
facet normal -0.491 0.114 0.864
outer loop
vertex -16 25.2 24.79
vertex -9.6 25.2 28.43
vertex -9.6 27.6 28.12
endloop
endfacet
facet normal -0.469 0.03 0.882
outer loop
vertex -16 25.2 24.79
vertex -9.6 27.6 28.12
vertex -16 27.6 24.71
endloop
endfacet
facet normal 0.508 0.42 0.752
outer loop
vertex -9.6 25.2 28.43
vertex -3.2 25.2 24.11
vertex -3.2 27.6 22.77
endloop
endfacet
facet normal 0.638 0.1 0.763
outer loop
vertex -9.6 25.2 28.43
vertex -3.2 27.6 22.77
vertex -9.6 27.6 28.12
endloop
endfacet
facet normal 0.074 0.247 0.966
outer loop
vertex -3.2 25.2 24.11
vertex 3.2 25.2 23.62
vertex 3.2 27.6 23
endloop
endfacet
facet normal -0.032 0.487 0.873
outer loop
vertex -3.2 25.2 24.11
vertex 3.2 27.6 23
vertex -3.2 27.6 22.77
endloop
endfacet
facet normal -0.05 0.107 0.993
outer loop
vertex 3.2 25.2 23.62
vertex 9.6 25.2 23.94
vertex 9.6 27.6 23.69
endloop
endfacet
facet normal -0.102 0.247 0.964
outer loop
vertex 3.2 25.2 23.62
vertex 9.6 27.6 23.69
vertex 3.2 27.6 23
endloop
endfacet
facet normal -0.519 -0.473 0.712
outer loop
vertex 9.6 25.2 23.94
vertex 16 25.2 28.61
vertex 16 27.6 30.2
endloop
endfacet
facet normal -0.711 0.075 0.699
outer loop
vertex 9.6 25.2 23.94
vertex 16 27.6 30.2
vertex 9.6 27.6 23.69
endloop
endfacet
facet normal 0.7 0.238 0.674
outer loop
vertex 16 25.2 28.61
vertex 22.4 25.2 21.96
vertex 22.4 27.6 21.11
endloop
endfacet
facet normal 0.764 -0.357 0.538
outer loop
vertex 16 25.2 28.61
vertex 22.4 27.6 21.11
vertex 16 27.6 30.2
endloop
endfacet
facet normal 0.288 -0.219 0.932
outer loop
vertex 22.4 25.2 21.96
vertex 28.8 25.2 19.98
vertex 28.8 27.6 20.54
endloop
endfacet
facet normal 0.084 0.332 0.94
outer loop
vertex 22.4 25.2 21.96
vertex 28.8 27.6 20.54
vertex 22.4 27.6 21.11
endloop
endfacet
facet normal -0.489 0.216 0.845
outer loop
vertex 28.8 25.2 19.98
vertex 35.2 25.2 23.68
vertex 35.2 27.6 23.07
endloop
endfacet
facet normal -0.359 -0.213 0.909
outer loop
vertex 28.8 25.2 19.98
vertex 35.2 27.6 23.07
vertex 28.8 27.6 20.54
endloop
endfacet
facet normal 0.365 0.201 0.909
outer loop
vertex 35.2 25.2 23.68
vertex 41.6 25.2 21.11
vertex 41.6 27.6 20.58
endloop
endfacet
facet normal 0.353 0.232 0.907
outer loop
vertex 35.2 25.2 23.68
vertex 41.6 27.6 20.58
vertex 35.2 27.6 23.07
endloop
endfacet
facet normal -0.024 0.107 0.994
outer loop
vertex 41.6 25.2 21.11
vertex 48 25.2 21.27
vertex 48 27.6 21.01
endloop
endfacet
facet normal -0.065 0.216 0.974
outer loop
vertex 41.6 25.2 21.11
vertex 48 27.6 21.01
vertex 41.6 27.6 20.58
endloop
endfacet
facet normal 0.281 0.014 0.96
outer loop
vertex -48 27.6 8.64
vertex -41.6 27.6 6.77
vertex -41.6 30 6.74
endloop
endfacet
facet normal 0.175 0.283 0.943
outer loop
vertex -48 27.6 8.64
vertex -41.6 30 6.74
vertex -48 30 7.92
endloop
endfacet
facet normal -0.56 0.261 0.786
outer loop
vertex -41.6 27.6 6.77
vertex -35.2 27.6 11.33
vertex -35.2 30 10.54
endloop
endfacet
facet normal -0.511 0.012 0.86
outer loop
vertex -41.6 27.6 6.77
vertex -35.2 30 10.54
vertex -41.6 30 6.74
endloop
endfacet
facet normal 0.009 0.437 0.9
outer loop
vertex -35.2 27.6 11.33
vertex -28.8 27.6 11.27
vertex -28.8 30 10.1
endloop
endfacet
facet normal 0.064 0.314 0.947
outer loop
vertex -35.2 27.6 11.33
vertex -28.8 30 10.1
vertex -35.2 30 10.54
endloop
endfacet
facet normal -0.071 -0.285 0.956
outer loop
vertex -28.8 27.6 11.27
vertex -22.4 27.6 11.75
vertex -22.4 30 12.46
endloop
endfacet
facet normal -0.315 0.414 0.854
outer loop
vertex -28.8 27.6 11.27
vertex -22.4 30 12.46
vertex -28.8 30 10.1
endloop
endfacet
facet normal -0.896 0.048 0.442
outer loop
vertex -22.4 27.6 11.75
vertex -16 27.6 24.71
vertex -16 30 24.45
endloop
endfacet
facet normal -0.874 -0.139 0.466
outer loop
vertex -22.4 27.6 11.75
vertex -16 30 24.45
vertex -22.4 30 12.46
endloop
endfacet
facet normal -0.468 0.078 0.88
outer loop
vertex -16 27.6 24.71
vertex -9.6 27.6 28.12
vertex -9.6 30 27.9
endloop
endfacet
facet normal -0.472 0.095 0.876
outer loop
vertex -16 27.6 24.71
vertex -9.6 30 27.9
vertex -16 30 24.45
endloop
endfacet
facet normal 0.586 0.406 0.701
outer loop
vertex -9.6 27.6 28.12
vertex -3.2 27.6 22.77
vertex -3.2 30 21.38
endloop
endfacet
facet normal 0.712 0.062 0.699
outer loop
vertex -9.6 27.6 28.12
vertex -3.2 30 21.38
vertex -9.6 30 27.9
endloop
endfacet
facet normal -0.037 0.015 0.999
outer loop
vertex -3.2 27.6 22.77
vertex 3.2 27.6 23
vertex 3.2 30 22.97
endloop
endfacet
facet normal -0.21 0.489 0.846
outer loop
vertex -3.2 27.6 22.77
vertex 3.2 30 22.97
vertex -3.2 30 21.38
endloop
endfacet
facet normal -0.091 0.504 0.859
outer loop
vertex 3.2 27.6 23
vertex 9.6 27.6 23.69
vertex 9.6 30 22.28
endloop
endfacet
facet normal 0.108 0.014 0.994
outer loop
vertex 3.2 27.6 23
vertex 9.6 30 22.28
vertex 3.2 30 22.97
endloop
endfacet
facet normal -0.702 0.178 0.69
outer loop
vertex 9.6 27.6 23.69
vertex 16 27.6 30.2
vertex 16 30 29.58
endloop
endfacet
facet normal -0.701 0.361 0.615
outer loop
vertex 9.6 27.6 23.69
vertex 16 30 29.58
vertex 9.6 30 22.28
endloop
endfacet
facet normal 0.801 0.198 0.564
outer loop
vertex 16 27.6 30.2
vertex 22.4 27.6 21.11
vertex 22.4 30 20.27
endloop
endfacet
facet normal 0.815 0.145 0.561
outer loop
vertex 16 27.6 30.2
vertex 22.4 30 20.27
vertex 16 30 29.58
endloop
endfacet
facet normal 0.088 0.069 0.994
outer loop
vertex 22.4 27.6 21.11
vertex 28.8 27.6 20.54
vertex 28.8 30 20.38
endloop
endfacet
facet normal -0.015 0.331 0.944
outer loop
vertex 22.4 27.6 21.11
vertex 28.8 30 20.38
vertex 22.4 30 20.27
endloop
endfacet
facet normal -0.342 0.364 0.866
outer loop
vertex 28.8 27.6 20.54
vertex 35.2 27.6 23.07
vertex 35.2 30 22.06
endloop
endfacet
facet normal -0.254 0.067 0.965
outer loop
vertex 28.8 27.6 20.54
vertex 35.2 30 22.06
vertex 28.8 30 20.38
endloop
endfacet
facet normal 0.352 0.239 0.905
outer loop
vertex 35.2 27.6 23.07
vertex 41.6 27.6 20.58
vertex 41.6 30 19.94
endloop
endfacet
facet normal 0.291 0.371 0.882
outer loop
vertex 35.2 27.6 23.07
vertex 41.6 30 19.94
vertex 35.2 30 22.06
endloop
endfacet
facet normal -0.067 0.06 0.996
outer loop
vertex 41.6 27.6 20.58
vertex 48 27.6 21.01
vertex 48 30 20.86
endloop
endfacet
facet normal -0.138 0.253 0.958
outer loop
vertex 41.6 27.6 20.58
vertex 48 30 20.86
vertex 41.6 30 19.94
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -48 -30 -4
vertex -41.6 -30 -4
vertex -41.6 -30 7.54
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -48 -30 -4
vertex -41.6 -30 7.54
vertex -48 -30 7.21
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -41.6 -30 -4
vertex -35.2 -30 -4
vertex -35.2 -30 6.88
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -41.6 -30 -4
vertex -35.2 -30 6.88
vertex -41.6 -30 7.54
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -35.2 -30 -4
vertex -28.8 -30 -4
vertex -28.8 -30 9.92
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -35.2 -30 -4
vertex -28.8 -30 9.92
vertex -35.2 -30 6.88
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -28.8 -30 -4
vertex -22.4 -30 -4
vertex -22.4 -30 8.75
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -28.8 -30 -4
vertex -22.4 -30 8.75
vertex -28.8 -30 9.92
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -22.4 -30 -4
vertex -16 -30 -4
vertex -16 -30 12.18
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -22.4 -30 -4
vertex -16 -30 12.18
vertex -22.4 -30 8.75
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -16 -30 -4
vertex -9.6 -30 -4
vertex -9.6 -30 24.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -16 -30 -4
vertex -9.6 -30 24.38
vertex -16 -30 12.18
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -9.6 -30 -4
vertex -3.2 -30 -4
vertex -3.2 -30 28.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -9.6 -30 -4
vertex -3.2 -30 28.11
vertex -9.6 -30 24.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -3.2 -30 -4
vertex 3.2 -30 -4
vertex 3.2 -30 19.93
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -3.2 -30 -4
vertex 3.2 -30 19.93
vertex -3.2 -30 28.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 3.2 -30 -4
vertex 9.6 -30 -4
vertex 9.6 -30 22.61
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 3.2 -30 -4
vertex 9.6 -30 22.61
vertex 3.2 -30 19.93
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.6 -30 -4
vertex 16 -30 -4
vertex 16 -30 21.57
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.6 -30 -4
vertex 16 -30 21.57
vertex 9.6 -30 22.61
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16 -30 -4
vertex 22.4 -30 -4
vertex 22.4 -30 28.13
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16 -30 -4
vertex 22.4 -30 28.13
vertex 16 -30 21.57
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.4 -30 -4
vertex 28.8 -30 -4
vertex 28.8 -30 19.63
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.4 -30 -4
vertex 28.8 -30 19.63
vertex 22.4 -30 28.13
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.8 -30 -4
vertex 35.2 -30 -4
vertex 35.2 -30 23.26
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.8 -30 -4
vertex 35.2 -30 23.26
vertex 28.8 -30 19.63
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.2 -30 -4
vertex 41.6 -30 -4
vertex 41.6 -30 21.74
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.2 -30 -4
vertex 41.6 -30 21.74
vertex 35.2 -30 23.26
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.6 -30 -4
vertex 48 -30 -4
vertex 48 -30 19.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.6 -30 -4
vertex 48 -30 19.64
vertex 41.6 -30 21.74
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -48 30 -4
vertex -41.6 30 6.74
vertex -41.6 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -48 30 -4
vertex -48 30 7.92
vertex -41.6 30 6.74
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -41.6 30 -4
vertex -35.2 30 10.54
vertex -35.2 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -41.6 30 -4
vertex -41.6 30 6.74
vertex -35.2 30 10.54
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -35.2 30 -4
vertex -28.8 30 10.1
vertex -28.8 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -35.2 30 -4
vertex -35.2 30 10.54
vertex -28.8 30 10.1
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -28.8 30 -4
vertex -22.4 30 12.46
vertex -22.4 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -28.8 30 -4
vertex -28.8 30 10.1
vertex -22.4 30 12.46
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -22.4 30 -4
vertex -16 30 24.45
vertex -16 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -22.4 30 -4
vertex -22.4 30 12.46
vertex -16 30 24.45
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -16 30 -4
vertex -9.6 30 27.9
vertex -9.6 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -16 30 -4
vertex -16 30 24.45
vertex -9.6 30 27.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -9.6 30 -4
vertex -3.2 30 21.38
vertex -3.2 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -9.6 30 -4
vertex -9.6 30 27.9
vertex -3.2 30 21.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -3.2 30 -4
vertex 3.2 30 22.97
vertex 3.2 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex -3.2 30 -4
vertex -3.2 30 21.38
vertex 3.2 30 22.97
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 3.2 30 -4
vertex 9.6 30 22.28
vertex 9.6 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 3.2 30 -4
vertex 3.2 30 22.97
vertex 9.6 30 22.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.6 30 -4
vertex 16 30 29.58
vertex 16 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.6 30 -4
vertex 9.6 30 22.28
vertex 16 30 29.58
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16 30 -4
vertex 22.4 30 20.27
vertex 22.4 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16 30 -4
vertex 16 30 29.58
vertex 22.4 30 20.27
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.4 30 -4
vertex 28.8 30 20.38
vertex 28.8 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.4 30 -4
vertex 22.4 30 20.27
vertex 28.8 30 20.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.8 30 -4
vertex 35.2 30 22.06
vertex 35.2 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.8 30 -4
vertex 28.8 30 20.38
vertex 35.2 30 22.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.2 30 -4
vertex 41.6 30 19.94
vertex 41.6 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.2 30 -4
vertex 35.2 30 22.06
vertex 41.6 30 19.94
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.6 30 -4
vertex 48 30 20.86
vertex 48 30 -4
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.6 30 -4
vertex 41.6 30 19.94
vertex 48 30 20.86
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -30 -4
vertex -48 -27.6 6.85
vertex -48 -27.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -30 -4
vertex -48 -30 7.21
vertex -48 -27.6 6.85
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -27.6 -4
vertex -48 -25.2 7.45
vertex -48 -25.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -27.6 -4
vertex -48 -27.6 6.85
vertex -48 -25.2 7.45
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -25.2 -4
vertex -48 -22.8 8.25
vertex -48 -22.8 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -25.2 -4
vertex -48 -25.2 7.45
vertex -48 -22.8 8.25
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -22.8 -4
vertex -48 -20.4 8.72
vertex -48 -20.4 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -22.8 -4
vertex -48 -22.8 8.25
vertex -48 -20.4 8.72
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -20.4 -4
vertex -48 -18 9.83
vertex -48 -18 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -20.4 -4
vertex -48 -20.4 8.72
vertex -48 -18 9.83
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -18 -4
vertex -48 -15.6 10.13
vertex -48 -15.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -18 -4
vertex -48 -18 9.83
vertex -48 -15.6 10.13
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -15.6 -4
vertex -48 -13.2 10.34
vertex -48 -13.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -15.6 -4
vertex -48 -15.6 10.13
vertex -48 -13.2 10.34
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -13.2 -4
vertex -48 -10.8 10.91
vertex -48 -10.8 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -13.2 -4
vertex -48 -13.2 10.34
vertex -48 -10.8 10.91
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -10.8 -4
vertex -48 -8.4 11.19
vertex -48 -8.4 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -10.8 -4
vertex -48 -10.8 10.91
vertex -48 -8.4 11.19
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -8.4 -4
vertex -48 -6 11.01
vertex -48 -6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -8.4 -4
vertex -48 -8.4 11.19
vertex -48 -6 11.01
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -6 -4
vertex -48 -3.6 11.23
vertex -48 -3.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -6 -4
vertex -48 -6 11.01
vertex -48 -3.6 11.23
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -3.6 -4
vertex -48 -1.2 10.81
vertex -48 -1.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -3.6 -4
vertex -48 -3.6 11.23
vertex -48 -1.2 10.81
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -1.2 -4
vertex -48 1.2 9.92
vertex -48 1.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 -1.2 -4
vertex -48 -1.2 10.81
vertex -48 1.2 9.92
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 1.2 -4
vertex -48 3.6 10.65
vertex -48 3.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 1.2 -4
vertex -48 1.2 9.92
vertex -48 3.6 10.65
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 3.6 -4
vertex -48 6 10.08
vertex -48 6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 3.6 -4
vertex -48 3.6 10.65
vertex -48 6 10.08
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 6 -4
vertex -48 8.4 10.73
vertex -48 8.4 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 6 -4
vertex -48 6 10.08
vertex -48 8.4 10.73
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 8.4 -4
vertex -48 10.8 10.57
vertex -48 10.8 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 8.4 -4
vertex -48 8.4 10.73
vertex -48 10.8 10.57
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 10.8 -4
vertex -48 13.2 10.51
vertex -48 13.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 10.8 -4
vertex -48 10.8 10.57
vertex -48 13.2 10.51
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 13.2 -4
vertex -48 15.6 10.8
vertex -48 15.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 13.2 -4
vertex -48 13.2 10.51
vertex -48 15.6 10.8
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 15.6 -4
vertex -48 18 11.15
vertex -48 18 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 15.6 -4
vertex -48 15.6 10.8
vertex -48 18 11.15
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 18 -4
vertex -48 20.4 11.47
vertex -48 20.4 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 18 -4
vertex -48 18 11.15
vertex -48 20.4 11.47
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 20.4 -4
vertex -48 22.8 10.45
vertex -48 22.8 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 20.4 -4
vertex -48 20.4 11.47
vertex -48 22.8 10.45
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 22.8 -4
vertex -48 25.2 10.39
vertex -48 25.2 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 22.8 -4
vertex -48 22.8 10.45
vertex -48 25.2 10.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 25.2 -4
vertex -48 27.6 8.64
vertex -48 27.6 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 25.2 -4
vertex -48 25.2 10.39
vertex -48 27.6 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 27.6 -4
vertex -48 30 7.92
vertex -48 30 -4
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -48 27.6 -4
vertex -48 27.6 8.64
vertex -48 30 7.92
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -30 -4
vertex 48 -27.6 -4
vertex 48 -27.6 19.61
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -30 -4
vertex 48 -27.6 19.61
vertex 48 -30 19.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -27.6 -4
vertex 48 -25.2 -4
vertex 48 -25.2 21.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -27.6 -4
vertex 48 -25.2 21.1
vertex 48 -27.6 19.61
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -25.2 -4
vertex 48 -22.8 -4
vertex 48 -22.8 21.76
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -25.2 -4
vertex 48 -22.8 21.76
vertex 48 -25.2 21.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -22.8 -4
vertex 48 -20.4 -4
vertex 48 -20.4 22.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -22.8 -4
vertex 48 -20.4 22.14
vertex 48 -22.8 21.76
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -20.4 -4
vertex 48 -18 -4
vertex 48 -18 22.24
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -20.4 -4
vertex 48 -18 22.24
vertex 48 -20.4 22.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -18 -4
vertex 48 -15.6 -4
vertex 48 -15.6 22.93
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -18 -4
vertex 48 -15.6 22.93
vertex 48 -18 22.24
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -15.6 -4
vertex 48 -13.2 -4
vertex 48 -13.2 23.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -15.6 -4
vertex 48 -13.2 23.16
vertex 48 -15.6 22.93
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -13.2 -4
vertex 48 -10.8 -4
vertex 48 -10.8 22.73
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -13.2 -4
vertex 48 -10.8 22.73
vertex 48 -13.2 23.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -10.8 -4
vertex 48 -8.4 -4
vertex 48 -8.4 23.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -10.8 -4
vertex 48 -8.4 23.1
vertex 48 -10.8 22.73
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -8.4 -4
vertex 48 -6 -4
vertex 48 -6 22.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -8.4 -4
vertex 48 -6 22.59
vertex 48 -8.4 23.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -6 -4
vertex 48 -3.6 -4
vertex 48 -3.6 21.2
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -6 -4
vertex 48 -3.6 21.2
vertex 48 -6 22.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -3.6 -4
vertex 48 -1.2 -4
vertex 48 -1.2 20.04
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -3.6 -4
vertex 48 -1.2 20.04
vertex 48 -3.6 21.2
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -1.2 -4
vertex 48 1.2 -4
vertex 48 1.2 20.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 -1.2 -4
vertex 48 1.2 20.89
vertex 48 -1.2 20.04
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 1.2 -4
vertex 48 3.6 -4
vertex 48 3.6 20.74
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 1.2 -4
vertex 48 3.6 20.74
vertex 48 1.2 20.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 3.6 -4
vertex 48 6 -4
vertex 48 6 21.02
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 3.6 -4
vertex 48 6 21.02
vertex 48 3.6 20.74
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 6 -4
vertex 48 8.4 -4
vertex 48 8.4 20.34
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 6 -4
vertex 48 8.4 20.34
vertex 48 6 21.02
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 8.4 -4
vertex 48 10.8 -4
vertex 48 10.8 20.72
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 8.4 -4
vertex 48 10.8 20.72
vertex 48 8.4 20.34
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 10.8 -4
vertex 48 13.2 -4
vertex 48 13.2 19.81
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 10.8 -4
vertex 48 13.2 19.81
vertex 48 10.8 20.72
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 13.2 -4
vertex 48 15.6 -4
vertex 48 15.6 20.21
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 13.2 -4
vertex 48 15.6 20.21
vertex 48 13.2 19.81
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 15.6 -4
vertex 48 18 -4
vertex 48 18 20.8
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 15.6 -4
vertex 48 18 20.8
vertex 48 15.6 20.21
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 18 -4
vertex 48 20.4 -4
vertex 48 20.4 20.23
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 18 -4
vertex 48 20.4 20.23
vertex 48 18 20.8
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 20.4 -4
vertex 48 22.8 -4
vertex 48 22.8 21.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 20.4 -4
vertex 48 22.8 21.1
vertex 48 20.4 20.23
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 22.8 -4
vertex 48 25.2 -4
vertex 48 25.2 21.27
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 22.8 -4
vertex 48 25.2 21.27
vertex 48 22.8 21.1
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 25.2 -4
vertex 48 27.6 -4
vertex 48 27.6 21.01
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 25.2 -4
vertex 48 27.6 21.01
vertex 48 25.2 21.27
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 27.6 -4
vertex 48 30 -4
vertex 48 30 20.86
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48 27.6 -4
vertex 48 30 20.86
vertex 48 27.6 21.01
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -41.6 -30 -4
vertex -48 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -35.2 -30 -4
vertex -41.6 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -28.8 -30 -4
vertex -35.2 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -22.4 -30 -4
vertex -28.8 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -16 -30 -4
vertex -22.4 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -9.6 -30 -4
vertex -16 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -3.2 -30 -4
vertex -9.6 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 3.2 -30 -4
vertex -3.2 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 9.6 -30 -4
vertex 3.2 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 16 -30 -4
vertex 9.6 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 22.4 -30 -4
vertex 16 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 28.8 -30 -4
vertex 22.4 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 35.2 -30 -4
vertex 28.8 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 41.6 -30 -4
vertex 35.2 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -30 -4
vertex 41.6 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -27.6 -4
vertex 48 -30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -25.2 -4
vertex 48 -27.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -22.8 -4
vertex 48 -25.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -20.4 -4
vertex 48 -22.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -18 -4
vertex 48 -20.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -15.6 -4
vertex 48 -18 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -13.2 -4
vertex 48 -15.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -10.8 -4
vertex 48 -13.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -8.4 -4
vertex 48 -10.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -6 -4
vertex 48 -8.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -3.6 -4
vertex 48 -6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 -1.2 -4
vertex 48 -3.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 1.2 -4
vertex 48 -1.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 3.6 -4
vertex 48 1.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 6 -4
vertex 48 3.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 8.4 -4
vertex 48 6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 10.8 -4
vertex 48 8.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 13.2 -4
vertex 48 10.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 15.6 -4
vertex 48 13.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 18 -4
vertex 48 15.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 20.4 -4
vertex 48 18 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 22.8 -4
vertex 48 20.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 25.2 -4
vertex 48 22.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 27.6 -4
vertex 48 25.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 48 30 -4
vertex 48 27.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 41.6 30 -4
vertex 48 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 35.2 30 -4
vertex 41.6 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 28.8 30 -4
vertex 35.2 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 22.4 30 -4
vertex 28.8 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 16 30 -4
vertex 22.4 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 9.6 30 -4
vertex 16 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex 3.2 30 -4
vertex 9.6 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -3.2 30 -4
vertex 3.2 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -9.6 30 -4
vertex -3.2 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -16 30 -4
vertex -9.6 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -22.4 30 -4
vertex -16 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -28.8 30 -4
vertex -22.4 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -35.2 30 -4
vertex -28.8 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -41.6 30 -4
vertex -35.2 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 30 -4
vertex -41.6 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 27.6 -4
vertex -48 30 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 25.2 -4
vertex -48 27.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 22.8 -4
vertex -48 25.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 20.4 -4
vertex -48 22.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 18 -4
vertex -48 20.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 15.6 -4
vertex -48 18 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 13.2 -4
vertex -48 15.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 10.8 -4
vertex -48 13.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 8.4 -4
vertex -48 10.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 6 -4
vertex -48 8.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 3.6 -4
vertex -48 6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 1.2 -4
vertex -48 3.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -1.2 -4
vertex -48 1.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -3.6 -4
vertex -48 -1.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -6 -4
vertex -48 -3.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -8.4 -4
vertex -48 -6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -10.8 -4
vertex -48 -8.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -13.2 -4
vertex -48 -10.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -15.6 -4
vertex -48 -13.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -18 -4
vertex -48 -15.6 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -20.4 -4
vertex -48 -18 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -22.8 -4
vertex -48 -20.4 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -25.2 -4
vertex -48 -22.8 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -27.6 -4
vertex -48 -25.2 -4
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex 0 0 -4
vertex -48 -30 -4
vertex -48 -27.6 -4
endloop
endfacet
endsolid us_crude_stocks_2010_2025
```
<!-- /stocks:model -->

The [weekly version](assets/us-crude-stocks.stl) has every week at full resolution and is a closed solid, so it will 3D print as it is.

#### What I keep coming back to

- The shape of the futures curve, and the moments when the price of physical barrels and the price of paper contracts disagree
- Sanctions, and the gap between when a policy is announced and when barrels actually move
- Pipelines, terminals and refineries as the real limit on how fast anything changes

**Tools:** Python, SQL, DuckDB, Postgres, pandas, matplotlib, Next.js. Public data from the EIA, Energinet, EirGrid, GIE, ENTSO-E and the CFTC.

**Find me** at [kardamow.com](https://kardamow.com) and [@kardamow on X](https://x.com/kardamow).

<!-- built -->
<sub>Chart and model drawn by <code>build/build.py</code> from EIA data, last built for the week ending 6 Nov 2026.</sub>
<!-- /built -->
