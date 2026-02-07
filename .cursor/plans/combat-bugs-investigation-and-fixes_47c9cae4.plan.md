---
name: combat-bugs-investigation-and-fixes
overview: Investigate, verify, and fix four combat-related bugs in melee room validation, movement during combat, DP-based incapacitation, and XP rewards on NPC death.
todos:
  - id: bug1-room-validation-and-combat-end
    content: Investigate and update melee room validation so room mismatches fail the attack and cleanly end combat for both player–NPC and player–player combat.
    status: completed
  - id: bug2-block-movement-in-combat
    content: Audit and adjust player and NPC movement paths to ensure normal movement commands are blocked while entities are in combat.
    status: completed
  - id: bug3-dp-threshold-and-posture-flow
    content: Verify and align server and client handling of DP <= 0 so players become incapacitated and prone with correct events and UI behavior.
    status: completed
  - id: bug4-xp-award-on-npc-death
    content: Trace and fix the XP award pipeline on NPC death so GameMechanicsService.gain_experience is reliably invoked with correct values.
    status: completed
isProject: false
---

# Combat Bugs Investigation & Fix Plan

## Scope

Address four related combat issues:

1. Melee attacks must only succeed when attacker and target are in the same room; otherwise the attack fails and combat ends.
2. Normal movement must be blocked for **both players and NPCs** while in combat.
3. When a player’s DP ≤ 0, health must transition from `Critical` → `Incapacitated` and posture must become `prone`/`LYING` end‑to‑end (server + client).
4. Players must reliably receive XP when an NPC is slain.

---

## Bug 1: Melee attacker/target must share room

### Current understanding

- Player→NPC attacks via `NPCCombatIntegrationService.handle_player_attack_on_npc` in
  - `[server/services/npc_combat_integration_service.py](server/services/npc_combat_integration_service.py)`
- That method:
  - Validates NPC instance (`_validate_and_get_npc_instance`)
  - Calls `_validate_combat_location(player_id, npc_id, room_id, npc_instance)`
    - If `False`, currently just returns `False` and **does not explicitly end combat**.
  - Otherwise proceeds to `_setup_combat_uuids_and_mappings` then `_process_combat_attack` and result handling.
- Combat end is handled centrally by `CombatService.end_combat` in
  - `[server/services/combat_service.py](server/services/combat_service.py)` and used in several flows (participant death, login grace period, cleanup, etc.).

### Investigation steps

1. **Verify player–NPC room validation behavior**
  - Re-read `_validate_combat_location` implementation in
    - `[server/services/npc_combat_integration_service.py](server/services/npc_combat_integration_service.py)`
    - Confirm it compares `player_room_id`, `npc_room_id`, and `combat_room_id` and logs when mismatched.
  - Examine unit tests in
    - `[server/tests/unit/services/test_npc_combat_integration_service.py](server/tests/unit/services/test_npc_combat_integration_service.py)`
    - Ensure they cover different‑room behavior and expectations (currently just `False` return).
2. **Check player–player combat path**
  - In `[server/commands/combat.py](server/commands/combat.py)` and `[server/services/combat_service.py](server/services/combat_service.py)`:
    - Trace `handle_attack_command` → `_validate_combat_action` / `_execute_combat_action`.
    - Confirm whether any room validation is performed there (and if not, plan to add it).
3. **Understand how combat should end**
  - Study `CombatService.end_combat` implementation and side effects in
    - `[server/services/combat_service.py](server/services/combat_service.py)` (e.g., clearing participants, monitoring, publishing `CombatEndedEvent`).
  - Review how `CombatTurnProcessor` uses `end_combat` in
    - `[server/services/combat_turn_processor.py](server/services/combat_turn_processor.py)`
  - Confirm any invariants around when/end reasons are logged.

### Planned changes

