# Database Schema Design

# Database Philosophy

PostgreSQL is the source of truth.

Critical workflow state must never exist only in memory.

# Core Tables

## workflows

| Column | Purpose |
|---|---|
| workflow_id | Workflow identifier |
| tenant_id | Multi-tenant isolation |
| status | Workflow state |
| created_at | Creation timestamp |
| updated_at | Last update timestamp |

# workflow_runs

| Column | Purpose |
|---|---|
| run_id | Execution identifier |
| workflow_id | Linked workflow |
| state | Runtime state |
| started_at | Start timestamp |
| ended_at | Completion timestamp |

# workflow_events

| Column | Purpose |
|---|---|
| event_id | Event identifier |
| run_id | Linked execution |
| event_type | Event classification |
| payload | Event payload |
| timestamp | Event timestamp |

# workflow_checkpoints

| Column | Purpose |
|---|---|
| checkpoint_id | Checkpoint identifier |
| run_id | Linked execution |
| graph_state | Serialized workflow state |
| node_name | Current workflow node |
| created_at | Checkpoint timestamp |

# Indexing Strategy

Indexes required:
- workflow_id
- tenant_id
- run_id
- created_at
- status

# Concurrency Strategy

Use:
- optimistic locking
- transactional updates
- connection pooling