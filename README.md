# 🐙 MythosMUD

A text-based, browser-accessible Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.

## Status Badges

[![CI](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml)
[![CodeQL](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/codeql.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/codeql.yml)
[![Codacy
Badge](https://app.codacy.com/project/badge/Grade/0c361cf70a234b86b1b0f058ffd00549)](https://app.codacy.com/gh/arkanwolfshade/MythosMUD/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

## Table of Contents

[🐙 MythosMUD](#-mythosmud)

- [🐙 MythosMUD](#-mythosmud)
  - [Status Badges](#status-badges)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Current Status](#current-status)
    - [✅ Completed Systems](#-completed-systems)
    - [🔄 In Progress](#-in-progress)
    - [📋 Planned Features](#-planned-features)
  - [Features](#features)
    - [Core Gameplay](#core-gameplay)
    - [Technical Features](#technical-features)
    - [Security \& Privacy](#security--privacy)
  - [Getting Started](#getting-started)
    - [Quickstart](#quickstart)
  - [Project Structure](#project-structure)
  - [Development](#development)
    - [Utility Scripts](#utility-scripts)
    - [Development Tools](#development-tools)
  - [Documentation](#documentation)
    - [Core Documentation](#core-documentation)
    - [Development Guides](#development-guides)
    - [Testing Documentation](#testing-documentation)
    - [Architecture \& Technical Specs](#architecture--technical-specs)
    - [Logging \& Monitoring](#logging--monitoring)
    - [Security \& Error Handling](#security--error-handling)
  - [License](#license)

---

## Overview

**MythosMUD** is a persistent, multiplayer, text-based adventure game with a Lovecraftian horror theme. It is designed
to be beginner-friendly for both players and contributors, with a focus on exploration, narrative, and light horror
combat.

**Authors:** @arkanwolfshade & @TylerWolfshade

**Audience:** Friends, family, and invited contributors (not public)

**Tech Stack:**

- Frontend: React 19.1+ + TypeScript 5.9 (Vite 7.1+)
- Backend: Python 3.12+ (FastAPI 0.121+)
- Database: PostgreSQL (development, tests, and production)
- Real-time: WebSockets + NATS messaging
- Authentication: FastAPI Users + Argon2 + JWT
- Testing: pytest + Playwright + Vitest
- Dependency Management: uv for Python, npm for Node.js
- Code Quality: ruff (Python linter/formatter), ESLint + Prettier (JavaScript/TypeScript)

---

## Current Status

**🟢 Beta Development** - Core systems implemented and tested, multiplayer features active

### ✅ Completed Systems

**Authentication & User Management** - Complete JWT-based auth with Argon2 password hashing and invite system

**Real-time Communication** - Dual connection system with NATS-based messaging and WebSocket/SSE clients

**Player Management** - Character creation, stats generation, and persistence with PostgreSQL

**Room System** - Hierarchical room structure with movement, navigation, and dynamic descriptions

**Chat System** - Multi-channel communication (say, local, whisper, system, emotes)

**Command Processing** - Unified command handler with alias system and help system

**Admin Tools** - Teleportation, player management, and monitoring commands

**NPC System** - Basic NPC spawning, behavior, and combat interactions

**Magic/Spellcasting System** - Complete spell system with MP (Magic Points), spell learning and mastery, material

components, casting times, and integration with combat and lucidity systems

**Database Layer** - PostgreSQL persistence with async operations, connection pooling, and migration support

**Enhanced Logging** - Structured logging with MDC, correlation IDs, security sanitization, and performance monitoring

- **Testing Framework** - Comprehensive test suite with 80%+ coverage, 304 test files, and automated E2E tests
- **Security Framework** - Input validation, rate limiting, XSS protection, and COPPA compliance measures

### 🔄 In Progress

**Advanced Chat Channels** - Tab-based channel management and filtering

**Combat System** - Expanded combat mechanics with lucidity effects

**Performance Optimization** - Database connection pooling and query optimization

**Advanced NPC Behaviors** - Improved AI patterns and dialogue systems

### 📋 Planned Features

**Quest System** - Dynamic quest generation and tracking

**Crafting System** - Item crafting and modification

**Advanced World Systems** - Dynamic events, weather, and time progression

**Player Housing** - Personal spaces and storage systems

- **Achievement System** - Tracking player accomplishments

---

## Features

### Core Gameplay

**Real-time Multiplayer** - Multiple players can interact simultaneously (100ms server tick rate for responsive
gameplay)

**Character Creation** - Random stats generation with Lovecraftian investigator archetypes

**Room-based Exploration** - Navigate through a persistent world with exits and descriptions

**Chat Communication** - Multiple channels including say, local, whisper, and system messages

**Command System** - Text-based commands with alias support and help system

**Magic System** - Cast spells, learn new spells, track mastery, and manage MP (Magic Points) with automatic

regeneration

### Technical Features

**Browser Accessible** - No client installation required, runs in modern browsers

**Dual Connection System** - WebSocket for commands + Server-Sent Events for real-time updates

**Secure Authentication** - JWT tokens with Argon2 password hashing and invite-only system

**COPPA Compliant** - Privacy-first design for minor users with no personal data collection

**Comprehensive Testing** - 80%+ test coverage with automated CI/CD and comprehensive E2E test suite

**Enhanced Structured Logging** - Enterprise-grade logging with:

- MDC (Mapped Diagnostic Context) for automatic context propagation

- Correlation IDs for request tracing across service boundaries

- Automatic security sanitization of sensitive data

- Built-in performance monitoring and metrics collection

- 100% exception coverage with rich context

**Modular Test Framework** - Hierarchical test organization with 304 test files across unit, integration, E2E,

security, and performance categories

### Security & Privacy

**Security-First Design** - All features built with security in mind

**Input Validation** - Comprehensive server-side validation for all inputs

**Rate Limiting** - Per-user and per-endpoint rate limiting

**XSS Protection** - Complete client-side XSS vulnerability elimination

- **Privacy by Design** - Minimal data collection with easy deletion rights

---

## Getting Started

See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for full setup instructions.

### Quickstart

1. **Prerequisites:**
   - Python 3.12+ (managed via pyenv-win recommended)
   - Node.js 22+ and npm (NVM for Windows recommended)
   - PostgreSQL 15+ (for database - required for tests and development)
   - [uv](https://github.com/astral-sh/uv) for Python dependency management
   - Git

2. **Clone the repository with submodules:**

   ```sh
   # Option 1: Clone with submodules in one command

   git clone --recursive <your-repo-url>
   cd MythosMUD
   ```

   ```sh
   # Option 2: Clone first, then fetch submodules

   git clone <your-repo-url>
   cd MythosMUD
   git submodule update --init --recursive
   ```

3. **Set up test environment:**

   ```powershell
   # Create test environment files (required before running tests)

   .\scripts\setup_test_environment.ps1
   ```

4. **Install dependencies:**

   ```sh
   # Python dependencies

   cd server
   uv sync
   uv run pre-commit install -f

   # Client dependencies

   cd ../client
   npm install
   ```

5. **Start the development environment:**

   ```powershell
   # Windows PowerShell - Start both server and client

   .\scripts\start_local.ps1
   ```

   Or start components separately:

   ```powershell
   # Start server only

   .\scripts\start_server.ps1

   # Start client only (in another terminal)

   .\scripts\start_client.ps1
   ```

6. **Visit:**
   - Frontend: <http://localhost:5173>
   - Backend API: <http://localhost:54731>
   - API Documentation: <http://localhost:54731/docs>

7. **Test the setup:**

   ```sh
   # Run tests

   make test

   # Run linting

   make lint
   ```

---

## Project Structure

```text
MythosMUD/
├── client/                    # React 19 + TypeScript frontend (Vite 7)
│   ├── src/
│   │   ├── components/        # React components (GameTerminal, Panels, UI)
│   │   │   ├── panels/        # Chat, Command, Room, Connection panels
│   │   │   ├── ui/            # Reusable UI components
│   │   │   └── layout/        # Grid layout management
│   │   ├── hooks/             # React hooks (useGameConnection, useGameTerminal)
│   │   ├── stores/            # Zustand state management
│   │   ├── contexts/          # React contexts (GameTerminal, Panel, Theme)
│   │   ├── utils/             # Utility functions (ansiToHtml, errorHandler)
│   │   ├── theme/             # Theming system (mythosTheme)
│   │   ├── styles/            # Style files (motd-preserved.css)
│   │   └── test/              # Test utilities and setup
│   ├── tests/                 # End-to-end tests (Playwright)
│   ├── public/                # Public assets
│   └── [config files]         # TypeScript, Vite, TailwindCSS, ESLint configs
│
├── server/                    # Python FastAPI backend
│   ├── auth/                  # Authentication system (Argon2, JWT, invites)
│   ├── api/                   # API endpoints (game, players, rooms, monitoring, admin)
│   ├── game/                  # Game logic services (chat, movement, stats, character creation)
│   ├── realtime/              # Real-time communication (WebSockets, NATS, SSE dual connection)
│   ├── commands/              # Command processing (admin, alias, chat, help, exploration)
│   ├── models/                # Data models (player, room, command, chat, user, NPC)
│   ├── services/              # Business logic services (NATS, chat logging, rate limiting)
│   ├── utils/                 # Utility modules (command parsing, processing)
│   ├── validators/            # Input validation (command, security)
│   ├── middleware/            # Request middleware (correlation IDs, logging, security headers)
│   ├── schemas/               # JSON schemas (player, invite, user)
│   ├── sql/                   # Database schema and migrations
│   ├── help/                  # Help system (help_content)
│   ├── events/                # Event system (event_bus, event_types)
│   ├── app/                   # Application factory (factory, lifespan, memory management)
│   ├── npc/                   # NPC system (behaviors, combat, communication, state machines)
│   ├── structured_logging/    # Enhanced logging (MDC, correlation IDs, security sanitization)
│   ├── tests/                 # Hierarchical test suite (304 test files organized by type)
│   │   ├── unit/              # Unit tests
│   │   ├── integration/       # Integration tests
│   │   ├── e2e/               # End-to-end tests
│   │   ├── security/          # Security-specific tests
│   │   ├── performance/       # Performance and load tests
│   │   ├── regression/        # Bug fix regression tests
│   │   ├── monitoring/        # Monitoring and observability tests
│   │   ├── coverage/          # Coverage improvement tests
│   │   ├── verification/      # Verification tests
│   │   ├── fixtures/          # Shared test fixtures
│   │   └── scripts/           # Test utility scripts
│   └── [core files]           # Main app, persistence, config, etc.
│
├── data/                      # World data (git submodule)
│   ├── players/               # Player database files (PostgreSQL)
│   ├── npcs/                  # NPC database files
│   ├── rooms/                 # Hierarchical room structure (earth/yeng planes)
│   ├── user_management/       # User management data
│   └── [game data]            # Emotes, MOTD, visualizations
│
├── scripts/                   # Utility scripts (PowerShell & Python)
│   ├── start_local.ps1          # Development server startup
│   ├── stop_server.ps1        # Server shutdown
│   ├── start_server.ps1       # Server-only startup
│   ├── start_client.ps1       # Client-only startup
│   └── [other utilities]      # Testing, linting, formatting
│
├── e2e-tests/                 # End-to-end testing framework
│   ├── scenarios/             # 21 multiplayer test scenarios
│   ├── MULTIPLAYER_TEST_RULES.md # Master test execution rules
│   ├── CLEANUP.md             # Post-scenario cleanup procedures
│   └── TROUBLESHOOTING.md     # Error handling and debugging
│
├── docs/                      # Documentation
│   ├── archive/               # Consolidated planning documents
│   ├── PRD.md                 # Product Requirements Document
│   ├── REAL_TIME_ARCHITECTURE.md # Real-time system architecture
│   └── [technical docs]       # Security, database, room planning
│
├── schemas/                   # JSON schemas for validation
│   ├── room_schema.json       # Room definition schema
│   ├── intersection_schema.json # Intersection schema
│   └── unified_room_schema.json # Unified room schema
│
├── tools/                     # Development tools
│   ├── invite_tools/          # Invite management utilities
│   └── room_toolkit/          # Room validation and tools
│
├── .github/                   # GitHub Actions workflows (CI, CodeQL)
├── .cursor/                   # Cursor IDE configuration
├── PLANNING.md                # Comprehensive project planning
├── docs/DEVELOPMENT.md         # Development environment setup
├── docs/DEVELOPMENT_AI.md     # AI agent development guide
├── TASKS.md                   # Task tracking (deprecated - use GitHub Issues)
├── TASKS.local.md             # Local task tracking
├── Makefile                   # Build and development commands
├── pyproject.toml             # Python project configuration
├── uv.lock                    # Python dependency lock file
└── README.md                  # This file
```

---

## Development

### Utility Scripts

The `scripts/` directory contains PowerShell and Python utility scripts for managing the development environment:

**PowerShell Scripts:**

- `scripts/start_local.ps1` - Start complete development environment (server + client)
- `scripts/start_server.ps1` - Start the FastAPI server only
- `scripts/start_client.ps1` - Start the React client only
- `scripts/stop_server.ps1` - Stop server processes

**Python Scripts:**

- `scripts/run.py` - Run the server
- `scripts/test.py` - Run tests (server, client, or both)
- `scripts/lint.py` - Lint code with ruff
- `scripts/format.py` - Format code with ruff

**Test Setup Scripts:**

- `scripts/setup_test_environment.ps1` - Setup test environment files (required before running tests)
- See [Test Setup Guide](server/tests/SETUP.md) for detailed instructions

**Make Commands:**

- `make test` - Run default test suite from project root (~5-7 min)
- `make test-comprehensive` - Run comprehensive test suite via act (mirrors CI, ~30 min)
- `make test-client` - Run client unit tests only (Vitest)
- `make test-client-e2e` - Run automated E2E tests (Playwright)
- `make lint` - Run linting for both server and client
- `make format` - Format code for both server and client

For multiplayer E2E scenarios, see [e2e-tests/MULTIPLAYER_TEST_RULES.md](e2e-tests/MULTIPLAYER_TEST_RULES.md)

See [scripts/README.md](scripts/README.md) for detailed documentation.

### Development Tools

**Linting and formatting:**

- Python: `ruff check .` and `ruff format .` in `/server` (120 char line limit)
- JS/TS: `npx prettier --check .` and `npx eslint .` in `/client`
- **Pre-commit hooks:**
  - Installed at the repository root to catch linting/formatting issues before commit
  - Includes ruff, prettier, eslint, and semgrep security analysis
- **Cursor Hooks:**
  - Configured in `.cursor/hooks.json` (Settings → Hooks in Cursor IDE)
  - **afterFileEdit:** Formats agent-edited files (ruff for `server/` Python, prettier for `client/` TS/JSON/MD) so agent output matches pre-commit; script: `.cursor/hooks/format-after-edit.ps1`
  - Project hooks run from the project root; scripts live in `.cursor/hooks/`
  - Formatting after agent edit is handled by Cursor hooks; for manual edits use "Format Document" or run pre-commit before commit
- **CI/CD:**
  - Automated with GitHub Actions for both backend and frontend
  - Includes CI, CodeQL security analysis, and Semgrep static analysis
- **Testing:**
  - Server: pytest with 80%+ coverage (target 90%)
  - Client: Vitest for unit tests, Playwright for E2E tests
  - Test Organization: Hierarchical structure with 304 test files across 9 categories
  - E2E Automated: Comprehensive Playwright CLI tests for runtime scenarios
  - E2E Manual: 21 multiplayer MCP scenarios requiring AI Agent coordination (see e2e-tests/scenarios/)
  - See [E2E Testing Guide](docs/E2E_TESTING_GUIDE.md) for details
  - **CRITICAL**: Run `make setup-test-env` before running server tests for the first time
  - **CRITICAL**: Always use `make test` from project root, NEVER from `/server/` directory
  - See [Test Setup Guide](server/tests/SETUP.md) for detailed setup instructions
- **Security:**
  - COPPA compliance verification
  - Comprehensive input validation and XSS protection
- **AI Agents:**
  - See [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) for comprehensive AI agent guidelines
  - Includes task prioritization framework and development workflow

---

---

## Documentation

### Core Documentation

[Product Requirements Document (PRD)](docs/PRD.md) — Full game and technical design

- [Deployment](docs/deployment.md) — Production deployment with Gunicorn + Uvicorn
- [PLANNING.md](PLANNING.md) — Comprehensive project planning and current status
- [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) — Current tasks and development priorities

### Development Guides

[DEVELOPMENT.md](docs/DEVELOPMENT.md) — Dev environment setup with security guidelines

- [DEVELOPMENT_AI.md](docs/DEVELOPMENT_AI.md) — AI agent development guide and workflow
- [AI Development Workflow](docs/AI_DEVELOPMENT_WORKFLOW.md) — Detailed AI agent task management
- [Cursor Setup Guide](docs/CURSOR_SETUP_GUIDE.md) — Optimize Cursor IDE for subagents and CLI usage
- [Cursor Hooks](docs/CURSOR_HOOKS.md) — Cursor Hooks configuration (afterFileEdit formatter, Settings → Hooks)

### Testing Documentation

[E2E Testing Guide](docs/E2E_TESTING_GUIDE.md) — Comprehensive E2E testing documentation

- [Multiplayer Test Rules](e2e-tests/MULTIPLAYER_TEST_RULES.md) — E2E testing framework and 21 scenarios
- [Command Testing Guide](docs/COMMAND_TESTING_GUIDE.md) — Testing command implementations

### Architecture & Technical Specs

[Real-time Architecture](docs/REAL_TIME_ARCHITECTURE.md) — Dual connection system architecture

- [Advanced Chat Channels Spec](docs/ADVANCED_CHAT_CHANNELS_SPEC.md) — Communication system design
- [Dual Connection System](docs/DUAL_CONNECTION_SYSTEM_SPEC.md) — WebSocket + SSE architecture

### Logging & Monitoring

[Enhanced Logging Guide](docs/LOGGING_BEST_PRACTICES.md) — Structured logging best practices and patterns

- [Logging Quick Reference](docs/LOGGING_QUICK_REFERENCE.md) — One-page logging cheat sheet
- [Enhanced Logging Implementation](docs/ENHANCED_LOGGING_GUIDE.md) — Detailed logging implementation guide

### Security & Error Handling

[Security Fixes](docs/SECURITY_FIXES.md) — Security implementation and fixes

- [Error Handling Guide](docs/ERROR_HANDLING_GUIDE.md) — Error handling patterns and best practices
- [Troubleshooting Guide](docs/TROUBLESHOOTING_GUIDE.md) — Common issues and solutions

---

## License

[https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE](https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE)
