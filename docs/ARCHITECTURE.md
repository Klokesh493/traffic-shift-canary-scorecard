# Traffic Shift Canary Scorecard architecture

Scores canary shifts by error rate, latency, saturation, and rollback readiness.

```mermaid
flowchart LR
    N0["sample_canary.csv"]
    N1["canary_scorecard.py"]
    N2["verdict"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
