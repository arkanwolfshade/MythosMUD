# Async Persistence

> 151 nodes

## Key Concepts

- **AsyncPersistenceLayer** (171 connections) — `server/async_persistence.py`
- **test_async_persistence_delegates.py** (34 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **asyncio** (22 connections)
- **Player** (20 connections)
- **UUID** (15 connections)
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- **test_apply_corruption_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_fear_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_lucidity_loss_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_damage_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_heal_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_params()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_damage_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_gain_occult_knowledge_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_player_by_user_id_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_heal_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **_ApplicationContainerType** (4 connections) — `server/container/async_persistence_access.py`
- **.ensure_item_instance()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_batch()** (4 connections) — `server/async_persistence.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- *... and 126 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (18 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (12 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (5 shared connections)
- [Async Persistence Room Loader](Async_Persistence_Room_Loader.md) (5 shared connections)
- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (5 shared connections)
- [Test Async Persistence Core](Test_Async_Persistence_Core.md) (4 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (4 shared connections)
- [Test Container Events](Test_Container_Events.md) (4 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (4 shared connections)
- [Item Instance Persistence](Item_Instance_Persistence.md) (4 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/container/async_persistence_access.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 307 (85%)
- INFERRED: 56 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*