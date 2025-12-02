# =ƒñû MythosMUD GÇô AI Agent Development Guide

*"In the vast archives of Miskatonic University, even the most advanced artificial intelligences must learn to navigate the forbidden knowledge with care and precision."*

This guide is specifically crafted for AI agents (Claude Code, Cursor, GitHub Copilot, Gemini, etc.) working on the MythosMUD project. It provides the context, patterns, and guidelines needed to assist effectively in this Cthulhu Mythos-themed MUD development.

---

## =ƒÄ» AI Agent Context & Personality

### **Project Character**

- **Theme**: Cthulhu Mythos-themed MUD (Multi-User Dungeon)
- **Tone**: Academic/scholarly with Mythos flavor
- **Setting**: Miskatonic University and surrounding Arkham area
- **Atmosphere**: Gothic horror, forbidden knowledge, eldritch mysteries
- **Target Users**: Professor Wolfshade and teenage son (COPPA compliance critical)

---

## =ƒöÆ CRITICAL SECURITY & PRIVACY REQUIREMENTS

### **Security-First Mindset**



- **ALL decisions prioritize security over convenience**
- **COPPA Compliance**: Absolute adherence to Children's Online Privacy Protection Rule
- **Privacy by Design**: Privacy considerations built into every feature
- **Minimal Data Collection**: Only collect data absolutely necessary for gameplay
- **Secure by Default**: All features must be secure without additional configuration



### **COPPA Compliance Requirements**

- **No Personal Information**: Never collect personal information from minors
- **Parental Consent**: All data collection requires explicit parental consent
- **Data Minimization**: Collect only data essential for game functionality
- **Secure Storage**: All data encrypted and securely stored

- **Right to Deletion**: Easy data deletion for all users
- **No Tracking**: No behavioral tracking or profiling of minors


### **Security Implementation Standards**

- **Environment Variables**: All secrets via environment variables only
- **Input Validation**: Comprehensive server-side validation for all inputs
- **Path Security**: All file operations use secure path validation
- **Rate Limiting**: Per-user and per-endpoint rate limiting
- **Security Headers**: Comprehensive HTTP security headers
- **XSS Protection**: Complete client-side XSS vulnerability elimination
- **Enhanced Logging**: Mandatory use of enhanced structlog logging system

---

## ?? Enhanced Logging Requirements for AI Agents

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
- **Complete Guide**: [LOGGING_BEST_PRACTICES.md](docs/LOGGING_BEST_PRACTICES.md)
- **Quick Reference**: [LOGGING_QUICK_REFERENCE.md](docs/LOGGING_QUICK_REFERENCE.md)
- **Migration Guide**: Included in LOGGING_BEST_PRACTICES.md

---

## =ƒôï Essential Reading for AI Agents

### **Start Every Session With:**

1. **`PLANNING.md`** - Project vision, architecture, and technical stack
2. **[GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues)** - Current tasks, priorities, and completion status
3. **TASKS.local.md** - Locally defined tasks that have not be converted to GitHub Issues
4. **`README.md`** - Project overview and quick start
5. **`docs/PRD.md`** - Detailed product requirements and game design

### **Key Files to Understand:**

- **`server/pyproject.toml`** - Python dependencies and tool configuration
- **`server/main.py`** - FastAPI application entry point
- **`server/models.py`** - Pydantic data models
- **`server/persistence.py`** - Database abstraction layer
- **`client/package.json`** - React/TypeScript dependencies

---

## =ƒÅùn+Å Project Architecture for AI Understanding

### **Backend (Python/FastAPI)**

