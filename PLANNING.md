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
| Front-End     | React + TypeScript            | ✅ Implemented |
| Terminal UI   | xterm.js or similar           | ✅ Implemented |
| Back-End      | Python (FastAPI, Starlette)   | ✅ Implemented |
| Real-Time     | WebSockets                    | ✅ Implemented |
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

## Recent Completed Work (Latest Session)

### Core Infrastructure ✅

- WebSocket real-time communication system
- Client terminal interface with React + TypeScript
- Basic command parser and handler (look, go, say, help)
- Room navigation and movement system
- Player authentication and session management
- SQLite database integration with proper schema management
- Comprehensive logging system with log rotation
- Room pathing validator utility

### Game Systems ✅

- Alias system for command shortcuts
- Help system with comprehensive command documentation
- Player connection handling with username integration
- Real-time room updates and player movement
- Basic inventory and stats commands
- Security improvements and automated testing

### Development Tools ✅

- Enhanced testing infrastructure with mock persistence layer
- Development startup scripts (start/stop server)
- Pre-commit hooks with ruff linting
- Code coverage requirements (80% target)
- Room hierarchy validation and testing

---

## Current Status

**MVP Core Functionality: COMPLETE** ✅

The basic MUD functionality is now working:

- Server starts without errors
- Client connects to server via WebSocket
- Players can authenticate and create/load characters
- Room navigation works (look, go north/south/east/west)
- Real-time updates show room changes
- Basic MUD interface is functional
- Alias system allows command shortcuts
- Help system provides comprehensive documentation

**Ready for limited invite-only launch testing**

---

## Next Phase Priorities

1. **Content Creation** - Add more hand-authored zones and content
2. **Admin Tools** - Implement admin/moderator commands and tools
3. **UI/UX Polish** - Improve accessibility and user experience
4. **Performance** - Optimize for scalability
5. **Advanced Systems** - Implement magic/spellcasting, combat, death mechanics

---

## Task Tracking

All development tasks and priorities are now tracked through [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues). This provides better collaboration, tracking, and integration with GitHub's project management features.

For current development priorities and task status, please refer to the [Issues page](https://github.com/arkanwolfshade/MythosMUD/issues).

---

_This document will be updated as decisions are made and the project evolves._
