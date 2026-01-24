# WebSocket Code Review - Branch: feature/sqlite-to-postgresql

> ⚠️ **DEPRECATION NOTICE** (December 4, 2025)
>
> This code review references the original monolithic ConnectionManager (3,653 lines).
> The ConnectionManager has since been refactored into a modular architecture (35% reduction).
> Many issues identified below may have been resolved by the refactoring.
>
> **See**: `CONNECTION_MANAGER_ARCHITECTURE.md` for current architecture
> **See**: `REFACTORING_SUMMARY.md` for refactoring details

**Review Date**: 2025-01-XX
**Reviewer**: AI Code Review Agent
**Scope**: WebSocket implementation changes vs. `main` branch
**Reference**: `.cursor/rules/websocket.mdc` best practices
**Status**: ⚠️ OUTDATED - ConnectionManager refactored December 2025

## Executive Summary

This review examines WebSocket-related code changes in the `feature/sqlite-to-postgresql` branch against WebSocket best
practices. Overall, the codebase demonstrates good architectural patterns with dependency injection and modular design.
However, several anti-patterns and potential issues were identified that should be addressed.

**Note**: Line numbers and specific code references below are now outdated due to the December 2025 refactoring.

## ✅ Positive Findings

### 1. **Dependency Injection Pattern**

✅ ConnectionManager is injected rather than using global singletons

✅ Event handlers receive dependencies via constructor

✅ No global WebSocket instances found

### 2. **Modern Async Patterns**

✅ Uses `asyncio.get_running_loop()` instead of deprecated `get_event_loop()`

✅ Proper async/await usage throughout

✅ Task tracking for memory leak prevention

### 3. **Error Boundaries**

✅ Circuit breaker pattern implemented in NATSMessageHandler

✅ Dead letter queue for failed messages

✅ Retry logic with exponential backoff

### 4. **Security**

✅ Input sanitization on client side (`inputSanitizer.sanitizeCommand`)

✅ Message validation in NATS handler (`validate_message`)

✅ CSRF token structure in place (validation TODO noted)

## 🔴 Critical Issues

### 1. **Event Loop Anti-Pattern in Connection Manager**

**Location**: `server/realtime/connection_manager.py:1152-1162`

**Issue**: The code attempts to handle event loop edge cases but may skip critical disconnect processing:

```python
except RuntimeError:
    # No running loop - log warning and skip to avoid nested event loop errors
    # asyncio.run() cannot be called from within a running event loop

    logger.warning(
        "No event loop available for disconnect processing",
        player_id=player_id,
    )
    # Skip disconnect processing when no event loop is available
    # This is safe because force_disconnect already cleaned up the connection

```

**Problem**: Skipping disconnect processing can lead to:

- Memory leaks (connections not properly cleaned up)
- Stale connection references
- Inconsistent state between connection tracking and actual connections

**Recommendation**: Use `asyncio.create_task()` or ensure the disconnect handler is always called from an async context.
If truly no loop exists, use a background thread with proper synchronization.

**Severity**: HIGH - Can cause memory leaks and connection state inconsistencies

---

### 2. **Missing Input Validation on Server Side**

**Location**: `server/realtime/websocket_handler.py:342-356`

**Issue**: Server receives and parses JSON without comprehensive validation:

```python
data = await websocket.receive_text()
message = json.loads(data)

# CRITICAL FIX: Handle wrapped message format from useWebSocketConnection

if "message" in message and isinstance(message["message"], str):
    try:
        inner_message = json.loads(message["message"])
        # Verify CSRF token if present
        # TODO: Implement CSRF validation

        message = inner_message
    except json.JSONDecodeError:
        pass
```

**Problems**:

- No size limit on incoming messages (DoS risk)
- No schema validation before processing
- CSRF validation is TODO (security gap)
- Nested JSON parsing without depth limits

**Recommendation**:

1. Add message size limits (e.g., 10KB max)
2. Implement Pydantic schema validation
3. Add JSON depth limits
4. Implement CSRF token validation
5. Add rate limiting per connection

