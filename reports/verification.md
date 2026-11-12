# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 canary_scorecard.py sample_canary.csv
api advance
edge rollback
test_rolls_back_high_error_rate (test_canary_scorecard.CanaryScorecardTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
