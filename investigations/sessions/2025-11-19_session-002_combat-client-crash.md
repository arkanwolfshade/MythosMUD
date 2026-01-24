# BUG INVESTIGATION REPORT: Combat Client Crash

**Investigation Date**: 2025-11-19 20:59:53 UTC
**Investigator**: AI Assistant
**Session ID**: 2025-11-19_session-002_combat-client-crash

## EXECUTIVE SUMMARY

The client crashed when initiating combat with an NPC (`/attack dr`) while in the sanitarium foyer entrance with Dr. Francis Morgan. The crash was caused by **two critical issues**:

1. **Connection Manager Initialization Failure**: The `CombatMessagingIntegration` service failed to resolve the connection manager from the application container, preventing combat messages from being broadcast to players.

2. **NATS Message Schema Validation Errors**: Combat events published to NATS have an incorrect message structure that violates the `EventMessageSchema` requirements, causing all combat events to be rejected and sent to the dead letter queue.

## DETAILED FINDINGS

### Bug Description

**User Report**: Client crashed when starting combat (logged in as ArkanWolfshade/Cthulhu1) by `/attack dr` when in the sanitarium foyer entrance with Dr. Francis Morgan.

**Error Timestamps**: 2025-11-19 20:59:53 UTC

**Affected Systems**:

- Combat messaging system
- NATS message processing
- WebSocket connection management
- Client UI (crash)

### Phase 1: Log Analysis

**Primary Error Log**: `logs/local/errors.log`

**Key Error Messages Identified**:

1. **Connection Manager Errors** (Lines 1-2, 3-4):

   ```
   ERROR - error='Application container does not have an initialized connection_manager'
   event='Failed to resolve connection manager from container'
   ```

2. **Combat Messaging Integration Errors** (Lines 3-4):

   ```
   ERROR - player_id='<ArkanWolfshade>' npc_id='dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001'
   error='Connection manager is not available'
   event='Error handling player attack on NPC: Connection manager is not available'
   ```

3. **NATS Message Validation Errors** (Lines 6-17):

   ```
   CRITICAL - error="4 validation errors for EventMessageSchema
   message_id: Field required
   timestamp: Field required
   event_data: Field required
   data: Extra inputs are not permitted"
   event='Unhandled error in message processing - this indicates a bug!'
   ```

4. **Dead Letter Queue Errors** (Lines 8-9, 12-13, 16-17):

   ```
   ERROR - filepath='.../dlq_20251119_205954_*.json'
   error="4 validation errors for EventMessageSchema..."
   event='Message added to dead letter queue'
   ```

5. **Performance Warning** (Line 5):

   ```
   WARNING - operation='passive_lucidity_flux_tick' duration_ms=1350.564
   threshold_ms=1000.0
   event='Performance alert: operation exceeded threshold'
   ```

### Phase 2: Code Analysis

#### Issue 1: Connection Manager Initialization Failure

**Location**: `server/services/combat_messaging_integration.py`

**Problem**:

1. In `server/services/npc_combat_integration_service.py` line 111:

   ```python
   self._messaging_integration = CombatMessagingIntegration()
   ```

   The `CombatMessagingIntegration` is created **without** a connection manager.

2. When combat happens and `broadcast_combat_attack()` is called (line 304 in `npc_combat_integration_service.py`), it tries to access `self.connection_manager` property.

3. The `connection_manager` property (lines 68-74 in `combat_messaging_integration.py`) tries to lazy-load from the container:

   ```python
   @property
   def connection_manager(self):
       if self._connection_manager is None:
           self._connection_manager = self._resolve_connection_manager_from_container()
       return self._connection_manager
   ```

4. The `_resolve_connection_manager_from_container()` method (lines 42-65) tries to get the connection manager from `ApplicationContainer.get_instance()`, but the container's `connection_manager` attribute is not initialized or not accessible at this point.

**Root Cause**: The `CombatMessagingIntegration` service is not being initialized with a connection manager instance, and the lazy-loading mechanism fails because the application container's connection manager is not properly initialized or accessible.

#### Issue 2: NATS Message Schema Validation Errors

**Location**: `server/services/combat_event_publisher.py`

**Problem**:

1. Combat events are published to NATS with an incorrect message structure (lines 301-316):

   ```python
   message_data = {
       "event_type": "player_attacked",
       "data": {
           "combat_id": str(event.combat_id),
           "room_id": event.room_id,
           # ... other fields

       },
   }
   ```

