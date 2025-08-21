# 🤖 MythosMUD – AI Agent Development Guide

*"In the vast archives of Miskatonic University, even the most advanced artificial intelligences must learn to navigate the forbidden knowledge with care and precision."*

This guide is specifically crafted for AI agents (Claude Code, Cursor, GitHub Copilot, Gemini, etc.) working on the MythosMUD project. It provides the context, patterns, and guidelines needed to assist effectively in this Cthulhu Mythos-themed MUD development.

---

## 🎯 AI Agent Context & Personality

### **Project Character**

- **Theme**: Cthulhu Mythos-themed MUD (Multi-User Dungeon)
- **Tone**: Academic/scholarly with Mythos flavor
- **Setting**: Miskatonic University and surrounding Arkham area
- **Atmosphere**: Gothic horror, forbidden knowledge, eldritch mysteries
- **Target Users**: Professor Wolfshade and teenage son (COPPA compliance critical)

---

## 🔒 CRITICAL SECURITY & PRIVACY REQUIREMENTS

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

---

## 📋 Essential Reading for AI Agents

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

## 🏗️ Project Architecture for AI Understanding

### **Backend (Python/FastAPI)**

```
server/
├── main.py                    # FastAPI app entry point
├── models.py                  # Pydantic data models
├── persistence.py             # Database abstraction (PersistenceLayer)
├── database.py                # Database connection management
├── config_loader.py           # Configuration management
├── logging_config.py          # Structured logging setup
├── security_utils.py          # Path validation & security
├── auth_utils.py              # JWT & password utilities
├── world_loader.py            # Room/world data loading
├── server_config.yaml         # Server configuration
├── env.example                # Environment variables template
├── pytest.ini                # Test configuration
├── pyproject.toml            # Python dependencies
├── uv.lock                   # Dependency lock file
│
├── auth/                      # Authentication system
│   ├── __init__.py
│   ├── endpoints.py           # Auth API endpoints
│   ├── users.py               # User management
│   ├── invites.py             # Invite system
│   ├── argon2_utils.py        # Argon2 password hashing
│   ├── email_utils.py         # Email utilities
│   └── dependencies.py        # Auth dependencies
│
├── api/                       # API endpoints
│   ├── __init__.py
│   ├── base.py                # Base API configuration
│   ├── game.py                # Game API endpoints
│   ├── players.py             # Player management API
│   ├── rooms.py               # Room API endpoints
│   ├── real_time.py           # Real-time API
│   └── monitoring.py          # System monitoring API
│
├── game/                      # Game logic services
│   ├── __init__.py
│   ├── chat_service.py        # Chat system (NATS-based)
│   ├── movement_service.py    # Player movement logic
│   ├── movement_monitor.py    # Movement monitoring
│   ├── room_service.py        # Room management
│   ├── player_service.py      # Player state management
│   ├── stats_generator.py     # Character stats generation
│   ├── emote_service.py       # Emote system
│   └── mechanics.py           # Game mechanics
│
├── realtime/                  # Real-time communication
│   ├── __init__.py
│   ├── connection_manager.py  # WebSocket connection management
│   ├── websocket_handler.py   # WebSocket message handling
│   ├── sse_handler.py         # Server-Sent Events
│   ├── event_handler.py       # Event processing
│   ├── nats_message_handler.py # NATS message handling
│   ├── request_context.py     # Request context for WebSocket
│   └── envelope.py            # Message envelope utilities
│
├── commands/                  # Command processing
│   ├── __init__.py
│   ├── admin_commands.py      # Admin commands
│   ├── alias_commands.py      # Alias system commands
│   ├── chat_commands.py       # Chat commands
│   ├── help_commands.py       # Help system
│   ├── movement_commands.py   # Movement commands
│   └── stats_commands.py      # Stats commands
│
├── models/                    # Data models
│   ├── __init__.py
│   ├── player.py              # Player model
│   ├── room.py                # Room model
│   ├── command.py             # Command model
│   ├── chat.py                # Chat model
│   ├── alias.py               # Alias model
│   ├── invite.py              # Invite model
│   └── user.py                # User model
│
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── nats_service.py        # NATS messaging service
│   ├── chat_logger.py         # Chat logging service
│   └── monitoring_service.py  # System monitoring
│
├── utils/                     # Utility modules
│   ├── __init__.py
│   ├── command_parser.py      # Command parsing utilities
│   └── command_processor.py   # Command processing utilities
│
├── validators/                # Input validation
│   ├── __init__.py
│   ├── command_validator.py   # Command validation
│   └── security_validator.py  # Security validation
│
├── middleware/                # Request middleware
│   ├── __init__.py
│   └── request_logging.py     # Request logging middleware
│
├── schemas/                   # JSON schemas
│   ├── __init__.py
│   ├── player.py              # Player schemas
│   └── invite.py              # Invite schemas
│
├── sql/                       # Database schema
│   └── schema.sql             # SQLite schema definition
│
├── help/                      # Help system
│   ├── __init__.py
│   └── help_content.py        # Help content and documentation
│
├── events/                    # Event system
│   ├── __init__.py
│   ├── event_bus.py           # Event bus implementation
│   └── event_types.py         # Event type definitions
│
├── app/                       # Application factory
│   ├── __init__.py
│   ├── factory.py             # FastAPI app factory
│   └── lifespan.py            # Application lifecycle
│
├── logs/                      # Log files directory
├── data/                      # Data files
│
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── conftest.py            # Test configuration
│   ├── data/                  # Test data
│   │   └── players/           # Test player database
│   └── [test_*.py]            # Test modules
│
├── command_handler_unified.py # Unified command handler (replaces all previous versions)
├── alias_storage.py           # Alias storage system
├── error_handlers.py          # Error handling
├── error_types.py             # Error type definitions
├── exceptions.py              # Custom exceptions
├── real_time.py               # Real-time utilities
├── check_invites.py           # Invite validation
├── check_routes.py            # Route validation
├── test_integration.py        # Integration testing
├── metadata.py                # Package metadata
├── player_manager.py          # Player manager (legacy)
├── TEST_PROD_SEPARATION.md    # Test/prod separation guide
└── README.md                  # Server documentation
```