1. **Player–NPC melee validation**
  - In `NPCCombatIntegrationService.handle_player_attack_on_npc`:
    - When `_validate_combat_location` returns `False`, **ensure any existing combat instance between that player and NPC is ended**:
      - Look up active combat via injected `CombatService` or existing combat mappings.
      - If a combat exists, call `combat_service.end_combat(combat_id, "Invalid combat location - participants not in same room")`.
      - Ensure this is robust even if there are multiple participants.
    - Return a clear failure result to the caller so the command handler can send appropriate feedback to the player.
2. **Player–player melee validation (if applicable)**
  - In `CombatService` (or `CombatAttackHandler`) add a **room consistency check** before applying damage:
    - For melee actions, confirm both participants share `combat.room_id` and their current room IDs in persistence.
    - If mismatch:
      - Log at warning level with player IDs and room IDs.
      - End the combat via `end_combat`.
      - Return a result representing a failed attack and ended combat.
3. **Guard against race conditions**
  - Ensure room IDs are retrieved as close to attack processing as possible to minimize stale data.
  - Consider using the same source of truth for room IDs as movement/combat services to avoid divergence.

### Testing

1. **Unit tests**
  - Update/create tests in
    - `server/tests/unit/services/test_npc_combat_integration_service.py`
    - New tests for player–player combat room mismatch in appropriate combat service test module.
  - Cases:
    - Player and NPC in same room → attack proceeds, combat remains active.
    - Player and NPC in different rooms **before first attack** → attack fails, no combat created.
    - Player and NPC start in same room, then NPC moves (e.g., idle move) while combat active → next attack:
      - Fails due to room mismatch.
      - Ends combat cleanly.
2. **Integration tests**
  - Add high‑level test(s) that:
    - Start combat, then move NPC via `NPCMovementIntegration` or idle movement.
    - Attempt another player attack and assert combat is ended / player is notified.

---

## Bug 2: Block movement while in combat (players & NPCs)

### Current understanding

- **Players**:
  - Movement runs through `MovementService.move_player` in
    - `[server/game/movement_service.py](server/game/movement_service.py)`
  - This calls `_check_combat_state`, which uses `PlayerCombatService.is_player_in_combat_sync(player_id)` from
    - `[server/services/player_combat_service.py](server/services/player_combat_service.py)`
  - If `is_in_combat` is `True`, `_check_combat_state` returns `False`, and movement is blocked.
  - Entry point command: `[server/commands/go_command.py](server/commands/go_command.py)` calls `_execute_movement` → `MovementService.move_player`.
- **NPCs**:
  - NPC movement is orchestrated by:
    - `[server/npc/npc_base.py](server/npc/npc_base.py)` for direct `move_to_room` and movement via `NPCMovementIntegration` (see `move_with_integration`/`move_to_room` methods around lines 440+).
    - `[server/npc/idle_movement.py](server/npc/idle_movement.py)` defines `IdleMovementHandler` with `should_idle_move` and `execute_idle_movement`.
      - `should_idle_move` explicitly checks if NPC is in combat and **skips idle movement when in combat**.
    - `[server/npc/threading.py](server/npc/threading.py)` routes `WANDER` actions to `IdleMovementHandler.execute_idle_movement`.
  - NPC idle wandering therefore already respects combat state, but **direct movement APIs may not**.

### Investigation steps

1. **Confirm player movement protection**
  - Re‑read `_check_combat_state` and `move_player` in `MovementService` to confirm no bypass paths.
  - Search for any other direct manipulations of `player.current_room_id` outside movement service that might bypass combat checks.
2. **Audit NPC movement paths**
  - In `[server/npc/npc_base.py](server/npc/npc_base.py)`:
    - Review `move_with_integration`, `move_to_room`, and associated helpers.
  - In `[server/npc/idle_movement.py](server/npc/idle_movement.py)`:
    - Confirm `should_idle_move` combat check (likely using `PlayerCombatService` or a similar combat registry).
  - In `[server/services/npc_instance_service.py]` (if present):
    - Inspect `move_npc_instance` and ensure it either uses idle movement / NPCMovementIntegration or is updated to check combat status.
3. **Define policy for NPC movement in combat**
  - Clarify whether **any** NPC movement while in combat should be blocked (most likely yes for “normal” movement, excluding special combat actions like flee, spells, etc.).

