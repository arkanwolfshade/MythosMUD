# subject admin controller

> 185 nodes

## Key Concepts

- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **handle_combat_completion()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (11 connections) — `server/services/combat_service_attack.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **validate_melee_location()** (10 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (10 connections) — `server/services/combat_service_attack.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- *... and 160 more nodes in this community*

## Relationships

- [npc database infrastructure](npc_database_infrastructure.md) (33 shared connections)
- [models npc rationale](models_npc_rationale.md) (27 shared connections)
- [command factories exploration](command_factories_exploration.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (19 shared connections)
- [Item Instances](Item_Instances.md) (17 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (14 shared connections)
- [game chat service](game_chat_service.md) (11 shared connections)
- [player look commands](player_look_commands.md) (8 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (5 shared connections)
- [rest grace period](rest_grace_period.md) (5 shared connections)
- [tools generate invite](tools_generate_invite.md) (4 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 874 (98%)
- INFERRED: 17 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*