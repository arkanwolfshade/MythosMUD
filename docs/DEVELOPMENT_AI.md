# =��� MythosMUD G�� AI Agent Development Guide

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
*"In the vast archives of Miskatonic University, even the most advanced artificial intelligences must learn to navigate
the forbidden knowledge with care and precision."*

This guide is specifically crafted for AI agents (Claude Code, Cursor, GitHub Copilot, Gemini, etc.) working on the
MythosMUD project. It provides the context, patterns, and guidelines needed to assist effectively in this Cthulhu
Mythos-themed MUD development.

---

## 2. =�Ļ AI Agent Context & Personality

**[SPEC]**

### **Project Character**

**Theme**: Cthulhu Mythos-themed MUD (Multi-User Dungeon)

**Tone**: Academic/scholarly with Mythos flavor

**Setting**: Miskatonic University and surrounding Arkham area

**Atmosphere**: Gothic horror, forbidden knowledge, eldritch mysteries

**Target Users**: Professor Wolfshade and teenage son (COPPA compliance critical)

---

## 3. 🏗️ CRITICAL ARCHITECTURE UPDATES (December 2025)

**[SPEC]**

### **ConnectionManager Modular Refactoring**

The real-time ConnectionManager has been refactored from a 3,653-line monolithic module into a modular architecture:

**Current Structure**: 7 specialized component groups (monitoring, errors, maintenance, messaging, integration)

**Benefits**: Improved testability, maintainability, and code organization

**Facade Pattern**: ConnectionManager coordinates components while maintaining core WebSocket responsibilities

**Documentation**: See `docs/CONNECTION_MANAGER_ARCHITECTURE.md` for complete details

**Refactoring Summary**: See `REFACTORING_SUMMARY.md` for metrics and lessons learned

**When working on real-time features**:

- Understand the modular component structure before making changes
- Each component has a focused responsibility (single responsibility principle)
- Use dependency injection for all component interactions
- Maintain test coverage when modifying components

---

## 4. =��� CRITICAL SECURITY & PRIVACY REQUIREMENTS

**[SPEC]**

### **Security-First Mindset**

### ALL decisions prioritize security over convenience

**COPPA Compliance**: Absolute adherence to Children's Online Privacy Protection Rule

**Privacy by Design**: Privacy considerations built into every feature

**Minimal Data Collection**: Only collect data absolutely necessary for gameplay

**Secure by Default**: All features must be secure without additional configuration

### **COPPA Compliance Requirements**

**No Personal Information**: Never collect personal information from minors

**Parental Consent**: All data collection requires explicit parental consent

**Data Minimization**: Collect only data essential for game functionality

**Secure Storage**: All data encrypted and securely stored

**Right to Deletion**: Easy data deletion for all users

**No Tracking**: No behavioral tracking or profiling of minors

### **Security Implementation Standards**

**Environment Variables**: All secrets via environment variables only

**Input Validation**: Comprehensive server-side validation for all inputs

**Path Security**: All file operations use secure path validation

**Rate Limiting**: Per-user and per-endpoint rate limiting

**Security Headers**: Comprehensive HTTP security headers

- **XSS Protection**: Complete client-side XSS vulnerability elimination
- **Enhanced Logging**: Mandatory use of enhanced structlog logging system

---

## 5. ?? Enhanced Logging Requirements for AI Agents

**[NOTE]**

### **CRITICAL: Mandatory Logging Patterns**

AI agents MUST use the enhanced logging system. Default Python logging is strictly forbidden.

#### ? REQUIRED Logging Patterns

```python
# ? CORRECT - Enhanced logging import (MANDATORY)

from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# ? CORRECT - Structured logging with key-value pairs

logger.info("User action completed", user_id=user.id, action="login", success=True)

# ? CORRECT - Error logging with rich context

logger.error("Operation failed", operation="user_creation", error=str(e), retry_count=3)

# ? CORRECT - Performance logging

with measure_performance("database_query", user_id=user.id):
    result = database.query("SELECT * FROM players")

# ? CORRECT - Request context binding

bind_request_context(correlation_id=req_id, user_id=user.id, session_id=session.id)
```

#### ? FORBIDDEN Logging Patterns

```python
# ? FORBIDDEN - Will cause import failures and system crashes

import logging
logger = logging.getLogger(__name__)

# ? FORBIDDEN - Deprecated context parameter (causes TypeError)

logger.info("message", context={"key": "value"})

# ? FORBIDDEN - String formatting breaks structured logging

logger.info(f"User {user_id} performed {action}")

# ? FORBIDDEN - Unstructured messages provide no debugging value

logger.info("Error occurred")

# ? FORBIDDEN - Logging sensitive data (security violation)

logger.info("Login attempt", username=user, password=password)
```