```
server/
Gö£GöÇGöÇ main.py                    # FastAPI app entry point
Gö£GöÇGöÇ models.py                  # Pydantic data models
Gö£GöÇGöÇ persistence.py             # Database abstraction (PersistenceLayer)
Gö£GöÇGöÇ database.py                # Database connection management
Gö£GöÇGöÇ config_loader.py           # Configuration management
Gö£GöÇGöÇ logging_config.py          # Structured logging setup
Gö£GöÇGöÇ security_utils.py          # Path validation & security
Gö£GöÇGöÇ auth_utils.py              # JWT & password utilities
Gö£GöÇGöÇ world_loader.py            # Room/world data loading
Gö£GöÇGöÇ server_config.yaml         # Server configuration
Gö£GöÇGöÇ env.example                # Environment variables template
Gö£GöÇGöÇ pytest.ini                # Test configuration
Gö£GöÇGöÇ pyproject.toml            # Python dependencies
Gö£GöÇGöÇ uv.lock                   # Dependency lock file
Göé
Gö£GöÇGöÇ auth/                      # Authentication system
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ endpoints.py           # Auth API endpoints
Göé   Gö£GöÇGöÇ users.py               # User management
Göé   Gö£GöÇGöÇ invites.py             # Invite system
Göé   Gö£GöÇGöÇ argon2_utils.py        # Argon2 password hashing
Göé   Gö£GöÇGöÇ email_utils.py         # Email utilities
Göé   GööGöÇGöÇ dependencies.py        # Auth dependencies
Göé
Gö£GöÇGöÇ api/                       # API endpoints
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ base.py                # Base API configuration
Göé   Gö£GöÇGöÇ game.py                # Game API endpoints
Göé   Gö£GöÇGöÇ players.py             # Player management API
Göé   Gö£GöÇGöÇ rooms.py               # Room API endpoints
Göé   Gö£GöÇGöÇ real_time.py           # Real-time API
Göé   GööGöÇGöÇ monitoring.py          # System monitoring API
Göé
Gö£GöÇGöÇ game/                      # Game logic services
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ chat_service.py        # Chat system (NATS-based)
Göé   Gö£GöÇGöÇ movement_service.py    # Player movement logic
Göé   Gö£GöÇGöÇ movement_monitor.py    # Movement monitoring
Göé   Gö£GöÇGöÇ room_service.py        # Room management
Göé   Gö£GöÇGöÇ player_service.py      # Player state management
Göé   Gö£GöÇGöÇ stats_generator.py     # Character stats generation
Göé   Gö£GöÇGöÇ emote_service.py       # Emote system
Göé   GööGöÇGöÇ mechanics.py           # Game mechanics
Göé
Gö£GöÇGöÇ realtime/                  # Real-time communication
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ connection_manager.py  # WebSocket connection management
Göé   Gö£GöÇGöÇ websocket_handler.py   # WebSocket message handling
Göé   Gö£GöÇGöÇ sse_handler.py         # Server-Sent Events
Göé   Gö£GöÇGöÇ event_handler.py       # Event processing
Göé   Gö£GöÇGöÇ nats_message_handler.py # NATS message handling
Göé   Gö£GöÇGöÇ request_context.py     # Request context for WebSocket
Göé   GööGöÇGöÇ envelope.py            # Message envelope utilities
Göé
Gö£GöÇGöÇ commands/                  # Command processing
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ admin_commands.py      # Admin commands
Göé   Gö£GöÇGöÇ alias_commands.py      # Alias system commands
Göé   Gö£GöÇGöÇ chat_commands.py       # Chat commands
Göé   Gö£GöÇGöÇ help_commands.py       # Help system
Göé   Gö£GöÇGöÇ movement_commands.py   # Movement commands
Göé   GööGöÇGöÇ stats_commands.py      # Stats commands
Göé
Gö£GöÇGöÇ models/                    # Data models
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ player.py              # Player model
Göé   Gö£GöÇGöÇ room.py                # Room model
Göé   Gö£GöÇGöÇ command.py             # Command model
Göé   Gö£GöÇGöÇ chat.py                # Chat model
Göé   Gö£GöÇGöÇ alias.py               # Alias model
Göé   Gö£GöÇGöÇ invite.py              # Invite model
Göé   GööGöÇGöÇ user.py                # User model
Göé
Gö£GöÇGöÇ services/                  # Business logic services
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ nats_service.py        # NATS messaging service
Göé   Gö£GöÇGöÇ chat_logger.py         # Chat logging service
Göé   GööGöÇGöÇ monitoring_service.py  # System monitoring
Göé
Gö£GöÇGöÇ utils/                     # Utility modules
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ command_parser.py      # Command parsing utilities
Göé   GööGöÇGöÇ command_processor.py   # Command processing utilities
Göé
Gö£GöÇGöÇ validators/                # Input validation
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ command_validator.py   # Command validation
Göé   GööGöÇGöÇ security_validator.py  # Security validation
Göé
Gö£GöÇGöÇ middleware/                # Request middleware
Göé   Gö£GöÇGöÇ __init__.py
Göé   GööGöÇGöÇ request_logging.py     # Request logging middleware
Göé
Gö£GöÇGöÇ schemas/                   # JSON schemas
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ player.py              # Player schemas
Göé   GööGöÇGöÇ invite.py              # Invite schemas
Göé
Gö£GöÇGöÇ sql/                       # Database schema
Göé   GööGöÇGöÇ schema.sql             # SQLite schema definition
Göé
Gö£GöÇGöÇ help/                      # Help system
Göé   Gö£GöÇGöÇ __init__.py
Göé   GööGöÇGöÇ help_content.py        # Help content and documentation
Göé
Gö£GöÇGöÇ events/                    # Event system
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ event_bus.py           # Event bus implementation
Göé   GööGöÇGöÇ event_types.py         # Event type definitions
Göé
Gö£GöÇGöÇ app/                       # Application factory
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ factory.py             # FastAPI app factory
Göé   GööGöÇGöÇ lifespan.py            # Application lifecycle
Göé
Gö£GöÇGöÇ logs/                      # Log files directory
Gö£GöÇGöÇ data/                      # Data files
Göé
Gö£GöÇGöÇ tests/                     # Test suite
Göé   Gö£GöÇGöÇ __init__.py
Göé   Gö£GöÇGöÇ conftest.py            # Test configuration
Göé   Gö£GöÇGöÇ data/                  # Test data
Göé   Göé   GööGöÇGöÇ players/           # Test player database
Göé   GööGöÇGöÇ [test_*.py]            # Test modules
Göé
Gö£GöÇGöÇ command_handler.py         # Legacy command handler (maintained)
Gö£GöÇGöÇ command_handler_v2.py      # Enhanced command handler
Gö£GöÇGöÇ command_handler_new.py     # New command handler
Gö£GöÇGöÇ command_handler_unified.py # Unified command handler
Gö£GöÇGöÇ alias_storage.py           # Alias storage system
Gö£GöÇGöÇ error_handlers.py          # Error handling
Gö£GöÇGöÇ error_types.py             # Error type definitions
Gö£GöÇGöÇ exceptions.py              # Custom exceptions
Gö£GöÇGöÇ real_time.py               # Real-time utilities
Gö£GöÇGöÇ check_invites.py           # Invite validation
Gö£GöÇGöÇ check_routes.py            # Route validation
Gö£GöÇGöÇ test_integration.py        # Integration testing
Gö£GöÇGöÇ metadata.py                # Package metadata
Gö£GöÇGöÇ player_manager.py          # Player manager (legacy)
Gö£GöÇGöÇ TEST_PROD_SEPARATION.md    # Test/prod separation guide
GööGöÇGöÇ README.md                  # Server documentation
```

