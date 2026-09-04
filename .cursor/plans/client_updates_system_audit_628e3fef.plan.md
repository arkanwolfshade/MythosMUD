---
name: Client Updates System Audit
overview: Full audit of the client event/update pipeline with Option C (replacement client updates system) chosen for implementation. Delivers event-sourced derivation, single-source room/combat state, and request/response for critical handoffs.
todos:
  - id: c1-event-log-types
    content: Define event log types and append-only event store (client); document event schema per type
    status: completed
  - id: c1-projector-reducer
    content: Implement single GameState projector/reducer that derives state from event log (room, player, messages, combat, system)
    status: completed
  - id: c1-wire-websocket
    content: Wire WebSocket to append events to log and trigger single derivation pass (replace current queue + handlers)
    status: completed
  - id: c1-migrate-handlers
    content: Migrate existing handler logic into projector (room merge, occupant preservation, message append)
    status: completed
  - id: c1-tests
    content: Add unit tests for projector (replay event sequences for room, combat, chat); integration test for enter-room
    status: completed
  - id: c2-room-stream
    content: Server: add room_state or room_snapshot message type with room + occupants; client: consume as single source for room
    status: completed
  - id: c2-combat-stream
    content: Optional - Server: combat_state message per combat; client: derive combat UI from combat_state
    status: cancelled
  - id: c3-enter-room-rr
    content: Server: enter_room request/response returning room_snapshot; client: send on enter, set state from response
    status: completed
  - id: c3-other-handoffs
    content: Document and implement request/response for other critical handoffs (e.g. login state, respawn) if needed
    status: completed
  - id: cleanup-old-pipeline
    content: Remove old event queue, per-event handlers, ref-based context for room; remove OCCUPANT_DEBUG logs
    status: completed
isProject: false
---

# Client Updates System Audit and Fix Plan

## Decision: Option C (Replacement Client Updates System)

Option C is chosen for implementation. It provides:

- **C1 (Event-sourced):** Single derivation path for all state (room, combat, chat, player); consistency, testability, replay.
- **C2 (Single source per entity):** One room state stream/snapshot per room; optional combat state stream.
- **C3 (Request/response for critical state):** Enter-room and other handoffs use request/response to avoid ordering bugs.

---

## 1. Current Architecture (Summary)

- **Entry:** WebSocket messages invoke `handleGameEvent`; events are pushed to `eventQueue.current` and processed in a 10ms-deferred batch.
- **Processing:** [useEventProcessing.ts](client/src/components/ui-v2/hooks/useEventProcessing.ts) drains the queue, calls `processGameEvent` per event, accumulates into `Partial<GameState>`, then calls `sanitizeAndApplyUpdates(updates, setGameState)` once per batch.
- **Handlers:** [eventHandlers/index.ts](client/src/components/ui-v2/eventHandlers/index.ts) maps event types to handlers. Refs (`currentRoomRef`, etc.) are only updated after state commit; within a batch every handler sees the same previous-render refs.
- **Room merge:** Two layers—batch accumulation (`mergeRoomUpdate` / `mergeOccupantData`) and state commit (`mergeRoomState`). Observed bug: entering player sometimes ends with empty occupants due to ordering/ref staleness.

---

## 2. Option C Implementation Plan

### Phase 1: C1 – Event-sourced derivation (client)

| Todo ID                  | Task                                               | Details                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **c1-event-log-types**   | Define event log types and append-only event store | Create typed event log (e.g. `GameEvent[]` or immutable list) and interface to append events. Document event schema per type (room, combat, chat, player, system). Location: new module under `client/src/components/ui-v2/` (e.g. `eventLog/` or `state/`).                                                                                                                                                       |
| **c1-projector-reducer** | Implement single GameState projector/reducer       | Single function: `(eventLog: GameEvent[]) => GameState` (or incremental: `(prevState, nextEvent) => nextState`). Derives room, player, messages, combat-related state, grace period, etc. No refs; pure derivation.                                                                                                                                                                                                |
| **c1-wire-websocket**    | Wire WebSocket to append events and derive         | On WebSocket message: append event(s) to log, run projector, call `setGameState(derivedState)`. Replace current `handleGameEvent` → queue → `processEventQueue` flow. Optionally keep batching (append batch, then derive once).                                                                                                                                                                                   |
| **c1-migrate-handlers**  | Migrate handler logic into projector               | Move room merge rules (preserve occupants when new has no occupant data, same-room semantics), message append, player update, combat state, system state from [roomHandlers.ts](client/src/components/ui-v2/eventHandlers/roomHandlers.ts), [stateUpdateUtils.ts](client/src/components/ui-v2/utils/stateUpdateUtils.ts), [roomMergeUtils.ts](client/src/components/ui-v2/utils/roomMergeUtils.ts) into projector. |
| **c1-tests**             | Tests for projector                                | Unit tests: replay event sequences (e.g. room_occupants then room_update; game_state with empty room then room_occupants) and assert derived state. Integration test: enter-room scenario (two tabs) with occupant visibility.                                                                                                                                                                                     |

