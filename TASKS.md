# 📝 MythosMUD – Task Breakdown & Milestones

> **Development Discipline Checklist:**
>
> - [ ] Write/update tests before implementing features (TDD)
> - [ ] Mark tasks as complete in TASKS.md as soon as they are done
> - [ ] Commit to git after each feature or fix is complete
> - [ ] Keep this file and PLANNING.md in sync with actual progress

---

## TOP PRIORITY: Implement Unified PersistenceLayer

- [x] Design PersistenceLayer API
- [x] Implement CRUD for all game data (players, rooms, inventory, etc.)
- [x] Support batch/atomic operations (ACID)
- [x] Handle conversion between DB rows and Pydantic models
- [x] Implement hooks/callbacks (sync, with async support planned)
- [x] Add file-based logging with configurable verbosity
- [x] Load all room data at startup (static and dynamic)
- [x] Support FastAPI dependency injection (Depends)
- [x] Read DB config from environment config file
- [x] Refactor all managers to use the new layer
- [x] Create and pre-populate a persistent test DB in tests/
- [x] Ensure thread safety and context management
- [x] Remove old direct DB/file access from managers
- [x] Update all tests to use the new persistence layer
- [x] Document the new architecture and usage
  - [x] Refactor all managers to use the new PersistenceLayer for all data access
  - [x] Refactor all FastAPI endpoints to use the PersistenceLayer (via DI or singleton)
  - [x] Add a Room Pydantic model if not already present
  - [x] Update all tests to use the test DB and the new PersistenceLayer
  - [ ] Add missing CRUD for inventory, status effects, etc. to PersistenceLayer
  - [ ] Implement missing CRUD and effect/stat logic in the PersistenceLayer
  - [ ] Implement CRUD methods for inventory and status effects (e.g., apply_sanity_loss, apply_fear)
  - [ ] Implement log rotation for persistence.log to prevent log file bloat
  - [x] Define a server config file (YAML or TOML) and implement a config loader
  - [ ] Fix config loader bool handling for invalid types
  - [ ] Wire game server to respect game_tick_rate from config
  - [ ] Debug /auth/login test setup and token generation issues
  - [x] Fix test_player_manager.py to use PersistenceLayer (in progress)
  - [ ] Update test_auth.py and test_command_handler.py to use PersistenceLayer
  - [ ] Several tests in test_command_handler.py and test_auth.py are failing or incomplete (see .pytest_cache)
  - [ ] Mock data migration from code to JSON files is done, but tests relying on this data may not be fully updated
  - [x] Add delete_player method to PersistenceLayer
  - [ ] Add status/effect methods to PersistenceLayer (apply_sanity_loss, apply_fear, etc.)
  - [ ] Add async support for hooks in PersistenceLayer (currently synchronous, see TODO)
  - [x] Debug and fix "KeyError: 'access_token'" failures in auth tests
  - [ ] Fix command handler tests to work with new PersistenceLayer architecture
  - [x] Fix auth tests to work with new PersistenceLayer architecture
  - [x] Fix command handler tests database issues (15/23 tests now passing)
  - [x] Fix command handler tests room data and movement logic (remaining 8 tests need mock room data)
  - [x] Migrate mock room data from code to JSON files (completed - removed MOCK_ROOMS from mock_data.py)
  - [ ] Fix auth test setup and token generation issues (temporary files causing user conflicts)
  - [ ] Implement log rotation: move existing persistence.log to timestamped name (e.g., persistence.log.2025_07_25_221030) before creating new log file
  - [x] Fix critical security vulnerabilities (hardcoded secret key, path injection)
  - [ ] Migrate user storage from JSON files to database (security improvement)
  - [ ] Implement rate limiting for authentication endpoints to prevent brute-force attacks

---

## Milestone 1: Project Foundation

- [x] Initialize repository and set up version control
- [x] Create initial documentation (`README.md`, `PRD.md`, `PLANNING.md`, `TASKS.md`)
- [x] Decide on core technology stack (front-end, back-end, database)
- [x] Set up basic project structure for client and server
- [x] Configure development environment (linters, formatters, pre-commit hooks)
- [x] Set up basic CI (GitHub Actions for backend and frontend)
- [x] Add CodeQL analysis workflow
- [x] Add SECURITY.md file
- [x] Add Dependabot configuration (optional)

