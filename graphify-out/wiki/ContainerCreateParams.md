# ContainerCreateParams

> 58 nodes

## Key Concepts

- **ContainerCreateParams** (41 connections) — `server/persistence/container_create_params.py`
- **test_bank_service.py** (24 connections) — `server/tests/unit/services/test_bank_service.py`
- **get_or_create_bank_box()** (18 connections) — `server/services/bank_service.py`
- **FakeBankPersistence** (15 connections) — `server/tests/unit/services/test_bank_service.py`
- **container_create_params.py** (14 connections) — `server/persistence/container_create_params.py`
- **forward_to_bank_box()** (13 connections) — `server/services/bank_service.py`
- **BankBoxPersistence** (12 connections) — `server/services/bank_service.py`
- **test_deleting_the_owner_leaves_an_orphaned_box_nobody_can_look_up()** (12 connections) — `server/tests/integration/test_bank_box_persistence.py`
- **test_box_is_created_once_and_stacks_persist_in_order_without_trimming()** (11 connections) — `server/tests/integration/test_bank_box_persistence.py`
- **test_each_owner_has_their_own_box_and_the_database_allows_only_one_each()** (11 connections) — `server/tests/integration/test_bank_box_persistence.py`
- **_create_player()** (10 connections) — `server/tests/integration/test_bank_box_persistence.py`
- **is_bank_room()** (8 connections) — `server/services/bank_service.py`
- **_cleanup()** (8 connections) — `server/tests/integration/test_bank_box_persistence.py`
- **asyncio** (7 connections)
- **test_a_create_failure_with_no_box_to_fall_back_on_is_raised()** (6 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_forward_over_fills_a_full_box_rather_than_evicting()** (6 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_forward_creates_the_box_when_the_player_has_none()** (5 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_losing_a_create_race_uses_the_winners_box()** (5 connections) — `server/tests/unit/services/test_bank_service.py`
- **UUID** (5 connections)
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **test_create_container_wraps_psycopg2_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **.create_container()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_each_player_gets_their_own_box()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_first_use_creates_a_bank_box_owned_by_the_player()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (35 shared connections)
- [Room](Room.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (7 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (6 shared connections)
- [ContainerData](ContainerData.md) (5 shared connections)
- [ContainerRepository](ContainerRepository.md) (5 shared connections)
- [alias_storage.py](alias_storage.py.md) (5 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (4 shared connections)
- [session_factory](session_factory.md) (3 shared connections)
- [WearableContainerService](WearableContainerService.md) (2 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (2 shared connections)
- [container_query_helpers_async.py](container_query_helpers_async.py.md) (2 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/services/bank_service.py`
- `server/tests/integration/test_bank_box_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/tests/unit/services/test_bank_service.py`
- `server/tests/unit/services/test_room_furniture_loader.py`

## Audit Trail

- EXTRACTED: 184 (90%)
- INFERRED: 20 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*