### Planned changes

1. **Players**
  - If any code path updates `player.current_room_id` without going through `MovementService.move_player`, refactor to use the movement service or add equivalent combat checks.
  - Ensure error messages / feedback when movement is blocked are clear to the player.
2. **NPCs**
  - Introduce a **central NPC‑combat check helper** (if not already present), similar to `PlayerCombatService`:
    - Either reuse `PlayerCombatService` (if it already tracks NPC participants) or create a thin `NPCCombatStateService` or utility that queries active combats for a given `npc_id`.
  - In all NPC movement entry points (including `NPCMovementIntegration.move_npc_to_room`, `npc_base.move_to_room`, any `npc_instance_service.move_npc_instance`):
    - Before moving, check if NPC is currently in combat.
    - If yes, log at debug/info and block movement for “normal” commands (idle wander, scripted moves).
    - Allow explicitly‑marked combat actions (e.g., a dedicated flee API) to bypass this, if such behavior exists or is desired later.

### Testing

1. **Unit tests**
  - Add/extend tests in:
    - `server/tests/unit/game/test_movement_service.py` (or equivalent) for players.
    - `server/tests/unit/npc/test_idle_movement.py` and any `npc_instance_service` tests.
  - Cases:
    - Player in combat attempting `go`/movement → movement blocked, room unchanged.
    - NPC in combat:
      - Idle movement handler’s `should_idle_move` returns `False`.
      - Direct movement helper returns failure / skips movement.
2. **Integration tests**
  - Scenario: player engages NPC, then NPC idle movement tick fires → NPC must not wander until combat ends.

---

## Bug 3: DP ≤ 0 → Incapacitated + prone

### Current understanding

- **Server‑side DP & posture**
  - `Player` model in `[server/models/player.py](server/models/player.py)`:
    - `apply_dp_decay` and `apply_dp_change` update `current_dp` and set `stats["position"] = PositionState.LYING` when `new_dp <= 0`.
  - Combat DP persistence & events in
    - `[server/services/combat_persistence_handler.py](server/services/combat_persistence_handler.py)` and/or
    - `[server/services/combat_hp_sync.py](server/services/combat_hp_sync.py)`
    - These publish `PlayerDPUpdated` events via `_publish_player_dp_update_event` with `old_dp`, `new_dp`, `max_dp`, etc.
  - Player death and DP decay in
    - `[server/services/player_death_service.py](server/services/player_death_service.py)`
    - This also ensures posture is LYING on death and publishes `PlayerDPDecayEvent`.
- **Server → client event bridge**
  - `[server/realtime/player_event_handlers.py](server/realtime/player_event_handlers.py)`
    - `handle_player_dp_updated` → delegates to `_state_handler.handle_player_dp_updated(event)`.
    - `handle_player_dp_decay` → delegates similarly.
  - `[server/services/combat_event_publisher.py](server/services/combat_event_publisher.py)`
    - Builds event payloads that include `current_dp`, `max_dp`, and related fields.
- **Client‑side health UI**
  - `[client/src/utils/healthEventUtils.ts](client/src/utils/healthEventUtils.ts)`
    - `determineDpTier(newDp, maxDp)` decides tier; DP ≤ 0 must map to `Incapacitated`.
    - Also derives `posture` and `inCombat` from received events.
  - `[client/src/components/GameTerminal.tsx](client/src/components/GameTerminal.tsx)`
    - Computes `isIncapacitated` from `derivedHealthStatus.current <= 0` and shows `IncapacitatedBanner`.

### Investigation steps

1. **Verify server posture logic is hooked into combat DP flows**
  - In `combat_persistence_handler` / `combat_hp_sync`:
    - Confirm they **delegate DP & posture updates to `Player**` (e.g., call `Player.apply_dp_change` / `apply_dp_decay`).
    - Ensure that when DP crosses from >0 to ≤0 during combat, posture is set to LYING.
