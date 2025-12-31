# GitHub Copilot Instructions for MythosMUD

Repository-specific instructions for GitHub Copilot to generate code aligned with MythosMUD standards.

---

## Project Overview

MythosMUD is a Cthulhu Mythos-themed MUD (Multi-User Dungeon) built with:

- **Backend**: Python, FastAPI, PostgreSQL
- **Frontend**: React, TypeScript
- **Architecture**: Client-server with WebSocket real-time communication
- **Testing**: pytest with 80%+ coverage requirement

---

## 🔒 Security & Privacy Requirements

### COPPA Compliance

- Never collect personal information from minors
- All data collection requires explicit parental consent
- Collect only data essential for game functionality
- All data encrypted and securely stored
- Easy data deletion for all users
- No behavioral tracking or profiling of minors

### Security Standards

- All secrets via environment variables only (never hardcode)
- Comprehensive server-side input validation
- Secure path validation for all file operations
- Per-user and per-endpoint rate limiting
- Comprehensive HTTP security headers
- Complete client-side XSS protection

---

## 🖥️ Server Management

### Critical Rules

- **ONE SERVER ONLY**: Never start multiple server instances
- Always run `./scripts/stop_server.ps1` before starting server
- Always use `./scripts/start_local.ps1` to start server
- Never use background mode for server operations
- Verify ports are free before starting (ports 54731 and 5173)

---

## 📊 Database Rules

### Placement Rules

- **Production databases**: `/data/players/` and `/data/npcs/` ONLY
- **Test databases**: `/server/tests/data/players/` and `/server/tests/data/npcs/` ONLY
- Never create database files in any other location
- Always verify database file location before creating or modifying files

### Type Rules

- `player_id` is a UUID datatype, not a string
- Use PostgreSQL (SQLite is deprecated)
- Prefer PostgreSQL CLI over Python for debugging
- Do not create *.db files without explicit permission

---

## 🧪 Testing Requirements

### Execution Rules

- **NEVER run tests from `/server/` directory**
- **NEVER use `python -m pytest` directly**
- **ONLY use `make test` and `make test-comprehensive` from project root**

### Test Quality

- Tests MUST test server code, not test infrastructure or Python built-ins
- Write tests to catch bugs before fixing them
- Maintain 80% minimum overall coverage (target 82%+)
- Critical code coverage: 98% minimum

### Test Organization

- Tests belong in: `server/tests/unit/`, `server/tests/integration/`, etc.
- Fixtures directory (`server/tests/fixtures/`) is for utilities ONLY

---

## 📝 Code Quality Standards

### Linting & Formatting

- Use ruff as the sole linter/formatter (no black/flake8)
- Enforce 120-character line length maximum
- All code must pass codacy, lint, and mypy reviews
- When suppressing tool findings, add a comment justifying why

### Code Organization

- If a file exceeds 500 lines, consider refactoring into multiple files
- Use "controller" or "coordinator" instead of "master"
- Use "agent" instead of "slave"
- Do not use unicode characters in Python files

---

## 🪵 Logging Standards

### Required Pattern

```python
# ✅ CORRECT - Always use enhanced logging
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# ✅ CORRECT - Structured logging with key-value pairs
logger.info("User action completed", user_id=user.id, action="login", success=True)

# ❌ WRONG - Never use standard logging
import logging
logger = logging.getLogger(__name__)

# ❌ WRONG - Never use f-string logging (destroys structured logging)
logger.info(f"User {user_id} performed {action}")

# ❌ WRONG - Never use deprecated context parameter
logger.info("message", context={"key": "value"})
```

### Logging Best Practices

- Use structured logging with key-value pairs: `logger.info("message", key=value)`
- Bind request context: `bind_request_context(correlation_id=id, user_id=uid)`
- Use performance monitoring: `with measure_performance("operation"):`
- Never use f-strings for log messages

---

## 🛠️ Development Practices

### Environment

- Use PowerShell syntax (never bash-style && for command chaining)
- Only kill tasks that are part of this project by name
- Never use taskkill on node.exe

### Task Prioritization

1. 🔴 Critical Security Issues (fix immediately)
2. 🟡 High Priority (complete within session)
3. 🟢 Medium Priority (plan for next session)
4. 🔵 Low Priority (nice to have)

### Development Workflow

1. Review GitHub Issues
2. Write tests first (TDD)
3. Implement feature
4. Run tests and ensure coverage
5. Update documentation
6. Commit with descriptive message

### Definition of Done

- Passing formatting checks
- Passing linting checks
- Passing tests with appropriate coverage
- All code quality standards met

---

## 📦 Dependency Management

- Use uv for Python dependency management (required)
- Use pyenv-win for Python version management on Windows
- Use NVM for Windows for Node.js and npm management
- Run pre-commit hooks with `pre-commit install -f`

---

## 🔄 Git Workflow

### Commit Messages

- Use concise, descriptive commit messages (50-72 chars for first line)
- Include bullet points for specific changes in body
- NEVER include verbose closing paragraphs like "These changes reflect our commitment..."
- Link commits to issues using `#issue-number`

### Branch Management

- Always verify current branch before git operations
- Never switch branches without explicit user permission
- Check branch with `git branch --show-current` at session start

---

## 🏗️ Architecture Guidelines

### Implementation Requirements

- When implementing a feature, implement the entire stack: client, server, and persistence
- Use TypeScript for client-side code
- Use FastAPI for backend API development
- Use Pydantic for data validation and serialization
- Implement thread-safe singleton pattern for persistence
- Use proper error handling with custom exceptions

### Code Comments

- Write comments for humans that explain concepts and business logic
- Include Mythos references in comments when appropriate (but keep code names conventional)
- When writing comments for humans, also include comments for agentic AI if different

---

## 🎭 Mythos Integration

- Reference canonical Lovecraft works and invented academic sources in comments
- Draw from the broader Cthulhu pantheon for flavor
- Treat development as serious academic work into forbidden territories
- Keep variable/function names conventionally readable (Mythos flavor in comments, not code)

---

## 📚 Code Patterns

### Common Patterns to Follow

```python
# Error handling pattern
try:
    result = await operation()
except SpecificError as e:
    logger.error("Operation failed", operation="operation_name", error=str(e))
    raise CustomError("User-friendly message") from e

# Async function pattern
async def handler(request: Request, current_user: User) -> dict:
    logger.info("Handler called", handler="handler_name", user_id=current_user.id)
    # Implementation
    return {"status": "success"}

# Database operation pattern
async def save_entity(entity: Entity) -> None:
    with measure_performance("database_save", entity_type=type(entity).__name__):
        await persistence.save(entity)
        logger.info("Entity saved", entity_id=entity.id, entity_type=type(entity).__name__)
```

---

## ❓ Communication Guidelines

- Ask questions one at a time
- Don't claim user is correct unless actually verified
- Stop and ask for help if terminal output problems detected

---

## 📚 Key Files & References

- Main rules: `.cursorrules`
- User rules: `USER_RULES.md`
- Task tracking: GitHub Issues
- Testing docs: `docs/TESTING.md`
- Development docs: `docs/DEVELOPMENT.md`

---

> May your code be as unfathomable yet functional as the depths themselves.
