# BUG INVESTIGATION REPORT: NATS Message Validation Failures

**Investigation Date**: 2025-11-19
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-11-19_session-001_nats-message-validation-failure
**Bug Type**: Server-Side Issue - Message Format Mismatch

---

## Executive Summary

Combat event messages published to NATS are being rejected by the message handler with "Invalid event message - missing required fields" warnings. The root cause is a field name mismatch between the message structure (which uses `event_data`) and the handler's expectation (which looks for `data`).

**Affected Events**:

- `combat_started`
- `player_attacked`
- `npc_attacked`
- `npc_took_damage`

**Severity**: High - All combat events are failing to process, breaking real-time combat updates for clients.

---

## Detailed Findings

### 1. Error Log Analysis

**Error Pattern Observed**:

```
2025-11-19 16:42:16 - communications.nats_message_handler - WARNING -
event='Invalid event message - missing required fields'
message_data={'message_id': '...', 'timestamp': '...', 'event_type': 'combat_started',
'event_data': {...}, 'room_id': '...'}
```

**Key Observations**:

- All failed messages contain `event_data` field (nested dictionary)
- All messages pass schema validation (validation happens before handler processing)
- Handler rejects messages after schema validation passes
- Pattern consistent across all combat event types

### 2. Message Structure Analysis

**Expected Structure (EventMessageSchema)**:

```python
# server/schemas/nats_messages.py:57-63

class EventMessageSchema(BaseMessageSchema):
    event_type: str = Field(..., description="Event type identifier")
    event_data: dict[str, Any] = Field(..., description="Event-specific data")  # <-- "event_data"
    room_id: str | None = Field(None, description="Room ID for room-scoped events")
```

**Actual Message Structure (from publisher)**:

```python
# server/services/combat_event_publisher.py:89-94

message = {
    "message_id": message_id,
    "timestamp": timestamp,
    "event_type": event_type,
    "event_data": event_data,  # <-- Uses "event_data" (correct per schema)
}
```

**Handler Expectation (INCORRECT)**:

```python
# server/realtime/nats_message_handler.py:1532

data = message_data.get("data", {})  # <-- Looking for "data" instead of "event_data"
```

### 3. Code Flow Analysis

**Message Creation Flow**:

