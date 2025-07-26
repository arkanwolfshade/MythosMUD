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
  - Database choice: **TODO** (PostgreSQL or AWS DynamoDB preferred).

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
| Back-End      | Python (FastAPI, Starlette) or Node.js (Express, ws) | TODO     |
| Real-Time     | WebSockets                    | Planned  |
| Database      | PostgreSQL or DynamoDB        | TODO     |
| Hosting       | AWS EC2/Fargate, RDS/DynamoDB | TODO     |
| Static Assets | S3/CloudFront (if needed)     | TODO     |
| Auth          | Custom invite-only system     | Planned  |
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
  - Pytest or equivalent (if Python back-end) **TODO**
  - Cypress or Playwright (end-to-end tests) **TODO**

- **Deployment**
  - AWS CLI & SDKs
  - Docker (for local dev and deployment) **TODO**
  - Terraform or AWS CDK (for infrastructure as code) **TODO**

- **Documentation**
  - Markdown editors
  - Diagrams.net or similar for architecture diagrams **TODO**

---

## Open Questions / TODOs

- Finalize front-end and back-end frameworks/languages.
- Decide on database (PostgreSQL vs DynamoDB).
- Choose terminal UI library for the web client.
- Define CI/CD pipeline and testing frameworks.
- Select infrastructure-as-code tool (if any).
- Create initial architecture diagrams.

---

## TOP PRIORITY: Unified Persistence Layer Implementation Plan

### Rationale
A unified, extensible persistence layer is critical for maintainability, testability, and future-proofing. It will allow all game code and tests to interact with data storage in a consistent, safe, and easily swappable way, and will enable rapid iteration on features and data models without risking production data or test isolation.

### Implementation Plan
- Implement a `PersistenceLayer` class responsible for all game data (players, rooms, inventory, etc.).
- Provide a high-level CRUD API (e.g., `get_player_by_name`, `save_player`, `get_room`, `save_room`, etc.).
- Only SQLite will be supported initially, but the design will allow for future backends (e.g., Postgres, in-memory, mock).
- The persistence layer will handle conversion between DB rows and Pydantic model objects, fully abstracting storage from game logic.
- All transaction management will be handled internally, with batch/bulk operations being atomic (ACID-compliant).
- Custom exceptions will be raised for errors (e.g., unique constraint violations).
- The persistence layer will load all room data (static and dynamic) at startup for fast access.
- Hooks/callbacks will be supported for after-save, after-delete, etc. (sync now, async in future), registered via a decorator.
- Logging will be to a file, with verbosity (full SQL or summaries) configurable from the server config file.
- The persistence layer will be a singleton per app/test session, but endpoints will receive it via FastAPI dependency injection (`Depends`).
- The DB path/config will be loaded from an environment config file.
- Schema creation/migration will be handled by external scripts/utilities, not by the persistence layer.
- The test DB will be a persistent file in the `tests/` directory, pre-populated with mock room/player data at the start of each test session.
- All managers (PlayerManager, etc.) will be refactored immediately to use the new persistence layer.
- The persistence layer will be thread-safe and support context management (`with persistence as db:`).

---

_This document will be updated as decisions are made and the project evolves._

## SUMMARY (as of current session)

- The authentication system is robust, JWT-based, and fully tested.
- The /command endpoint supports 'look', 'look <direction>', 'go <direction>', and 'say', with comprehensive input validation and security.
- Room data is loaded from static JSON files for the real app, but all command handler tests now use fully mocked room and player data for isolation and reliability.
- The player manager and room data are patched in tests to ensure consistent, fast, and side-effect-free testing.
- The 'look' and 'go' commands are implemented with real logic, including movement and room description output.
- The test suite covers all edge cases, including command injection, whitespace, case insensitivity, and movement.
- Duplicate test function for invalid direction was removed to avoid confusion.
- The mock room graph was visualized for clarity.
- Two movement-related tests (`test_go_valid_direction` and `test_go_blocked_exit`) are still failing due to player state not persisting as expected in the test context; this is the next debugging target.
- Next steps: debug/fix player state persistence in tests, then continue fleshing out gameplay commands and features.
