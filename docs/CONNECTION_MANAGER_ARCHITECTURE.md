# ConnectionManager Modular Architecture

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Last Updated**: December 4, 2025
**Status**: ✅ Refactoring Complete

## 2. Overview

**[NOTE]**
The ConnectionManager has been successfully refactored from a monolithic module into a well-structured,
modular system following the Facade design pattern. This document describes the new architecture and how components
interact.

## 3. Architecture Diagram

**[NOTE]**

```
┌─────────────────────────────────────────────────────────────────┐
│                      ConnectionManager                          │
│                          (Facade)                               │
│                                                                 │
│  Core Responsibilities:                                         │
│  • WebSocket lifecycle (connect/disconnect)                     │
│  • Player presence tracking (online_players, last_seen)         │
│  • Connection metadata management                               │
│  • Component coordination & delegation                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ Delegates to:
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────┐            ┌─────────────────┐
│   Monitoring    │            │     Errors      │
├─────────────────┤            ├─────────────────┤
│• PerformanceTracker│         │• ErrorHandler   │
│• StatisticsAggregator│       │                 │
│• HealthMonitor  │            └─────────────────┘
└─────────────────┘
         │                               │
         ▼                               ▼
┌─────────────────┐            ┌─────────────────┐
│  Maintenance    │            │    Messaging    │
├─────────────────┤            ├─────────────────┤
│• ConnectionCleaner│          │• PersonalMessageSender│
│                 │            │• MessageBroadcaster│
└─────────────────┘            └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Integration    │
├─────────────────┤
│• GameStateProvider│
│• RoomEventHandler│
└─────────────────┘
```

## 4. Component Descriptions

**[SPEC]**

### 1. Monitoring (`realtime/monitoring/`)

**Purpose**: Performance tracking, statistics collection, and health monitoring

**Components**:

#### `PerformanceTracker`

Tracks connection establishment times

- Records message delivery times
- Monitors disconnection times
- Provides performance statistics

#### `StatisticsAggregator`

Aggregates stats from multiple sources

- Provides unified reporting interface
- Combines memory, performance, and connection stats

#### `HealthMonitor`

Periodic connection health checks

- JWT token revalidation
- Background health check task management
- Detects unhealthy connections

### 2. Errors (`realtime/errors/`)

**Purpose**: Centralized error handling and recovery

**Components**:

#### `ErrorHandler`

Error state detection

- WebSocket error handling
- Authentication error handling
- Security violation handling
- Automated error recovery

### 3. Maintenance (`realtime/maintenance/`)

**Purpose**: Connection cleanup and data maintenance

**Components**:

#### `ConnectionCleaner`

Stale player pruning

- Orphaned data cleanup
- Ghost player removal
- Dead WebSocket cleanup
- Memory-triggered cleanup coordination

### 4. Messaging (`realtime/messaging/`)

**Purpose**: Message delivery and broadcasting

**Components**:

#### `PersonalMessageSender`

Direct message delivery to individual players

- Payload optimization
- Message queueing for offline players
- Delivery status tracking

#### `MessageBroadcaster`

Room-scoped broadcasting

- Global broadcasting
- Concurrent message delivery optimization
- Player exclusion support

### 5. Integration (`realtime/integration/`)

**Purpose**: External system integration and event handling

**Components**:

#### `GameStateProvider`

Initial game state delivery on connection

- Player data fetching
- NPC data fetching
- Room occupant list generation
- UUID to name conversion

#### `RoomEventHandler`

PlayerEnteredRoom event handling

- PlayerLeftRoom event handling
- EventBus integration
- NATS event publishing
- Room occupant updates

## 5. Component Interaction Patterns

**[NOTE]**

### Connection Flow

```python
# 1. Client connects

await connection_manager.connect_websocket(websocket, player_id, token)

# 2. Health monitoring starts

connection_manager.health_monitor.start_health_checks()

# 3. Initial game state delivered

await connection_manager.game_state_provider.send_initial_game_state(player_id)

# 4. Messages flow through messaging components

await connection_manager.personal_message_sender.send_message(player_id, event)
await connection_manager.message_broadcaster.broadcast_to_room(room_id, event)

# 5. Periodic health checks

connection_manager.health_monitor.check_player_connection_health(player_id)

# 6. Cleanup when needed

await connection_manager.connection_cleaner.prune_stale_players()
```

### Dependency Injection

All components receive their dependencies via constructor:

```python
# Example: ErrorHandler initialization

self.error_handler = ConnectionErrorHandler(
    connection_manager=self  # Callback reference
)

# Example: MessageBroadcaster initialization

self.message_broadcaster = MessageBroadcaster(
    room_manager=self.room_manager,
    send_personal_message_callback=self.send_personal_message
)
```

## 6. Benefits Achieved

**[NOTE]**

### 1. **Improved Maintainability**

Each component is small and single-purpose (vs. the original monolith)

- Changes localized to specific modules
- Clear ownership of responsibilities

### 2. **Better Testability**

Components can be unit tested in isolation

- Mock dependencies easily in tests
- Integration tests focus on component interaction

### 3. **Enhanced Readability**

Clear separation of concerns

- Self-documenting component names
- Easier to navigate codebase

### 4. **Increased Reusability**

Components can be used independently

- Extracted modules reusable in other contexts
- Clear interfaces between components

### 5. **Better Performance Profiling**

Easy to identify bottlenecks in specific components

- Targeted optimization opportunities
- Clear performance metrics per component

## 7. Design Patterns Applied

**[NOTE]**

### Facade Pattern

ConnectionManager coordinates components

- Provides unified interface to clients
- Delegates to specialized components

### Dependency Injection

Components receive dependencies via constructor

- No hard-coded dependencies
- Easy to mock for testing

### Single Responsibility Principle

Each component has one reason to change

- Clear, focused responsibilities
- No mixed concerns

### Strategy Pattern

Different strategies for error handling

- Pluggable message delivery mechanisms
- Flexible component implementations

## 8. Migration Notes

**[NOTE]**

### API Compatibility

Public API remains unchanged

- Existing callers require no modifications
- Internal delegation transparent to clients

### Testing Updates

Some tests updated to reflect new architecture

- Mock strategies adjusted for component delegation
- Test suite kept passing throughout the refactoring

### Performance Impact

No measurable performance degradation

- Some improvements due to better separation
- Memory usage unchanged

## 9. Future Opportunities

**[SPEC]**
While significant improvements were achieved, additional refinement could include:

1. **Session Management Module**: If session logic expands beyond current scope
2. **Presence Tracking Module**: If presence features grow more complex
3. **WebSocket Lifecycle Module**: If connection patterns become more sophisticated
4. **Additional Monitoring**: More granular performance metrics per component

## 10. References

**[SPEC]**
**Refactoring Summary**: `archive/REFACTORING_SUMMARY.md`

**Original Plan**: `.cursor/plans/connection-manager-refactor_b94299a2.plan.md`

**Real-Time Architecture**: `REAL_TIME_ARCHITECTURE.md`

**Python Best Practices**: `.cursor/rules/python.mdc`

## 11. Metrics

**[SPEC]**
**Original Size**: a single monolithic module

**Current Size**: a thin facade delegating to the modules below. Line counts are deliberately not recorded here — they rot on every commit; measure the file directly.

**Components**: 7 specialized modules

- **Refactoring Duration**: December 4, 2025

## 12. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Remove hard-coded line counts and point-in-time CI metrics (#722) |
