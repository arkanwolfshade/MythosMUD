---
name: Architecture review remediation
overview: "Remediate server-side violations of ADR-001/002/005 and the domain model audit: remove deprecated global get_async_persistence() in favor of container injection, and implement high-priority anemic domain model enrichments. Client architecture is aligned with event-sourced handoffs and server authority; no code changes required there."
todos: []
isProject: false
---

# Architecture Review Remediation Plan

## Reference

- **ADRs:** [docs/architecture/decisions/ADR-001-layered-architecture-event-driven.md](docs/architecture/decisions/ADR-001-layered-architecture-event-driven.md), [ADR-002-application-container-dependency-injection.md](docs/architecture/decisions/ADR-002-application-container-dependency-injection.md), [ADR-005-repository-pattern-data-access.md](docs/architecture/decisions/ADR-005-repository-pattern-data-access.md)
- **Domain audit:** [docs/architecture/DOMAIN_MODEL_ANEMIC_AUDIT.md](docs/architecture/DOMAIN_MODEL_ANEMIC_AUDIT.md)
- **Container:** [server/container/](server/container/); **DI accessors:** [server/dependencies.py](server/dependencies.py) (`get_container`, `get_async_persistence(request)`)

---

## Finding 1: Deprecated global `get_async_persistence()` still used (ADR-002 violation)

**Issue:** [server/async_persistence.py](server/async_persistence.py) marks `get_async_persistence()` as deprecated and directs callers to `ApplicationContainer.async_persistence`. Several modules still call the global accessor, bypassing container-based injection and making tests and lifecycle harder to reason about.

**Locations:**

- [server/api/real_time.py](server/api/real_time.py): `_resolve_player_id_from_path_or_token` (lines 442–445) calls `get_async_persistence()`. The WebSocket endpoint has access to `websocket.app.state` and can resolve the container (same pattern as `_resolve_connection_manager_from_state`).
- [server/realtime/websocket_handler.py](server/realtime/websocket_handler.py): One call at 359–361 uses `get_async_persistence()`. The handler already receives `connection_manager`, which has `async_persistence` set by the container; use `connection_manager.async_persistence` instead.
- [server/realtime/websocket_room_updates.py](server/realtime/websocket_room_updates.py): Line 258 calls `get_async_persistence()`. Callers of the function that need persistence should pass it in (or receive a `ConnectionManager` that exposes `async_persistence`). Trace call sites and add an `async_persistence` parameter (or get it from a passed-in manager) so the module does not import or call `get_async_persistence`.

**Required changes:**

1. **real_time.py**
   In the WebSocket route that calls `_resolve_player_id_from_path_or_token`, resolve the container from `websocket.app.state` (reuse the same pattern as for `connection_manager`). Pass `container.async_persistence` into `_resolve_player_id_from_path_or_token` and add an optional parameter `async_persistence` to that function. Use the passed-in instance instead of `get_async_persistence()`.
2. **websocket_handler.py**
   Replace the block that calls `get_async_persistence()` with use of `connection_manager.async_persistence` (with a null check consistent with the rest of the handler). Remove the import of `get_async_persistence` from this file.
3. **websocket_room_updates.py**
   Identify the function that contains line 258 and its callers. Add an `async_persistence` parameter to that function and have callers pass `connection_manager.async_persistence` (or the persistence from the container they already have). Remove the `get_async_persistence` import and call.
4. **Tests**
   Update any tests that patch `get_async_persistence` for these code paths to instead set `connection_manager.async_persistence` or pass a mock persistence into the new parameters. Rely on existing container/app.state setup where it already provides persistence.
5. **follow-up**
   After no remaining callers use `get_async_persistence()`, deprecate or remove the global in [server/async_persistence.py](server/async_persistence.py) and document removal in a short ADR or changelog note.

---

## Finding 2: Anemic domain model – high-priority enrichments (ADR-001 / DDD)

**Issue:** [DOMAIN_MODEL_ANEMIC_AUDIT.md](docs/architecture/DOMAIN_MODEL_ANEMIC_AUDIT.md) identifies business logic in services that belongs in domain models. High-priority items centralize invariants (DP decay, death/posture, respawn) in the model and keep services as orchestrators.

