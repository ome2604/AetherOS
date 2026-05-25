# ADR-005 — LangGraph Adoption

# Status
ACCEPTED

# Context

AetherOS requires:
- stateful workflow orchestration
- graph-based execution
- future multi-agent coordination
- resumable workflows

Traditional task pipelines were insufficient for complex orchestration.

---

# Decision

LangGraph selected as orchestration runtime.

---

# Rationale

LangGraph provides:
- graph execution modeling
- stateful execution
- workflow transitions
- orchestration primitives
- agent coordination support

This aligns with long-term AI Operating System goals.

---

# Alternatives Considered

## Celery Chains
Rejected due to:
- limited orchestration visibility
- weak state modeling
- poor graph abstraction

## Custom DAG Engine
Rejected due to:
- increased maintenance burden
- higher implementation complexity

---

# Consequences

## Positive
- enterprise orchestration support
- scalable workflow management
- future AI agent extensibility

## Negative
- additional orchestration complexity
- learning curve

---

# Final Assessment

LangGraph best supports:
- durable AI execution
- orchestration scalability
- future autonomous systems