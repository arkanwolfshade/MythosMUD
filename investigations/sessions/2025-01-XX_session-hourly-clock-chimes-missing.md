# BUG INVESTIGATION REPORT: Missing Hourly Clock Chimes in Game Info Panel

**Investigation Date**: 2025-01-28
**Investigator**: AI Assistant (GPT-4)
**Session ID**: `2025-01-28_session-hourly-clock-chimes-missing`

---

## EXECUTIVE SUMMARY

Hourly clock chime messages are not appearing in the Game Info panel feed because the client-side
 `mythos_time_update` event handler only creates messages when the daypart changes (e.g., morning → afternoon), not
  on every hourly tick. While the server correctly publishes hourly tick events and broadcasts `mythos_time_update`
   events, the client does not generate user-visible clock chime messages from these events.

**Root Cause**: Missing clock chime message generation logic in client-side `mythos_time_update` event handler. The
 handler only creates messages for daypart transitions, not for every hourly tick.

**Severity**: Medium - Feature not working as intended, but does not break core functionality.

---

## DETAILED FINDINGS

### 1. Server-Side Time Event System

**Status**: ✅ **WORKING CORRECTLY**

**Location**: `server/time/tick_scheduler.py` and `server/time/time_event_consumer.py`

The server's Mythos time system is functioning properly:

1. **MythosTickScheduler** publishes `MythosHourTickEvent` events on hourly boundaries
2. **MythosTimeEventConsumer** subscribes to hourly tick events and processes them
3. Server broadcasts `mythos_time_update` events via SSE with complete time data

**Evidence**:

```75:79:server/time/time_event_consumer.py
        payload = self._build_broadcast_payload(event, active_holidays, active_schedules)
        try:
            await broadcast_game_event("mythos_time_update", payload)
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.error("Failed to broadcast Mythos time update", error=str(exc))
```

**Log Evidence**: Events log shows hourly tick events being published:

```
2025-11-28 13:15:59 - EventBus - DEBUG - event_type='MythosHourTickEvent' event='Published event'
2025-11-28 13:16:15 - EventBus - DEBUG - event_type='MythosHourTickEvent' event='Published event'
```

**Key Finding**: The server broadcasts `mythos_time_update` events with time data including `mythos_clock`
 (formatted time string), but these events are intended for HUD clock display updates, not for generating
  user-visible messages.

### 2. Client-Side Event Reception

**Status**: ✅ **WORKING CORRECTLY**

**Location**: `client/src/components/ui-v2/GameClientV2Container.tsx:494-507`

The client correctly receives and processes `mythos_time_update` events:

```570:589:client/src/components/ui-v2/GameClientV2Container.tsx
          case 'mythos_time_update': {
            const payload = event.data as MythosTimePayload;
            if (payload && payload.mythos_clock) {
              const nextState = buildMythosTimeState(payload);
              setMythosTime(nextState);
              const previousDaypart = lastDaypartRef.current;
              if (previousDaypart && previousDaypart !== nextState.daypart) {
                const description =
                  DAYPART_MESSAGES[nextState.daypart] ?? `The Mythos clock shifts into the ${nextState.daypart} watch.`;
                appendMessage(
                  sanitizeChatMessageForState({
                    text: `[Time] ${description}`,
                    timestamp: event.timestamp,
                    messageType: 'system',
                    channel: 'system',
                  })
                );
              }
              lastDaypartRef.current = nextState.daypart;
            }
            break;
          }
```

**Evidence**:

- Events are received and processed correctly
- Time state is updated (`setMythosTime(nextState)`)
- **BUT**: Messages are only created when `previousDaypart !== nextState.daypart` (daypart transitions)
- **MISSING**: No logic to create clock chime messages on every hourly tick

### 3. Missing Clock Chime Message Generation

**Status**: ❌ **NO LOGIC EXISTS**

**Location**: `client/src/components/ui-v2/GameClientV2Container.tsx:594-614`

**The Problem**:

The `mythos_time_update` event handler only creates messages when daypart changes (e.g., "morning" → "afternoon"),
 not on every hourly tick. There is no logic to create clock chime messages like "The clock chimes 14:00" on every
  hour.

**Current Behavior**:
✅ Receives `mythos_time_update` events every hour

✅ Updates HUD clock display

✅ Creates messages when daypart changes (e.g., dawn, dusk)

- ❌ **DOES NOT** create clock chime messages on every hourly tick

**Expected Behavior** (based on user report):

- Should create clock chime messages like "The clock chimes 14:00" on every hourly tick
- These messages should appear in the Game Info panel

### 4. Game Info Panel Message Display

**Status**: ✅ **WORKING CORRECTLY**

**Location**: `client/src/components/ui-v2/panels/GameInfoPanel.tsx`

The Game Info panel correctly displays system messages:

