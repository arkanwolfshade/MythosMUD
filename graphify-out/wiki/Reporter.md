# Reporter

> 84 nodes · cohesion 0.07

## Key Concepts

- **SuccessLevel** (53 connections) — `server/game/skill_service.py`
- **test_combat_protect_action.py** (38 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_combat_taunt_action.py** (35 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **skill_service.py** (34 connections) — `server/game/skill_service.py`
- **resolve_protect_action()** (22 connections) — `server/services/combat_protect_action.py`
- **resolve_taunt_action()** (21 connections) — `server/services/combat_taunt_action.py`
- **_doubles()** (21 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **asyncio** (20 connections)
- **intercept_for_guard()** (18 connections) — `server/services/combat_protect_action.py`
- **_doubles()** (14 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **_hate()** (14 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **asyncio** (12 connections)
- **taunt_outcome_line()** (8 connections) — `server/services/combat_taunt_action.py`
- **_covered_fight()** (8 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **_hate()** (8 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_failure_and_fumble_do_nothing_but_still_announce()** (8 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **taunt_outcome_parts()** (7 connections) — `server/services/combat_taunt_action.py`
- **_Fight** (7 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_a_redirect_happens_once_it_never_chains_to_the_protectors_own_guardian()** (7 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_an_intercepted_blow_earns_the_protector_threat_with_the_guarding_multiplier()** (7 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_a_fumble_by_the_current_tank_hands_the_npc_to_the_next_in_line()** (7 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **test_hard_and_extreme_successes_double_the_lead()** (7 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **test_taunt_stays_room_local_if_the_taunter_has_left()** (7 connections) — `server/tests/unit/services/test_combat_taunt_action.py`
- **_p()** (6 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- **test_a_new_protect_replaces_the_protectors_old_cover()** (6 connections) — `server/tests/unit/services/test_combat_protect_action.py`
- *... and 59 more nodes in this community*

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (36 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (16 shared connections)
- [DatabaseManager](DatabaseManager.md) (13 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (7 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [PerformanceTester](PerformanceTester.md) (5 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [Room](Room.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (2 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (2 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/services/combat_protect_action.py`
- `server/services/combat_taunt_action.py`
- `server/tests/unit/services/test_combat_protect_action.py`
- `server/tests/unit/services/test_combat_status_segments.py`
- `server/tests/unit/services/test_combat_taunt_action.py`

## Audit Trail

- EXTRACTED: 305 (86%)
- INFERRED: 49 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*