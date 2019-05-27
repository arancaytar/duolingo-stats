# duolingo-stats

Acquire your stats from Duolingo's public-facing API.

## Setup

Create a file named `uid.txt` in this directory, and enter only your Duolingo
user ID.

You can automatically create this file using the script `./get_id.py`, which
prompts your username and password. The password is only required for this
request.

## Acquisition

Run `./acquire_main.py` to load your profile data from Duolingo. It will be
saved as a timestamped JSON file in the `data/` directory. You can use cron or
another external scheduler to regularly run `acquire.py`.

This will store the current course data from Duolingo, which contains your XP
and crown levels for each active course.

## Aggregation

You can load the JSON data into a [Pandas Dataframe](https://pandas.pydata.org/)
with your individual language scores at each given time, row-indexed by
timestamp and column-indexed by language name:

```python

import analyze

xp, crowns = analyze.load_scores()

```

## CSV Export

To further process the data with non-Python tools, you can export the Dataframe
in CSV form using `./export_csv.py <xp.csv> <crowns.csv>`.

Two CSV files will be created, one for XP and one for crowns.
