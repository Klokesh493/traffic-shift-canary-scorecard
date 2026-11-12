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

## Business problem

A traffic shift needs a consistent stop or advance decision when errors, latency, saturation, or rollback readiness change.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