```59:76:client/src/components/ui-v2/panels/GameInfoPanel.tsx
  const filteredMessages = messages.filter(message => {
    // Always exclude chat messages from Game Info Panel - they belong in Chat Panel
    if (message.messageType === 'chat') {
      return false;
    }

    // Apply message type filter
    if (messageFilter !== 'all' && message.messageType !== messageFilter) {
      return false;
    }

    // Apply search filter
    if (searchQuery && !message.text.toLowerCase().includes(searchQuery.toLowerCase())) {
      return false;
    }

    return true;
  });
```

**Evidence**:

- Panel correctly filters and displays messages
- Excludes chat messages (as intended)
- Accepts `messageType: 'system'` messages (which clock chimes should use)
- **The panel would display clock chime messages if they were added to the messages array**

### 5. Server-Side Message Generation

**Status**: ❌ **NO MESSAGE GENERATION ON SERVER**

**Location**: `server/time/time_event_consumer.py`

The server's `MythosTimeEventConsumer` does not create user-visible clock chime messages:

```41:79:server/time/time_event_consumer.py
    async def _handle_tick(self, event: MythosHourTickEvent) -> None:
        """Dispatch hour tick events to each dependent subsystem."""

        mythos_dt = event.mythos_datetime
        active_holidays = self._holiday_service.refresh_active(mythos_dt)
        active_schedules = self._schedule_service.get_active_entries(
            mythos_dt=event.mythos_datetime, day_name=event.day_name
        )

        if self._room_service:
            holiday_names = [holiday.name for holiday in active_holidays]
            try:
                self._room_service.update_environment_state(
                    daypart=event.daypart,
                    is_daytime=event.is_daytime,
                    active_holidays=holiday_names,
                )
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to update room environment state", error=str(exc))

        if self._npc_lifecycle_manager and hasattr(self._npc_lifecycle_manager, "apply_schedule_state"):
            try:
                self._npc_lifecycle_manager.apply_schedule_state(active_schedules)
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to apply NPC schedule state", error=str(exc))

        logger.debug(
            "Processed Mythos hour tick",
            mythos_time=event.mythos_datetime.isoformat(),
            daypart=event.daypart,
            active_holiday_count=len(active_holidays),
            active_schedule_count=len(active_schedules),
        )

        payload = self._build_broadcast_payload(event, active_holidays, active_schedules)
        try:
            await broadcast_game_event("mythos_time_update", payload)
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.error("Failed to broadcast Mythos time update", error=str(exc))
```

**Evidence**:

- Server only broadcasts time data via `broadcast_game_event("mythos_time_update", payload)`
- No clock chime message creation on server side
- No `broadcast_game_event()` or `send_room_event()` calls that create user-visible messages

### 6. Codebase Search Results

**Status**: ✅ **NO CLOCK CHIME LOGIC FOUND**

**Search Patterns Used**:

- `clock.*chime|chime|hourly.*message|time.*chime` (case-insensitive)
- No matches found in server codebase

**Conclusion**: Clock chime message generation logic does not exist in the current codebase. This functionality was either:

1. Never implemented in the current architecture
2. Removed during a previous refactor
3. Implemented differently than expected

---

## ROOT CAUSE ANALYSIS

### Primary Root Cause

**Missing Client-Side Clock Chime Logic**: The client-side `mythos_time_update` event handler in
 `GameClientV2Container.tsx` does not generate clock chime messages on every hourly tick. It only creates messages
  when daypart transitions occur.

**Technical Details**:

1. **Server Flow** (Working):

   - `MythosTickScheduler` publishes `MythosHourTickEvent` every hour
   - `MythosTimeEventConsumer` receives event and broadcasts `mythos_time_update` via SSE
   - Event payload includes `mythos_clock` (formatted time string like "14:00 Mythos")

2. **Client Flow** (Incomplete):

   - Client receives `mythos_time_update` events correctly
   - Handler updates HUD clock display (`setMythosTime(nextState)`)
   - Handler checks for daypart changes and creates messages only then
   - **MISSING**: No logic to create clock chime messages on every hourly tick

3. **Message Format**:

   - Expected format: "The clock chimes 14:00" or similar
   - Should use `messageType: 'system'` to appear in Game Info panel
   - Should use `channel: 'system'` for proper routing

### Secondary Issues

1. **No Server-Side Message Generation**: The server does not create clock chime messages either. All message
 generation would need to happen client-side.

2. **Event Payload Available**: The `mythos_time_update` payload includes `mythos_clock` field with formatted time,
 which can be used for clock chime messages.

---

## SYSTEM IMPACT ASSESSMENT

### Scope

**Affected Component**: Client-side event processing (`GameClientV2Container.tsx`)

**Affected Feature**: Hourly clock chime message display in Game Info panel

**User Impact**: Users cannot see hourly clock chimes that previously appeared

### Severity

**Severity Level**: Medium

**Reasoning**:

- Feature is non-functional but does not break core game functionality
- No data loss or security implications
- Affects user experience and immersion
- Easy to fix (add missing message generation logic in client handler)

### Dependencies

