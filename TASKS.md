# 📝 MythosMUD – Task Breakdown & Milestones

This document organizes development tasks into milestones for building MythosMUD.
Tasks are high-level and will be refined as the project progresses.

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
- [x] Set up database schema and persistence layer (JSON-based for now)

- [ ] Basic command parser and handler (e.g., `look`, `go`, `say`)
- [ ] Implement player authentication (invite-only)
- [ ] Create additional hand-authored zones (Arkham, etc.)

---

## Milestone 3: Client Terminal Interface

- [ ] Set up web-based terminal UI (React + xterm.js or similar)
- [ ] Implement real-time communication (WebSockets)
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

---

## Milestone 5: Multiplayer & Social Features

- [ ] Implement chat channels (global, local, party, say, whisper)
- [ ] Add communication controls (mute, filters, admin alerts)
- [ ] Implement party XP sharing and quest sync
- [ ] Add admin/moderator commands (kick, ban, spawn NPCs, etc.)
- [ ] Build real-time monitoring/admin panel (optional)

---

## Milestone 6: Content & Polish

- [ ] Expand world with additional zones (Innsmouth, Dunwich, Kingsport, remote areas)
- [ ] Add more NPCs, mobs, and quests
- [ ] Polish UI/UX (client enhancements, accessibility)
- [ ] Improve documentation and onboarding guides
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