**Severity**: HIGH - Security and DoS vulnerability

---

### 3. **Synchronous Blocking Operations in Async Context**

**Location**: `server/realtime/nats_message_handler.py:602-621`

**Issue**: Batch loading mute data is async, but individual mute checks may block:

```python
# Use async batch loading to prevent blocking the event loop

load_results = await user_manager.load_player_mutes_batch(receiver_ids)
```

**Problem**: While batch loading is async, the subsequent mute checks in the loop
(`_is_player_muted_by_receiver_with_user_manager`) may still perform synchronous I/O operations that block the event
loop.

**Recommendation**: Audit all mute checking methods to ensure they're fully async and don't perform blocking I/O. Use
async database queries throughout.

**Severity**: MEDIUM - Performance degradation under load

---

### 4. **Large Payload Risk in Room Updates**

**Location**: `server/realtime/websocket_handler.py:230-241`, `server/realtime/event_handler.py:175-196`

**Issue**: Room update events can contain large amounts of data:

```python
game_state_event = build_event(
    "game_state",
    {
        "player": player_data_for_client,
        "room": room_data,  # Can be large with full room details
        "occupants": occupant_names,
        "occupant_count": len(occupant_names),
    },
    player_id=player_id_str,
    room_id=str(canonical_room_id),
)
```

**Problem**:

- No payload size limits
- Full room data sent on every connection
- No compression for large payloads
- Can cause network congestion with many players

**Recommendation**:

1. Implement payload size limits and monitoring
2. Use incremental updates instead of full state dumps
3. Consider compression for large payloads
4. Paginate room occupants if list is large

**Severity**: MEDIUM - Performance and scalability concern

---

## 🟡 Anti-Patterns and Code Smells

### 5. **Complex Event Handlers**

**Location**: `server/realtime/event_handler.py:90-234` (`_handle_player_entered`)

**Issue**: The `_handle_player_entered` method is 144 lines and performs multiple responsibilities:

- Event processing
- Player lookup
- Room occupant updates
- Multiple message broadcasts
- Error handling

**Problem**: Violates single responsibility principle, making testing and maintenance difficult.

**Recommendation**: Break into smaller, focused methods:

- `_process_player_entered_event()`
- `_send_room_occupants_update()`
- `_send_initial_room_state()`
- `_broadcast_player_entered()`

**Severity**: LOW - Code maintainability

---

### 6. **Tight Coupling Between Components**

**Location**: `server/realtime/websocket_handler.py:441-445`

**Issue**: Direct access to app state through connection manager:

```python
from ..main import app
connection_manager = app.state.container.connection_manager
```

**Problem**: Creates tight coupling between WebSocket handler and application structure, making testing difficult.

**Recommendation**: Pass connection_manager as parameter (already done in some places, needs consistency).

**Severity**: LOW - Testability and maintainability

---

### 7. **Missing Reconnection Logic on Server**

**Location**: `server/realtime/connection_manager.py`

**Issue**: Client has reconnection logic, but server doesn't handle reconnection scenarios gracefully:

- No detection of stale connections
- No automatic cleanup of dead connections
- Connection health checks are minimal

**Problem**: Dead connections can accumulate, causing memory leaks.

**Recommendation**:

1. Implement periodic connection health checks
2. Add timeout-based connection cleanup
3. Detect and remove stale connections proactively

**Severity**: MEDIUM - Memory leak risk

---

### 8. **Error Handling Gaps**

**Location**: Multiple locations

**Issues**:

1. `server/realtime/websocket_handler.py:374-376` - WebSocketDisconnect caught but no cleanup logging
2. `server/realtime/event_handler.py:519-521` - RuntimeError caught but async operation silently skipped
3. Missing error context in several catch blocks

**Recommendation**:

1. Add comprehensive error logging with context
2. Ensure all error paths perform cleanup
3. Don't silently skip critical operations

**Severity**: MEDIUM - Debugging and reliability

---

