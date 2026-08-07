# cleanup combat handler

> 30 nodes

## Key Concepts

- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (16 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **.handle_attack_events_and_xp()** (8 connections) — `server/services/combat_event_handler.py`
- **.award_xp_to_player()** (5 connections) — `server/services/combat_event_handler.py`
- **.publish_combat_ended_event()** (5 connections) — `server/services/combat_event_handler.py`
- **._resolve_participant_display_name()** (4 connections) — `server/services/combat_event_handler.py`
- **UUID** (4 connections)
- **._calculate_xp_reward()** (4 connections) — `server/services/combat_event_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_event_handler.py`
- **test_resolve_participant_display_name_player()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_resolve_participant_display_name_npc_fallback()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_resolve_participant_display_name_npc_from_lifecycle()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_no_publisher()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_handle_attack_events_and_xp_npc_death()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_player_target()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_award_xp_to_player()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_calculate_xp_reward_default()** (2 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_combat_ended_event()** (2 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **Type of combat participant.** (1 connections) — `server/models/combat.py`
- **Any** (1 connections)
- **Handles combat event publishing.** (1 connections) — `server/services/combat_event_handler.py`
- **Initialize the event handler.          Args:             combat_service: Referen** (1 connections) — `server/services/combat_event_handler.py`
- **Resolve display name for combat messages. For NPCs, resolve from lifecycle** (1 connections) — `server/services/combat_event_handler.py`
- *... and 5 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (16 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (5 shared connections)
- [subject admin controller](subject_admin_controller.md) (4 shared connections)
- [command factories exploration](command_factories_exploration.md) (4 shared connections)
- [game chat service](game_chat_service.md) (4 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [commands position system](commands_position_system.md) (2 shared connections)
- [services service phantom](services_service_phantom.md) (2 shared connections)
- [models player rationale](models_player_rationale.md) (2 shared connections)
- [player look commands](player_look_commands.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 156 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*