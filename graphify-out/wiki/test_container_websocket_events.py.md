# test_container_websocket_events.py

> 69 nodes

## Key Concepts

- **test_container_websocket_events.py** (32 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **game_tick_corpses.py** (24 connections) — `server/app/game_tick_corpses.py`
- **container_websocket_events.py** (19 connections) — `server/services/container_websocket_events.py`
- **asyncio** (16 connections)
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **_async_attr()** (14 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **emit_container_updated()** (13 connections) — `server/services/container_websocket_events.py`
- **ContainerConnectionManagerLike** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (11 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (11 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **emit_container_created()** (7 connections) — `server/services/container_websocket_events.py`
- **_real_container_with_datetime()** (7 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **UUID** (7 connections)
- **test_emit_container_created()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_created_payload_is_json_serializable()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_with_owner()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_no_room_id()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated_payload_is_json_serializable()** (6 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_no_room_id()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_returns_stats()** (5 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 44 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (24 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (9 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 184 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*