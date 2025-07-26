# 🐙 MythosMUD

A text-based, browser-accessible Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.

---
[![CI](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml/badge.svg)](https://github.com/arkanwolfshade/MythosMUD/actions/workflows/ci.yml)
---

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development](#development)

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

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd MythosMUD
   ```
2. **Set up the backend:**
   ```sh
   cd server
   pyenv local 3.11.8  # or your preferred Python 3.11+ version
   uv sync
   uv run uvicorn main:app --reload
   ```
3. **Set up the frontend:**
   ```sh
   cd ../client
   npm install
   npm run dev
   ```
4. **Visit:**
   - Backend: http://localhost:8000
   - Frontend: http://localhost:5173

---

## Project Structure

```
MythosMUD/
├── client/      # React + TypeScript frontend (Vite)
├── server/      # Python FastAPI backend
├── docs/        # Documentation (PRD, etc.)
├── .github/     # GitHub Actions workflows
├── PLANNING.md  # Vision, architecture, stack
├── TASKS.md     # Milestones and tasks
├── DEVELOPMENT.md # Dev environment setup
└── README.md    # This file
```

---

## Development

- **Linting and formatting:**
  - Python: `ruff check .` and `ruff format .` in `/server`
  - JS/TS: `npx prettier --check .` and `npx eslint .` in `/client`
- **Pre-commit hooks:**
  - Installed in `/server` to catch linting/formatting issues before commit
- **CI:**
  - Automated with GitHub Actions for both backend and frontend
- **AI Agents:**
  - See [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) for comprehensive AI agent guidelines

---



---

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md) — Full game and technical design
- [PLANNING.md](PLANNING.md) — Vision, architecture, stack
- [TASKS.md](TASKS.md) — Milestones and tasks
- [DEVELOPMENT.md](DEVELOPMENT.md) — Dev environment setup
- [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) — AI agent development guide

---

## License

[https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE](https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE)
