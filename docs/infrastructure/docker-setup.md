# Infrastructure Setup

# Infrastructure Stack

| Component | Technology |
|---|---|
| API Gateway | FastAPI |
| Queue Broker | Redis |
| Worker Runtime | Celery |
| Database | PostgreSQL |
| AI Runtime | LangGraph |
| Frontend | Next.js |

# Docker Architecture

Docker Network
↓
FastAPI
↓
Redis
↓
Celery Workers
↓
PostgreSQL

# Infrastructure Principles

## Principle 1
All services must be containerized.

## Principle 2
Services must be independently scalable.

## Principle 3
Execution must survive crashes.

# Required Services

## backend-api
FastAPI application.

## redis
Queue + Pub/Sub.

## postgres
Durable persistence.

## celery-worker
Background execution.

## frontend
Next.js application.

# Environment Variables

## Backend
- DATABASE_URL
- REDIS_URL
- SECRET_KEY

## Frontend
- NEXT_PUBLIC_API_URL