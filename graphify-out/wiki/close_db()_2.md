# close db()

> 254 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **CombatInstance** (167 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **UUID** (11 connections)
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **._resolve_original_npc_id()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- *... and 229 more nodes in this community*

## Relationships

- [test combat attack handler](test_combat_attack_handler.md) (79 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (61 shared connections)
- [.validate target()](validate_target%28%29.md) (45 shared connections)
- [Any](Any.md) (37 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (16 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (16 shared connections)
- [process dead players()](process_dead_players%28%29.md) (9 shared connections)
- [combat flee](combat_flee.md) (8 shared connections)
- [get health service()](get_health_service%28%29.md) (7 shared connections)
- [test exploration service](test_exploration_service.md) (6 shared connections)
- [test flee command](test_flee_command.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 1136 (98%)
- INFERRED: 29 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*