---

## Milestone 2: Core Server & World Model

- [x] Scaffold server event loop (tick-based, 1000ms)
- [x] Design JSON schema for room/world data model
- [x] Create sample hand-authored room file (e.g., `arkham_001.json`)
- [x] Scaffold Python loader to read all room files from zone directories
- [x] Integrate room/world loader into FastAPI app and expose `/rooms/{room_id}` endpoint
- [x] Implement player and NPC data models
- [x] Set up database schema and persistence layer (SQLite-based)
- [x] Basic command parser and handler (e.g., `look`, `go`, `say`)
  - [x] Command endpoint and parser implemented
  - [x] `look`, `go`, `say` logic implemented
  - [x] Input scrubbing and edge case handling
  - [x] Duplicate test function for invalid direction removed
  - [x] Mock room graph visualized for clarity
  - [x] All command handler tests use mock data for isolation
  - [x] All tests passing for movement and look commands
    - [x] Debug/fix player state persistence in tests
- [x] Implement player authentication (invite-only)
  - [ ] MVP definition of done: Migrate to FastAPI Users and a database for authentication
  - [x] Use SQLite for MVP database for players
- [ ] Robust logging system with separate files for: system logs, player activity, communication channels - should be well structured for eventual ingestion into ELK stack
- [ ] Add automated tests to verify path traversal and file access security (e.g., for invites_file and similar parameters)
- [ ] Error handling for room cache loading may not be robust enough for edge cases

---

## Milestone 3: Client Terminal Interface

- [ ] Set up web-based terminal UI (React + xterm.js or similar)
- [ ] Implement real-time communication (WebSockets)
  - [ ] Add WebSocket support for real-time command handling (needed for node client interface)
- [ ] Use test-driven development (TDD) for new features: write tests first, cover edge cases, and iterate code until tests pass
- [ ] Implement a room pathing validator utility to check for path consistency and highlight one-way or non-physical exits (with support for special cases)
- [ ] Display text output and accept user commands
- [ ] Add command history, scrollback, and basic styling
- [ ] Render ASCII navigation map

---

## Milestone 4: Gameplay Systems

- [ ] Implement combat system (room-based, aggro, tanking)
- [ ] Add sanity system (tracking, effects, recovery)
- [ ] Implement death and resurrection mechanics
- [ ] Add inventory and equipment system
- [ ] Implement basic magic/spellcasting (with sanity costs)
- [ ] Add quest system (linear quests, quest givers)
- [ ] Implement party/grouping mechanics
- [ ] Add detailed implementation plans for combat, inventory management, and quest systems

---

## Milestone 5: Multiplayer & Social Features

- [ ] Implement chat channels (global, local, party, say, whisper)
- [ ] Add communication controls (mute, filters, admin alerts)
- [ ] Implement party XP sharing and quest sync
- [ ] Add admin/moderator commands (kick, ban, spawn NPCs, etc.)
- [ ] Build real-time monitoring/admin panel (optional)

---

## Milestone 6: Content & Polish

- [ ] Create additional hand-authored zones (Arkham, etc.)
- [ ] Expand world with additional zones (Innsmouth, Dunwich, Kingsport, remote areas)
- [ ] Add more NPCs, mobs, and quests
- [ ] Polish UI/UX (client enhancements, accessibility)
- [ ] Improve documentation and onboarding guides
- [ ] Ensure TASKS.md and PLANNING.md are fully synchronized with the current state of development
- [ ] Optimize performance and scalability
- [ ] Prepare for limited invite-only launch

---

## Milestone 7: Future Features (Post-MVP)

- [ ] Cultist faction and PvP mechanics
- [ ] Branching quests and morality system
- [ ] Full crafting and alchemy systems
- [ ] Dynamic world events (Mythos incursions)
- [ ] Content creation tools or web-based builder
- [ ] Plugin/modding system

---

_This list will be updated and refined as the project evolves._