2. However, the `EventMessageSchema` in `server/schemas/nats_messages.py` (lines 57-71) requires:

   - `message_id`: str (required) - **MISSING**
   - `timestamp`: str (required) - **MISSING**
   - `event_type`: str (required) - ✓ Present
   - `event_data`: dict[str, Any] (required) - **MISSING** (has `data` instead)
   - No extra fields (`extra="forbid"`) - **VIOLATED** (has `data` field)

3. When NATS messages are processed by `NATSMessageHandler._handle_nats_message()` (line 311 in `nats_message_handler.py`), the validation fails:

   ```python
   validate_message(message_data, message_type=message_type)
   ```

4. All combat events (`combat_started`, `player_attacked`, `npc_took_damage`) are being rejected and sent to the dead letter queue.

**Root Cause**: The `CombatEventPublisher` is using an incorrect message structure that doesn't match the `EventMessageSchema` requirements. The messages are missing required fields (`message_id`, `timestamp`) and use the wrong field name (`data` instead of `event_data`).

### Phase 3: System Impact Assessment

#### Severity: **CRITICAL**

**Impact Scope**:

1. **Combat System**: All combat events fail to be broadcast to clients
2. **Player Experience**: Players cannot see combat messages or updates
3. **Client Stability**: Client crashes when combat is initiated
4. **Message Processing**: All combat events are sent to dead letter queue
5. **Real-time Updates**: Combat status updates are not delivered to players

**Affected Components**:

- `CombatMessagingIntegration` service
- `CombatEventPublisher` service
- `NPCCombatIntegrationService` service
- NATS message handler
- Client WebSocket message processing

**Data Loss Risk**: **LOW** - Messages are being sent to DLQ for potential recovery, but they're not being processed.

**User Impact**: **HIGH** - Combat is completely non-functional, client crashes on combat initiation.

### Phase 4: Evidence Collection

#### Error Log Evidence

**Connection Manager Errors** (Timestamp: 2025-11-19T20:59:53.340755Z):

```
ERROR - error='Application container does not have an initialized connection_manager'
event='Failed to resolve connection manager from container'
correlation_id='a804e721-4d38-4d53-aaa2-db57e579f7e2'
logger='server.services.combat_messaging_integration'
```

**Combat Messaging Integration Errors** (Timestamp: 2025-11-19T20:59:53.407205Z):

```
ERROR - player_id='<ArkanWolfshade>' npc_id='dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001'
error='Connection manager is not available'
event='Error handling player attack on NPC: Connection manager is not available'
correlation_id='1bc37b73-7c4f-40da-88df-1b1181c86b19'
```

**NATS Message Validation Errors** (Timestamp: 2025-11-19T20:59:54.043342Z):

```
CRITICAL - error="4 validation errors for EventMessageSchema
message_id: Field required [type=missing, input_value={'event_type': 'combat_st...}]
timestamp: Field required [type=missing, input_value={'event_type': 'combat_st...}]
event_data: Field required [type=missing, input_value={'event_type': 'combat_st...}]
data: Extra inputs are not permitted [type=extra_forbidden, input_value={'combat_id': 'ce3bf9a7-f...}]"
event='Unhandled error in message processing - this indicates a bug!'
correlation_id='98a1aef9-609c-4bff-832b-28bf9336b6c7'
```

**Affected Event Types**:

- `combat_started` (correlation_id: 98a1aef9-609c-4bff-832b-28bf9336b6c7)
- `player_attacked` (correlation_id: 95e62658-203b-4899-bbea-ed801d94fc21)
- `npc_took_damage` (correlation_id: d72d6fcb-4338-41a3-9f7d-76fbeb042666)

#### Code Evidence

**CombatMessagingIntegration Initialization** (`server/services/npc_combat_integration_service.py:111`):

```python
self._messaging_integration = CombatMessagingIntegration()
# Missing connection_manager parameter

```

**Connection Manager Resolution** (`server/services/combat_messaging_integration.py:42-65`):

```python
def _resolve_connection_manager_from_container(self):
    try:
        from server.container import ApplicationContainer
        container = ApplicationContainer.get_instance()
        connection_manager = getattr(container, "connection_manager", None)
        if connection_manager is None:
            raise RuntimeError("Application container does not have an initialized connection_manager")
        return connection_manager
    except Exception as exc:
        logger.error("Failed to resolve connection manager from container", error=str(exc))
        raise RuntimeError("Connection manager is not available") from exc
```

**Incorrect NATS Message Structure** (`server/services/combat_event_publisher.py:301-316`):

```python
message_data = {
    "event_type": "player_attacked",
    "data": {  # Should be "event_data"
        "combat_id": str(event.combat_id),
        # ... missing message_id, timestamp

    },
}
```

