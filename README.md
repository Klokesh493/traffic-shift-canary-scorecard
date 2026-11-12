# Traffic Shift Canary Scorecard

Scores canary shifts by error rate, latency, saturation, and rollback readiness.

Focus: Telecom DevOps progressive delivery.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 canary_scorecard.py sample_canary.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.
