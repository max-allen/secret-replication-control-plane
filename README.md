![status](https://img.shields.io/badge/status-in%20development-yellow)

# Multi-Region Secret Replication Control Plane (Demo)

⚠️ **Work in Progress**

This repository is an educational demo intended to showcase the design and implementation of a distributed control plane responsible for orchestrating multi-region secret replication.

The project is currently in the **architecture and design phase**. Initial implementation will begin shortly.

## Planned Features

- Event-driven replication control plane
- Desired state tracking in Postgres
- Kafka-based event distribution
- Regional workers responsible for reconciliation
- Observability of replication lifecycle and failure states

## Current Status

- [x] Problem statement and design exploration
- [x] System context diagram
- [x] Data model design
- [x] Architecture document
- [ ] API implementation
- [ ] Event publishing pipeline
- [ ] Regional worker prototype

## Quick Start

```bash
# Clone the repository
git clone https://github.com/max-allen/multi-region-control-plane.git
cd multi-region-control-plane

# Build and start the API and Postgres database
docker compose up --build
```

**NOTE:** The API will be available at `http://localhost:8000` once the database is healthy and the container starts.
