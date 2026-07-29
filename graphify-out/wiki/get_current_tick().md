# get current tick()

> 79 nodes

## Key Concepts

- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **UUID** (6 connections)
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.validate_and_get_combat_participants()** (5 connections) — `server/services/combat_service.py`
- **.handle_attack_events_and_xp()** (5 connections) — `server/services/combat_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (45 shared connections)
- [combat](combat.md) (39 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [Reset the current tick for](Reset_the_current_tick_for.md) (3 shared connections)
- [.end combat()](end_combat%28%29.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [game tick processing](game_tick_processing.md) (1 shared connections)
- [lifespan](lifespan.md) (1 shared connections)
- [MagicServiceCore](MagicServiceCore.md) (1 shared connections)
- [login grace period](login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 340 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*