2. **Trace DP events to client**
  - Follow `PlayerDPUpdated` → `player_event_handlers.handle_player_dp_updated` → state handler (likely in realtime/state code) → client WebSocket message format.
  - Confirm that the payload includes `current_dp`, `max_dp`, and any posture field or enough information for the client to infer posture.
3. **Verify DP tier mapping on client**
  - Review `determineDpTier` implementation in `healthEventUtils.ts`:
    - Ensure DP ≤ 0 yields an `Incapacitated` tier distinct from `Critical`.
  - Confirm that `derivedHealthStatus` is built from DP events and that `GameTerminal` reads the correct tier.

### Planned changes

1. **Server: consistent LYING posture on DP ≤ 0**
  - If any combat DP path still updates `current_dp` without going through `Player`’s posture logic, refactor:
    - Centralize DP changes through `Player.apply_dp_change` / `apply_dp_decay`.
  - In `player_death_service` and `combat_persistence_handler`:
    - Ensure posture is updated to LYING on death or DP ≤ 0 and corresponding events reflect the new posture in state.
2. **Server → client event shape**
  - Ensure `PlayerDPUpdated` (and, if used, `PlayerDPDecayEvent`) include all fields required for the client’s health computation:
    - At minimum: `player_id`, `old_dp`, `new_dp`, `max_dp`, and a reliable posture field or a separate posture update event.
  - Verify `combat_event_publisher` and NATS integration send these correctly.
3. **Client: Critical → Incapacitated transition**
  - In `healthEventUtils.ts`:
    - Confirm thresholds: e.g., `Critical` for low positive DP, `Incapacitated` for `dp <= 0`.
    - If necessary, adjust to exactly match server semantics.
  - Ensure `GameTerminal` uses tier or DP to derive `isIncapacitated` consistently and displays banner and any controls restrictions.

### Testing

1. **Server unit tests**
  - Extend tests in:
    - `server/tests/unit/models/test_player_model.py` (already covers posture at DP ≤ 0).
    - `server/tests/unit/services/test_combat_persistence_handler*.py` and `test_player_death_service.py`.
  - Cases:
    - DP drops from >0 to 0 or below → posture becomes LYING, events reflect new DP.
    - `Player.apply_dp_change` used by combat persistence logic.
2. **End‑to‑end / integration tests**
  - Simulate combat attack sequence that drives DP from positive to ≤ 0 and assert:
    - Player can no longer act (`can_act_in_combat` false).
    - Player posture in persistence is LYING.
  - If feasible, add a client‑facing integration/UI test (or manual test script) to confirm incapacitated banner behavior.

---

## Bug 4: XP not granted on NPC slain

### Current understanding

- XP pipeline components:
  - `CombatService` in `[server/services/combat_service.py](server/services/combat_service.py)`:
    - After processing damage and determining `target_died`, calls `_event_handler.handle_attack_events_and_xp(...)` which returns `xp_awarded`.
    - Then calls `_award_xp_to_player(...)` → `self._event_handler.award_xp_to_player(...)`.
  - `CombatEventHandler` in `[server/services/combat_event_handler.py](server/services/combat_event_handler.py)`:
    - `_calculate_xp_reward` uses `PlayerCombatService.calculate_xp_reward(npc_id)` when available; otherwise returns `0` (explicit default to highlight DB lookup issues).
    - `award_xp_to_player` checks that attacker is `CombatParticipantType.PLAYER` and target is `CombatParticipantType.NPC`, then calls:
      - `player_combat_service.award_xp_on_npc_death(player_id, npc_id, xp_amount)`.
  - `PlayerCombatService` in `[server/services/player_combat_service.py](server/services/player_combat_service.py)`:
    - Implements `award_xp_on_npc_death`, which should:
      - Look up the player in persistence.
      - Delegate to `NPCCombatRewards.award_xp_to_killer` or directly call game mechanics.
  - `NPCCombatRewards` in `[server/services/npc_combat_rewards.py](server/services/npc_combat_rewards.py)`:
    - `award_xp_to_killer(killer_id, npc_id, xp_reward)` uses `_game_mechanics.gain_experience(killer_id, xp_reward, f"killed_{npc_id}")`.
      - There is a **CRITICAL FIX** comment emphasizing this.
  - `GameMechanicsService.gain_experience` in `[server/game/mechanics.py](server/game/mechanics.py)`:
    - Calls persistence: `persistence.gain_experience(player, amount, source)` implemented by
      - `[server/persistence/repositories/experience_repository.py](server/persistence/repositories/experience_repository.py)`.
