# APIRouter

> 188 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (15 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **audit_logger.py** (11 connections) — `server/utils/audit_logger.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **containers.py** (9 connections) — `server/api/containers.py`
- **register_loot_endpoints()** (8 connections) — `server/api/container_endpoints_loot.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_loot_all_items_container_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_transfer_all_items_from_container_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 163 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (51 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (37 shared connections)
- [BaseCommand](BaseCommand.md) (36 shared connections)
- [Room](Room.md) (21 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (15 shared connections)
- [datetime](datetime.md) (14 shared connections)
- [metrics](metrics.md) (12 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (7 shared connections)
- [real time](real_time.md) (6 shared connections)
- [test path validator](test_path_validator.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/models/container.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 764 (87%)
- INFERRED: 114 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*