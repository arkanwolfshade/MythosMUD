# Item Instances

> 541 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **CombatInstance** (167 connections) — `server/models/combat.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (51 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipantType** (36 connections) — `server/models/combat.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **UUID** (20 connections)
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- *... and 516 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (133 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (41 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (24 shared connections)
- [command factories exploration](command_factories_exploration.md) (22 shared connections)
- [command inventory factories](command_inventory_factories.md) (20 shared connections)
- [player event handlers](player_event_handlers.md) (20 shared connections)
- [command models admin](command_models_admin.md) (15 shared connections)
- [models npc rationale](models_npc_rationale.md) (15 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (15 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (11 shared connections)
- [combat flee commands](combat_flee_commands.md) (11 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/test_config_smoke.py`

## Audit Trail

- EXTRACTED: 2260 (98%)
- INFERRED: 47 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*