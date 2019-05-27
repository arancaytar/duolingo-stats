#!/usr/bin/env python3

import analyse
import sys

scores = analyse.load_scores()
scores[0].to_csv(sys.argv[1])
scores[1].to_csv(sys.argv[2])