**EventMessageSchema Requirements** (`server/schemas/nats_messages.py:57-71`):

```python
class EventMessageSchema(BaseMessageSchema):
    event_type: str = Field(..., description="Event type identifier")
    event_data: dict[str, Any] = Field(..., description="Event-specific data")  # Not "data"
    # ... inherits message_id, timestamp from BaseMessageSchema

```

### Phase 5: Root Cause Analysis

#### Root Cause 1: Connection Manager Initialization Failure

**Primary Cause**: The `CombatMessagingIntegration` service is instantiated without a connection manager, and the lazy-loading mechanism fails because:

1. The `NPCCombatIntegrationService` creates `CombatMessagingIntegration()` without passing the connection manager
2. The application container's `connection_manager` may not be initialized at the time `CombatMessagingIntegration` is created (during `NPCCombatIntegrationService.__init__`)
3. The container singleton pattern may not guarantee that `connection_manager` is accessible when `CombatMessagingIntegration` tries to resolve it

**Contributing Factors**:

- Dependency injection not properly configured for `CombatMessagingIntegration`
- Timing issue: container initialization vs. service instantiation
- Missing connection manager propagation from application container to combat services

#### Root Cause 2: NATS Message Schema Validation Errors

**Primary Cause**: The `CombatEventPublisher` uses an incorrect message structure that doesn't match the `EventMessageSchema` requirements:

1. Missing required fields: `message_id` and `timestamp` are not included in published messages
2. Incorrect field name: Uses `data` instead of `event_data`
3. Schema mismatch: The published message structure doesn't match the expected `EventMessageSchema` format

**Contributing Factors**:

- `CombatEventPublisher` was implemented before or without awareness of the `EventMessageSchema` requirements
- No validation testing to catch schema mismatches
- Different message structures used by different publishers (e.g., `EventPublisher._create_event_message` uses `data`, but schema expects `event_data`)

### Phase 6: Investigation Recommendations

#### Priority 1: CRITICAL - Connection Manager Initialization

**Immediate Actions**:

1. Ensure `CombatMessagingIntegration` receives a connection manager instance during initialization
2. Verify application container properly initializes `connection_manager` before combat services are created
3. Update `NPCCombatIntegrationService` to pass connection manager to `CombatMessagingIntegration`

**Investigation Areas**:

1. Check application container initialization order in `server/app/lifespan.py`
2. Verify connection manager is properly added to container before combat services
3. Review dependency injection patterns for combat services

#### Priority 2: CRITICAL - NATS Message Schema Compliance

**Immediate Actions**:

1. Update `CombatEventPublisher` to use correct message structure matching `EventMessageSchema`
2. Add required fields: `message_id` and `timestamp` to all combat event messages
3. Rename `data` field to `event_data` in all combat event messages

**Investigation Areas**:

1. Review all event publishers to ensure consistent message structure
2. Add validation tests for NATS message schema compliance
3. Document message structure requirements for event publishers

#### Priority 3: MEDIUM - Performance Monitoring

**Investigation Areas**:

1. Review `passive_lucidity_flux_tick` operation performance (exceeded 1000ms threshold)
2. Investigate if performance degradation is related to combat system issues
3. Monitor system performance during combat scenarios

## REMEDIATION PROMPT

**For Cursor Chat**:

```markdown
Fix the combat system client crash issue by addressing two critical bugs:

1. **Connection Manager Initialization**: Update `NPCCombatIntegrationService` to pass the connection manager to `CombatMessagingIntegration` during initialization. The connection manager should be obtained from the application container or passed as a parameter. Ensure the connection manager is properly initialized before combat services are created.

2. **NATS Message Schema Compliance**: Update `CombatEventPublisher` to use the correct message structure matching `EventMessageSchema` requirements:
   - Add `message_id` field (generate UUID for each message)
   - Add `timestamp` field (ISO format timestamp)
   - Rename `data` field to `event_data` in all combat event messages
   - Ensure all combat event messages match the `EventMessageSchema` structure

Files to modify:
- `server/services/npc_combat_integration_service.py` (line 111)
- `server/services/combat_event_publisher.py` (all event publishing methods)
- Verify `server/app/lifespan.py` connection manager initialization

Test that combat messages are properly broadcast and NATS messages pass validation.
```

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials were used (ArkanWolfshade/Cthulhu1)
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

**Investigation Status**: ✅ COMPLETE

**Next Steps**: Use remediation prompt to fix identified issues.
