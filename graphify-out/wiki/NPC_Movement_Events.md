# NPC Movement Events

> 149 nodes

## Key Concepts

- **test_message_category_invariants.py** (77 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **MessageBuilder** (34 connections) — `server/realtime/message_builders.py`
- **NPCEventHandler** (32 connections) — `server/realtime/npc_event_handlers.py`
- **_Transport** (25 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **Emitted** (15 connections)
- **_OfflineRespawnHandler** (12 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_as()** (9 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **_drive_combat_publisher()** (8 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_state_handler()** (8 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_StatsPlayer** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **_drive_command_chokepoint()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_setstat_posture()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **test_every_text_event_carries_a_valid_category()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **_client_text_event_types()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_npc_died()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_rest_countdown()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **test_emitter_chooses_the_documented_category()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- *... and 124 more nodes in this community*

## Relationships

- [Game Event Types](Game_Event_Types.md) (10 shared connections)
- [Community 75](Community_75.md) (8 shared connections)
- [Community 136](Community_136.md) (8 shared connections)
- [Community 41](Community_41.md) (7 shared connections)
- [Community 299](Community_299.md) (7 shared connections)
- [Community 98](Community_98.md) (7 shared connections)
- [Community 368](Community_368.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 244](Community_244.md) (4 shared connections)
- [Community 106](Community_106.md) (4 shared connections)
- [Community 144](Community_144.md) (4 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (3 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/movement_integration.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_room_system_message_categories.py`

## Audit Trail

- EXTRACTED: 329 (92%)
- INFERRED: 29 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*