- Alternative / legacy paths:
  - `server/npc/combat_integration.py` and `server/services/npc_combat_handlers.py` have their own `handle_npc_death` and XP calculation logic; we must verify how these interact with the newer `CombatEventHandler` / `PlayerCombatService` path.

### Investigation steps

1. **Trace the actual runtime path on NPC death**
  - From `CombatService.process_attack` (or equivalent):
    - Confirm when `target_died` is set and how `handle_attack_events_and_xp` is called.
    - Verify `CombatEventHandler.handle_attack_events_and_xp` calls `_calculate_xp_reward` and then delegates to the appropriate death handler (`NPCCombatHandlers` / `CombatDeathHandler`).
  - Confirm that `award_xp_to_player` is invoked **after** a successful XP calculation.
2. **Inspect `PlayerCombatService.award_xp_on_npc_death**`
  - Ensure it calls `NPCCombatRewards.award_xp_to_killer` or `GameMechanicsService.gain_experience` directly.
  - Confirm correct player ID, npc ID, and XP values are passed.
3. **Check for misconfigured or missing services**
  - In `CombatService` initialization / DI container (`ApplicationContainer`):
    - Ensure `_player_combat_service` and `_npc_combat_integration_service` are wired correctly.
  - Confirm unit tests such as `test_award_xp_on_npc_death_success` and `test_npc_combat_rewards` accurately represent intended behavior.
4. **Reconcile alternate death handlers**
  - Determine if `server/npc/combat_integration.py.handle_npc_death` and `server/services/npc_combat_handlers.py.handle_npc_death` are still used on the main combat path, or only in legacy / non‑combat flows.
  - Ensure XP is awarded **exactly once** per NPC kill.

### Planned changes

1. **Centralize XP award through PlayerCombatService + NPCCombatRewards**
  - Make `CombatEventHandler.award_xp_to_player` the **single entry point** for combat‑driven XP grants.
  - Ensure `PlayerCombatService.award_xp_on_npc_death`:
    - Validates the player exists.
    - Calls `NPCCombatRewards.award_xp_to_killer(player_id, npc_id, xp_amount)`.
    - Handles and logs failures without crashing combat or disconnecting clients.
2. **Fix `_calculate_xp_reward` behavior**
  - Ensure `PlayerCombatService.calculate_xp_reward(npc_id)` returns a non‑zero positive XP value for valid NPCs.
  - Investigate why the current runtime may be returning 0 (e.g., NPC not found in mapping, DB lookup failure, misconfigured mapping service).
  - Optionally:
    - Log a clear warning when XP calculation returns 0 for a defeated NPC.
3. **Align or deprecate alternate XP paths**
  - If `npc_combat_integration.handle_npc_death` and `npc_combat_handlers.handle_npc_death` are still granting XP separately:
    - Either refactor them to call into `PlayerCombatService.award_xp_on_npc_death` or ensure they are not used on the main combat path.
  - Document the canonical XP award flow for future debugging.

### Testing

1. **Unit tests**
  - Strengthen tests in:
    - `server/tests/unit/services/test_player_combat_service.py` for `award_xp_on_npc_death` success, player not found, and error cases.
    - `server/tests/unit/services/test_npc_combat_rewards.py` (already checks `gain_experience` calls).
    - Any `test_combat_event_handler.py` to confirm `award_xp_to_player` calls `PlayerCombatService` with correct args.
2. **Integration tests**
  - End‑to‑end combat scenario:
    - Player kills NPC via normal combat.
    - Assert that:
      - XP in persistence increases by expected amount.
      - No duplicate XP awards.
      - Logs show XP calculation and award steps.

---

## Cross‑cutting concerns