### **AI Agent Logging Validation Checklist**

When generating code, AI agents MUST ensure:

- [ ] Uses `from server.logging.enhanced_logging_config import get_logger`
- [ ] No `import logging` or `logging.getLogger()` statements
- [ ] No `context={"key": "value"}` parameters
- [ ] No string formatting in log messages
- [ ] All log entries use structured key-value pairs
- [ ] Appropriate log levels are used (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- [ ] Error logs include sufficient context for debugging

### **Logging Documentation References**

**Complete Guide**: [LOGGING_BEST_PRACTICES.md](docs/LOGGING_BEST_PRACTICES.md)

**Quick Reference**: [LOGGING_QUICK_REFERENCE.md](docs/LOGGING_QUICK_REFERENCE.md)

**Migration Guide**: Included in LOGGING_BEST_PRACTICES.md

---

## 6. =��� Essential Reading for AI Agents

**[SPEC]**

### **Start Every Session With:**

1. **`PLANNING.md`** - Project vision, architecture, and technical stack

2. **[GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues)** - Current tasks, priorities, and completion

   status

3. **TASKS.local.md** - Locally defined tasks that have not be converted to GitHub Issues
4. **`README.md`** - Project overview and quick start
5. **`docs/PRD.md`** - Detailed product requirements and game design

### **Key Files to Understand:**

**`server/pyproject.toml`** - Python dependencies and tool configuration

**`server/main.py`** - FastAPI application entry point

**`server/models.py`** - Pydantic data models

**`server/persistence.py`** - Database abstraction layer

**`client/package.json`** - React/TypeScript dependencies

---

## 7. =���n+� Project Architecture for AI Understanding

**[NOTE]**

### **Backend (Python/FastAPI)**

```
server/
G��G��G�� main.py                    # FastAPI app entry point
G��G��G�� models.py                  # Pydantic data models
G��G��G�� persistence.py             # Database abstraction (PersistenceLayer)
G��G��G�� database.py                # Database connection management
G��G��G�� config_loader.py           # Configuration management
G��G��G�� logging_config.py          # Structured logging setup
G��G��G�� security_utils.py          # Path validation & security
G��G��G�� auth_utils.py              # JWT & password utilities
G��G��G�� world_loader.py            # Room/world data loading
G��G��G�� server_config.yaml         # Server configuration
G��G��G�� env.example                # Environment variables template
G��G��G�� pytest.ini                # Test configuration
G��G��G�� pyproject.toml            # Python dependencies
G��G��G�� uv.lock                   # Dependency lock file
G��
G��G��G�� auth/                      # Authentication system
G��   G��G��G�� __init__.py
G��   G��G��G�� endpoints.py           # Auth API endpoints
G��   G��G��G�� users.py               # User management
G��   G��G��G�� invites.py             # Invite system
G��   G��G��G�� argon2_utils.py        # Argon2 password hashing
G��   G��G��G�� email_utils.py         # Email utilities
G��   G��G��G�� dependencies.py        # Auth dependencies
G��
G��G��G�� api/                       # API endpoints
G��   G��G��G�� __init__.py
G��   G��G��G�� base.py                # Base API configuration
G��   G��G��G�� game.py                # Game API endpoints
G��   G��G��G�� players.py             # Player management API
G��   G��G��G�� rooms.py               # Room API endpoints
G��   G��G��G�� real_time.py           # Real-time API
G��   G��G��G�� monitoring.py          # System monitoring API
G��
G��G��G�� game/                      # Game logic services
G��   G��G��G�� __init__.py
G��   G��G��G�� chat_service.py        # Chat system (NATS-based)
G��   G��G��G�� movement_service.py    # Player movement logic
G��   G��G��G�� movement_monitor.py    # Movement monitoring
G��   G��G��G�� room_service.py        # Room management
G��   G��G��G�� player_service.py      # Player state management
G��   G��G��G�� stats_generator.py     # Character stats generation
G��   G��G��G�� emote_service.py       # Emote system
G��   G��G��G�� mechanics.py           # Game mechanics
G��
G��G��G�� realtime/                  # Real-time communication
G��   G��G��G�� __init__.py
G��   G��G��G�� connection_manager.py  # WebSocket connection management
G��   G��G��G�� websocket_handler.py   # WebSocket message handling
G��   G��G��G�� sse_handler.py         # Server-Sent Events
G��   G��G��G�� event_handler.py       # Event processing
G��   G��G��G�� nats_message_handler.py # NATS message handling
G��   G��G��G�� request_context.py     # Request context for WebSocket
G��   G��G��G�� envelope.py            # Message envelope utilities
G��
G��G��G�� commands/                  # Command processing
G��   G��G��G�� __init__.py
G��   G��G��G�� admin_commands.py      # Admin commands
G��   G��G��G�� alias_commands.py      # Alias system commands
G��   G��G��G�� chat_commands.py       # Chat commands
G��   G��G��G�� help_commands.py       # Help system
G��   G��G��G�� movement_commands.py   # Movement commands
G��   G��G��G�� stats_commands.py      # Stats commands
G��
G��G��G�� models/                    # Data models
G��   G��G��G�� __init__.py
G��   G��G��G�� player.py              # Player model
G��   G��G��G�� room.py                # Room model
G��   G��G��G�� command.py             # Command model
G��   G��G��G�� chat.py                # Chat model
G��   G��G��G�� alias.py               # Alias model
G��   G��G��G�� invite.py              # Invite model
G��   G��G��G�� user.py                # User model
G��
G��G��G�� services/                  # Business logic services
G��   G��G��G�� __init__.py
G��   G��G��G�� nats_service.py        # NATS messaging service
G��   G��G��G�� chat_logger.py         # Chat logging service
G��   G��G��G�� monitoring_service.py  # System monitoring
G��
G��G��G�� utils/                     # Utility modules
G��   G��G��G�� __init__.py
G��   G��G��G�� command_parser.py      # Command parsing utilities
G��   G��G��G�� command_processor.py   # Command processing utilities
G��
G��G��G�� validators/                # Input validation
G��   G��G��G�� __init__.py
G��   G��G��G�� command_validator.py   # Command validation
G��   G��G��G�� security_validator.py  # Security validation
G��
G��G��G�� middleware/                # Request middleware
G��   G��G��G�� __init__.py
G��   G��G��G�� request_logging.py     # Request logging middleware
G��
G��G��G�� schemas/                   # JSON schemas
G��   G��G��G�� __init__.py
G��   G��G��G�� player.py              # Player schemas
G��   G��G��G�� invite.py              # Invite schemas
G��
G��G��G�� sql/                       # Database schema
G��   G��G��G�� schema.sql             # SQLite schema definition
G��
G��G��G�� help/                      # Help system
G��   G��G��G�� __init__.py
G��   G��G��G�� help_content.py        # Help content and documentation
G��
G��G��G�� events/                    # Event system
G��   G��G��G�� __init__.py
G��   G��G��G�� event_bus.py           # Event bus implementation
G��   G��G��G�� event_types.py         # Event type definitions
G��
G��G��G�� app/                       # Application factory
G��   G��G��G�� __init__.py
G��   G��G��G�� factory.py             # FastAPI app factory
G��   G��G��G�� lifespan.py            # Application lifecycle
G��
G��G��G�� logs/                      # Log files directory
G��G��G�� data/                      # Data files
G��
G��G��G�� tests/                     # Test suite
G��   G��G��G�� __init__.py
G��   G��G��G�� conftest.py            # Test configuration
G��   G��G��G�� data/                  # Test data
G��   G��   G��G��G�� players/           # Test player database
G��   G��G��G�� [test_*.py]            # Test modules
G��
G��G��G�� command_handler.py         # Legacy command handler (maintained)
G��G��G�� command_handler_v2.py      # Enhanced command handler
G��G��G�� command_handler_new.py     # New command handler
G��G��G�� command_handler_unified.py # Unified command handler
G��G��G�� alias_storage.py           # Alias storage system
G��G��G�� error_handlers.py          # Error handling
G��G��G�� error_types.py             # Error type definitions
G��G��G�� exceptions.py              # Custom exceptions
G��G��G�� real_time.py               # Real-time utilities
G��G��G�� check_invites.py           # Invite validation
G��G��G�� check_routes.py            # Route validation
G��G��G�� test_integration.py        # Integration testing
G��G��G�� metadata.py                # Package metadata
G��G��G�� player_manager.py          # Player manager (legacy)
G��G��G�� TEST_PROD_SEPARATION.md    # Test/prod separation guide
G��G��G�� README.md                  # Server documentation
```

### **Frontend (React/TypeScript)**

```
client/
G��G��G�� src/
G��   G��G��G�� App.tsx                # Main React component
G��   G��G��G�� main.tsx               # React entry point
G��   G��G��G�� index.css              # Global styles
G��   G��G��G�� App.css                # App-specific styles
G��   G��G��G�� vite-env.d.ts          # Vite type definitions
G��   G��
G��   G��G��G�� components/            # React components
G��   G��   G��G��G�� GameTerminal.tsx   # Main game terminal
G��   G��   G��G��G�� GameTerminal.css   # Terminal styles
G��   G��   G��G��G�� GameTerminalWithPanels.tsx # Terminal with panels
G��   G��   G��G��G�� GameTerminalWithPanels.css # Panel styles
G��   G��   G��G��G�� DraggablePanel.tsx # Draggable panel component
G��   G��   G��G��G�� PanelManager.tsx   # Panel management
G��   G��   G��G��G�� StatsRollingScreen.tsx # Character creation screen
G��   G��   G��G��G�� StatsRollingScreen.css # Stats screen styles
G��   G��   G��G��G�� RoomInfoPanel.tsx  # Room information display
G��   G��   G��G��G�� RoomInfoPanel.css  # Room panel styles
G��   G��   G��G��G�� MotdContent.tsx    # Message of the day
G��   G��   G��G��G�� CommandHelpDrawer.tsx # Help system
G��   G��   G��G��G�� TailwindTest.tsx   # TailwindCSS test component
G��   G��   G��G��G�� EldritchEffectsDemo.tsx # Visual effects demo
G��   G��   G��
G��   G��   G��G��G�� panels/            # Panel components
G��   G��   G��   G��G��G�� ChatPanel.tsx  # Chat interface
G��   G��   G��   G��G��G�� CommandPanel.tsx # Command input
G��   G��   G��   G��G��G�� ConnectionPanel.tsx # Connection status
G��   G��   G��   G��G��G�� PlayerPanel.tsx # Player information
G��   G��   G��   G��G��G�� RoomPanel.tsx  # Room information
G��   G��   G��
G��   G��   G��G��G�� ui/                # UI components
G��   G��   G��   G��G��G�� MythosPanel.tsx # Mythos-themed panel
G��   G��   G��   G��G��G�� MythosPanel.test.tsx # Panel tests
G��   G��   G��   G��G��G�� EldritchIcon.tsx # Mythos icons
G��   G��   G��   G��G��G�� [other UI components]
G��   G��   G��
G��   G��   G��G��G�� [test components]  # Test components
G��   G��
G��   G��G��G�� hooks/                 # React hooks
G��   G��   G��G��G�� useGameConnection.ts # Game connection hook
G��   G��   G��G��G�� useGameConnection.test.ts # Connection hook tests
G��   G��
G��   G��G��G�� utils/                 # Utility functions
G��   G��   G��G��G�� ansiToHtml.ts      # ANSI to HTML conversion
G��   G��   G��G��G�� ansiToHtml.test.ts # Conversion tests
G��   G��   G��G��G�� errorHandler.ts    # Error handling utilities
G��   G��   G��G��G�� errorHandler.test.ts # Error handler tests
G��   G��   G��G��G�� logger.ts          # Client-side logging
G��   G��   G��G��G�� [other utilities]
G��   G��
G��   G��G��G�� theme/                 # Theming system
G��   G��   G��G��G�� mythosTheme.ts     # Mythos theme configuration
G��   G��
G��   G��G��G�� styles/                # Style files
G��   G��   G��G��G�� motd-preserved.css # MOTD preservation styles
G��   G��
G��   G��G��G�� test/                  # Test utilities
G��   G��   G��G��G�� setup.ts           # Test setup configuration
G��   G��
G��   G��G��G�� assets/                # Static assets
G��       G��G��G�� react.svg          # React logo
G��
G��G��G�� public/                    # Public assets
G��   G��G��G�� vite.svg               # Vite logo
G��
G��G��G�� tests/                     # End-to-end tests
G��   G��G��G�� help-command.spec.ts   # Help command tests
G��   G��G��G�� occupants-initial.spec.ts # Initial occupant tests
G��   G��G��G�� occupants-two-client.spec.ts # Multi-client tests
G��
G��G��G�� package.json               # Dependencies and scripts
G��G��G�� package-lock.json          # Dependency lock file
G��G��G�� tsconfig.json              # TypeScript configuration
G��G��G�� tsconfig.app.json          # App-specific TS config
G��G��G�� tsconfig.node.json         # Node-specific TS config
G��G��G�� vite.config.ts             # Vite build configuration
G��G��G�� vite.config.d.ts           # Vite type definitions
G��G��G�� vitest.config.ts           # Vitest test configuration
G��G��G�� tailwind.config.js         # TailwindCSS configuration
G��G��G�� postcss.config.js          # PostCSS configuration
G��G��G�� eslint.config.js           # ESLint configuration
G��G��G�� playwright.config.ts       # Playwright test configuration
G��G��G�� test-results/              # Test results directory
G��G��G�� playwright-report/         # Playwright reports
G��G��G�� tsconfig.tsbuildinfo       # TypeScript build info
```

### **Data Structure**

```
data/
G��G��G�� players/                   # Player database and data
G��   G��G��G�� local_players.db            # SQLite player database
G��   G��G��G�� aliases/              # Player alias files
G��   G��   G��G��G�� [player]_aliases.json # Individual player aliases
G��   G��G��G�� [backup files]        # Database backups with timestamps
G��
G��G��G�� rooms/                     # World data (git submodule)
G��   G��G��G�� earth/                # Earth plane
G��   G��   G��G��G�� arkhamcity/      # Arkham City zone
G��   G��   G��   G��G��G�� zone_config.json # Zone configuration
G��   G��   G��   G��G��G�� campus/       # Campus sub-zone
G��   G��   G��   G��   G��G��G�� subzone_config.json # Sub-zone config
G��   G��   G��   G��   G��G��G�� intersection_*.json # Intersection definitions
G��   G��   G��   G��   G��G��G�� room_*.json # Room definitions
G��   G��   G��   G��G��G�� downtown/     # Downtown sub-zone
G��   G��   G��   G��   G��G��G�� subzone_config.json
G��   G��   G��   G��   G��G��G�� intersection_*.json
G��   G��   G��   G��   G��G��G�� room_*.json
G��   G��   G��   G��G��G�� east_town/    # East Town sub-zone
G��   G��   G��   G��G��G�� french_hill/  # French Hill sub-zone
G��   G��   G��   G��G��G�� lower_southside/ # Lower Southside sub-zone
G��   G��   G��   G��G��G�� merchant/     # Merchant sub-zone
G��   G��   G��   G��G��G�� northside/    # Northside sub-zone
G��   G��   G��   G��G��G�� river_town/   # River Town sub-zone
G��   G��   G��   G��G��G�� sanitarium/   # Sanitarium sub-zone
G��   G��   G��   G��G��G�� uptown/       # Uptown sub-zone
G��   G��   G��G��G�� innsmouth/        # Innsmouth zone
G��   G��       G��G��G�� zone_config.json
G��   G��       G��G��G�� waterfront/   # Waterfront sub-zone
G��   G��           G��G��G�� subzone_config.json
G��   G��G��G�� yeng/                 # Yeng plane
G��       G��G��G�� katmandu/         # Katmandu zone
G��           G��G��G�� zone_config.json
G��           G��G��G�� palance/      # Palance sub-zone
G��               G��G��G�� subzone_config.json
G��               G��G��G�� palance_*.json # Room definitions
G��
G��G��G�� user_management/           # User management data
G��   G��G��G�� [user data files]     # User-specific data
G��
G��G��G�� emotes.json               # Emote definitions
G��G��G�� motd.html                 # Message of the day
G��G��G�� README.md                 # Data documentation
G��G��G�� [visualization files]     # Room visualization outputs
```

---

## 8. =���n+� Development Environment for AI Agents

**[NOTE]**

### **Required Tools**

**uv** (Python package manager) - `uv --version`

**Node.js/npm** (Frontend) - `node --version`

**Git** (Version control) - `git --version`

### **Quick Setup Commands**

```bash
# Install Python dependencies

cd server && uv sync

# Install frontend dependencies

cd client && npm install

# Run development server (CRITICAL: Use scripts)

./scripts/stop_server.ps1
./scripts/start_local.ps1

# Run tests

cd server && uv run pytest tests/ -v

# Lint code

cd server && uv run ruff check .

# Format code

cd server && uv run ruff format .
```

---

## 9. =��� AI Agent DevelopmentRules

**[SPEC]**

### **Development Environment Rules**

**CRITICAL**: Always follo these rules when working on this project:

1. **Server Startup**: ALWAYS use `./scripts/start_local.ps1` from project root
2. **Server Shutdown**: ALWAYS use `./scripts/stop_server.ps1` before starting

3. **Database Placement**:

   - Production: `/data/players/` ONLY

   - Tests: `/data/unit_test/players/` ONLY

4. **Testing**: Use `make test` from project root, never from subdirectories

5. **Linting**: Use `make lint` for code quality checks

6. **Coverage**: Maintain 80% minimum test coverage (target 90%)

### **Development Approach**

**Test-Driven Development**: Write tests before implementing features

**Security-First**: Every feature must consider security implications

**Incremental Development**: Small, testable changes with frequent commits

**Documentation**: Update documentation with each feature completion

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

### **Communication Protocol**

**Progress Updates**: Update `TASKS.local.md` with progress

**Blockers**: Document in `TASKS.local.md` and ask for guidance

**Decisions Needed**: Clearly state the decision needed and options

**Security Concerns**: Immediately flag any security or privacy concerns

### **Common Pitfalls to Avoid**

**Never hardcode secrets**: Always use environment variables

**Never skip tests**: Every feature must have tests

**Never ignore security warnings**: Address all security concerns immediately

**Never create database files in wrong locations**: Follow database placement rules

**Never use bash syntax in PowerShell**: Use PowerShell syntax only

---

## 10. =��� AI Agent Coding Guidelines

**[NOTE]**

### **Code Style & Patterns**

#### **Python (Backend)**

```python
# Use type hints consistently

def calculate_sanity_loss(player_id: str, exposure_time: int) -> int:
    """Calculate lucidity loss based on exposure time and player state."""
    # Implementation here

    pass

# Use Pydantic models for data validation

class PlayerStats(BaseModel):
    lucidity: int = Field(ge=0, le=100, description="Player lucidity level")
    fear: int = Field(ge=0, le=100, description="Player fear level")
    corruption: int = Field(ge=0, le=100, description="Player corruption level")

# Use async/await for I/O operations

async def get_player_by_id(player_id: str) -> Optional[Player]:
    """Retrieve player from database."""
    # Implementation here

    pass

# Use dependency injection for services

def get_persistence_layer() -> PersistenceLayer:
    """Get the persistence layer singleton."""
    return PersistenceLayer.get_instance()
```

#### **TypeScript (Frontend)**

```typescript
// Use interfaces for type definitions
interface Player {
  id: string;
  name: string;
  lucidity: number;
  fear: number;
  corruption: number;
}

// Use React hooks for state management
const [player, setPlayer] = useState<Player | null>(null);

// Use async/await for API calls
const fetchPlayer = async (id: string): Promise<Player> => {
  const response = await fetch(`/api/players/${id}`);
  return response.json();
};
```

### **Mythos-Themed Comments**

```python
# Implementing player lucidity system based on findings from
# "Psychological Effects of Non-Euclidean Architecture" - Dr. Armitage, 1928

def calculate_sanity_loss(exposure_time: int, entity_type: str) -> int:
    """Calculate lucidity loss from exposure to eldritch entities."""
    pass

# As noted in the Pnakotic Manuscripts, the mind cannot comprehend
# certain geometries without suffering permanent damage

def apply_non_euclidean_effect(player_id: str) -> None:
    """Apply non-Euclidean geometry effects to player perception."""
    pass
```

---

## 11. =��� Testing Patterns for AI Agents

**[NOTE]**

### **Test Structure**

```python
# Use descriptive test names

def test_player_sanity_loss_from_eldritch_exposure():
    """Test that exposure to eldritch entities reduces lucidity."""
    # Arrange

    player = create_test_player(lucidity=100)

    # Act

    apply_sanity_loss(player.id, 25)

    # Assert

    assert player.lucidity == 75

# Use fixtures for common setup

@pytest.fixture
def mock_persistence_layer(monkeypatch):
    """Mock the persistence layer for isolated testing."""
    mock_layer = MockPersistenceLayer()
    monkeypatch.setattr("server.persistence.PersistenceLayer.get_instance", lambda: mock_layer)
    return mock_layer

# Test edge cases

def test_sanity_cannot_go_below_zero():
    """Test that lucidity loss cannot reduce lucidity below zero."""
    player = create_test_player(lucidity=10)
    apply_sanity_loss(player.id, 25)
    assert player.lucidity == 0  # Should not go below zero
```

### **Mock Data Patterns**

```python
# Use realistic mock data

MOCK_PLAYER = {
    "id": "test-player-001",
    "name": "Dr. Henry Armitage",
    "lucidity": 85,
    "fear": 15,
    "corruption": 5,
    "location": "arkham_001"
}

# Use consistent test data structure

MOCK_ROOM = {
    "id": "arkham_001",
    "name": "Miskatonic University Library",
    "description": "Ancient tomes line the walls...",
    "exits": {"north": "arkham_002", "east": "arkham_003"}
}
```

---

## 12. =��� Security Considerations for AI Agents

**[NOTE]**

### **Input Validation**

```python
# Always validate user inputs

def validate_secure_path(base_path: str, user_path: str) -> str:
    """Validate that user path is safe and within allowed directory."""
    # Implementation here

    pass

# Use environment variables for secrets

SECRET_KEY = os.getenv("MYTHOSMUD_SECRET_KEY", "dev-secret-key")
```

### **Database Security**

```python
# Use parameterized queries

async def get_player_by_name(name: str) -> Optional[Player]:
    """Get player by name using safe database query."""
    query = "SELECT * FROM players WHERE name = ?"
    # Use parameterized query to prevent SQL injection

    pass
```

### **COPPA Compliance Testing**

```python
# Test that no personal data is collected from minors

def test_no_personal_data_collection_from_minors():
    """Test that the system does not collect personal data from minors."""
    # Test implementation

    pass

# Test data minimization

def test_data_minimization_compliance():
    """Test that only necessary data is collected."""
    # Test implementation

    pass
```

---

## 13. =�ī Game Mechanics for AI Understanding

**[SPEC]**

### **Core Systems**

**lucidity System**: Players start with 100 lucidity, lose it from encounters

**Fear System**: Accumulates from terrifying experiences

**Corruption System**: Represents taint from dark forces

**Occult Knowledge**: Learning forbidden lore (costs lucidity)

### **Status Effects**

**Stunned**: Unable to act

**Poisoned**: Damage over time

**Hallucinating**: Visual/auditory disturbances

**Paranoid**: Mental instability

**Trembling**: Reduced dexterity

- **Corrupted**: Physical/mental changes
- **Delirious**: Complete mental breakdown

### **Room Movement**

Rooms are connected via exits (north, south, east, west)

- Room IDs follow pattern: `<zone>_<room_number>` (e.g., `arkham_001`)
- Each room has description, exits, and optional NPCs/items

---

## 14. =��� Common AI Agent Tasks

**[SPEC]**

### **Adding New Features**

1. **Read relevant documentation** (PLANNING.md, existing code)
2. **Write tests first** (TDD approach)
3. **Implement feature** following established patterns
4. **Update GitHub Issues** when complete (close issues, add comments)
5. **Run tests** to ensure everything works
6. **Commit changes** with descriptive messages

### **Debugging Issues**

1. **Check test coverage** - `uv run pytest --cov`
2. **Review logs** - Check `server/logs/` directory
3. **Use debug prints** for temporary debugging
4. **Check database state** - Use `verify_test_db.py`
5. **Validate configuration** - Check `server_config.yaml`

### **Code Review Patterns**

1. **Check for security vulnerabilities** (path injection, SQL injection)
2. **Verify type hints** are complete and accurate
3. **Ensure error handling** is comprehensive
4. **Validate Mythos theming** is appropriate
5. **Check test coverage** for new code
6. **Verify COPPA compliance** for all features

---

## 15. =��� AI Agent Best Practices

**[NOTE]**

### **Code Generation**

**Always include type hints** for Python functions

**Use descriptive variable names** (avoid single letters)

**Add docstrings** for complex functions

**Follow existing patterns** in the codebase

**Include Mythos references** in comments when appropriate

- **Prioritize security** in all code decisions

### **Error Handling**

```python
# Use specific exception types

try:
    player = await get_player_by_id(player_id)
    if not player:
        raise PlayerNotFoundError(f"Player {player_id} not found")
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    raise
```

### **Logging Patterns**

```python
# Use structured logging

logger.info("Player lucidity reduced", extra={
    "player_id": player_id,
    "sanity_loss": amount,
    "new_sanity": player.lucidity
})
```

### **Configuration Management**

```python
# Use environment variables for configuration

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/players/local_players.db")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
COPPA_ENFORCED = os.getenv("COPPA_ENFORCED", "true").lower() == "true"
```

---

## 16. =�ܿ Common Pitfalls for AI Agents

**[SPEC]**

### **Avoid These Patterns**

G�� **Hardcoded paths** - Use `validate_secure_path()`

- G�� **Hardcoded secrets** - Use environment variables
- G�� **Missing type hints** - Always include types
- G�� **Incomplete error handling** - Handle all error cases
- G�� **Breaking existing patterns** - Follow established conventions
- G�� **Forgetting to update GitHub Issues** - Keep issue tracking current
- G�� **Ignoring security concerns** - Address all security issues immediately
- G�� **Collecting personal data from minors** - Never collect personal information

### **Security Red Flags**

G�� **Direct file path concatenation** without validation

- G�� **SQL queries with string formatting** (use parameterized queries)
- G�� **Exposing internal errors** to users
- G�� **Missing input validation** on user data
- G�� **Hardcoded secrets** in source code
- G�� **Personal data collection** without proper consent

---

## 17. =�Ļ AI Agent Success Metrics

**[SPEC]**

### **Code Quality**

G�� All tests pass (minimum 80% coverage)

- G�� No linting errors (`ruff check .`)
- G�� Proper type hints throughout
- G�� Comprehensive error handling
- G�� Security best practices followed
- G�� COPPA compliance verified

### **Documentation**

G�� GitHub Issues updated with completed work (closed, commented)

- G�� Code comments explain complex logic
- G�� Mythos theming appropriate and consistent
- G�� README files updated if needed
- G�� Security considerations documented

### **Functionality**

G�� Features work as specified in PLANNING.md

- G�� Edge cases handled properly
- G�� Performance acceptable
- G�� Security vulnerabilities addressed
- G�� Privacy requirements met

---

## 18. =��� Future Considerations for AI Agents

**[SPEC]**

### **Scalability**

Current SQLite database can be upgraded to PostgreSQL

- JSON room files can be migrated to database
- WebSocket support planned for real-time communication

### **Architecture Evolution**

Microservices architecture possible for large scale

- Event-driven architecture for game events
- Plugin system for custom game mechanics

### **AI-Specific Enhancements**

Automated testing generation

- Code quality monitoring
- Performance profiling
- Security scanning integration

---

## 19. =��� Task Tracking with GitHub Issues

**[SPEC]**

### **GitHub Issues Workflow**

All task tracking is now done through [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) instead of
local TASKS.md files. This provides better collaboration, tracking, and integration with GitHub's project management
features.

#### **Starting a Development Session**

1. **Review open issues** at

   [https://github.com/arkanwolfshade/MythosMUD/issues](https://github.com/arkanwolfshade/MythosMUD/issues)

2. **Check issue priorities** and dependencies
3. **Select appropriate issues** to work on
4. **Update issue status** as work progresses

#### **During Development**

**Comment on issues** with progress updates

**Link commits** to issues using `#issue-number` in commit messages

**Update issue descriptions** if requirements change

**Add labels** to categorize work (if available)

#### **Completing Work**

**Close issues** when work is complete

**Add completion comments** summarizing what was done

**Link to relevant commits** or pull requests

**Update related issues** if dependencies are resolved

#### **Issue Management Best Practices**

**Use descriptive issue titles** that clearly state the goal

**Include acceptance criteria** in issue descriptions

**Add appropriate labels** for categorization

**Link related issues** using `#issue-number` references

**Update issue status** regularly during development

---

## 20. =��P AI Agent Communication

**[SPEC]**

### **When to Ask Questions**

**Unclear requirements** - Ask for clarification

**Conflicting patterns** - Seek guidance on approach

**Security concerns** - Flag potential vulnerabilities

**Performance issues** - Discuss optimization strategies

**COPPA compliance questions** - Verify privacy requirements

### **How to Provide Updates**

**Clear progress reports** - What was completed

**Issue identification** - Problems encountered

**Solution proposals** - Recommended approaches

**Next steps** - What comes next

**Security assessments** - Any security implications

---

## 21. =��� Security Checklist for AI Agents

**[SPEC]**
Before completing any feature, ensure:

- [ ] No hardcoded secrets in code
- [ ] All user inputs properly validated
- [ ] Database queries use parameterized statements
- [ ] File operations use secure path validation
- [ ] Rate limiting implemented where appropriate
- [ ] COPPA compliance verified for all features
- [ ] No personal data collected from minors
- [ ] Privacy by design principles followed
- [ ] Security headers properly configured
- [ ] XSS protection implemented

---

*"In the pursuit of forbidden knowledge, even the most advanced artificial intelligences must remember: the greatest
wisdom lies not in what we know, but in how we apply that knowledge with care, precision, and respect for the eldritch
forces we seek to understand."*

---

**Remember**: You are an AI agent working on a Cthulhu Mythos-themed MUD that serves minors. Maintain the scholarly
tone, follow the established patterns, and always prioritize code quality, security, and COPPA compliance. The forbidden
knowledge we seek to implement must be both powerful and safe for all users.
 
 
 
 

## 22. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