### **Frontend (React/TypeScript)**

```
client/
├── src/
│   ├── App.tsx                # Main React component
│   ├── main.tsx               # React entry point
│   ├── index.css              # Global styles
│   ├── App.css                # App-specific styles
│   ├── vite-env.d.ts          # Vite type definitions
│   │
│   ├── components/            # React components
│   │   ├── GameTerminal.tsx   # Main game terminal
│   │   ├── GameTerminal.css   # Terminal styles
│   │   ├── GameTerminalWithPanels.tsx # Terminal with panels
│   │   ├── GameTerminalWithPanels.css # Panel styles
│   │   ├── DraggablePanel.tsx # Draggable panel component
│   │   ├── PanelManager.tsx   # Panel management
│   │   ├── StatsRollingScreen.tsx # Character creation screen
│   │   ├── StatsRollingScreen.css # Stats screen styles
│   │   ├── RoomInfoPanel.tsx  # Room information display
│   │   ├── RoomInfoPanel.css  # Room panel styles
│   │   ├── MotdContent.tsx    # Message of the day
│   │   ├── CommandHelpDrawer.tsx # Help system
│   │   ├── TailwindTest.tsx   # TailwindCSS test component
│   │   ├── EldritchEffectsDemo.tsx # Visual effects demo
│   │   │
│   │   ├── panels/            # Panel components
│   │   │   ├── ChatPanel.tsx  # Chat interface
│   │   │   ├── CommandPanel.tsx # Command input
│   │   │   ├── ConnectionPanel.tsx # Connection status
│   │   │   ├── PlayerPanel.tsx # Player information
│   │   │   └── RoomPanel.tsx  # Room information
│   │   │
│   │   ├── ui/                # UI components
│   │   │   ├── MythosPanel.tsx # Mythos-themed panel
│   │   │   ├── MythosPanel.test.tsx # Panel tests
│   │   │   ├── EldritchIcon.tsx # Mythos icons
│   │   │   └── [other UI components]
│   │   │
│   │   └── [test components]  # Test components
│   │
│   ├── hooks/                 # React hooks
│   │   ├── useGameConnection.ts # Game connection hook
│   │   └── useGameConnection.test.ts # Connection hook tests
│   │
│   ├── utils/                 # Utility functions
│   │   ├── ansiToHtml.ts      # ANSI to HTML conversion
│   │   ├── ansiToHtml.test.ts # Conversion tests
│   │   ├── errorHandler.ts    # Error handling utilities
│   │   ├── errorHandler.test.ts # Error handler tests
│   │   ├── logger.ts          # Client-side logging
│   │   └── [other utilities]
│   │
│   ├── theme/                 # Theming system
│   │   └── mythosTheme.ts     # Mythos theme configuration
│   │
│   ├── styles/                # Style files
│   │   └── motd-preserved.css # MOTD preservation styles
│   │
│   ├── test/                  # Test utilities
│   │   └── setup.ts           # Test setup configuration
│   │
│   └── assets/                # Static assets
│       └── react.svg          # React logo
│
├── public/                    # Public assets
│   └── vite.svg               # Vite logo
│
├── tests/                     # End-to-end tests
│   ├── help-command.spec.ts   # Help command tests
│   ├── occupants-initial.spec.ts # Initial occupant tests
│   └── occupants-two-client.spec.ts # Multi-client tests
│
├── package.json               # Dependencies and scripts
├── package-lock.json          # Dependency lock file
├── tsconfig.json              # TypeScript configuration
├── tsconfig.app.json          # App-specific TS config
├── tsconfig.node.json         # Node-specific TS config
├── vite.config.ts             # Vite build configuration
├── vite.config.d.ts           # Vite type definitions
├── vitest.config.ts           # Vitest test configuration
├── tailwind.config.js         # TailwindCSS configuration
├── postcss.config.js          # PostCSS configuration
├── eslint.config.js           # ESLint configuration
├── playwright.config.ts       # Playwright test configuration
├── test-results/              # Test results directory
├── playwright-report/         # Playwright reports
└── tsconfig.tsbuildinfo       # TypeScript build info
```

