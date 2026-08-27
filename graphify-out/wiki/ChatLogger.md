# ChatLogger

> 45 nodes

## Key Concepts

- **RealTimeEventHandler** (32 connections) — `server/realtime/event_handler.py`
- **._create_player_entered_message()** (4 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (4 connections) — `server/realtime/event_handler.py`
- **Any** (4 connections)
- **._get_room_occupants()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **._send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **._send_room_occupants_update_internal()** (3 connections) — `server/realtime/event_handler.py`
- **._subscribe_to_events()** (3 connections) — `server/realtime/event_handler.py`
- **test_event_handler_init()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **._get_next_sequence()** (2 connections) — `server/realtime/event_handler.py`
- **.shutdown()** (2 connections) — `server/realtime/event_handler.py`
- **UUID** (2 connections)
- **Delegate player XP awarded event to specialized handler.** (2 connections) — `server/realtime/event_handler.py`
- *... and 20 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (14 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (2 shared connections)
- [run-vitest.js](run-vitest.js.md) (1 shared connections)
- [FStringLoggingFixer](FStringLoggingFixer.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 69 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*