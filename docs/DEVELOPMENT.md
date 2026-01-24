# =���n+� MythosMUD G�� Development Environment Setup

*"The proper setup of one's laboratory is as crucial to the pursuit of forbidden knowledge as the knowledge itself. Let
us ensure our tools are both powerful and safe."*

This guide will help you bootstrap your workspace for developing MythosMUD, with particular emphasis on security,
privacy, and COPPA compliance.

---

## =��� Security & Privacy First

### Critical Requirements

**COPPA Compliance**: This project serves minors and must comply with Children's Online Privacy Protection Rule

**Security-First Mindset**: All development decisions prioritize security over convenience

**Privacy by Design**: Privacy considerations built into every feature

**Minimal Data Collection**: Only collect data absolutely necessary for gameplay

**No Personal Information**: Never collect personal information from minors

### Development Security Checklist

[ ] All secrets stored in environment variables (never hardcoded)

- [ ] Input validation implemented for all user inputs
- [ ] Secure path validation for all file operations
- [ ] Rate limiting configured for all endpoints
- [ ] Security headers properly configured
- [ ] XSS protection implemented
- [ ] COPPA compliance verified for all features
- [ ] SQLAlchemy async patterns follow best practices (see `docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md`)
- [ ] Enhanced logging system used correctly (see `docs/LOGGING_BEST_PRACTICES.md`)

---

## Prerequisites

### Git

