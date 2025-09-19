# MythosMUD E2E Test Suite - Modular Structure

## Overview

This directory contains the modular E2E test suite for MythosMUD, refactored from the monolithic `MULTIPLAYER_SCENARIOS_PLAYBOOK.md` into a structured, maintainable format. The modular approach reduces AI context requirements, enables selective scenario execution, and provides the most appropriate testing tool for each scenario's complexity level.

## Directory Structure

```
e2e-tests/
├── README.md                           # This file - overview and navigation
├── MULTIPLAYER_TEST_RULES.md          # Master rules and common procedures (11.5 KB)
├── CLEANUP.md                         # Post-scenario cleanup procedures (5.7 KB)
├── TROUBLESHOOTING.md                 # Error handling and debugging guide (10.8 KB)
├── TESTING_APPROACH.md                # Testing methodology documentation (7.3 KB)
├── EXECUTION_PROTOCOL_CHANGES.md      # Documentation of changes made (8.2 KB)
└── scenarios/                         # Individual scenario files (21 files)
    ├── scenario-01-basic-connection.md           # Basic connection/disconnection (11.3 KB)
    ├── scenario-02-clean-game-state.md           # Clean game state on connection (7.6 KB)
    ├── scenario-03-movement-between-rooms.md     # Movement between rooms (8.4 KB)
    ├── scenario-04-muting-system-emotes.md       # Muting system and emotes (9.7 KB)
    ├── scenario-05-chat-messages.md              # Basic chat communication (8.5 KB)
    ├── scenario-06-admin-teleportation.md        # Admin teleportation (10.1 KB)
    ├── scenario-07-who-command.md                # Player listing and filtering (10.6 KB)
    ├── scenario-08-local-channel-basic.md        # Basic local channel communication (10.8 KB)
    ├── scenario-09-local-channel-isolation.md    # Local message isolation (12.7 KB)
    ├── scenario-10-local-channel-movement.md     # Local channel movement routing (13.5 KB)
    ├── scenario-11-local-channel-errors.md       # Local channel error handling (14.1 KB)
    ├── scenario-12-local-channel-integration.md  # Local channel system integration (17.5 KB)
    ├── scenario-13-whisper-basic.md              # Basic whisper functionality (12.8 KB)
    ├── scenario-14-whisper-errors.md             # Whisper error handling (15.3 KB)
    ├── scenario-15-whisper-rate-limiting.md      # Whisper spam prevention (14.8 KB)
    ├── scenario-16-whisper-movement.md           # Whisper across player locations (16.8 KB)
    ├── scenario-17-whisper-integration.md        # Whisper system integration (19.1 KB)
    ├── scenario-18-whisper-logging.md            # Whisper privacy and moderation (16.0 KB)
    ├── scenario-19-logout-button.md              # Basic logout functionality (12.8 KB)
    ├── scenario-20-logout-errors.md              # Logout error handling (14.8 KB)
    └── scenario-21-logout-accessibility.md       # Logout accessibility features (15.4 KB)
```

## File Descriptions

### Master Documentation Files

- **`MULTIPLAYER_TEST_RULES.md`** - Master rules file containing:
  - Critical AI executor requirements
  - Mandatory execution order and protocols
  - Test configuration and player credentials
  - Server management procedures
  - Safety checks and prerequisites
  - Performance optimization settings

- **`CLEANUP.md`** - Post-scenario cleanup procedures:
  - Browser tab management
  - Server shutdown procedures
  - Clean state verification
  - Error recovery steps

- **`TROUBLESHOOTING.md`** - Comprehensive error handling guide:
  - Common issues and solutions
  - Server startup problems
  - Connection issues
  - Database state problems
  - Low-performance machine optimizations
  - Debugging commands and procedures

- **`TESTING_APPROACH.md`** - Testing methodology documentation:
  - Playwright MCP vs standard Playwright analysis
  - Scenario-by-scenario testing approach rationale
  - Hybrid approach considerations
  - Future testing enhancements
  - Implementation guidelines

- **`EXECUTION_PROTOCOL_CHANGES.md`** - Documentation of refactoring changes:
  - File structure changes
  - Execution protocol changes
  - Cursor rule updates
  - Backward compatibility analysis
  - Performance improvements

### Individual Scenario Files

Each scenario file follows a standardized structure:

