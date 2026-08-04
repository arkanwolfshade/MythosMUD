# task registry app

> 437 nodes

## Key Concepts

- **ContainerComponent** (106 connections) — `server/models/container.py`
- **__init__.py** (73 connections) — `server/models/__init__.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (28 connections) — `server/models/container.py`
- **container.py** (26 connections) — `server/models/container.py`
- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **ContainerLockState** (15 connections) — `server/models/container.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 412 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (119 shared connections)
- [Loot Generation](Loot_Generation.md) (30 shared connections)
- [world models rationale](world_models_rationale.md) (17 shared connections)
- [nats services service](nats_services_service.md) (13 shared connections)
- [Database Config](Database_Config.md) (10 shared connections)
- [player requests schemas](player_requests_schemas.md) (9 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [command factories communication](command_factories_communication.md) (4 shared connections)
- [grace period login](grace_period_login.md) (4 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/models/__init__.py`
- `server/models/container.py`
- `server/services/container_websocket_events.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 1607 (92%)
- INFERRED: 138 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*