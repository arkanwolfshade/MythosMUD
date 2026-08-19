# MythosMUD Development Environment Setup

**Version 1.1.0** · MythosMUD · 2026-08-03

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified -- treat with lower confidence.

---

## 1. Overview

**[NOTE]**

_"The proper setup of one's laboratory is as crucial to the pursuit of forbidden knowledge as the knowledge itself. Let
us ensure our tools are both powerful and safe."_

This guide will help you bootstrap your workspace for developing MythosMUD, with particular emphasis on security,
privacy, and COPPA compliance.

For contributor workflow and pull requests, see [CONTRIBUTING.md](../CONTRIBUTING.md). Agent-oriented rules live in
[AGENTS.md](../AGENTS.md) and [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md).

---

## 2. Security & Privacy First

**[SPEC]**

### Critical Requirements

**COPPA Compliance**: This project serves minors and must comply with Children's Online Privacy Protection Rule

**Security-First Mindset**: All development decisions prioritize security over convenience

**Privacy by Design**: Privacy considerations built into every feature

**Minimal Data Collection**: Only collect data absolutely necessary for gameplay

**No Personal Information**: Never collect personal information from minors

### Development Security Checklist

- [ ] All secrets stored in environment variables (never hardcoded)
- [ ] Input validation implemented for all user inputs
- [ ] Secure path validation for all file operations
- [ ] Rate limiting configured for all endpoints
- [ ] Security headers properly configured
- [ ] XSS protection implemented
- [ ] COPPA compliance verified for all features
- [ ] SQLAlchemy async patterns follow best practices (see `SQLALCHEMY_ASYNC_BEST_PRACTICES.md`)
- [ ] Enhanced logging system used correctly (see `LOGGING_BEST_PRACTICES.md`)

---

## 3. Prerequisites

**[SPEC]**