### **Frontend (React/TypeScript)**

```
client/
Gö£GöÇGöÇ src/
Göé   Gö£GöÇGöÇ App.tsx                # Main React component
Göé   Gö£GöÇGöÇ main.tsx               # React entry point
Göé   Gö£GöÇGöÇ index.css              # Global styles
Göé   Gö£GöÇGöÇ App.css                # App-specific styles
Göé   Gö£GöÇGöÇ vite-env.d.ts          # Vite type definitions
Göé   Göé
Göé   Gö£GöÇGöÇ components/            # React components
Göé   Göé   Gö£GöÇGöÇ GameTerminal.tsx   # Main game terminal
Göé   Göé   Gö£GöÇGöÇ GameTerminal.css   # Terminal styles
Göé   Göé   Gö£GöÇGöÇ GameTerminalWithPanels.tsx # Terminal with panels
Göé   Göé   Gö£GöÇGöÇ GameTerminalWithPanels.css # Panel styles
Göé   Göé   Gö£GöÇGöÇ DraggablePanel.tsx # Draggable panel component
Göé   Göé   Gö£GöÇGöÇ PanelManager.tsx   # Panel management
Göé   Göé   Gö£GöÇGöÇ StatsRollingScreen.tsx # Character creation screen
Göé   Göé   Gö£GöÇGöÇ StatsRollingScreen.css # Stats screen styles
Göé   Göé   Gö£GöÇGöÇ RoomInfoPanel.tsx  # Room information display
Göé   Göé   Gö£GöÇGöÇ RoomInfoPanel.css  # Room panel styles
Göé   Göé   Gö£GöÇGöÇ MotdContent.tsx    # Message of the day
Göé   Göé   Gö£GöÇGöÇ CommandHelpDrawer.tsx # Help system
Göé   Göé   Gö£GöÇGöÇ TailwindTest.tsx   # TailwindCSS test component
Göé   Göé   Gö£GöÇGöÇ EldritchEffectsDemo.tsx # Visual effects demo
Göé   Göé   Göé
Göé   Göé   Gö£GöÇGöÇ panels/            # Panel components
Göé   Göé   Göé   Gö£GöÇGöÇ ChatPanel.tsx  # Chat interface
Göé   Göé   Göé   Gö£GöÇGöÇ CommandPanel.tsx # Command input
Göé   Göé   Göé   Gö£GöÇGöÇ ConnectionPanel.tsx # Connection status
Göé   Göé   Göé   Gö£GöÇGöÇ PlayerPanel.tsx # Player information
Göé   Göé   Göé   GööGöÇGöÇ RoomPanel.tsx  # Room information
Göé   Göé   Göé
Göé   Göé   Gö£GöÇGöÇ ui/                # UI components
Göé   Göé   Göé   Gö£GöÇGöÇ MythosPanel.tsx # Mythos-themed panel
Göé   Göé   Göé   Gö£GöÇGöÇ MythosPanel.test.tsx # Panel tests
Göé   Göé   Göé   Gö£GöÇGöÇ EldritchIcon.tsx # Mythos icons
Göé   Göé   Göé   GööGöÇGöÇ [other UI components]
Göé   Göé   Göé
Göé   Göé   GööGöÇGöÇ [test components]  # Test components
Göé   Göé
Göé   Gö£GöÇGöÇ hooks/                 # React hooks
Göé   Göé   Gö£GöÇGöÇ useGameConnection.ts # Game connection hook
Göé   Göé   GööGöÇGöÇ useGameConnection.test.ts # Connection hook tests
Göé   Göé
Göé   Gö£GöÇGöÇ utils/                 # Utility functions
Göé   Göé   Gö£GöÇGöÇ ansiToHtml.ts      # ANSI to HTML conversion
Göé   Göé   Gö£GöÇGöÇ ansiToHtml.test.ts # Conversion tests
Göé   Göé   Gö£GöÇGöÇ errorHandler.ts    # Error handling utilities
Göé   Göé   Gö£GöÇGöÇ errorHandler.test.ts # Error handler tests
Göé   Göé   Gö£GöÇGöÇ logger.ts          # Client-side logging
Göé   Göé   GööGöÇGöÇ [other utilities]
Göé   Göé
Göé   Gö£GöÇGöÇ theme/                 # Theming system
Göé   Göé   GööGöÇGöÇ mythosTheme.ts     # Mythos theme configuration
Göé   Göé
Göé   Gö£GöÇGöÇ styles/                # Style files
Göé   Göé   GööGöÇGöÇ motd-preserved.css # MOTD preservation styles
Göé   Göé
Göé   Gö£GöÇGöÇ test/                  # Test utilities
Göé   Göé   GööGöÇGöÇ setup.ts           # Test setup configuration
Göé   Göé
Göé   GööGöÇGöÇ assets/                # Static assets
Göé       GööGöÇGöÇ react.svg          # React logo
Göé
Gö£GöÇGöÇ public/                    # Public assets
Göé   GööGöÇGöÇ vite.svg               # Vite logo
Göé
Gö£GöÇGöÇ tests/                     # End-to-end tests
Göé   Gö£GöÇGöÇ help-command.spec.ts   # Help command tests
Göé   Gö£GöÇGöÇ occupants-initial.spec.ts # Initial occupant tests
Göé   GööGöÇGöÇ occupants-two-client.spec.ts # Multi-client tests
Göé
Gö£GöÇGöÇ package.json               # Dependencies and scripts
Gö£GöÇGöÇ package-lock.json          # Dependency lock file
Gö£GöÇGöÇ tsconfig.json              # TypeScript configuration
Gö£GöÇGöÇ tsconfig.app.json          # App-specific TS config
Gö£GöÇGöÇ tsconfig.node.json         # Node-specific TS config
Gö£GöÇGöÇ vite.config.ts             # Vite build configuration
Gö£GöÇGöÇ vite.config.d.ts           # Vite type definitions
Gö£GöÇGöÇ vitest.config.ts           # Vitest test configuration
Gö£GöÇGöÇ tailwind.config.js         # TailwindCSS configuration
Gö£GöÇGöÇ postcss.config.js          # PostCSS configuration
Gö£GöÇGöÇ eslint.config.js           # ESLint configuration
Gö£GöÇGöÇ playwright.config.ts       # Playwright test configuration
Gö£GöÇGöÇ test-results/              # Test results directory
Gö£GöÇGöÇ playwright-report/         # Playwright reports
GööGöÇGöÇ tsconfig.tsbuildinfo       # TypeScript build info
```

