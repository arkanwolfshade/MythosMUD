# combat commands handler

> 133 nodes

## Key Concepts

- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (56 connections) — `server/models/combat.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **test_negative_status_effect_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_blocked_during_grace_period()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Enum** (3 connections)
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- *... and 108 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (50 shared connections)
- [command factories exploration](command_factories_exploration.md) (47 shared connections)
- [models npc rationale](models_npc_rationale.md) (40 shared connections)
- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (11 shared connections)
- [spell game magic](spell_game_magic.md) (11 shared connections)
- [services combat sync](services_combat_sync.md) (9 shared connections)
- [command utility models](command_utility_models.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (7 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (4 shared connections)
- [movement monitor game](movement_monitor_game.md) (4 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 558 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*