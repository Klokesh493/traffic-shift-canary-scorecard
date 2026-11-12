# Traffic Shift Canary Scorecard

A traffic shift needs a consistent stop or advance decision when errors, latency, saturation, or rollback readiness change.

## What I built

I built a staged rollout scorecard that checks the error rate first for rollback, then checks latency, saturation, and rollback readiness before allowing a traffic increase.

## How it works

```mermaid
flowchart LR
    A["Canary errors, latency, saturation, rollback readiness"]
    B["Check error rollback threshold first"]
    C{"Rollback threshold crossed?"}
    D["Recommend rollback"]
    E["Otherwise pause on health or readiness checks, else advance"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [canary_scorecard.py](canary_scorecard.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 canary_scorecard.py sample_canary.csv
```

The API canary advances. The edge canary crosses the error threshold and gets a rollback recommendation. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 canary_scorecard.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The scorecard uses supplied metrics and does not change traffic. Review sample size, baseline, and rollback readiness before applying a decision.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