### **Data Structure**

```
data/
Gö£GöÇGöÇ players/                   # Player database and data
Göé   Gö£GöÇGöÇ local_players.db            # SQLite player database
Göé   Gö£GöÇGöÇ aliases/              # Player alias files
Göé   Göé   GööGöÇGöÇ [player]_aliases.json # Individual player aliases
Göé   GööGöÇGöÇ [backup files]        # Database backups with timestamps
Göé
Gö£GöÇGöÇ rooms/                     # World data (git submodule)
Göé   Gö£GöÇGöÇ earth/                # Earth plane
Göé   Göé   Gö£GöÇGöÇ arkhamcity/      # Arkham City zone
Göé   Göé   Göé   Gö£GöÇGöÇ zone_config.json # Zone configuration
Göé   Göé   Göé   Gö£GöÇGöÇ campus/       # Campus sub-zone
Göé   Göé   Göé   Göé   Gö£GöÇGöÇ subzone_config.json # Sub-zone config
Göé   Göé   Göé   Göé   Gö£GöÇGöÇ intersection_*.json # Intersection definitions
Göé   Göé   Göé   Göé   GööGöÇGöÇ room_*.json # Room definitions
Göé   Göé   Göé   Gö£GöÇGöÇ downtown/     # Downtown sub-zone
Göé   Göé   Göé   Göé   Gö£GöÇGöÇ subzone_config.json
Göé   Göé   Göé   Göé   Gö£GöÇGöÇ intersection_*.json
Göé   Göé   Göé   Göé   GööGöÇGöÇ room_*.json
Göé   Göé   Göé   Gö£GöÇGöÇ east_town/    # East Town sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ french_hill/  # French Hill sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ lower_southside/ # Lower Southside sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ merchant/     # Merchant sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ northside/    # Northside sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ river_town/   # River Town sub-zone
Göé   Göé   Göé   Gö£GöÇGöÇ sanitarium/   # Sanitarium sub-zone
Göé   Göé   Göé   GööGöÇGöÇ uptown/       # Uptown sub-zone
Göé   Göé   GööGöÇGöÇ innsmouth/        # Innsmouth zone
Göé   Göé       Gö£GöÇGöÇ zone_config.json
Göé   Göé       GööGöÇGöÇ waterfront/   # Waterfront sub-zone
Göé   Göé           GööGöÇGöÇ subzone_config.json
Göé   GööGöÇGöÇ yeng/                 # Yeng plane
Göé       GööGöÇGöÇ katmandu/         # Katmandu zone
Göé           Gö£GöÇGöÇ zone_config.json
Göé           GööGöÇGöÇ palance/      # Palance sub-zone
Göé               Gö£GöÇGöÇ subzone_config.json
Göé               GööGöÇGöÇ palance_*.json # Room definitions
Göé
Gö£GöÇGöÇ user_management/           # User management data
Göé   GööGöÇGöÇ [user data files]     # User-specific data
Göé
Gö£GöÇGöÇ emotes.json               # Emote definitions
Gö£GöÇGöÇ motd.html                 # Message of the day
Gö£GöÇGöÇ README.md                 # Data documentation
GööGöÇGöÇ [visualization files]     # Room visualization outputs
```

