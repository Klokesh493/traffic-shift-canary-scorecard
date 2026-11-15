# Skills and verification

## What this repository demonstrates

A staged rollout scorecard that checks the error rate first for rollback, then checks latency, saturation, and rollback readiness before allowing a traffic increase.

## Reproduce the result

The API canary advances. The edge canary crosses the error threshold and gets a rollback recommendation. Reproduce the primary fixture with `python3 canary_scorecard.py sample_canary.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

Missing or invalid numeric metrics return pause. The gate rejects nonfinite latency or error samples and saturation outside 0–100 percent.

## Scope

The scorecard uses supplied metrics and does not change traffic. Review sample size, baseline, and rollback readiness before applying a decision.

Review the rollback decision before considering pause or advance. Confirm a tested rollback path before expanding traffic.

[canary_scorecard.py](../canary_scorecard.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