No other systems depend on clock chime message display

- Fix will not affect other event processing
- No database or persistence changes required
- No server-side changes required (can be fixed client-side only)

---

## EVIDENCE DOCUMENTATION

### Code References

1. **Server Broadcast** (Working):

   - File: `server/time/time_event_consumer.py`
   - Lines: 75-79
   - Function: `_handle_tick()`
   - Evidence: `await broadcast_game_event("mythos_time_update", payload)`

2. **Client Event Reception** (Working):

   - File: `client/src/components/ui-v2/GameClientV2Container.tsx`
   - Lines: 570-589
   - Function: `processEventQueue()` → `case 'mythos_time_update':`
   - Evidence: Events are received and time state is updated

3. **Client Message Generation** (Missing Logic):

   - File: `client/src/components/ui-v2/GameClientV2Container.tsx`
   - Lines: 574-586
   - Function: `processEventQueue()` → `case 'mythos_time_update':`
   - Evidence: Only creates messages when `previousDaypart !== nextState.daypart`
   - **MISSING**: No logic to create clock chime messages on every hourly tick

4. **Game Info Panel** (Working):

   - File: `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
   - Lines: 59-76
   - Evidence: Panel correctly displays system messages when provided

5. **Time Formatting** (Available):

   - File: `server/time/time_service.py`
   - Lines: 177-183
   - Function: `format_clock()`
   - Evidence: `mythos_clock` field in payload contains formatted time string

### Log Evidence

**Server Logs** (from `logs/local/events.log`):

```
2025-11-28 13:15:59 - EventBus - DEBUG - event_type='MythosHourTickEvent' event='Published event'
2025-11-28 13:16:15 - EventBus - DEBUG - event_type='MythosHourTickEvent' event='Published event'
```

**Evidence**: Hourly tick events are being published correctly.

**Client Logs**: No specific log entries for clock chime messages found, confirming they are not being generated.

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Add Clock Chime Message Generation (Client-Side)

**Action**: Add clock chime message creation logic in the `mythos_time_update` event handler in `GameClientV2Container.tsx`

**Requirements**:

1. Track the last hour that generated a clock chime message (use a ref similar to `lastDaypartRef`)
2. On every `mythos_time_update` event, check if the hour has changed
3. If hour changed, create a clock chime message using the `mythos_clock` value from the payload
4. Message format: `The clock chimes ${mythos_clock}` or similar
5. Use `messageType: 'system'` and `channel: 'system'` for Game Info panel display
6. Add message via `appendMessage()` helper function

**Implementation Location**:

- File: `client/src/components/ui-v2/GameClientV2Container.tsx`
- Function: `processEventQueue()` → `case 'mythos_time_update':`
- Around lines: 570-589

### Priority 2: Consider Message Format Options

**Action**: Determine the preferred clock chime message format

**Options**:

1. Simple format: `The clock chimes 14:00`
2. Mythos-themed format: `The clock chimes 14:00 Mythos`
3. Descriptive format: `[Time] The clock chimes 14:00 Mythos`

**Recommendation**: Use format that matches existing time messages (`[Time]` prefix) for consistency.

### Priority 3: Testing

**Action**: Test clock chime message generation

**Requirements**:

1. Verify messages appear in Game Info panel on every hourly tick
2. Verify messages do not duplicate when daypart messages are shown
3. Verify message format matches expected style
4. Verify messages appear with correct timestamp

---

## REMEDIATION PROMPT

**For Cursor Chat**:

```
Fix missing hourly clock chime messages in Game Info panel

Hourly clock chime messages are not appearing in the Game Info panel feed. The client receives mythos_time_update
 events every hour but only creates messages when daypart changes, not on every hourly tick.

Requirements:
1. Add a ref to track the last hour that generated a clock chime (similar to lastDaypartRef)
2. In the mythos_time_update event handler (GameClientV2Container.tsx, around line 570-589), add logic to:
   - Extract the hour from the mythos_clock or mythos_datetime in the payload
   - Compare with the last hour ref
   - If hour changed, create a clock chime message
3. Message format: "[Time] The clock chimes ${payload.mythos_clock}"
   - Use messageType: 'system'
   - Use channel: 'system'
   - Use the existing appendMessage() helper function
4. Update the last hour ref after creating the message

The mythos_time_update payload includes:
- mythos_clock: formatted time string (e.g., "14:00 Mythos")
- mythos_datetime: ISO datetime string

This is a client-side fix only - no server changes needed.
```

---

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Code references provided with line numbers
- [x] Remediation prompt generated

---

*"In the restricted archives of Miskatonic University, we learn that proper investigation requires systematic
 methodology, comprehensive evidence collection, and thorough analysis. The truth lies not in hasty conclusions,
  but in methodical examination of all available evidence."*

**Investigation Status**: ✅ **COMPLETE**
**Root Cause**: ✅ **IDENTIFIED**
**Remediation**: ✅ **PROMPT GENERATED**
