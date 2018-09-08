# duolingo-stats

Acquire your stats from Duolingo's public-facing API.

## Acquisition

Create a file named `username.txt` in this directory, and enter only
your Duolingo username.

Run `./acquire_main.py` to load your profile data from Duolingo. It
will be saved as a timestamped JSON file in the `data/` directory.
You can use cron or another external scheduler to regularly run
`acquire.py`.

Note that the raw JSON response returns much more data than is stored;
this script only saves the 'languages' key containing the scores.
The discarded information includes miscellaneous profile data, streak
stats, and the entire tree of the currently active language.

## Aggregation

You can load the JSON data into a [Pandas Dataframe](https://pandas.pydata.org/)
with your individual language scores at each given time, row-indexed by timestamp
and column-indexed by language name:

```python

import analyze

df = analyze.load_scores()
```

## CSV Export

To further process the data with non-Python tools, you can export the
Dataframe in CSV form using `./export_csv.py`.
