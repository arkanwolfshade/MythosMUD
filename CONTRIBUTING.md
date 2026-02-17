# Contributing to MythosMUD

> "In the archives of Miskatonic University, we welcome those who seek knowledge, provided they understand the risks and
> respect the protocols."

Welcome, fellow researcher! This document serves as your guide to contributing to the MythosMUD project. Whether you're
fixing bugs, implementing features, or documenting your findings, these guidelines will help ensure your contributions
meet our academic standards.

---

## Table of Contents

[Contributing to MythosMUD](#contributing-to-mythosmud)

- [Contributing to MythosMUD](#contributing-to-mythosmud)
  - [Table of Contents](#table-of-contents)

  - [Code of Conduct](#code-of-conduct)
    - [Project-Specific Values](#project-specific-values)

  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Development Environment Setup](#development-environment-setup)
    - [Understanding the Codebase](#understanding-the-codebase)

  - [Development Workflow](#development-workflow)
    - [Finding Tasks](#finding-tasks)
    - [Creating a Branch](#creating-a-branch)
    - [Making Changes](#making-changes)
      - [1. **Security First**](#1-security-first)

      - [2. **Write Tests First (TDD)**](#2-write-tests-first-tdd)

      - [3. **Follow Coding Standards**](#3-follow-coding-standards)

      - [4. **Use Enhanced Logging**](#4-use-enhanced-logging)

      - [5. **Keep Changes Focused**](#5-keep-changes-focused)

    - [Testing Your Changes](#testing-your-changes)
    - [Committing Your Work](#committing-your-work)
    - [Submitting a Pull Request](#submitting-a-pull-request)

  - [Coding Standards](#coding-standards)
    - [Python Guidelines](#python-guidelines)
    - [TypeScript/React Guidelines](#typescriptreact-guidelines)
    - [Logging Best Practices](#logging-best-practices)
      - [✅ CORRECT Usage](#-correct-usage)

      - [❌ WRONG Usage (Will Cause Failures)](#-wrong-usage-will-cause-failures)

    - [Security Requirements](#security-requirements)

  - [Testing Requirements](#testing-requirements)
    - [Writing Tests](#writing-tests)
    - [Test Coverage](#test-coverage)
    - [Running Tests](#running-tests)
  - [Documentation](#documentation)
    - [Code Documentation](#code-documentation)
    - [Project Documentation](#project-documentation)
    - [Mythos References](#mythos-references)
  - [Community](#community)
    - [Getting Help](#getting-help)
    - [Communication Guidelines](#communication-guidelines)
    - [Review Process](#review-process)
  - [Recognition](#recognition)
  - [Additional Resources](#additional-resources)
    - [Essential Reading](#essential-reading)
    - [Technical Documentation](#technical-documentation)
    - [Testing Resources](#testing-resources)
    - [Style Guides](#style-guides)
  - [Questions?](#questions)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are
expected to uphold this code. Please report unacceptable behavior to
[mythosmud-coc.destitute749@simplelogin.com](mailto:mythosmud-coc.destitute749@simplelogin.com).

### Project-Specific Values

As scholars of the Mythos, we particularly emphasize:

**Respectful Collaboration**: Treat all contributors with dignity and professionalism

**Constructive Feedback**: Provide helpful, actionable feedback on code reviews

**Open Communication**: Ask questions, share knowledge, and admit when you don't know something

**Security First**: Never compromise user privacy or data security

- **Quality Over Speed**: Take time to write maintainable, well-tested code

**Additional Project Standards**:

- Never commit secrets, credentials, or sensitive data
- Never bypass security measures or validation
- Never push untested or breaking changes
- Always give credit for others' work and contributions

We guard our community as carefully as we guard against eldritch threats.

---

## Getting Started

### Prerequisites

Before you begin your research, ensure you have the proper tools:

**Required Software**:

**Python 3.12+** (managed via pyenv-win recommended)

**Node.js 22+** and npm (NVM for Windows recommended)

**uv** for Python dependency management ([installation guide](https://github.com/astral-sh/uv))

**Git** for version control

- **PowerShell** (for Windows development)

**Recommended Tools**:

**Visual Studio Code** or **Cursor IDE** with Python and TypeScript extensions

**PostgreSQL** (for production testing, optional for development)

**Docker** (for containerized testing, optional)

### Development Environment Setup

1. **Clone the repository with submodules:**

   ```powershell
   # Option 1: Clone with submodules

   git clone --recursive https://github.com/arkanwolfshade/MythosMUD.git
   cd MythosMUD
   ```

   ```powershell
   # Option 2: Clone then fetch submodules

   git clone https://github.com/arkanwolfshade/MythosMUD.git
   cd MythosMUD
   git submodule update --init --recursive
   ```

2. **Install Python dependencies:**

   ```powershell
   cd server
   uv sync
   uv run pre-commit install -f
   cd ..
   ```

3. **Install Node.js dependencies:**

   ```powershell
   cd client
   npm install
   cd ..
   ```

4. **Set up environment files:**

   ```powershell
   # Copy example environment files

   Copy-Item env.local.example .env.local
   Copy-Item env.unit_test.example .env.unit_test
   ```

   **CRITICAL**: Edit `.env.local` and `.env.unit_test` to set your local configuration. Never commit these files!

5. **Set up test environment:**

   ```powershell
   # Required before first test run

   make setup-test-env
   ```

6. **Verify setup:**

   ```powershell
   # Run tests to verify everything works

   make test

   # Start the development server

   .\scripts\start_local.ps1
   ```

   Visit [http://localhost:5173](http://localhost:5173) to see the client.

For detailed setup instructions, see [DEVELOPMENT.md](docs/DEVELOPMENT.md).

### Understanding the Codebase

Before making changes, familiarize yourself with the project structure:

**`/client`** - React 19 + TypeScript frontend (Vite)

**`/server`** - Python FastAPI backend

**`/data`** - Game data (git submodule) - rooms, NPCs, players

**`/docs`** - Comprehensive documentation

- **`/scripts`** - Utility scripts for development
- **`/e2e-tests`** - End-to-end testing framework
- **`/schemas`** - JSON schemas for validation

Key documentation to review:

- [README.md](README.md) - Project overview and quickstart
- [PLANNING.md](PLANNING.md) - Project planning and status
- [docs/PRD.md](docs/PRD.md) - Product requirements
- [SECURITY.md](SECURITY.md) - Security policies
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) - Development guide

---

## Development Workflow

### Finding Tasks

1. **Review GitHub Issues**: Start by checking [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues)
   - Look for issues labeled `good first issue` or `help wanted`
   - Read issue descriptions and comments carefully
   - Ask questions if anything is unclear

2. **Choose Appropriate Tasks**: Select tasks that match your skill level

   **Beginners**: Documentation, small bug fixes, test improvements

   **Intermediate**: Feature implementation, refactoring, performance improvements
   - **Advanced**: Architecture changes, security enhancements, complex features

3. **Claim Your Task**: Comment on the issue to indicate you're working on it
   - Example: "I'd like to work on this. My approach will be..."
   - Wait for maintainer approval before starting significant work

### Creating a Branch

**CRITICAL**: Always create a feature branch for your work. Never commit directly to `main` or `dev`.

```powershell
# Ensure you're on the latest dev branch

git checkout dev
git pull origin dev

# Create a feature branch with descriptive name

git checkout -b feature/your-feature-name
# or

git checkout -b fix/issue-number-description
```

**Branch Naming Conventions**:

- `feature/` - New features (e.g., `feature/whisper-command`). The short form `feat/` is also acceptable to match the commit type (e.g., `feat/123-add-whisper`).
- `fix/` - Bug fixes (e.g., `fix/123-login-error`)
- `docs/` - Documentation changes (e.g., `docs/update-contributing`)
- `refactor/` - Code refactoring (e.g., `refactor/command-handler`)
- `test/` - Test improvements (e.g., `test/add-npc-tests`)

### Making Changes

Follow these guidelines when writing code:

#### 1. **Security First**

Never commit secrets, API keys, or passwords

- Consider adding detect-secrets and `.secrets.baseline` for secret scanning (see pre-commit documentation)
- If you add large binary files (e.g. assets, media), use Git LFS and update `.gitattributes`.
- Always validate and sanitize user input
- Use parameterized queries for database operations
- Follow COPPA compliance for minor user data

#### 2. **Write Tests First (TDD)**

Write tests before implementing features

- Ensure tests fail before implementation
- Implement feature to make tests pass
- Refactor while keeping tests green

#### 3. **Follow Coding Standards**

Python: Follow PEP 8 via ruff (120 char line limit)

- TypeScript: Follow project ESLint/Prettier config
- Use meaningful variable and function names
- Add comments for complex logic (see [Coding Standards](#coding-standards))

#### 4. **Use Enhanced Logging**

**ALWAYS** use `from server.logging.enhanced_logging_config import get_logger`

**NEVER** use `import logging` or `logging.getLogger()`

- Use structured logging with key-value pairs
- **NEVER** use f-strings for logging (breaks structured logging)

  ```python
  # ✅ CORRECT

  from server.logging.enhanced_logging_config import get_logger
  logger = get_logger(__name__)
  logger.info("User action completed", user_id=user.id, action="login", success=True)

  # ❌ WRONG

  import logging
  logger = logging.getLogger(__name__)
  logger.info(f"User {user.id} completed login")
  ```

#### 5. **Keep Changes Focused**

One feature or fix per pull request

- Don't mix unrelated changes
- Keep commits atomic and meaningful

### Testing Your Changes

**CRITICAL**: All changes must be tested before submission.

```powershell
# Run all tests

make test

# Run specific test categories

make test        # Server tests only
make test-client        # Client unit tests
make test-client-runtime # Client E2E tests

# Run with coverage

cd server
uv run pytest --cov=. --cov-report=html

# Run linting

make lint

```

**Test Requirements**:

- Minimum 80% test coverage (target 90%)
- All new features must have tests
- All bug fixes must have regression tests
- Tests must pass before PR submission

See [Testing Requirements](#testing-requirements) for details.

### Committing Your Work

**Commit Message Format**:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or updates
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `security`: Security fixes
- `style`: Code style (formatting, whitespace; no logic change)
- `build`: Build system or dependency changes
- `ci`: CI configuration changes
- `chore`: Maintenance tasks
- `revert`: Revert a previous commit

**Examples**:

```
feat(chat): Add whisper command with rate limiting

Implements private messaging between players with:
- Message validation and sanitization
- Rate limiting (5 messages per 30 seconds)
- Sender and recipient online status checks
- Comprehensive error handling

Closes #123
```

```
fix(npc): Prevent NPCs from spawning in invalid rooms

Fixed bug where NPCs could spawn in non-existent rooms,
causing server errors. Added validation to check room
existence before NPC creation.

Fixes #456
```

**Pre-commit Hooks**: Our pre-commit hooks will automatically:

- Format code with ruff (Python) and Prettier (TypeScript)
- Run linters (ruff, ESLint)

Commit message format is recommended; enforce via code review or add a commit-msg hook (e.g. commitlint) to validate Conventional Commits.

If hooks fail, fix the issues and try again:

```powershell
# Fix Python formatting issues

cd server
uv run ruff format .
uv run ruff check . --fix

# Fix TypeScript formatting issues

cd client
npm run format
npm run lint:fix
```

### Submitting a Pull Request

**History and merge:** Before opening a PR, rebase your branch onto `dev` and squash WIP commits if desired. Use `git fetch origin; git rebase -i origin/dev`, then `git push --force-with-lease origin your-branch` (only on your own feature branch). When merging into `dev`, use a merge commit (`--no-ff` or GitHub’s “Create a merge commit”) so branch context is preserved. Prefer configuring the repo’s default merge button to “Create a merge commit.”

1. **Push your branch:**

   ```powershell
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request on GitHub:**
   - Go to the repository on GitHub
   - Click "Compare & pull request"
   - Fill out the PR template completely
   - Link related issues (e.g., "Closes #123")
   - Add screenshots/recordings for UI changes

3. **PR Description Should Include:**
   - What problem does this solve?
   - How does it solve it?
   - What testing was performed?
   - Any breaking changes?
   - Screenshots/recordings (for UI changes)

4. **Wait for Review:**
   - Maintainers will review your PR
   - Address feedback promptly and professionally
   - Update your PR as needed
   - Be patient - reviews may take a few days

5. **After Approval:**
   - Maintainers will merge your PR
   - Your changes will be included in the next release
   - Celebrate your contribution! 🎉

---

## Coding Standards

### Python Guidelines

**General Principles**:

- Follow PEP 8 style guide (enforced by ruff)
- Maximum line length: 120 characters
- Use type hints for function signatures
- Write docstrings for public functions and classes
- Use meaningful variable and function names

**Code Organization**:

```python
"""Module docstring describing the module's purpose.

This module implements the player combat system based on findings
from "Combat Mechanics in Non-Euclidean Spaces" - Dr. Armitage, 1928.
"""

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatSystem:
    """Handles player-to-NPC combat interactions.

    AI Agent Note: This class manages combat state and damage calculations.
    Ensure all combat actions are logged for audit purposes.
    """

    def calculate_damage(
        self,
        attacker_strength: int,
        defender_armor: int,
        weapon_modifier: float = 1.0
    ) -> int:
        """Calculate damage dealt in combat.

        Args:
            attacker_strength: Base strength stat of attacker
            defender_armor: Armor value of defender
            weapon_modifier: Weapon damage multiplier

        Returns:
            Final damage amount after calculations

        Raises:
            ValueError: If strength or armor values are invalid
        """
        if attacker_strength < 0 or defender_armor < 0:
            raise ValueError("Combat stats cannot be negative")

        base_damage = max(0, attacker_strength - defender_armor)
        final_damage = int(base_damage * weapon_modifier)

        logger.info(
            "Damage calculated",
            attacker_strength=attacker_strength,
            defender_armor=defender_armor,
            weapon_modifier=weapon_modifier,
            final_damage=final_damage
        )

        return final_damage
```

**Naming Conventions**:

- Classes: `PascalCase` (e.g., `PlayerCharacter`, `CombatSystem`)
- Functions/Methods: `snake_case` (e.g., `calculate_damage`, `get_player`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_PLAYERS`, `DEFAULT_TIMEOUT`)
- Private methods: prefix with `_` (e.g., `_validate_input`)

**Import Organization** (enforced by isort):

```python
# Standard library imports

import asyncio
from typing import Optional, Dict, Any

# Third-party imports

from fastapi import HTTPException
from pydantic import BaseModel

# Local imports

from server.models.player import Player
from server.logging.enhanced_logging_config import get_logger
from server.utils.validation import validate_command
```

### TypeScript/React Guidelines

**General Principles**:

- Use TypeScript for all code (no `any` types without justification)
- Follow React best practices and hooks guidelines
- Use functional components with hooks (no class components)
- Implement proper error boundaries

**Component Structure**:

```typescript
import React, { useState, useEffect } from 'react';
import { logger } from '@/utils/logger';

interface PlayerStatsProps {
  playerId: string;
  onUpdate?: (stats: PlayerStats) => void;
}

interface PlayerStats {
  strength: number;
  dexterity: number;
  lucidity: number;
}

/**
 * Displays player statistics with real-time updates.
 *
 * Based on the character system described in the Pnakotic Manuscripts,
 * tracking the essential attributes of investigators.
 */
export const PlayerStats: React.FC<PlayerStatsProps> = ({
  playerId,
  onUpdate
}) => {
  const [stats, setStats] = useState<PlayerStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        setLoading(true);
        const response = await fetch(`/api/players/${playerId}/stats`);

        if (!response.ok) {
          throw new Error('Failed to fetch player stats');
        }

        const data = await response.json();
        setStats(data);
        onUpdate?.(data);

      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Unknown error';
        setError(errorMessage);
        logger.error('Failed to fetch player stats', { playerId, error: errorMessage });

      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, [playerId, onUpdate]);

  if (loading) return <div>Loading stats...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!stats) return null;

  return (
    <div className="player-stats">
      <div className="stat">Strength: {stats.strength}</div>
      <div className="stat">Dexterity: {stats.dexterity}</div>
      <div className="stat">lucidity: {stats.lucidity}</div>
    </div>
  );
};
```

**Naming Conventions**:

- Components: `PascalCase` (e.g., `PlayerStats`, `GameTerminal`)
- Hooks: `camelCase` with `use` prefix (e.g., `useGameConnection`)
- Utilities: `camelCase` (e.g., `parseCommand`, `sanitizeInput`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_CHAT_LENGTH`)

### Logging Best Practices

**CRITICAL**: MythosMUD uses an enhanced structured logging system. Follow these rules strictly:

#### ✅ CORRECT Usage

```python
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# Structured logging with key-value pairs

logger.info("User action completed", user_id=user.id, action="login", success=True)

# Error logging with context

logger.error("Operation failed", operation="user_creation", error=str(e), retry_count=3)

# Performance monitoring

from server.logging.enhanced_logging_config import measure_performance
with measure_performance("database_query", user_id=user.id):
    result = database.query("SELECT * FROM players")
```

#### ❌ WRONG Usage (Will Cause Failures)

```python
# ❌ WRONG - Will cause import failures

import logging
logger = logging.getLogger(__name__)

# ❌ WRONG - F-string logging destroys structured logging

logger.info(f"User {user_id} performed {action}")
logger.error(f"Failed to process: {error}")

# ❌ WRONG - Deprecated context parameter

logger.info("message", context={"key": "value"})

# ❌ WRONG - Unstructured messages

logger.info("Error occurred")  # No context!
```

**Logging Guidelines**:

- Always use structured logging with key-value pairs
- Never use f-strings or string formatting in log messages
- Include relevant context (user_id, operation, error details)
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Never log sensitive data (passwords, tokens, PII)
- Use correlation IDs for request tracing

See [docs/LOGGING_BEST_PRACTICES.md](docs/LOGGING_BEST_PRACTICES.md) for comprehensive logging guide.

### Security Requirements

**CRITICAL SECURITY RULES** - Violation will result in PR rejection:

1. **Never Commit Secrets**
   - No API keys, passwords, tokens, or credentials in code
   - Use environment variables for all sensitive configuration
   - Review changes carefully before committing

2. **Input Validation**
   - Always validate and sanitize user input on the server side
   - Never trust client-side validation alone
   - Use Pydantic models for request validation

3. **Database Security**
   - Always use parameterized queries (never string concatenation)
   - Implement proper access controls
   - Validate all file paths to prevent traversal attacks

4. **Authentication & Authorization**
   - Always verify user permissions before allowing actions
   - Use JWT tokens properly (check expiration, validate signature)
   - Implement rate limiting for sensitive endpoints

5. **COPPA Compliance**
   - Never collect personal information from minors
   - Implement parental consent where required
   - Minimize data collection to essential game functionality

6. **Error Handling**
   - Never expose sensitive information in error messages
   - Log errors with context but sanitize sensitive data
   - Use generic error messages for users, detailed logs for debugging

**Security Checklist for PRs**:

- [ ] No hardcoded secrets or credentials
- [ ] All user input validated server-side
- [ ] Database queries use parameterized statements
- [ ] Authentication/authorization checks in place
- [ ] Rate limiting implemented where needed
- [ ] Error messages don't expose sensitive data
- [ ] Security tests included

See [SECURITY.md](SECURITY.md) for comprehensive security policies.

---

## Testing Requirements

### Writing Tests

**Test-Driven Development (TDD)**: We practice TDD for all features:

1. **Write the test first** (it should fail)
2. **Implement the feature** (make the test pass)
3. **Refactor** (improve code while keeping tests green)

**Test Organization**:

```text
server/tests/
├── unit/              # Unit tests (fast, isolated)
├── integration/       # Integration tests (multiple components)
├── e2e/              # End-to-end tests (full system)
├── security/         # Security-specific tests
├── performance/      # Performance and load tests
└── fixtures/         # Shared test fixtures
```

**Test Example**:

```python
"""Unit tests for combat system damage calculation.

Tests based on combat mechanics described in "Eldritch Combat Theory"
by Prof. Armitage, ensuring mathematically sound damage calculations.
"""

import pytest
from server.game.combat import CombatSystem


class TestCombatSystem:
    """Test suite for CombatSystem class."""

    @pytest.fixture
    def combat_system(self):
        """Provide a fresh CombatSystem instance for each test."""
        return CombatSystem()

    def test_calculate_damage_basic(self, combat_system):
        """Test basic damage calculation with no armor."""
        damage = combat_system.calculate_damage(
            attacker_strength=10,
            defender_armor=0,
            weapon_modifier=1.0
        )
        assert damage == 10

    def test_calculate_damage_with_armor(self, combat_system):
        """Test damage calculation with armor reduction."""
        damage = combat_system.calculate_damage(
            attacker_strength=10,
            defender_armor=3,
            weapon_modifier=1.0
        )
        assert damage == 7

    def test_calculate_damage_with_weapon_modifier(self, combat_system):
        """Test damage calculation with weapon modifier."""
        damage = combat_system.calculate_damage(
            attacker_strength=10,
            defender_armor=0,
            weapon_modifier=1.5
        )
        assert damage == 15

    def test_calculate_damage_negative_result(self, combat_system):
        """Test that damage cannot be negative."""
        damage = combat_system.calculate_damage(
            attacker_strength=5,
            defender_armor=10,
            weapon_modifier=1.0
        )
        assert damage == 0

    def test_calculate_damage_invalid_stats(self, combat_system):
        """Test that invalid stats raise ValueError."""
        with pytest.raises(ValueError, match="Combat stats cannot be negative"):
            combat_system.calculate_damage(
                attacker_strength=-5,
                defender_armor=10,
                weapon_modifier=1.0
            )
```

**Test Guidelines**:

- One test class per module/class being tested
- Descriptive test names that explain what is being tested
- Use fixtures for setup and teardown
- Test happy path, edge cases, and error conditions
- Mock external dependencies (database, network, etc.)
- Keep tests fast and isolated

### Test Coverage

**Requirements**:

**Critical Files**: 90% test coverage (security, authentication, data handling)

- `server/auth/*` - Authentication and password hashing
- `server/security_utils.py` - Security utilities
- `server/validators/security_validator.py` - Security validation
- `server/database.py` - Database initialization
- `server/persistence/*` - Data persistence
- `server/services/admin_auth_service.py` - Admin authentication
- `server/services/inventory_mutation_guard.py` - Inventory security
- **Normal Files**: 70% test coverage (all other code)
- **CI Enforcement**: Coverage thresholds are enforced in CI/CD
- **Pre-commit Hook**: Coverage thresholds checked before commit (if coverage.xml exists)

**Coverage Exclusions**:

- Type stubs and protocol definitions (`server/stubs/*`)
- Test files (`server/tests/*`)
- Database migrations (`server/alembic/*`)
- Intentionally unreachable code (defensive programming)
- Third-party integration code (test integration points)

**Check Coverage**:

```powershell
# Run tests with coverage

make test-server-coverage

# View HTML report
# Open htmlcov/index.html in browser

# Check coverage thresholds

python scripts/check_coverage_thresholds.py

# Analyze coverage gaps and generate status document

python scripts/analyze_coverage_gaps.py
```

**Coverage Configuration**:

- Coverage settings are in `.coveragerc` and `pyproject.toml`
- Per-file thresholds are enforced via `scripts/check_coverage_thresholds.py`
- Coverage reports are automatically uploaded to Codacy in CI/CD

**Coverage Report Example**:

```
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
server/auth/argon2_utils.py               234      5    98%  (CRITICAL: requires 90%)
server/security_utils.py                 147      8    95%  (CRITICAL: requires 90%)
server/game/combat.py                     45      3    93%
server/game/movement.py                   32      0   100%
server/commands/chat.py                   56     18    68%  (NORMAL: requires 70%)
-----------------------------------------------------------
TOTAL                                    1234     89    93%
```

### Running Tests

**CRITICAL RULES**:

**ALWAYS** use `make test` from project root

**NEVER** run tests from `/server/` directory

**NEVER** use `python -m pytest` directly

```powershell
# Run all tests

make test

# Run server tests only

make test

# Run client unit tests (Vitest)

make test-client

# Run client E2E tests (Playwright)

make test-client-runtime

# Run tests with coverage

make test-server-coverage

# Check coverage thresholds (after running tests)

python scripts/check_coverage_thresholds.py

# Analyze coverage gaps

python scripts/analyze_coverage_gaps.py

# Run specific test file

cd server
uv run pytest tests/unit/game/test_combat.py -v

# Run specific test function

uv run pytest tests/unit/game/test_combat.py::TestCombatSystem::test_calculate_damage_basic -v

# Run with verbose output

make test PYTEST_ARGS="-v"

# Run with debug output

make test PYTEST_ARGS="-vv -s"
```

**Test Execution Notes**:

- First test run may be slower (database setup)
- Tests use isolated test databases
- All tests should be idempotent (repeatable)
- Tests clean up after themselves

See [server/tests/SETUP.md](server/tests/SETUP.md) for detailed testing guide.

---

## Documentation

**Documentation is as important as code.** When making changes:

### Code Documentation

1. **Docstrings**: Write clear docstrings for all public functions and classes

   ```python
   def calculate_lucidity_loss(exposure_time: int, entity_type: str) -> int:
       """Calculate lucidity loss from exposure to eldritch entities.

       Based on research from "Psychological Effects of Non-Euclidean Architecture"
       by Dr. Armitage, 1928. lucidity loss increases exponentially with exposure time
       and varies by entity type.

       Args:
           exposure_time: Duration of exposure in seconds
           entity_type: Type of eldritch entity ("shoggoth", "deep_one", etc.)

       Returns:
           Amount of lucidity points lost (0-100)

       Raises:
           ValueError: If entity_type is not recognized

       Example:
           >>> calculate_lucidity_loss(10, "shoggoth")
           25
       """
   ```

2. **Inline Comments**: Explain complex logic and business rules

   ```python
   # The Wilmarth Coefficient adjusts lucidity loss based on entity proximity
   # See: "The Whisperer in Darkness" correspondence, 1928

   proximity_factor = 1.0 / max(1, distance_to_entity)
   lucidity_loss = base_loss * proximity_factor * WILMARTH_COEFFICIENT
   ```

3. **Type Hints**: Use type hints for better code clarity

   ```python
   from typing import Optional, List, Dict, Any

   def get_player_inventory(
       player_id: str,
       include_equipped: bool = True
   ) -> List[Dict[str, Any]]:
       """Retrieve player's inventory items."""
       ...
   ```

### Project Documentation

When making significant changes, update relevant documentation:

**README.md**: For project-wide changes

**PLANNING.md**: For feature status updates

**docs/**: For technical specifications and guides

**Code comments**: For implementation details

### Mythos References

We encourage (but don't require) adding Lovecraftian flavor to documentation:

- Reference canonical Lovecraft works
- Invent academic sources (journals, researchers)
- Maintain scholarly tone
- Keep variable/function names readable

**Example**:

```python
# Implementing player position tracking as described in
# "Dimensional Mapping in Non-Euclidean Spaces" - Prof. Peaslee, 1932

class PositionTracker:
    """Track player positions across interconnected rooms.

    AI Agent Note: This uses a graph-based approach for efficient
    pathfinding and proximity calculations.
    """
```

---

## Community

### Getting Help

**GitHub Issues**: Ask questions or report problems

**Pull Request Comments**: Discuss implementation details

**Documentation**: Check existing docs first

**Maintainers**: Reach out to @arkanwolfshade or @TylerWolfshade

### Communication Guidelines

Be respectful and professional

- Provide context when asking questions
- Share relevant code, logs, or screenshots
- Be patient - maintainers are volunteers
- Thank contributors and reviewers

### Review Process

**For Contributors**:

- Expect reviews to take 1-7 days
- Address feedback promptly
- Ask questions if feedback is unclear
- Be open to suggestions and alternatives
- Learn from the review process

**For Reviewers**:

- Be constructive and specific
- Explain the "why" behind feedback
- Acknowledge good work
- Suggest improvements, don't demand perfection
- Approve when code meets standards

---

## Recognition

We value all contributions, large and small. Contributors will be:

- Listed in project documentation
- Credited in release notes
- Mentioned in relevant GitHub issues/PRs
- Acknowledged in commit history

**Types of Contributions We Celebrate**:

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🧪 Test coverage increases
- 🔒 Security enhancements
- ♿ Accessibility improvements
- 🎨 UI/UX enhancements
- 🔧 Tooling and infrastructure
- 💡 Ideas and suggestions

---

## Additional Resources

### Essential Reading

[README.md](README.md) - Project overview

- [PLANNING.md](PLANNING.md) - Development roadmap
- [SECURITY.md](SECURITY.md) - Security policies
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) - Development guide
- [docs/DEVELOPMENT_AI.md](docs/DEVELOPMENT_AI.md) - AI agent guidelines

### Technical Documentation

[docs/PRD.md](docs/PRD.md) - Product requirements

- [docs/REAL_TIME_ARCHITECTURE.md](docs/REAL_TIME_ARCHITECTURE.md) - Real-time system
- [docs/LOGGING_BEST_PRACTICES.md](docs/LOGGING_BEST_PRACTICES.md) - Logging guide
- [docs/E2E_TESTING_GUIDE.md](docs/E2E_TESTING_GUIDE.md) - E2E testing
- [docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md](docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md) - PostgreSQL standards and SQL guardrails

### Testing Resources

[server/tests/SETUP.md](server/tests/SETUP.md) - Test setup guide

- [e2e-tests/MULTIPLAYER_TEST_RULES.md](e2e-tests/MULTIPLAYER_TEST_RULES.md) - E2E scenarios
- [docs/COMMAND_TESTING_GUIDE.md](docs/COMMAND_TESTING_GUIDE.md) - Command testing

### Style Guides

[PEP 8](https://pep8.org/) - Python style guide

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) - TypeScript guide
- [React Documentation](https://react.dev/) - React best practices

---

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search closed GitHub issues
3. Ask in a new GitHub issue with the `question` label
4. Contact maintainers directly for sensitive matters

---

> "Together, we forge ahead into territories unknown, our tools our typewriters and terminals, our mission to chronicle
> and contain the Mythos within this digital realm. May your contributions be scholarly, your tests comprehensive, and
> your commits meaningful."
>
> — The Faculty of Miskatonic University's Department of Computer Sciences and Occult Studies

---

**Last Updated**: January 2025
**Version**: 1.0
**Maintainers**: @arkanwolfshade, @TylerWolfshade
