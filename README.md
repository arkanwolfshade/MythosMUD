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
- [AI Agent Instructions](#ai-agent-instructions)
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
   pip install -r requirements.txt
   uvicorn main:app --reload
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

---

## AI Agent Instructions

Welcome, AI agents! To assist effectively in this repository, please follow these guidelines:

- **Context & Preparation:**
  - Always read `PLANNING.md`, `TASKS.md`, and `README.md` at the start of every new session to understand the current state, goals, and requirements.
  - The primary product requirements and design details are in [`docs/PRD.md`](docs/PRD.md).
  - Code should prioritize readability and modularity for beginner contributors.
  - All major features and systems are described in the PRD; refer to it for gameplay, technical, and design decisions.

- **Task Management:**
  - Check `TASKS.md` before starting any work.
  - Mark completed tasks in `TASKS.md` immediately after finishing them.
  - Add any newly discovered or follow-up tasks to `TASKS.md` as soon as they are found.

- **When generating code or documentation:**
  - Use clear, commented code.
  - Reference the PRD for feature requirements and terminology.
  - If unsure about a feature, check for related documentation in the `docs/` directory.

- **When updating documentation:**
  - Keep this `README.md` and `docs/PRD.md` in sync regarding major features and instructions.
  - Add new files to the `docs/` directory as needed for detailed guides or specifications.

- **For setup, deployment, or CI/CD:**
  - Follow the instructions in [DEVELOPMENT.md](DEVELOPMENT.md).
  - Use cost-effective, beginner-friendly solutions where possible.

- **Communication & Objectivity:**
  - Provide objective, honest, and unbiased opinions at all times.
  - It is acceptable to say "I don't know." If you do not know the answer, say so clearly—do not make up answers.
  - Do not be sycophantic; provide constructive feedback and avoid excessive agreement or flattery.

---

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md) — Full game and technical design
- [PLANNING.md](PLANNING.md) — Vision, architecture, stack
- [TASKS.md](TASKS.md) — Milestones and tasks
- [DEVELOPMENT.md](DEVELOPMENT.md) — Dev environment setup

---

## License

[https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE](https://github.com/arkanwolfshade/MythosMUD/blob/main/LICENSE)