### **Data Structure**

```
data/
├── players/                   # Player database and data
│   ├── players.db            # SQLite player database
│   ├── aliases/              # Player alias files
│   │   └── [player]_aliases.json # Individual player aliases
│   └── [backup files]        # Database backups with timestamps
│
├── rooms/                     # World data (git submodule)
│   ├── earth/                # Earth plane
│   │   ├── arkham_city/      # Arkham City zone
│   │   │   ├── zone_config.json # Zone configuration
│   │   │   ├── campus/       # Campus sub-zone
│   │   │   │   ├── subzone_config.json # Sub-zone config
│   │   │   │   ├── intersection_*.json # Intersection definitions
│   │   │   │   └── room_*.json # Room definitions
│   │   │   ├── downtown/     # Downtown sub-zone
│   │   │   │   ├── subzone_config.json
│   │   │   │   ├── intersection_*.json
│   │   │   │   └── room_*.json
│   │   │   ├── east_town/    # East Town sub-zone
│   │   │   ├── french_hill/  # French Hill sub-zone
│   │   │   ├── lower_southside/ # Lower Southside sub-zone
│   │   │   ├── merchant/     # Merchant sub-zone
│   │   │   ├── northside/    # Northside sub-zone
│   │   │   ├── river_town/   # River Town sub-zone
│   │   │   ├── sanitarium/   # Sanitarium sub-zone
│   │   │   └── uptown/       # Uptown sub-zone
│   │   └── innsmouth/        # Innsmouth zone
│   │       ├── zone_config.json
│   │       └── waterfront/   # Waterfront sub-zone
│   │           └── subzone_config.json
│   └── yeng/                 # Yeng plane
│       └── katmandu/         # Katmandu zone
│           ├── zone_config.json
│           └── palance/      # Palance sub-zone
│               ├── subzone_config.json
│               └── palance_*.json # Room definitions
│
├── user_management/           # User management data
│   └── [user data files]     # User-specific data
│
├── emotes.json               # Emote definitions
├── motd.html                 # Message of the day
├── README.md                 # Data documentation
└── [visualization files]     # Room visualization outputs
```

---

## 🛠️ Development Environment for AI Agents

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
./scripts/start_dev.ps1

# Run tests
cd server && uv run pytest tests/ -v

# Lint code
cd server && uv run ruff check .

# Format code
cd server && uv run ruff format .
```


---


## 🤖 AI Agent DevelopmentRules

### **Development Environment Rules**

**CRITICAL**: Always follo these rules when working on this project:

1. **Server Startup**: ALWAYS use `./scripts/start_dev.ps1` from project root
2. **Server Shutdown**: ALWAYS use `./scripts/stop_server.ps1` before starting

3. **Database Placement**:
   - Production: `/data/players/` ONLY
   - Tests: `/server/tests/data/players/` ONLY
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

1. **🔴 Critical Security Issues** (Fix immediately)
   - Security vulnerabilities
   - Privacy compliance issues
   - Data protection problems

2. **🟡 High Priority** (Complete within current session)
   - Core functionality bugs
   - Authentication/authorization issues
   - Critical user experience problems


3. **🟢 Medium Priority** (Plan for next session)
   - Feature enhancements
   - Performance improvements
   - Code quality improvements



4. **🔵 Low Priority** (Nice to have)
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

## 📝 AI Agent Coding Guidelines

### **Code Style & Patterns**

#### **Python (Backend)**

```python
# Use type hints consistently
def calculate_sanity_loss(player_id: str, exposure_time: int) -> int:
    """Calculate sanity loss based on exposure time and player state."""
    # Implementation here
    pass

# Use Pydantic models for data validation
class PlayerStats(BaseModel):
    sanity: int = Field(ge=0, le=100, description="Player sanity level")
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
  sanity: number;
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
# Implementing player sanity system based on findings from
# "Psychological Effects of Non-Euclidean Architecture" - Dr. Armitage, 1928
def calculate_sanity_loss(exposure_time: int, entity_type: str) -> int:
    """Calculate sanity loss from exposure to eldritch entities."""
    pass

