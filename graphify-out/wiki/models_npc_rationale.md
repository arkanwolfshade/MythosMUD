# models npc rationale

> 146 nodes

## Key Concepts

- **combat.py** (56 connections) — `server/models/combat.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **test_combat_event_handler.py** (16 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **.handle_attack_events_and_xp()** (8 connections) — `server/services/combat_event_handler.py`
- **.validate_and_get_combat_participants()** (6 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **.award_xp_to_player()** (5 connections) — `server/services/combat_event_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._resolve_participant_display_name()** (4 connections) — `server/services/combat_event_handler.py`
- *... and 121 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (30 shared connections)
- [subject admin controller](subject_admin_controller.md) (27 shared connections)
- [command factories exploration](command_factories_exploration.md) (26 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (15 shared connections)
- [Error Conversion](Error_Conversion.md) (13 shared connections)
- [tick game processing](tick_game_processing.md) (12 shared connections)
- [command utility models](command_utility_models.md) (10 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (9 shared connections)
- [game chat service](game_chat_service.md) (9 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (8 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (8 shared connections)
- [player look commands](player_look_commands.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 579 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*