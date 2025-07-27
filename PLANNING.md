# 🗺️ MythosMUD – Planning Document

This document outlines the vision, high-level architecture, technology stack, and required tools for the MythosMUD project.
If a decision is pending, it is marked as **TODO**.

---

## Vision

- Build a browser-accessible, text-based Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.
- Focus on collaborative storytelling, exploration, and light horror combat.
- Make the codebase beginner-friendly for contributors and maintainers.
- Support persistent multiplayer gameplay with real-time interactions.
- Prioritize modularity, readability, and extensibility.

---

## Architecture

### High-Level Overview

- **Client (Front-End):**
  - Web-based terminal interface for text commands and output.
  - Features: command history, triggers, aliases, highlighting, ASCII navigation map.
  - Communicates with the server via WebSockets or similar real-time protocol.

- **Server (Back-End):**
  - Real-time, tick-based event loop.
  - Handles game logic, world state, combat, chat, and persistence.
  - Modular design for rooms, NPCs, combat, sanity, quests, etc.
  - Exposes APIs for client communication and admin tools.

- **Persistence Layer:**
  - Stores character data, world state, inventory, quest progress, and sanity.
  - Database choice: **SQLite for MVP, PostgreSQL or AWS DynamoDB preferred for production**.

- **Hosting/Deployment:**
  - Cloud-based, cost-optimized (AWS preferred).
  - SSL/TLS for secure connections.
  - Invite-only authentication.

---

## Technology Stack

| Layer         | Technology (Preferred)         | Status   |
|---------------|-------------------------------|----------|
| Front-End     | React + TypeScript            | TODO     |
| Terminal UI   | xterm.js or similar           | TODO     |
| Back-End      | Python (FastAPI, Starlette)   | ✅ Implemented |
| Real-Time     | WebSockets                    | Planned  |
| Database      | SQLite (MVP), PostgreSQL or DynamoDB | ✅ SQLite Implemented |
| Hosting       | AWS EC2/Fargate, RDS/DynamoDB | TODO     |
| Static Assets | S3/CloudFront (if needed)     | TODO     |
| Auth          | Custom invite-only system     | ✅ Implemented |
| CI/CD         | GitHub Actions (optional)     | TODO     |

---

## Required Tools

- **Development**
  - Node.js & npm/yarn (for front-end and possibly back-end)
  - Python 3.x (if using Python back-end)
  - PostgreSQL or DynamoDB local emulator
  - Git & GitHub
  - VSCode or preferred code editor

- **Testing**
  - Jest (front-end/unit tests) **TODO**
  - Pytest or equivalent (if Python back-end) **✅ Implemented**
  - Cypress or Playwright (end-to-end tests) **TODO**

- **Deployment**
  - AWS CLI & SDKs
  - Docker (for local dev and deployment) **TODO**
  - Terraform or AWS CDK (for infrastructure as code) **TODO**

- **Documentation**
  - Markdown editors
  - Diagrams.net or similar for architecture diagrams **TODO**

---

---

## Task Tracking

All development tasks and priorities are now tracked through [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues). This provides better collaboration, tracking, and integration with GitHub's project management features.

For current development priorities and task status, please refer to the [Issues page](https://github.com/arkanwolfshade/MythosMUD/issues).

---

_This document will be updated as decisions are made and the project evolves._
