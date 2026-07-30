# APIRouter

> 376 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **container.py** (25 connections) — `server/models/container.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 351 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (124 shared connections)
- [BaseCommand](BaseCommand.md) (31 shared connections)
- [Room](Room.md) (30 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (29 shared connections)
- [Connection Manager](Connection_Manager.md) (17 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (15 shared connections)
- [Lock](Lock.md) (12 shared connections)
- [Player](Player.md) (11 shared connections)
- [world](world.md) (11 shared connections)
- [close db()](close_db%28%29.md) (10 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/models/container.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 1552 (92%)
- INFERRED: 143 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*