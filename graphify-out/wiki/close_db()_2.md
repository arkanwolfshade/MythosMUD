# close db()

> 97 nodes

## Key Concepts

- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **UUID** (11 connections)
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **test_aggro_healer_overpull_switches_target()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_taunt_from_next_room_no_effect()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_stealth_wipe_switches_to_next()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_passive_mob_no_damage_threat_taunt_switches()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_nightgaunt_like_damage_and_heal_threat()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_aggro_tank_swap_taunt_sequence()** (6 connections) — `server/tests/integration/test_aggro_flow.py`
- *... and 72 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (14 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (13 shared connections)
- [Any](Any.md) (12 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (5 shared connections)
- [.model dump()](model_dump%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [.end combat()](end_combat%28%29.md) (4 shared connections)
- [process dead players()](process_dead_players%28%29.md) (2 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_end.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 480 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*