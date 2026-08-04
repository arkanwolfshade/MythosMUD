# auth rationale access

> 137 nodes

## Key Concepts

- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **TestEmitTransferEventDirections** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **UUID** (6 connections)
- **UUID** (5 connections)
- **Any** (5 connections)
- **Any** (4 connections)
- **.test_emit_transfer_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 112 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (32 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (31 shared connections)
- [task registry app](task_registry_app.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [tick game processing](tick_game_processing.md) (1 shared connections)
- [services npc startup](services_npc_startup.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 488 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*