---

## =ƒ¢án+Å Development Environment for AI Agents

### **Required Tools**

- **uv** (Python package manager) - `uv --version`
- **Node.js/npm** (Frontend) - `node --version`
- **Git** (Version control) - `git --version`

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


## =ƒñû AI Agent DevelopmentRules

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

- **Test-Driven Development**: Write tests before implementing features

- **Security-First**: Every feature must consider security implications
- **Incremental Development**: Small, testable changes with frequent commits
- **Documentation**: Update documentation with each feature completion

### **Task Prioritization Framework**

When multiple tasks are pending, prioritize in this order:

1. **=ƒö¦ Critical Security Issues** (Fix immediately)
   - Security vulnerabilities
   - Privacy compliance issues
   - Data protection problems

2. **=ƒƒí High Priority** (Complete within current session)
   - Core functionality bugs
   - Authentication/authorization issues
   - Critical user experience problems


3. **=ƒƒó Medium Priority** (Plan for next session)
   - Feature enhancements
   - Performance improvements
   - Code quality improvements



4. **=ƒö¦ Low Priority** (Nice to have)
   - UI/UX polish
   - Documentation improvements
   - Advanced features

### **Communication Protocol**


- **Progress Updates**: Update `TASKS.local.md` with progress
- **Blockers**: Document in `TASKS.local.md` and ask for guidance
- **Decisions Needed**: Clearly state the decision needed and options
- **Security Concerns**: Immediately flag any security or privacy concerns