### Logging & observability

- Add structured logging around each fix boundary:
  - Room mismatch validation failures and combat termination.
  - Movement blocked while in combat (for both players and NPCs).
  - DP crossing to ≤ 0 with posture change.
  - XP calculation and award decisions.

### Test coverage

- Ensure new/updated tests keep coverage ≥ 70% overall and ≥ 90% for critical combat and XP modules:
  - `combat_service`, `combat_event_handler`, `player_combat_service`, `npc_combat_integration_service`, `combat_persistence_handler`.

### Manual verification checklist

- Scenario scripts to run on a dev server:
  1. Start combat, move NPC out of room (admin command or forced move), attempt attack → attack fails, combat ends.
  2. Player in combat attempts normal movement → blocked; after combat ends, movement resumes.
  3. Drive player DP from positive to 0 or below via combat → UI shows Incapacitated banner and posture is prone; player cannot act.
  4. Kill NPC → verify XP increase, and no duplicate awards.

---

## Implementation summary (completed)

All four bugs have been implemented and tested.

### Bug 1: Melee attacker/target must share room — **Done**

- **NPC combat integration** (`npc_combat_integration_service.py`): `_validate_combat_location` now also ensures `room_id` matches both `player_room_id` and `npc_room_id`; on mismatch it returns `False` and logs. When validation fails, `_end_combat_if_participant_in_combat` is already called and the attack returns `False`.
- **CombatService** (`combat_service.py`): Added `_get_participant_current_room` and `_validate_melee_location`. In `process_attack`, after resolving participants, melee location is validated; if invalid, combat is ended with reason `"Invalid combat location - participants not in same room"` and a failed `CombatResult` is returned.
- **Tests**: `test_validate_combat_location_combat_room_mismatch` in `test_npc_combat_integration_service.py`.

### Bug 2: Block movement while in combat — **Done**

- **Players**: Confirmed `MovementService._check_combat_state` already blocks movement when `PlayerCombatService.is_player_in_combat_sync` is true.
- **NPCs**: In `npc_base.py`, added `_is_npc_in_combat()` and at the start of `move_to_room` a combat check that blocks movement and returns `False` when the NPC is in combat. `NPCMovementIntegration.move_npc_to_room` and `npc_instance_service.move_npc_instance` already had combat checks.
- **Tests**: `test_npc_base_move_to_room_blocked_when_in_combat` in `test_npc_base.py`.

### Bug 3: DP ≤ 0 → Incapacitated + prone — **Done**

- **Server**: Confirmed `Player.apply_dp_change` sets `position` to `LYING` when `new_dp <= 0`; combat persistence uses it. `player_event_handlers_state.handle_player_dp_updated` sets `posture = "lying"` when `event.new_dp <= 0` and includes it in the client payload.
- **Client**: Confirmed `determineDpTier` returns `incapacitated` for `current <= 0`; `GameTerminal` uses `derivedHealthStatus.current <= 0` for `isIncapacitated`.
- **Tests**: In `healthEventUtils.test.ts`, added a test that when `new_dp <= 0` and `posture: 'lying'`, the built status has `tier: 'incapacitated'` and `posture: 'lying'`.

### Bug 4: XP not granted on NPC slain — **Done**

- **Root cause**: `PlayerCombatService.calculate_xp_reward` was reading `_uuid_to_xp_mapping` from the integration service; the XP mapping lives on `_uuid_mapping` (NPCCombatUUIDMapping) via `get_xp_value(npc_id)`.
- **Fix**: In `player_combat_service.calculate_xp_reward`, the first branch now uses `getattr(svc, "_uuid_mapping", None)` and, when present, `uuid_mapping.get_xp_value(npc_id)` to obtain XP; lifecycle/DB fallback unchanged.
- **Tests**: Updated `test_calculate_xp_reward_from_mapping`, `test_calculate_xp_reward_from_database`, and `test_calculate_xp_reward_default` in `test_player_combat_service.py` to mock `_uuid_mapping.get_xp_value` instead of `_uuid_to_xp_mapping`.
