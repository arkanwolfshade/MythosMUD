# Spec Requirements Document

> Spec: Player GUID Logging Enhancement
> Created: 2025-09-19

## Overview

Implement a logging formatter that automatically converts player GUIDs to display both player name and GUID in the format "<name>: <GUID>" across all server log files. This enhancement will improve log readability and debugging capabilities by making player identification more intuitive while maintaining the technical precision of GUID tracking.

## User Stories

### Enhanced Log Readability

As a **developer/admin**, I want to see player names alongside GUIDs in log messages, so that I can quickly identify which player is involved in specific events without having to cross-reference GUIDs with player data.

**Detailed Workflow:**
1. When a log message contains a player GUID (UUID format), the logging formatter automatically detects it
2. The formatter looks up the corresponding player name from in-memory player data
3. If found, the GUID is replaced with "<player_name>: <GUID>" format
4. If not found, displays "<UNKNOWN>: <GUID>" and logs the lookup failure to errors.log
5. The enhanced log message is written to the appropriate log file

### Improved Debugging Experience

As a **system administrator**, I want log messages to be more human-readable while preserving technical accuracy, so that I can efficiently troubleshoot player-related issues and monitor system behavior.

**Detailed Workflow:**
1. All existing log files (server.log, world.log, persistence.log, etc.) automatically receive the enhanced formatting
2. Player-related events become immediately identifiable without external lookups
3. Failed GUID lookups are tracked separately for system health monitoring
4. No changes required to existing logging code - enhancement is transparent

## Spec Scope

1. **GUID Detection** - Implement regex pattern matching to identify UUID-format player GUIDs in log messages
2. **Player Lookup** - Create efficient in-memory player name resolution using existing player data structures
3. **Log Formatter Enhancement** - Modify the existing logging formatter to perform GUID-to-name conversion at output time
4. **Error Handling** - Implement fallback display for unresolved GUIDs and separate error logging for lookup failures
5. **Performance Optimization** - Ensure minimal performance impact by leveraging existing in-memory player data

## Out of Scope

- Modifying individual logging statements throughout the codebase
- Creating separate caching mechanisms for player data
- Changing the underlying logging infrastructure (structlog)
- Converting non-player GUIDs (database IDs, session IDs, etc.)
- Real-time log viewing enhancements

## Expected Deliverable

1. **Functional Logging Enhancement** - All log files display player names alongside GUIDs in the format "<name>: <GUID>"
2. **Error Tracking** - Failed GUID lookups are properly logged to errors.log with "<UNKNOWN>: <GUID>" fallback display
3. **Performance Validation** - Logging performance remains within acceptable limits with minimal overhead
