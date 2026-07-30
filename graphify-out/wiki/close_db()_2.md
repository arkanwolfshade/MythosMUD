# close db()

> 330 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **CombatInstance** (167 connections) — `server/models/combat.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat.py** (51 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (36 connections) — `server/models/combat.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- *... and 305 more nodes in this community*

## Relationships

- [. initialize handlers()](_initialize_handlers%28%29.md) (75 shared connections)
- [Any](Any.md) (65 shared connections)
- [.validate target()](validate_target%28%29.md) (54 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (53 shared connections)
- [test exploration service](test_exploration_service.md) (31 shared connections)
- [get health service()](get_health_service%28%29.md) (30 shared connections)
- [world](world.md) (29 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (23 shared connections)
- [process dead players()](process_dead_players%28%29.md) (21 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (21 shared connections)
- [. init ()](_init_%28%29.md) (19 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (18 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 1972 (98%)
- INFERRED: 48 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*