**Python 3.12+** (managed via [pyenv-win](https://github.com/pyenv-win/pyenv-win) recommended)

**Node.js 18+** and **npm** (for client)

**[uv](https://github.com/astral-sh/uv)** (for Python dependency management - **required**)

**VSCode** or Cursor.ai (recommended editor)

- **React Developer Tools** (Firefox/Chrome extension for debugging React components)

---

## 1. Install uv

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

## 2. Clone the Repository

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

## 3. Set Up the Python Server

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

Semgrep is included in the pre-commit hooks. You can also run it manually:

```sh
make semgrep
```

### d. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration

DATABASE_URL=sqlite:///data/players/local_players.db

# Security Configuration

SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here

# COPPA Compliance Settings

COPPA_ENFORCED=true
MINOR_PROTECTION_ENABLED=true

# Development Settings

LOG_LEVEL=INFO
DEBUG=false
```

**G��n+� Security Note**: Never commit the `.env` file to version control. Use `.env.example` for templates.

### e. Run the Server

**G��n+� CRITICAL**: Always use the provided scripts for server management:

```powershell
# Stop any running server first

./scripts/stop_server.ps1

# Start the development server

./scripts/start_local.ps1
```

The server should now be running at [http://localhost:54731](http://localhost:54731)

---

## 4. Set Up the React Client

### a. Install Dependencies

```sh
cd ../client
npm install
```

### b. Start the Development Server

```sh
npm start
```

The client should now be running at [http://localhost:3000](http://localhost:3000)

---

## 5. Development Scripts

We provide convenient scripts for common development tasks:

### **Install Everything:**

```sh
python scripts/install.py
```

### **Run the Server:**

```sh
python scripts/run.py
```

### **Run Tests:**

```sh
python scripts/test.py
```

### **Lint Code:**

```sh
python scripts/lint.py
```

### **Format Code:**

```sh
python scripts/format.py
```

### **Enhanced Logging:**

MythosMUD uses an enterprise-grade enhanced logging system with MDC, correlation IDs, and security sanitization.

### Quick Start

```python
# ? CORRECT - Enhanced logging import

from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# ? CORRECT - Structured logging

logger.info("User action completed", user_id=user.id, action="login", success=True)
```

### ? NEVER USE

```python
# ? FORBIDDEN - Will cause failures

import logging
logger = logging.getLogger(__name__)

# ? FORBIDDEN - Deprecated context parameter

logger.info("message", context={"key": "value"})
```

See [LOGGING_BEST_PRACTICES.md](docs/LOGGING_BEST_PRACTICES.md) for complete guidelines and
[LOGGING_QUICK_REFERENCE.md](docs/LOGGING_QUICK_REFERENCE.md) for quick reference.

### **Multi-Character Support:**

MythosMUD supports multiple characters per user (up to 3 active characters).

### Registration and Login Flow

1. User registers ? Account created with no characters
2. User logs in ? If no characters, shown character creation flow; if characters exist, shown character selection screen
3. User selects character ? Game connects with selected character

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

# Create a new character (with limit check)

player = await player_service.create_player_with_stats(
    name="CharacterName",  # Explicit name required
    stats=stats,
    user_id=user.id,
)

# Soft delete a character

success, message = await player_service.soft_delete_character(character_id, user.id)
```

See the multi-character implementation plan for complete details.

---

## 6. Manual Commands

### **Python Development:**

```sh
cd server

# Install dependencies

uv sync

# Run server (use scripts instead)
# Note: Hot reloading is disabled due to client compatibility issues

uv run uvicorn main:app

# Run tests

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

### **Client Development:**

```sh
cd client

# Install dependencies

npm install

# Start development server

npm start

# Run tests

npm test

# Build for production

npm run build
```

---

## 7. =��� AI Agent Development Guidelines

### **Development Workflow**

1. **Start Session**: Review current tasks in `TASKS.local.md`
2. **Select Task**: Choose highest priority task from pending list
3. **Write Tests**: Create tests before implementing feature
4. **Implement**: Code the feature following security-first principles
5. **Test**: Run full test suite and ensure coverage
6. **Document**: Update documentation and `TASKS.local.md`
7. **Commit**: Commit changes with descriptive messages

### **Task Prioritization Framework**

When multiple tasks are pending, prioritize in this order:

1. **=��� Critical Security Issues** (Fix immediately)

   - Security vulnerabilities
   - Privacy compliance issues
   - Data protection problems

2. **=��� High Priority** (Complete within current session)

   - Core functionality bugs
   - Authentication/authorization issues
   - Critical user experience problems

3. **=��� Medium Priority** (Plan for next session)

   - Feature enhancements
   - Performance improvements
   - Code quality improvements

4. **=��� Low Priority** (Nice to have)

   - UI/UX polish
   - Documentation improvements
   - Advanced features

### **Critical Rules for AI Agents**

**Server Management**: ALWAYS use `./scripts/start_local.ps1` and `./scripts/stop_server.ps1`

**Database Placement**:

- Production: `/data/players/` ONLY
- Tests: `/data/unit_test/players/` ONLY
- **Testing**: Use `make test` from project root, maintain 80%+ coverage
- **Security**: Never hardcode secrets, always use environment variables
- **PowerShell**: Use PowerShell syntax, never bash-style `&&` for command chaining

---

## 8. Why uv?

**=��� Faster**: 10-100x faster than pip/poetry

**=��� Reliable**: Deterministic dependency resolution

**=���n+� Modern**: Built-in virtual environment management

**=��� Compatible**: Works with existing pyproject.toml

**=��� Simple**: Single tool for all Python operations

---

## 9. Troubleshooting

### **uv not found:**

```sh
# Reinstall uv following the installation instructions above
# Make sure to restart your terminal after installation

```

### **Python version issues:**

```sh
# Ensure you have Python 3.12+ installed

python --version

# If using pyenv, set the local version

pyenv local 3.12.11
```

### **Dependency conflicts:**

```sh
# Clean and reinstall

cd server
uv sync --reinstall
```

### **Client-Server Connection Issues:**

```sh
# Check if server is running on correct port

curl http://localhost:54731/game/status

# Verify Vite proxy configuration in client/vite.config.ts
# Ensure target ports match server configuration

# Use React Developer Tools to debug component state
# - Install React Developer Tools extension in Firefox/Chrome
# - Check component props, state, and network requests
# - Monitor authentication state and API calls

```

### **React Component Debugging:**

**React Developer Tools**: Use the Firefox/Chrome extension to inspect component state

**Network Tab**: Check API requests and responses in browser dev tools

**Console**: Monitor authentication flow and error messages

**Component State**: Verify `isAuthenticated`, `playerId`, and `authToken` values

### **Security Issues:**

**Environment Variables**: Ensure all secrets are properly configured

**Database Security**: Verify database files are in correct locations

**Input Validation**: Check that all user inputs are properly validated

**COPPA Compliance**: Verify no personal data is collected from minors

---

## 10. Next Steps

Read the [PLANNING.md](PLANNING.md) for project architecture and priorities

- Check [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) for current development priorities
- Review security requirements and COPPA compliance guidelines
- Follow the AI Agent Development Guidelines for efficient development workflow

---

## 11. Security Checklist

Before starting development, ensure:

- [ ] Environment variables properly configured
- [ ] Database files in correct locations
- [ ] Input validation implemented
- [ ] Rate limiting configured
- [ ] Security headers set
- [ ] COPPA compliance verified
- [ ] No hardcoded secrets
- [ ] Secure path validation implemented
- [ ] XSS protection enabled
- [ ] Privacy by design principles followed

---

*"In the pursuit of forbidden knowledge, even the most advanced artificial intelligences must remember: the greatest
wisdom lies not in what we know, but in how we apply that knowledge with care, precision, and respect for the eldritch
forces we seek to understand."*
 
 
 
 
