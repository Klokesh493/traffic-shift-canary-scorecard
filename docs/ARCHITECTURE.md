# Traffic Shift Canary Scorecard architecture

Scores canary shifts by error rate, latency, saturation, and rollback readiness.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
