# PLANNING: Structlog Implementation for MythosMUD

*"As the Pnakotic Manuscripts teach us, proper categorization of knowledge is essential for its preservation. So too must our logging systems be organized with precision and foresight."*

## Overview

This document outlines the plan for implementing a configurable Structlog-based logging system for the MythosMUD Python server, replacing the current basic logging implementation with a robust, multi-environment, multi-logfile solution.

## Current State Analysis

### Existing Logging Implementation to Remove

1. **Files to be removed/modified:**

   - `server/logging_config.py` - Current basic logging setup
   - `server/uvicorn_logging.ini` - Uvicorn logging configuration
   - Environment variables: `PERSIST_LOG`, `SERVER_LOG`, `LOG_LEVEL`

2. **Code locations using current logging:**

   - `server/main.py` - Server startup/shutdown logging
   - `server/persistence.py` - Database operations logging
   - `server/real_time.py` - MOTD loading errors
   - `server/world_loader.py` - Room loading and world initialization
   - `server/auth/users.py` - User registration and authentication
   - `server/realtime/` modules - WebSocket and SSE communication
   - `server/app/lifespan.py` - Application lifecycle events
   - `server/check_routes.py` - Route debugging

### Current Logging Patterns Identified

Based on codebase analysis, the following logging categories are currently in use:

1. **Server Lifecycle** - Startup, shutdown, configuration loading
2. **Database Operations** - Persistence layer operations, SQL queries
3. **Authentication** - User registration, login attempts, password resets
4. **World Loading** - Room loading, zone configuration, world initialization
5. **Real-time Communication** - WebSocket connections, SSE streams, message handling
6. **Error Handling** - Exception logging, middleware error capture
7. **Command Processing** - Player commands, game mechanics
8. **File Operations** - MOTD loading, configuration file access

## Proposed Logfile Structure

### Environment-Based Logfile Organization

```
logs/
├── production/
│   ├── server.log          # Server lifecycle, startup/shutdown
│   ├── persistence.log     # Database operations, SQL queries
│   ├── authentication.log  # User auth, registration, security events
│   ├── world.log          # Room loading, world initialization
│   ├── communications.log # WebSocket, SSE, real-time messaging
│   ├── commands.log       # Player commands, game mechanics
│   ├── errors.log         # All error-level events
│   └── access.log         # HTTP requests, API access
├── development/
│   ├── server.log
│   ├── persistence.log
│   ├── authentication.log
│   ├── world.log
│   ├── communications.log
│   ├── commands.log
│   ├── errors.log
│   └── access.log
├── staging/
│   └── [same structure as production]
└── test/
    ├── test_server.log
    ├── test_persistence.log
    ├── test_authentication.log
    ├── test_world.log
    ├── test_communications.log
    ├── test_commands.log
    ├── test_errors.log
    └── test_access.log
```

### Logfile Content Categories

1. **server.log**

   - Server startup/shutdown events
   - Configuration loading
   - Health checks
   - Performance metrics

2. **persistence.log**

   - Database connection events
   - SQL query execution
   - Transaction commits/rollbacks
   - Cache operations
   - Data migration events

3. **authentication.log**

   - User registration attempts
   - Login/logout events
   - Password reset requests
   - JWT token generation/validation
   - Security events (failed logins, suspicious activity)

4. **world.log**

   - Room loading events
   - Zone configuration loading
   - World initialization
   - Room cache operations
   - World state changes

5. **communications.log**

   - WebSocket connection events
   - SSE stream creation/destruction
   - Message routing
   - Real-time event broadcasting
   - Connection timeouts

6. **commands.log**

   - Player command execution
   - Game mechanic events
   - Combat actions
   - Inventory operations
   - Player movement

7. **errors.log**

   - All ERROR level events from all loggers
   - Exception stack traces
   - System failures
   - Critical errors

8. **access.log**

   - HTTP request/response logging
   - API endpoint access
   - Rate limiting events
   - Request timing

## Environment Separation Strategy

### Configuration-Based Environment Detection

1. **Environment Detection Logic:**

   ```python
   # Detect environment based on:
   # - pytest running (test environment)
   # - MYTHOSMUD_ENV environment variable
   # - Configuration file loaded (server_config.yaml vs test_server_config.yaml)

   ```

2. **Log Directory Structure:**

   **Production:** `logs/production/`

   **Development:** `logs/development/`
   - **Staging:** `logs/staging/`
   - **Test:** `logs/test/`

3. **Cross-Contamination Prevention:**

   - Environment-specific log directories
   - Separate configuration files per environment
   - Environment variable overrides
   - Automatic log directory creation with proper permissions

### Configuration Schema

