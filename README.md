# duolingo-stats

Acquire your stats from Duolingo's public-facing API.

## Usage

Create a file named `username.txt` in this directory, and enter only
your Duolingo username.

Run `./acquire.py` to load your profile data from Duolingo. It will
be saved as a timestamped JSON file in the `data/` directory. You can
use cron or another external scheduler to regularly run `acquire.py`.

Note that the JSON file contains several hundred KB of likely
irrelevant data, and is not trimmed or compressed. Daily stats
will take up on the order of 100MB per year.

To analyze:

```python

import analyze

df = analyze.load_data()
```

This will create a [Pandas Dataframe](https://pandas.pydata.org/) with
your individual language scores at each given time, row-indexed by timestamp
and column-indexed by language name.
