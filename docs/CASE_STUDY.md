# Traffic Shift Canary Scorecard walkthrough

## Business problem

Scores canary shifts by error rate, latency, saturation, and rollback readiness.

## Reproduce the workflow

Run `python3 canary_scorecard.py sample_canary.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
api advance
edge rollback
```

The sample supplies these fields. `service`, `error_rate_pct`, `p95_latency_ms`, `saturation_pct`, `rollback_ready`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