**Required changes (implement in this order):**

1. **Player: DP decay and posture**
   In [server/models/player.py](server/models/player.py) (or the module that defines `Player`), add:

- `apply_dp_decay(amount: int = 1) -> tuple[int, int, bool]`
  Apply decay, cap at -10, update posture when crossing 0; return `(old_dp, new_dp, posture_changed)`.
- Use it in [server/services/player_death_service.py](server/services/player_death_service.py) (lines 143–173) instead of manually updating stats/posture.

1. **CombatParticipant: can_act_in_combat**
   Add `can_act_in_combat() -> bool` (e.g. `current_dp > 0`) on the combat participant model used in [server/services/combat_turn_processor.py](server/services/combat_turn_processor.py). Replace the inline “skip turn” checks (e.g. 307–319, 373–385) with calls to this method.
2. **Player: DP change and death/posture transitions**
   Add a method such as `apply_dp_change(new_dp: int) -> tuple[bool, bool]` that updates DP and posture and returns `(became_mortally_wounded, became_dead)` using existing `is_dead()` / `is_mortally_wounded()` semantics. Use it in:

- [server/services/combat_hp_sync.py](server/services/combat_hp_sync.py) (lines 172–182, 212–239, 261–273)
- [server/services/combat_persistence_handler.py](server/services/combat_persistence_handler.py) (lines 57–106, 134–173, 200–217)
  so death and posture rules live in the model and services only orchestrate persistence/events.

1. **Player: respawn health restore**
   Add `restore_to_full_health() -> int` (set DP to max, posture to STANDING; return previous DP). Use it in [server/services/player_respawn_service.py](server/services/player_respawn_service.py) (lines 178–192, 289–294) instead of direct stat manipulation.
2. **Tests**
   Add or extend unit tests for the new `Player` and `CombatParticipant` methods. Keep existing service tests passing by preserving observable behavior.

---

## Finding 3: Repository interfaces not explicit (ADR-005 consequence)

**Issue:** ADR-005 notes that “Repository interfaces could be more explicit (protocols)”. Services depend on concrete repository classes; explicit protocols would improve testability and dependency inversion.

**Required change (lower priority, optional in first pass):**

- Introduce `typing.Protocol` (or equivalent) for one or two key repositories (e.g. `PlayerRepository`, `RoomRepository`) in [server/persistence/repositories](server/persistence/repositories) or a dedicated `server/persistence/protocols.py`. Have the concrete repository classes implement the protocol and type the facade/container to depend on the protocol. This can be done incrementally; start with the repository most used by the code paths touched in Finding 1.

---

## Client architecture (no changes required)

- **Event-sourced UI:** [client/src/components/ui-v2/eventLog/](client/src/components/ui-v2/eventLog/) uses an event log and projector; server is authoritative ([HANDOFFS.md](client/src/components/ui-v2/eventLog/HANDOFFS.md)). Aligned with event-driven and clear handoffs.
- **Security:** Centralized in [client/src/utils/security.ts](client/src/utils/security.ts); SafeHtml and ansiToHtml use it. No further remediation from this review.

---

## Implementation order

| Priority | Finding   | Action                                                                                                                                                                          |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Finding 1 | Remove `get_async_persistence()` usage in real_time.py, websocket_handler.py, websocket_room_updates.py; use container/connection_manager.async_persistence and update tests.   |
| 2        | Finding 2 | Implement Player/CombatParticipant domain methods and refactor player_death_service, combat_turn_processor, combat_hp_sync, combat_persistence_handler, player_respawn_service. |
| 3        | Finding 3 | (Optional) Add repository protocols and wire container/facade to protocols.                                                                                                     |

---

## Verification

- Run server test suite (`make test` from project root) after each finding.
- For Finding 1: grep for `get_async_persistence()` and ensure no remaining call sites in production code (tests may still patch for legacy paths if any remain).
- For Finding 2: run services unit tests and any integration tests that cover death, combat, and respawn flows.
