# Django Backend Starter

An enterprise-ready Django backend starter with Docker, PostgreSQL, Redis, JWT authentication, and more.

## Quick Start

1. Navigate to your project:
   ```bash
   cd <project_name>
   ```

2. Start all services:
   ```bash
   make up
   ```

3. API will be available at: http://localhost:8000

4. Login endpoint: POST /api/auth/login/
   - Phone: 1234567890
   - Password: password

## Available Commands

- `make up`: Start all services with build
- `make down`: Stop all services
- `make migrate`: Run database migrations
- `make shell`: Open Django shell
- `make logs`: View service logs
- `make test`: Run tests with pytest

## API Documentation

- Swagger UI: http://localhost:8000/docs/
- Health checks:
  - /health/ - General health
  - /health/db/ - Database health
  - /health/redis/ - Redis health

## Project Structure

- `apps/`: Custom Django apps (users, authentication, audit)
- `core/`: Shared utilities (exceptions, permissions, health checks)
- `infrastructure/`: Infrastructure code (Celery, tasks)
- `docker/`: Docker configurations
- `requirements/`: Python dependencies
