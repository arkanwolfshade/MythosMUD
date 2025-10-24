# 🐙 MythosMUD

A text-based, browser-accessible Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.

## Status Badges

[![CI](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml) [![CodeQL](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/codeql.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/codeql.yml) [![Semgrep](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/semgrep.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/semgrep.yml)

## Table of Contents

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
  - [License](#license)

---

## Overview

**MythosMUD** is a persistent, multiplayer, text-based adventure game with a Lovecraftian horror theme. It is designed to be beginner-friendly for both players and contributors, with a focus on exploration, narrative, and light horror combat.

- **Authors:** @arkanwolfshade & @TylerWolfshade
- **Audience:** Friends, family, and invited contributors (not public)
- **Tech Stack:**
  - Frontend: React 19 + TypeScript (Vite 7)
  - Backend: Python 3.12+ (FastAPI 0.116)
  - Database: SQLite (MVP) → PostgreSQL (production)
  - Real-time: WebSockets + NATS messaging
  - Authentication: FastAPI Users + Argon2 + JWT
  - Testing: pytest + Playwright + Vitest

---

## Current Status

**🟡 Active Development** - Core systems implemented, multiplayer messaging in progress

### ✅ Completed Systems

- **Authentication & User Management** - Complete JWT-based auth with Argon2 password hashing
- **Real-time Communication** - NATS-based messaging system with WebSocket clients
- **Player Management** - Character creation, stats generation, and persistence
- **Room System** - Hierarchical room structure with movement and navigation
- **Chat System** - Multi-channel communication (say, local, whisper, system)
- **Command Processing** - Unified command handler with alias system
- **Database Layer** - SQLite persistence with thread-safe operations
- **Testing Framework** - Comprehensive test suite with 75%+ coverage

### 🔄 In Progress

- **Multiplayer Messaging** - Critical messaging system fixes and improvements
- **Advanced Chat Channels** - Enhanced communication features
- **Performance Optimization** - Database connection pooling and query optimization

### 📋 Planned Features

- **Combat System** - Real-time combat with Lovecraftian themes
- **Magic/Spellcasting** - Spell system with sanity costs
- **Quest System** - Dynamic quest generation and tracking
- **NPC System** - Advanced NPC behavior and interactions

---

## Features

### Core Gameplay

- **Real-time Multiplayer** - Multiple players can interact simultaneously
- **Character Creation** - Random stats generation with Lovecraftian investigator archetypes
- **Room-based Exploration** - Navigate through a persistent world with exits and descriptions
- **Chat Communication** - Multiple channels including say, local, whisper, and system messages
- **Command System** - Text-based commands with alias support and help system

### Technical Features

- **Browser Accessible** - No client installation required, runs in modern browsers
- **Real-time Updates** - WebSocket and Server-Sent Events for instant updates
- **Secure Authentication** - JWT tokens with Argon2 password hashing
- **COPPA Compliant** - Privacy-first design for minor users
- **Comprehensive Testing** - 75%+ test coverage with automated CI/CD
- **Enhanced Structured Logging** - Enterprise-grade logging with MDC, correlation IDs, security sanitization, and performance monitoring

### Security & Privacy

- **Security-First Design** - All features built with security in mind
- **Input Validation** - Comprehensive server-side validation for all inputs
- **Rate Limiting** - Per-user and per-endpoint rate limiting
- **XSS Protection** - Complete client-side XSS vulnerability elimination
- **Privacy by Design** - Minimal data collection with easy deletion rights

---

## Getting Started

See [DEVELOPMENT.md](DEVELOPMENT.md) for full setup instructions.

### Quickstart

1. **Prerequisites:**
   - Python 3.12+ (managed via pyenv-win recommended)
   - Node.js 18+ and npm
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

3. **Install dependencies:**

   ```sh
   # Python dependencies
   cd server
   uv sync
   uv run pre-commit install -f

   # Client dependencies
   cd ../client
   npm install
   ```

4. **Start the development environment:**

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

5. **Visit:**
   - Frontend: <http://localhost:5173>
   - Backend API: <http://localhost:54731>
   - API Documentation: <http://localhost:54731/docs>

6. **Test the setup:**

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
│   ├── realtime/              # Real-time communication (WebSockets, NATS, SSE)
│   ├── commands/              # Command processing (admin, alias, chat, help, exploration)
│   ├── models/                # Data models (player, room, command, chat, user)
│   ├── services/              # Business logic services (NATS, chat logging, rate limiting)
│   ├── utils/                 # Utility modules (command parsing, processing)
│   ├── validators/            # Input validation (command, security)
│   ├── middleware/            # Request middleware (logging, security headers)
│   ├── schemas/               # JSON schemas (player, invite, user)
│   ├── sql/                   # Database schema and migrations
│   ├── help/                  # Help system (help_content)
│   ├── events/                # Event system (event_bus, event_types)
│   ├── app/                   # Application factory (factory, lifespan)
│   ├── npc/                   # NPC system (behaviors, combat, communication)
│   ├── logging/               # Logging utilities and formatters
│   ├── tests/                 # Test suite (comprehensive test coverage)
│   └── [core files]           # Main app, persistence, config, etc.
│
├── data/                      # World data (git submodule)
│   ├── players/               # Player database files (SQLite)
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
│   └── [other utilities]      # Testing, linting, formatting, semgrep
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
├── .github/                   # GitHub Actions workflows (CI, CodeQL, Semgrep)
├── .cursor/                   # Cursor IDE configuration
├── .agent-os/                 # AI agent specifications and tasks
├── PLANNING.md                # Comprehensive project planning
├── DEVELOPMENT.md             # Development environment setup
├── DEVELOPMENT_AI.md          # AI agent development guide
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
- `scripts/semgrep.py` - Run security analysis with Semgrep

**Test Setup Scripts:**

- `scripts/setup_test_environment.ps1` - Setup test environment files (required before running tests)
- See [Test Setup Guide](server/tests/SETUP.md) for detailed instructions

**Make Commands:**

- `make test` - Run all tests from project root
- `make test-server` - Run server tests only
- `make test-client` - Run client unit tests only (Vitest)
- `make test-client-runtime` - Run automated E2E tests (Playwright)
- `make lint` - Run linting for both server and client
- `make format` - Format code for both server and client
- `make semgrep` - Run security analysis

For multiplayer E2E scenarios, see [e2e-tests/MULTIPLAYER_TEST_RULES.md](e2e-tests/MULTIPLAYER_TEST_RULES.md)

See [scripts/README.md](scripts/README.md) for detailed documentation.

### Development Tools

- **Linting and formatting:**
  - Python: `ruff check .` and `ruff format .` in `/server` (120 char line limit)
  - JS/TS: `npx prettier --check .` and `npx eslint .` in `/client`
- **Pre-commit hooks:**
  - Installed at the repository root to catch linting/formatting issues before commit
  - Includes ruff, prettier, eslint, and semgrep security analysis
- **CI/CD:**
  - Automated with GitHub Actions for both backend and frontend
  - Includes CI, CodeQL security analysis, and Semgrep static analysis
- **Testing:**
  - Server: pytest with 75%+ coverage target
  - Client: Vitest for unit tests, Playwright for E2E tests
  - E2E Automated: 114 automated Playwright CLI tests (10 scenarios)
  - E2E Manual: 11 multiplayer MCP scenarios requiring AI Agent coordination
  - See [E2E Testing Guide](docs/E2E_TESTING_GUIDE.md) for details
  - **IMPORTANT**: Run `make setup-test-env` before running server tests
  - See [Test Setup Guide](server/tests/SETUP.md) for detailed setup instructions
- **Security:**
  - Semgrep static analysis for security vulnerabilities
  - COPPA compliance verification
  - Comprehensive input validation and XSS protection
- **AI Agents:**
  - See [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) for comprehensive AI agent guidelines
  - Includes task prioritization framework and development workflow

---

---

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md) — Full game and technical design
- [PLANNING.md](PLANNING.md) — Comprehensive project planning and current status
- [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) — Current tasks and development priorities
- [DEVELOPMENT.md](DEVELOPMENT.md) — Dev environment setup with security guidelines
- [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) — AI agent development guide
- [Multiplayer Test Rules](e2e-tests/MULTIPLAYER_TEST_RULES.md) — E2E testing framework and scenarios
- [Real-time Architecture](docs/REAL_TIME_ARCHITECTURE.md) — Technical architecture documentation
- [Advanced Chat Channels Spec](docs/ADVANCED_CHAT_CHANNELS_SPEC.md) — Communication system design
- [Enhanced Logging Guide](docs/LOGGING_BEST_PRACTICES.md) — Structured logging best practices and patterns
- [Logging Quick Reference](docs/LOGGING_QUICK_REFERENCE.md) — One-page logging cheat sheet

---

## License

[https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE](https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE)
