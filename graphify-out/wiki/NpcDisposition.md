# NpcDisposition

> 206 nodes

## Key Concepts

- **NpcDisposition** (95 connections) — `server/constants/npc_disposition.py`
- **npc_disposition.py** (46 connections) — `server/constants/npc_disposition.py`
- **combat_attack.py** (40 connections) — `server/commands/combat_attack.py`
- **event_handlers.py** (32 connections) — `server/realtime/event_handlers.py`
- **npc_name_segment()** (31 connections) — `server/constants/message_segments.py`
- **message_segments.py** (30 connections) — `server/constants/message_segments.py`
- **NpcOccupant** (28 connections) — `server/constants/npc_disposition.py`
- **connection_utils.py** (28 connections) — `server/realtime/connection_utils.py`
- **npc_event_handlers.py** (27 connections) — `server/realtime/npc_event_handlers.py`
- **test_combat_status_segments.py** (23 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **message_with_segments()** (22 connections) — `server/constants/message_segments.py`
- **get_npc_disposition_from_instance()** (22 connections) — `server/utils/npc_disposition_lookup.py`
- **message_formatters.py** (22 connections) — `server/realtime/message_formatters.py`
- **player_event_handlers_utils.py** (21 connections) — `server/realtime/player_event_handlers_utils.py`
- **message_builders.py** (20 connections) — `server/realtime/message_builders.py`
- **combat_broadcasts.py** (20 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **MessageSegment** (19 connections) — `server/constants/message_segments.py`
- **test_message_builders.py** (18 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_look_room_segments.py** (17 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **npc_disposition_lookup.py** (17 connections) — `server/utils/npc_disposition_lookup.py`
- **_execute_combat_action()** (15 connections) — `server/commands/combat_attack.py`
- **join_parts()** (15 connections) — `server/constants/message_segments.py`
- **test_npc_disposition_wire.py** (15 connections) — `server/tests/unit/realtime/test_npc_disposition_wire.py`
- **test_room_subscription_manager_npcs.py** (15 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **_execute_phantom_combat_action()** (14 connections) — `server/commands/combat_attack.py`
- *... and 181 more nodes in this community*

## Relationships

- [event_handler.py](event_handler.py.md) (32 shared connections)
- [AttributeError](AttributeError.md) (24 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (22 shared connections)
- [CombatService](CombatService.md) (20 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (19 shared connections)
- [MessageCategory](MessageCategory.md) (18 shared connections)
- [test_look_room.py](test_look_room.py.md) (17 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (16 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (16 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (11 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (10 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/commands/look_room.py`
- `server/constants/message_segments.py`
- `server/constants/npc_disposition.py`
- `server/realtime/connection_utils.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_builders.py`
- `server/realtime/message_formatters.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/occupant_formatter.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/commands/test_combat_attack_segments.py`
- `server/tests/unit/commands/test_look_room_segments.py`
- `server/tests/unit/constants/test_message_segments.py`
- `server/tests/unit/constants/test_npc_disposition.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_npc_disposition_wire.py`

## Audit Trail

- EXTRACTED: 709 (87%)
- INFERRED: 102 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*