- **Git**
- **Python 3.12+** (managed via [pyenv-win](https://github.com/pyenv-win/pyenv-win) recommended)
- **Node.js 22+** and **npm** (NVM for Windows recommended)
- **PostgreSQL 15+** (**required** for local development and tests)
- **[uv](https://github.com/astral-sh/uv)** (for Python dependency management - **required**)
- **NATS Server** binary (set `NATS_SERVER_PATH` in `.env.local`)
- **VSCode** or Cursor (recommended editor)
- **React Developer Tools** (Firefox/Chrome extension for debugging React components)

---

## 4. Install uv

**[NOTE]**

### On macOS/Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### On Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify installation

```sh
uv --version
```

---

## 5. Clone the Repository

**[NOTE]**

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

**Note:** The `data/` directory is a git submodule containing world data. Make sure to fetch it using one of the methods
above.

---

## 6. Set Up the Python Server

**[NOTE]**

### a. Set Python Version (if using pyenv-win)

```sh
pyenv install 3.12.11  # if not already installed
pyenv local 3.12.11
```

### b. Install Dependencies

```sh
cd server
uv sync
```

### c. Set Up Pre-commit Hooks

```sh
uv run pre-commit install -f
```

Semgrep is included in the pre-commit hooks when configured. Prefer `pre-commit` / project lint Make
targets rather than inventing a `make semgrep` entry.

### d. Configure Environment Variables

From the **repository root**, copy the local template (not `.env.local.example`):

```powershell
Copy-Item env.local.example .env.local
Copy-Item env.unit_test.example .env.unit_test
.\scripts\setup_test_environment.ps1
```

Edit `.env.local` and set at least:

- `DATABASE_URL` (PostgreSQL connection to `mythos_dev`)
- `NATS_SERVER_PATH`
- secrets (`SECRET_KEY`, JWT keys, etc. as listed in the template)

**Security Note**: Never commit `.env.local` or other local env files. Templates are `env.*.example` in the repo root.

Ensure PostgreSQL is running. Create `mythos_dev` and apply environment DDL (uses
`DATABASE_URL` from `.env.local`), then apply procedures:

```powershell
.\scripts\setup_postgresql_test_db.ps1 -EnvFile .env.local
make apply-procedures
```

DDL source: `db/mythos_dev_ddl.sql`. See
[POSTGRESQL_CONTRIBUTOR_GUIDE.md](POSTGRESQL_CONTRIBUTOR_GUIDE.md).

### e. Run the Server

**CRITICAL**: Always use the provided scripts for server management (one server only):

```powershell
# Stop any running MythosMUD server first

.\scripts\stop_server.ps1

# Start API + Vite client (or use start_server.ps1 alone)

.\scripts\start_local.ps1
```

The API should now be running at [http://localhost:54768](http://localhost:54768)

OpenAPI docs: [http://localhost:54768/docs](http://localhost:54768/docs)

---

## 7. Set Up the React Client

**[NOTE]**

### a. Install Dependencies

```sh
cd ../client
npm install
```

### b. Start the Development Server

If you used `start_local.ps1`, the client is already started. Otherwise:

```powershell
.\scripts\start_client.ps1
```

Or from `client/`:

```sh
npm run dev
```

The client should now be running at [http://localhost:5173](http://localhost:5173)

(Vite; not `npm start` on port 3000.)

---

## 8. Development Scripts

**[NOTE]**

Prefer **Makefile** targets from the repository root for day-to-day work. Some older `python scripts/*.py` helpers still
exist for install/run/lint/format; there is no `scripts/test.py` -- use `make test` instead.

### Preferred Make targets

```powershell
make test              # Client unit + server (excludes integration marker)
make test-coverage     # Coverage reports
make test-ci           # CI-style suite (alias: make test-comprehensive)
make test-client-e2e   # Playwright E2E (alias: make test-e2e)
make test-playwright   # Client E2E + server integration helpers
make lint
make format
```

See [TESTING.md](TESTING.md).

### Install / run helpers (optional)

```sh
python scripts/install.py
python scripts/run.py
python scripts/lint.py
python scripts/format.py
```

### Enhanced Logging

MythosMUD uses an enhanced logging system with MDC, correlation IDs, and security sanitization.

### Quick Start

```python
# CORRECT - Enhanced logging import

from server.structured_logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# CORRECT - Structured logging

logger.info("User action completed", user_id=user.id, action="login", success=True)
```

### NEVER USE

```python
# FORBIDDEN - Will cause failures

import logging
logger = logging.getLogger(__name__)

# FORBIDDEN - Deprecated context parameter

logger.info("message", context={"key": "value"})
```

See [LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md) for complete guidelines and
[LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md) for quick reference.

### Multi-Character Support

MythosMUD supports multiple characters per user (up to 3 active characters).

### Registration and Login Flow

1. User registers -- Account created with no characters
2. User logs in -- If no characters, shown character creation flow; if characters exist, shown character selection screen
3. User selects character -- Game connects with selected character

### Character Management

Character names are case-insensitive unique (e.g., "Ithaqua" and "ithaqua" are mutually exclusive)

- Character names are stored with original case but checked case-insensitively
- Deleted character names can be reused (uniqueness only applies to active characters)
- Maximum 3 active characters per user
- Characters are soft-deleted (hidden but data preserved)

**Single Character Login**: Users can only be logged into the game with one character at a time. Selecting a different
character will automatically disconnect any existing connections for other characters owned by that user.

### Code Examples

```python
# Get all active characters for a user

characters = await persistence.get_active_players_by_user_id(str(user.id))

success, message = await player_service.soft_delete_character(character_id, user.id)
```

See the multi-character implementation plan for complete details.

---

## 9. Manual Commands

**[NOTE]**

### Python Development

```sh
cd server

# Install dependencies

uv sync

# Prefer scripts for a full stack run: ..\scripts\start_local.ps1
# If you must invoke uvicorn directly (advanced):

uv run uvicorn server.main:app --host 0.0.0.0 --port 54768

# Prefer Make from repo root for tests: make test
# Ad-hoc pytest from server/ (know what you are doing):

uv run pytest tests/ -v

# Lint code

uv run ruff check .

# Format code

uv run ruff format .

# Add new dependency

uv add package-name

# Add development dependency

uv add --dev package-name
```

### Client Development

```sh
cd client

# Install dependencies

npm install

# Start development server (Vite)

npm run dev

# Run unit tests

npm test

# Build for production

npm run build
```

---

## 10. AI Agent Guidelines (pointer)

**[NOTE]**

This file is for **human** lab setup. Do not duplicate agent policy here.

- Hard rules (server, DB, tests, COPPA): [AGENTS.md](../AGENTS.md)
- Agent workflow, patterns, pitfalls: [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md)

---

## 11. Why uv?

**[SPEC]**

**Faster**: 10-100x faster than pip/poetry

**Reliable**: Deterministic dependency resolution

**Modern**: Built-in virtual environment management

**Compatible**: Works with existing pyproject.toml

**Simple**: Single tool for all Python operations

---

## 12. Troubleshooting

**[NOTE]**

### uv not found

```sh
# Reinstall uv following the installation instructions above
# Make sure to restart your terminal after installation
```

### Python version issues

```sh
# Ensure you have Python 3.12+ installed

python --version

# If using pyenv, set the local version

pyenv local 3.12.11
```

### Dependency conflicts

```sh
# Clean and reinstall

cd server
uv sync --reinstall
```

### Missing or wrong env file

```powershell
# Template is env.local.example (not .env.local.example)

Copy-Item env.local.example .env.local
```

`start_server.ps1` will refuse to start without `.env.local`.

### Client-Server Connection Issues

```sh
# Check if server is running on correct port

curl http://localhost:54768/game/status

# Verify Vite proxy configuration in client/vite.config.ts
# Ensure target ports match server configuration

# Use React Developer Tools to debug component state
# - Install React Developer Tools extension in Firefox/Chrome
# - Check component props, state, and network requests
# - Monitor authentication state and API calls
```

### React Component Debugging

**React Developer Tools**: Use the Firefox/Chrome extension to inspect component state

**Network Tab**: Check API requests and responses in browser dev tools

**Console**: Monitor authentication flow and error messages

**Component State**: Verify `isAuthenticated`, `playerId`, and `authToken` values

### Security Issues

**Environment Variables**: Ensure all secrets are properly configured

**Database Security**: Verify database placement rules (PostgreSQL; see AGENTS.md / CONTRIBUTING)

**Input Validation**: Check that all user inputs are properly validated

**COPPA Compliance**: Verify no personal data is collected from minors

---

## 13. Next Steps

**[SPEC]**

- Read [PLANNING.md](../PLANNING.md) for project architecture and priorities
- Check [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) for current development priorities
- Review security requirements and COPPA compliance guidelines
- Contributors: [CONTRIBUTING.md](../CONTRIBUTING.md)
- Agents: [DEVELOPMENT_AI.md](DEVELOPMENT_AI.md) and [AGENTS.md](../AGENTS.md)

---

## 14. Security Checklist

**[SPEC]**

Before starting development, ensure:

- [ ] Environment variables properly configured (`.env.local` from `env.local.example`)
- [ ] PostgreSQL reachable; procedures applied (`make apply-procedures`)
- [ ] Input validation implemented
- [ ] Rate limiting configured
- [ ] Security headers set
- [ ] COPPA compliance verified
- [ ] No hardcoded secrets
- [ ] Secure path validation implemented
- [ ] XSS protection enabled
- [ ] Privacy by design principles followed

---

_"In the pursuit of forbidden knowledge, even the most advanced artificial intelligences must remember: the greatest
wisdom lies not in what we know, but in how we apply that knowledge with care, precision, and respect for the eldritch
forces we seek to understand."_

---

## 15. Changelog

**[SPEC]**

| Version | Date       | Change                                                                        |
| ------- | ---------- | ----------------------------------------------------------------------------- |
| 1.1.0   | 2026-08-03 | Fact-fix PostgreSQL/env/ports/Make; move agent rules to pointer; fix encoding |
| 1.0.0   | 2026-07-30 | Initial HADS structural conversion                                            |
