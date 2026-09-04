# Wearable Container Service

> 156 nodes

## Key Concepts

- **log_and_raise()** (170 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (100 connections) — `server/database.py`
- **player_repository.py** (29 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerRepository** (28 connections) — `server/persistence/repositories/player_repository.py`
- **WearableContainerService** (28 connections) — `server/services/wearable_container_service.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Any** (15 connections)
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **UUID** (14 connections)
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **._require_container_for_lock_ops()** (9 connections) — `server/services/container_service_lock.py`
- **._load_player_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.lock_container()** (8 connections) — `server/services/container_service_lock.py`
- *... and 131 more nodes in this community*

## Relationships

- [Player Skill Repository](Player_Skill_Repository.md) (27 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (26 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (22 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (21 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (18 shared connections)
- [Dialogue Definition Repository](Dialogue_Definition_Repository.md) (12 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (12 shared connections)
- [Test Wearable Container Service](Test_Wearable_Container_Service.md) (10 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (9 shared connections)
- [Item Instance Persistence](Item_Instance_Persistence.md) (9 shared connections)
- [Database](Database.md) (9 shared connections)
- [Movement Service](Movement_Service.md) (9 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/services/container_service_lock.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`
- `server/utils/error_logging.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 629 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*