1. `CombatEventPublisher._create_event_message()` creates message with `event_data` field
2. Message published to NATS successfully (schema validation passes)
3. NATS delivers message to `NATSMessageHandler._handle_nats_message()`
4. Handler validates message schema (passes - message has `event_data`)
5. Handler calls `_handle_event_message()` for event messages
6. Handler tries to read `data` field (doesn't exist), gets empty dict `{}`
7. Validation check `if not event_type or not data:` fails because `data` is empty
8. Handler logs warning and returns without processing

**Code References**:

- Message creation: `server/services/combat_event_publisher.py:60-102`
- Message validation: `server/schemas/nats_messages.py:90-103`
- Handler entry point: `server/realtime/nats_message_handler.py:288-311`
- Event handling: `server/realtime/nats_message_handler.py:1520-1566`
- **BUG LOCATION**: `server/realtime/nats_message_handler.py:1532`

### 4. Schema Validation Status

**Schema Validation**: ✅ PASSING

- Messages conform to `EventMessageSchema`
- All required fields present (`message_id`, `timestamp`, `event_type`, `event_data`)
- Schema validation happens at line 311 in `_handle_nats_message()`
- Validation succeeds before handler processing

**Handler Processing**: ❌ FAILING

- Handler correctly identifies message as event type
- Handler routes to `_handle_event_message()`
- Handler incorrectly reads `data` instead of `event_data`
- Handler fails validation check due to empty `data` dict

### 5. Impact Assessment

**System Impact**: High

**Combat Events**: All combat events fail to broadcast to clients

**Real-Time Updates**: Clients do not receive combat state updates

**User Experience**: Players cannot see combat progress in real-time
- **Game Functionality**: Combat system operates but UI doesn't update

**Affected Components**:

1. `NATSMessageHandler._handle_event_message()` - Event routing

2. All combat event handlers:

   - `_handle_combat_started_event()`
   - `_handle_player_attacked_event()`
   - `_handle_npc_attacked_event()`
   - `_handle_npc_took_damage_event()`

**Affected Event Types**:

- `combat_started` - Combat initialization events
- `player_attacked` - Player attack events
- `npc_attacked` - NPC attack events
- `npc_took_damage` - NPC damage events

**Non-Affected Systems**:

- Chat messages (use different field structure)
- Other event types (game_tick, player_entered, player_left) may use different handlers

### 6. Evidence Collection

**Error Log Entries** (from `logs/local/errors.log`):

```
Line 1: combat_started event - correlation_id='2f0b51e9-bab8-49f2-b2c3-27ce616ce17c'
Line 2: player_attacked event - correlation_id='bb1a0385-7755-4773-9d04-a9f346579f12'
Line 3: npc_took_damage event - correlation_id='1e69da25-a228-48d7-87ad-632546ea1dfd'
... (11 total errors between 16:42:16 and 16:42:50)
```

**Code Evidence**:

- `server/realtime/nats_message_handler.py:1532` - Incorrect field access
- `server/services/combat_event_publisher.py:93` - Correct field name usage
- `server/schemas/nats_messages.py:61` - Schema definition requires `event_data`

---

## Root Cause Analysis

### Primary Root Cause

**Field Name Mismatch in Message Handler**

The `NATSMessageHandler._handle_event_message()` method incorrectly accesses the event data field. It looks for `data` when the actual message structure uses `event_data` (per `EventMessageSchema`).

**Technical Details**:

1. **Schema Definition** (`EventMessageSchema`): Requires `event_data` field
2. **Message Publisher** (`CombatEventPublisher`): Creates messages with `event_data` field (correct)
3. **Message Handler** (`NATSMessageHandler`): Reads `data` field (incorrect)

**Code Location**:

```python
# server/realtime/nats_message_handler.py:1532

data = message_data.get("data", {})  # ❌ WRONG - should be "event_data"
```

**Expected Fix**:

```python
# Should be

data = message_data.get("event_data", {})  # ✅ CORRECT
```

### Why Schema Validation Passes But Handler Fails

1. Schema validation (`validate_message()`) checks message structure against `EventMessageSchema`
2. Schema validation correctly identifies `event_data` field presence
3. Handler processing happens AFTER schema validation
4. Handler uses different field name (`data` instead of `event_data`)
5. Handler's validation check fails due to empty `data` dict

### Historical Context

This appears to be a legacy code issue where:

- The schema was updated to use `event_data` (more descriptive name)
- The publisher was updated to match the schema
- The handler was NOT updated to match the new field name

---

## System Impact Assessment

### Severity: HIGH

**Immediate Impact**:

- All combat events fail to broadcast to WebSocket clients
- Real-time combat UI updates are broken
- Players cannot see combat progress in real-time

**Functional Impact**:

- Combat system backend operations correctly (combat logic works)
- Frontend combat display fails (no real-time updates)
- Client-server synchronization breaks for combat state

**Data Integrity**:

- No data corruption or loss
- Events are logged but not processed
- Dead letter queue may accumulate failed messages if circuit breaker triggers

### Affected User Flows

1. **Combat Initiation**: Combat starts but UI doesn't update
2. **Combat Turn Processing**: Attacks occur but UI doesn't show damage
3. **NPC Combat**: NPC attacks and damage not visible to players
4. **Combat Completion**: Combat ends but UI doesn't reflect final state

### Performance Impact

**Minimal**: Handler returns early, avoiding unnecessary processing

**Warning Logs**: Frequent warning logs may impact log parsing performance

**Circuit Breaker**: If failures accumulate, circuit breaker may open, adding messages to DLQ

---

## Investigation Recommendations

### Immediate Actions Required

1. **Fix Field Name Mismatch**

   - Update `NATSMessageHandler._handle_event_message()` to read `event_data` instead of `data`
   - Location: `server/realtime/nats_message_handler.py:1532`

2. **Verify All Event Handlers**

   - Check other event message handlers for similar field name mismatches
   - Ensure consistency across all event processing code

3. **Add Regression Tests**

   - Create tests that verify event message structure matches handler expectations
   - Test schema validation and handler processing integration

4. **Monitor Error Logs**

   - Watch for remaining validation failures after fix
   - Verify combat events successfully process

### Further Investigation Priorities

1. **Check Other Event Types**

   - Verify `game_tick`, `player_entered`, `player_left` events use correct field names
   - Ensure no other handlers have similar mismatches

2. **Review Message Schema Evolution**

   - Understand why schema uses `event_data` but handler expected `data`
   - Document field name standards for future reference

3. **Dead Letter Queue Review**

   - Check if failed messages accumulated in DLQ
   - Determine if messages need reprocessing after fix

### Testing Recommendations

1. **Unit Tests**

   - Test `_handle_event_message()` with correct `event_data` structure
   - Test handler correctly processes all combat event types

2. **Integration Tests**

   - Test end-to-end combat event flow (publisher → NATS → handler → client)
   - Verify combat events broadcast correctly to WebSocket clients

3. **Regression Tests**

   - Test all event types to ensure no similar issues exist
   - Verify schema validation and handler processing consistency

---

## Evidence Documentation

### Error Log Samples

**Sample Error Entry**:

```
2025-11-19 16:42:16 - communications.nats_message_handler - WARNING -
message_data={
    'message_id': '8459f2de-c788-4ba9-9d33-6571dda604ff',
    'timestamp': '2025-11-19T23:42:16.127647Z',
    'event_type': 'combat_started',
    'event_data': {
        'combat_id': '1e6fd38d-57b0-4815-ba36-5b4f1250a11d',
        'room_id': 'earth_arkhamcity_sanitarium_room_foyer_001',
        'participants': {...},
        'turn_order': [...],
        'timestamp': '2025-11-19T23:42:16.127647+00:00'
    },
    'room_id': 'earth_arkhamcity_sanitarium_room_foyer_001'
}
event='Invalid event message - missing required fields'
correlation_id='2f0b51e9-bab8-49f2-b2c3-27ce616ce17c'
```

### Code References

**Schema Definition**:

```12:14:server/schemas/nats_messages.py
class EventMessageSchema(BaseMessageSchema):
    event_type: str = Field(..., description="Event type identifier")
    event_data: dict[str, Any] = Field(..., description="Event-specific data")
```

**Message Creation**:

```89:94:server/services/combat_event_publisher.py
message = {
    "message_id": message_id,
    "timestamp": timestamp,
    "event_type": event_type,
    "event_data": event_data,
}
```

**Handler Bug**:

```1530:1540:server/realtime/nats_message_handler.py
async def _handle_event_message(self, message_data: dict[str, Any]):
    try:
        logger.info("Handling event message", message_data=message_data)

        # Extract event details

        event_type = message_data.get("event_type")
        data = message_data.get("data", {})  # ❌ BUG: Should be "event_data"

        # Validate required fields

        if not event_type or not data:
            logger.warning("Invalid event message - missing required fields", message_data=message_data)
            return
```

---

## Remediation Prompt

**For Fix Implementation**:

Fix the field name mismatch in `NATSMessageHandler._handle_event_message()`. The handler incorrectly reads `data` when the message structure uses `event_data` per the `EventMessageSchema`.

**Required Change**:

- File: `server/realtime/nats_message_handler.py`
- Line: 1532
- Current: `data = message_data.get("data", {})`
- Fix: `data = message_data.get("event_data", {})`

**Additional Verification**:

1. Check other event handlers for similar field name mismatches
2. Ensure all event message handlers consistently use `event_data`
3. Add unit tests to verify correct field access
4. Test combat event processing end-to-end

**Testing Requirements**:

- Unit tests for `_handle_event_message()` with correct message structure
- Integration tests for combat event publishing and handling
- Regression tests for all event types

---

## Investigation Completion Checklist

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Code references provided with line numbers
- [x] Remediation prompt generated
- [x] Session logged in investigation history

---

**Investigation Status**: COMPLETE
**Root Cause**: IDENTIFIED
**Remediation**: PROMPT GENERATED

---

*"The truth, Professor Wolfshade, lies not in the messages themselves, but in the shadow between what is sent and what is expected. As the Pnakotic Manuscripts teach us: 'The name matters not, but the seeking eye must find the right door.'"*