### **Common Pitfalls to Avoid**

- **Never hardcode secrets**: Always use environment variables
- **Never skip tests**: Every feature must have tests
- **Never ignore security warnings**: Address all security concerns immediately
- **Never create database files in wrong locations**: Follow database placement rules
- **Never use bash syntax in PowerShell**: Use PowerShell syntax only

---

## =ƒô¥ AI Agent Coding Guidelines

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

## =ƒº¬ Testing Patterns for AI Agents

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

## =ƒöÆ Security Considerations for AI Agents

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

## =ƒÄ« Game Mechanics for AI Understanding

### **Core Systems**

- **lucidity System**: Players start with 100 lucidity, lose it from encounters
- **Fear System**: Accumulates from terrifying experiences
- **Corruption System**: Represents taint from dark forces
- **Occult Knowledge**: Learning forbidden lore (costs lucidity)

### **Status Effects**

- **Stunned**: Unable to act
- **Poisoned**: Damage over time
- **Hallucinating**: Visual/auditory disturbances
- **Paranoid**: Mental instability
- **Trembling**: Reduced dexterity
- **Corrupted**: Physical/mental changes
- **Delirious**: Complete mental breakdown

### **Room Movement**

- Rooms are connected via exits (north, south, east, west)
- Room IDs follow pattern: `<zone>_<room_number>` (e.g., `arkham_001`)
- Each room has description, exits, and optional NPCs/items

---

## =ƒöä Common AI Agent Tasks

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

## =ƒôÜ AI Agent Best Practices

### **Code Generation**

- **Always include type hints** for Python functions
- **Use descriptive variable names** (avoid single letters)
- **Add docstrings** for complex functions
- **Follow existing patterns** in the codebase
- **Include Mythos references** in comments when appropriate
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

## =ƒÜ¿ Common Pitfalls for AI Agents

### **Avoid These Patterns**

- G¥î **Hardcoded paths** - Use `validate_secure_path()`
- G¥î **Hardcoded secrets** - Use environment variables
- G¥î **Missing type hints** - Always include types
- G¥î **Incomplete error handling** - Handle all error cases
- G¥î **Breaking existing patterns** - Follow established conventions
- G¥î **Forgetting to update GitHub Issues** - Keep issue tracking current
- G¥î **Ignoring security concerns** - Address all security issues immediately
- G¥î **Collecting personal data from minors** - Never collect personal information

