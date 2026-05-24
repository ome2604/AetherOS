# ADR-001 — Use Celery for Distributed Execution

# Context
The platform requires:
- asynchronous execution
- retries
- distributed workers
- durable workflow execution

# Decision
Use Celery with Redis broker.

# Alternatives Considered
- RQ
- Dramatiq
- custom worker engine

# Tradeoffs

## Pros
- mature ecosystem
- retry support
- distributed execution

## Cons
- operational complexity
- monitoring overhead

# Consequences
Enables:
- scalable execution
- background processing
- worker distribution