# As noted in the Pnakotic Manuscripts, the mind cannot comprehend
# certain geometries without suffering permanent damage
def apply_non_euclidean_effect(player_id: str) -> None:
    """Apply non-Euclidean geometry effects to player perception."""
    pass
```

---

## 🧪 Testing Patterns for AI Agents

### **Test Structure**

```python
# Use descriptive test names
def test_player_sanity_loss_from_eldritch_exposure():
    """Test that exposure to eldritch entities reduces sanity."""
    # Arrange
    player = create_test_player(sanity=100)

    # Act
    apply_sanity_loss(player.id, 25)

    # Assert
    assert player.sanity == 75

# Use fixtures for common setup
@pytest.fixture
def mock_persistence_layer(monkeypatch):
    """Mock the persistence layer for isolated testing."""
    mock_layer = MockPersistenceLayer()
    monkeypatch.setattr("server.persistence.PersistenceLayer.get_instance", lambda: mock_layer)
    return mock_layer

# Test edge cases
def test_sanity_cannot_go_below_zero():
    """Test that sanity loss cannot reduce sanity below zero."""
    player = create_test_player(sanity=10)
    apply_sanity_loss(player.id, 25)
    assert player.sanity == 0  # Should not go below zero
```

### **Mock Data Patterns**

```python
# Use realistic mock data
MOCK_PLAYER = {
    "id": "test-player-001",
    "name": "Dr. Henry Armitage",
    "sanity": 85,
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

## 🔒 Security Considerations for AI Agents

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

## 🎮 Game Mechanics for AI Understanding

### **Core Systems**

- **Sanity System**: Players start with 100 sanity, lose it from encounters
- **Fear System**: Accumulates from terrifying experiences
- **Corruption System**: Represents taint from dark forces
- **Occult Knowledge**: Learning forbidden lore (costs sanity)

### **Status Effects**

- **Stunned**: Unable to act
- **Poisoned**: Damage over time
- **Hallucinating**: Visual/auditory disturbances
- **Paranoid**: Mental instability
- **Trembling**: Reduced dexterity
- **Corrupted**: Physical/mental changes
- **Insane**: Complete mental breakdown

### **Room Movement**

- Rooms are connected via exits (north, south, east, west)
- Room IDs follow pattern: `<zone>_<room_number>` (e.g., `arkham_001`)
- Each room has description, exits, and optional NPCs/items

---

## 🔄 Common AI Agent Tasks

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

## 📚 AI Agent Best Practices

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
logger.info("Player sanity reduced", extra={
    "player_id": player_id,
    "sanity_loss": amount,
    "new_sanity": player.sanity
})
```

### **Configuration Management**

```python
# Use environment variables for configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/players/players.db")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
COPPA_ENFORCED = os.getenv("COPPA_ENFORCED", "true").lower() == "true"
```

---

## 🚨 Common Pitfalls for AI Agents

### **Avoid These Patterns**

- ❌ **Hardcoded paths** - Use `validate_secure_path()`
- ❌ **Hardcoded secrets** - Use environment variables
- ❌ **Missing type hints** - Always include types
- ❌ **Incomplete error handling** - Handle all error cases
- ❌ **Breaking existing patterns** - Follow established conventions
- ❌ **Forgetting to update GitHub Issues** - Keep issue tracking current
- ❌ **Ignoring security concerns** - Address all security issues immediately
- ❌ **Collecting personal data from minors** - Never collect personal information

### **Security Red Flags**

- ❌ **Direct file path concatenation** without validation
- ❌ **SQL queries with string formatting** (use parameterized queries)
- ❌ **Exposing internal errors** to users
- ❌ **Missing input validation** on user data
- ❌ **Hardcoded secrets** in source code
- ❌ **Personal data collection** without proper consent

---

## 🎯 AI Agent Success Metrics

### **Code Quality**

- ✅ All tests pass (minimum 80% coverage)
- ✅ No linting errors (`ruff check .`)
- ✅ Proper type hints throughout
- ✅ Comprehensive error handling
- ✅ Security best practices followed
- ✅ COPPA compliance verified

### **Documentation**

- ✅ GitHub Issues updated with completed work (closed, commented)
- ✅ Code comments explain complex logic
- ✅ Mythos theming appropriate and consistent
- ✅ README files updated if needed
- ✅ Security considerations documented

### **Functionality**

- ✅ Features work as specified in PLANNING.md
- ✅ Edge cases handled properly
- ✅ Performance acceptable
- ✅ Security vulnerabilities addressed
- ✅ Privacy requirements met

---

## 🔮 Future Considerations for AI Agents

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

## 📋 Task Tracking with GitHub Issues

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

## 📞 AI Agent Communication

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

## 🔒 Security Checklist for AI Agents

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
