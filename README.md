# 🐙 MythosMUD

A text-based, browser-accessible Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.

---

[![CI](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml)
---

## Table of Contents

- [🐙 MythosMUD](#-mythosmud)
  - [](#)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
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

- **Author:** Mark Henry
- **Audience:** Friends, family, and invited contributors (not public)
- **Tech Stack:**
  - Frontend: React + TypeScript (Vite)
  - Backend: Python (FastAPI)
  - Database: PostgreSQL (preferred)

---

## Getting Started

See [DEVELOPMENT.md](DEVELOPMENT.md) for full setup instructions.

### Quickstart

1. **Clone the repository with submodules:**

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

2. **Start the development environment:**

   ```powershell
   # Windows PowerShell
   .\scripts\start_dev.ps1
   ```

   Or manually:

   ```sh
   # Backend
    cd server
    pyenv local 3.12.11  # or your preferred Python 3.12+ version
   uv sync
   uv run uvicorn main:app --reload

   # Frontend (in another terminal)
   cd client
   npm install
   npm run dev
   ```

3. **Visit:**
   - Backend: <http://localhost:54731>
   - Frontend: <http://localhost:5173>

---

## Project Structure

```
MythosMUD/
├── client/      # React + TypeScript frontend (Vite)
├── server/      # Python FastAPI backend
├── data/        # World data (git submodule)
├── scripts/     # Utility scripts (PowerShell & Python)
├── docs/        # Documentation (PRD, etc.)
├── .github/     # GitHub Actions workflows
├── PLANNING.md  # Vision, architecture, stack
├── DEVELOPMENT.md # Dev environment setup
└── README.md    # This file
```

---

## Development

### Utility Scripts

The `scripts/` directory contains PowerShell and Python utility scripts for managing the development environment:

**PowerShell Scripts:**

- `scripts/start_server.ps1` - Start the FastAPI server
- `scripts/stop_server.ps1` - Stop server processes
- `scripts/start_dev.ps1` - Start complete development environment

**Python Scripts:**

- `scripts/run.py` - Run the server
- `scripts/test.py` - Run tests
- `scripts/lint.py` - Lint code
- `scripts/format.py` - Format code

See [scripts/README.md](scripts/README.md) for detailed documentation.

### Development Tools

- **Linting and formatting:**
  - Python: `ruff check .` and `ruff format .` in `/server`
  - JS/TS: `npx prettier --check .` and `npx eslint .` in `/client`
- **Pre-commit hooks:**
  - Installed at the repository root to catch linting/formatting issues before commit
- **CI:**
  - Automated with GitHub Actions for both backend and frontend
- **AI Agents:**
  - See [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) for comprehensive AI agent guidelines

---

---

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md) — Full game and technical design
- [PLANNING.md](PLANNING.md) — Vision, architecture, stack
- [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) — Current tasks and development priorities
- [DEVELOPMENT.md](DEVELOPMENT.md) — Dev environment setup
- [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) — AI agent development guide

---

## License

[https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE](https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE)