### Phase 2: C2 – Single source per entity (server + client)

| Todo ID              | Task                                        | Details                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **c2-room-stream**   | Room state / room_snapshot as single source | Server: Add message type `room_state` or `room_snapshot` (room metadata + occupants). Send to entering player and on room changes. Client: In projector, treat `room_state` as authoritative for that room id (replace, do not merge with older room_update/room_occupants for same id). Backward compatibility: accept both old events and new type during migration. |
| **c2-combat-stream** | Optional combat_state stream                | Server: Optionally add `combat_state` per combat instance. Client: Derive combat UI from last `combat_state` per combat id. Lower priority than room.                                                                                                                                                                                                                  |

### Phase 3: C3 – Request/response for critical handoffs

| Todo ID               | Task                        | Details                                                                                                                                                                                                                                             |
| --------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **c3-enter-room-rr**  | Enter-room request/response | Server: On player enter room, support request/response (e.g. client sends `enter_room` or server responds to movement with `room_snapshot`). Client: On enter-room, set room state from that single response (no reliance on order of push events). |
| **c3-other-handoffs** | Other critical handoffs     | Document which handoffs need request/response (e.g. login/game_state, respawn). Implement if needed; otherwise leave as push-only.                                                                                                                  |

### Phase 4: Cleanup

| Todo ID                  | Task                               | Details                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **cleanup-old-pipeline** | Remove old pipeline and debug logs | Remove event queue, `processEventQueue`, per-event handler registry usage for state derivation, ref-based context for room (`currentRoomRef` for handlers). Remove or gate OCCUPANT_DEBUG logs. Keep handler modules only if reused for validation or side effects (e.g. appendMessage); otherwise delete or archive. |

---

## 3. Key Files (Current)

- **Event flow:** [useEventProcessing.ts](client/src/components/ui-v2/hooks/useEventProcessing.ts), [eventHandlers/index.ts](client/src/components/ui-v2/eventHandlers/index.ts).
- **Room handlers:** [roomHandlers.ts](client/src/components/ui-v2/eventHandlers/roomHandlers.ts).
- **Merge logic:** [stateUpdateUtils.ts](client/src/components/ui-v2/utils/stateUpdateUtils.ts), [roomMergeUtils.ts](client/src/components/ui-v2/utils/roomMergeUtils.ts).
- **Context/refs:** [GameClientV2Container.tsx](client/src/components/ui-v2/GameClientV2Container.tsx), [useRefSynchronization.ts](client/src/components/ui-v2/hooks/useRefSynchronization.ts).
- **Server:** [player_event_handlers_room.py](server/realtime/player_event_handlers_room.py), [websocket_room_updates.py](server/realtime/websocket_room_updates.py), [message_builders.py](server/realtime/message_builders.py).

---

## 4. Implementation Order (Summary)

1. **C1 (client):** Event log + projector + wire WebSocket → derive state; migrate room/player/messages/combat/system logic; add tests.
2. **C2 (server + client):** Add `room_state`/`room_snapshot`; client projector uses it as authoritative for room.
3. **C3 (server + client):** Enter-room request/response; optional other handoffs.
4. **Cleanup:** Remove old queue, handlers-for-state, ref-based room context; remove debug logs.

---

## 5. Dependency for Architecture Review Plan

The **Architecture Review Plan** ([architecture_review_plan_7bcbc812.plan.md](.cursor/plans/architecture_review_plan_7bcbc812.plan.md)) should not proceed with its remaining implementation todos until this **Client Updates System Audit** plan is implemented. See that plan’s “Implementation order and prerequisites” section.