1. **Prerequisites** - Database state, server status, player connections, room configuration
2. **Test Configuration** - Players, starting room, testing approach, timeouts
3. **Testing Approach Rationale** - Why Playwright MCP is required
4. **Execution Steps** - Detailed step-by-step instructions
5. **Expected Results** - Clear success criteria and expected behavior
6. **Success Criteria Checklist** - Comprehensive validation points

## Usage Instructions

### Option 1: Execute All Scenarios (Legacy Compatibility)
```bash
# Follow master rules and execute all 21 scenarios in order
1. Read e2e-tests/MULTIPLAYER_TEST_RULES.md for master rules
2. Execute all scenarios from e2e-tests/scenarios/ in order
3. Follow cleanup procedures in e2e-tests/CLEANUP.md
```

### Option 2: Execute Individual Scenario
```bash
# Execute a specific scenario
1. Read e2e-tests/MULTIPLAYER_TEST_RULES.md for master rules
2. Execute the specific scenario from e2e-tests/scenarios/
3. Follow cleanup procedures in e2e-tests/CLEANUP.md
```

### Option 3: Execute Scenario Group
```bash
# Execute related scenarios
1. Read e2e-tests/MULTIPLAYER_TEST_RULES.md for master rules
2. Execute the specific scenarios from e2e-tests/scenarios/
3. Follow cleanup procedures in e2e-tests/CLEANUP.md
```

### Option 4: Use Original Playbook (Backward Compatibility)
```bash
# Use the original monolithic playbook
Execute MULTIPLAYER_SCENARIOS_PLAYBOOK.md (preserved unchanged)
```

## Testing Approach

**All scenarios use Playwright MCP** for the following reasons:
- **Multi-tab Coordination**: All scenarios require 2+ browser tabs for multiplayer testing
- **Real-time Interaction**: All scenarios involve real-time message broadcasting and state synchronization
- **Complex User Flows**: All scenarios require complex multiplayer interaction patterns
- **State Management**: All scenarios need to verify state consistency across multiple players
- **Message Broadcasting**: All scenarios test message delivery between players

## Key Benefits

### Modular Structure Benefits
- **Reduced AI Context Load**: Individual files fit within AI context limits
- **Selective Execution**: Can execute specific scenarios for targeted testing
- **Parallel Development**: Multiple scenarios can be developed simultaneously
- **Easier Maintenance**: Individual files are easier to maintain and update
- **Better Documentation**: Each scenario is self-documenting

### Backward Compatibility
- **Original Playbook Preserved**: `MULTIPLAYER_SCENARIOS_PLAYBOOK.md` remains unchanged
- **All Scenarios Preserved**: All 21 scenarios preserved in individual files
- **All Procedures Preserved**: All execution procedures preserved
- **All Safety Checks Preserved**: All safety checks preserved
- **No Breaking Changes**: No existing workflows are broken

## File Size Analysis

**Total Size**: ~280 KB (compared to original 2,901 lines in single file)
**Largest File**: `scenario-17-whisper-integration.md` (19.1 KB)
**Smallest File**: `scenario-02-clean-game-state.md` (7.6 KB)
**Average File Size**: ~13.3 KB per scenario
**AI Context Friendly**: All files are well within AI context limits

## Quick Navigation

### By Category
- **Connection & State**: scenarios 1-2
- **Movement & Communication**: scenarios 3-5
- **Admin & Commands**: scenarios 6-7
- **Local Channel**: scenarios 8-12
- **Whisper Channel**: scenarios 13-18
- **Logout Button**: scenarios 19-21

### By Complexity
- **Low-Medium**: scenarios 1-2, 4-5, 7, 19
- **Medium**: scenarios 3, 6, 8, 13, 16, 20
- **Medium-High**: scenarios 9-10, 14-15, 18, 21
- **High**: scenarios 11-12, 17

## Support and Maintenance

- **Master Rules**: Always reference `MULTIPLAYER_TEST_RULES.md` for common procedures
- **Cleanup**: Always follow `CLEANUP.md` procedures after scenario execution
- **Troubleshooting**: Use `TROUBLESHOOTING.md` for error resolution
- **Testing Approach**: See `TESTING_APPROACH.md` for methodology details
- **Changes**: See `EXECUTION_PROTOCOL_CHANGES.md` for refactoring documentation

---

**Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Total Scenarios**: 21
**Testing Approach**: Playwright MCP (All Scenarios)
**Backward Compatibility**: 100% maintained
**File Structure**: Modular and maintainable