```yaml
# server_config.yaml

logging:
  environment: production  # or development, staging, test
  level: INFO
  format: json  # or human, colored
  rotation:
    max_size: 100MB
    backup_count: 5
  compression: true
  logfiles:
    server: logs/production/server.log
    persistence: logs/production/persistence.log
    authentication: logs/production/authentication.log
    world: logs/production/world.log
    communications: logs/production/communications.log
    commands: logs/production/commands.log
    errors: logs/production/errors.log
    access: logs/production/access.log
```

## Implementation Plan

### Phase 1: Remove Current Logging

1. Remove `server/logging_config.py`
2. Remove `server/uvicorn_logging.ini`
3. Remove logging-related environment variables from `server/env.example`
4. Update all imports to use new Structlog-based logging

### Phase 2: Install and Configure Structlog

1. Add Structlog to `server/requirements.txt`
2. Create new `server/logging_config.py` with Structlog configuration
3. Implement environment detection logic
4. Create log directory structure

### Phase 3: Implement Multi-Logfile System

1. Create Structlog processors for different log types
2. Implement log rotation and compression
3. Configure different output formats per environment
4. Set up error aggregation to `errors.log`

### Phase 4: Update All Logging Calls

1. Replace all `get_logger()` calls with Structlog
2. Update logging calls to use structured logging
3. Add context information to log entries
4. Implement proper error logging with stack traces

### Phase 5: Testing and Validation

1. Test all environments (test, development, staging, production)
2. Verify log file separation
3. Test log rotation and compression
4. Validate structured log output
5. Update existing tests to work with new logging

## Technical Implementation Details

### Structlog Configuration

```python
# server/logging_config.py

import structlog
from structlog.stdlib import LoggerFactory
from structlog.processors import JSONRenderer, TimeStamper, add_log_level
from structlog.stdlib import BoundLogger

def configure_structlog(environment: str, log_level: str):
    """Configure Structlog based on environment."""

    # Base processors

    processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        TimeStamper(fmt="iso"),
    ]

    # Environment-specific processors

    if environment == "production":
        processors.append(JSONRenderer())
    else:
        processors.extend([
            structlog.dev.ConsoleRenderer(colors=True),
            structlog.dev.set_exc_info,
        ])

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
```

### Multi-Logfile Handler

```python
class MultiFileHandler:
    """Handler that routes logs to different files based on logger name."""

    def __init__(self, log_config: dict):
        self.log_config = log_config
        self.handlers = {}

    def get_handler(self, logger_name: str):
        """Get appropriate handler based on logger name."""
        # Map logger names to log files

        logger_mapping = {
            "server": "server",
            "persistence": "persistence",
            "auth": "authentication",
            "world": "world",
            "realtime": "communications",
            "commands": "commands",
            "errors": "errors",
            "access": "access"
        }

        # Determine log file based on logger name

        log_file = "server"  # default
        for prefix, file_type in logger_mapping.items():
            if logger_name.startswith(prefix):
                log_file = file_type
                break

        return self._get_or_create_handler(log_file)
```

## Migration Strategy

### Backward Compatibility

1. Maintain existing log message formats during transition
2. Provide migration script for existing log files
3. Keep existing environment variable support temporarily
4. Gradual rollout with feature flags

### Testing Strategy

1. Unit tests for new logging configuration
2. Integration tests for multi-logfile functionality
3. Environment separation tests
4. Performance tests for log rotation
5. Security tests for log file permissions

## Success Criteria

1. **Environment Separation:** No cross-contamination between test/dev/prod logs
2. **Multi-Logfile Support:** All 8 log categories properly separated
3. **Configurable Output:** JSON for production, human-readable for development
4. **Performance:** No significant impact on server performance
5. **Maintainability:** Easy to add new log categories
6. **Security:** Proper file permissions and secure log handling

## Risk Assessment

### Low Risk

Environment separation (well-defined directory structure)

- Log rotation (standard Structlog feature)
- Configuration management (YAML-based)

### Medium Risk

Performance impact of structured logging

- Migration of existing logging calls
- Test environment compatibility

### High Risk

Log file permissions and security

- Cross-platform compatibility (Windows/Linux)
- Integration with existing monitoring systems

## Next Steps

1. **Review this plan** - Ensure all requirements are captured
2. **Approve implementation approach** - Confirm technical decisions
3. **Begin Phase 1** - Remove current logging implementation
4. **Iterate on configuration** - Refine log categories and formats
5. **Implement incrementally** - Phase-by-phase rollout

---

*"The proper organization of eldritch knowledge requires both precision and flexibility. So too must our logging systems adapt to the shifting requirements of our digital realm."*