### **Security Red Flags**

- G¥î **Direct file path concatenation** without validation
- G¥î **SQL queries with string formatting** (use parameterized queries)
- G¥î **Exposing internal errors** to users
- G¥î **Missing input validation** on user data
- G¥î **Hardcoded secrets** in source code
- G¥î **Personal data collection** without proper consent

---

## =ƒÄ» AI Agent Success Metrics

### **Code Quality**

- G£à All tests pass (minimum 80% coverage)
- G£à No linting errors (`ruff check .`)
- G£à Proper type hints throughout
- G£à Comprehensive error handling
- G£à Security best practices followed
- G£à COPPA compliance verified

### **Documentation**

- G£à GitHub Issues updated with completed work (closed, commented)
- G£à Code comments explain complex logic
- G£à Mythos theming appropriate and consistent
- G£à README files updated if needed
- G£à Security considerations documented

### **Functionality**

- G£à Features work as specified in PLANNING.md
- G£à Edge cases handled properly
- G£à Performance acceptable
- G£à Security vulnerabilities addressed
- G£à Privacy requirements met

---

## =ƒö« Future Considerations for AI Agents

### **Scalability**

- Current SQLite database can be upgraded to PostgreSQL
- JSON room files can be migrated to database
- WebSocket support planned for real-time communication

### **Architecture Evolution**

- Microservices architecture possible for large scale
- Event-driven architecture for game events
- Plugin system for custom game mechanics

### **AI-Specific Enhancements**

- Automated testing generation
- Code quality monitoring
- Performance profiling
- Security scanning integration

---

## =ƒôï Task Tracking with GitHub Issues

### **GitHub Issues Workflow**

All task tracking is now done through [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) instead of local TASKS.md files. This provides better collaboration, tracking, and integration with GitHub's project management features.

#### **Starting a Development Session**

1. **Review open issues** at [https://github.com/arkanwolfshade/MythosMUD/issues](https://github.com/arkanwolfshade/MythosMUD/issues)
2. **Check issue priorities** and dependencies
3. **Select appropriate issues** to work on
4. **Update issue status** as work progresses

#### **During Development**

- **Comment on issues** with progress updates
- **Link commits** to issues using `#issue-number` in commit messages
- **Update issue descriptions** if requirements change
- **Add labels** to categorize work (if available)

#### **Completing Work**

- **Close issues** when work is complete
- **Add completion comments** summarizing what was done
- **Link to relevant commits** or pull requests
- **Update related issues** if dependencies are resolved

#### **Issue Management Best Practices**

- **Use descriptive issue titles** that clearly state the goal
- **Include acceptance criteria** in issue descriptions
- **Add appropriate labels** for categorization
- **Link related issues** using `#issue-number` references
- **Update issue status** regularly during development

---

## =ƒôP AI Agent Communication

### **When to Ask Questions**

- **Unclear requirements** - Ask for clarification
- **Conflicting patterns** - Seek guidance on approach
- **Security concerns** - Flag potential vulnerabilities
- **Performance issues** - Discuss optimization strategies
- **COPPA compliance questions** - Verify privacy requirements

### **How to Provide Updates**

- **Clear progress reports** - What was completed
- **Issue identification** - Problems encountered
- **Solution proposals** - Recommended approaches
- **Next steps** - What comes next
- **Security assessments** - Any security implications

---

## =ƒöÆ Security Checklist for AI Agents

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

*"In the pursuit of forbidden knowledge, even the most advanced artificial intelligences must remember: the greatest wisdom lies not in what we know, but in how we apply that knowledge with care, precision, and respect for the eldritch forces we seek to understand."*

---

**Remember**: You are an AI agent working on a Cthulhu Mythos-themed MUD that serves minors. Maintain the scholarly tone, follow the established patterns, and always prioritize code quality, security, and COPPA compliance. The forbidden knowledge we seek to implement must be both powerful and safe for all users.
 
 
 
 