## 🟢 Performance Concerns

### 9. **Inefficient Room Occupant Lookups**

**Location**: `server/realtime/event_handler.py:401-465` (`_get_room_occupants`)

**Issue**: Method performs multiple database lookups in a loop:

```python
for player_id in player_ids:
    player = self.connection_manager._get_player(player_id)
    # ... process player

for npc_id in npc_ids:
    npc_name = _get_npc_name_from_instance(npc_id)
    # ... process NPC

```

**Problem**: N+1 query pattern - one lookup per player/NPC instead of batch loading.

**Recommendation**: Implement batch loading for players and NPCs.

**Severity**: MEDIUM - Performance under load

---

### 10. **No Message Batching**

**Location**: `server/realtime/connection_manager.py` (broadcast methods)

**Issue**: Messages are sent individually to each connection:

```python
for player_id in filtered_targets:
    await self.connection_manager.send_personal_message(player_id, chat_event)
```

**Problem**: With many recipients, this creates many individual send operations instead of batching.

**Recommendation**: Implement message batching for broadcasts to multiple recipients.

**Severity**: LOW - Optimization opportunity

---

## 🔵 Security Considerations

### 11. **Missing Rate Limiting on WebSocket Messages**

**Location**: `server/realtime/websocket_handler.py:339-387`

**Issue**: No per-connection rate limiting on incoming WebSocket messages. Client can flood server with messages.

**Problem**: DoS vulnerability - malicious client can overwhelm server.

**Recommendation**:

1. Implement per-connection message rate limiting
2. Add throttling for command processing
3. Monitor and alert on suspicious patterns

**Severity**: MEDIUM - DoS vulnerability

---

### 12. **Insufficient Authentication Validation**

**Location**: `server/realtime/websocket_handler.py:54-91`

**Issue**: Authentication happens at connection time, but no re-validation during connection lifetime.

**Problem**: If token is revoked, connection remains active until disconnect.

**Recommendation**:

1. Implement periodic token validation
2. Add token expiration checks
3. Handle token revocation gracefully

**Severity**: LOW - Security hardening

---

## 📋 Recommendations Summary

### Immediate Actions (High Priority)

1. **Fix Event Loop Disconnect Handling** (Issue #1)

   - Ensure disconnect processing always occurs
   - Use proper async context management

2. **Add Server-Side Input Validation** (Issue #2)

   - Implement message size limits
   - Add schema validation
   - Complete CSRF validation

3. **Implement Connection Health Checks** (Issue #7)

   - Periodic connection validation
   - Automatic stale connection cleanup

### Short-Term Improvements (Medium Priority)

1. **Refactor Complex Event Handlers** (Issue #5)

   - Break down large methods
   - Improve testability

2. **Optimize Room Occupant Lookups** (Issue #9)

   - Implement batch loading
   - Reduce N+1 queries

3. **Add Rate Limiting** (Issue #11)

   - Per-connection message limits
   - Command throttling

### Long-Term Enhancements (Low Priority)

1. **Payload Optimization** (Issue #4)

   - Incremental updates
   - Compression for large payloads

2. **Message Batching** (Issue #10)

   - Batch broadcasts
   - Reduce individual send operations

3. **Enhanced Error Handling** (Issue #8)

   - Comprehensive error context
   - Better cleanup on errors

---

## Testing Recommendations

1. **Load Testing**: Test with 100+ concurrent connections
2. **Stress Testing**: Test message flooding scenarios
3. **Memory Leak Testing**: Long-running connection tests
4. **Error Injection**: Test all error paths
5. **Security Testing**: Input validation and rate limiting tests

---

## Conclusion

The WebSocket implementation shows good architectural patterns with dependency injection and modular design. However,
several critical issues need attention, particularly around event loop handling, input validation, and connection
lifecycle management. Addressing the high-priority issues will significantly improve reliability, security, and
performance.

**Overall Assessment**: ⚠️ **Needs Improvement** - Good foundation, but critical gaps need addressing before production
deployment.
