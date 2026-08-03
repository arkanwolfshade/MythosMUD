# player occupant processor

> 192 nodes

## Key Concepts

- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_player_occupant_processor.py** (26 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **test_room_occupant_manager.py** (16 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (11 connections)
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (8 connections) — `server/realtime/npc_occupant_processor.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **test_warded_indicator_removed_after_expiration()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 167 more nodes in this community*

## Relationships

- [Player Name Validation](Player_Name_Validation.md) (22 shared connections)
- [command utility models](command_utility_models.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [combat services turn](combat_services_turn.md) (7 shared connections)
- [look helpers commands](look_helpers_commands.md) (7 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (6 shared connections)
- [room websocket updates](room_websocket_updates.md) (5 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/player_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_room_id_utils.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 597 (98%)
- INFERRED: 14 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*