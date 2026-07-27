# Combat Command Handler

> 24 nodes · cohesion 0.01

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **UUID** (19 connections) — `server/services/player_combat_service.py`
- **Any** (17 connections) — `server/commands/combat_handler.py`
- **AppWithState** (16 connections) — `server/commands/combat_handler.py`
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **Room** (6 connections) — `server/npc/spawning_request_execution.py`
- **AppWithState** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **Any** (4 connections) — `server/validators/combat_validator.py`
- **.async_list_rooms()** (3 connections) — `server/async_persistence.py`
- **.list_rooms()** (3 connections) — `server/async_persistence.py`
- **UUID** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.close()** (2 connections) — `server/async_persistence.py`
- **.expire_player_effects_for_tick()** (2 connections) — `server/async_persistence.py`
- **.get_room_by_id()** (2 connections) — `server/async_persistence.py`
- **.item_instance_exists()** (2 connections) — `server/async_persistence.py`
- **List all rooms from the cache. Delegates to RoomRepository.          Returns:** (2 connections) — `server/async_persistence.py`
- **Close and cleanup resources.          Note: SQLAlchemy async sessions are manage** (1 connections) — `server/async_persistence.py`
- **Get a room by ID. Checks instance manager first, then cache.          Instanced** (1 connections) — `server/async_persistence.py`
- **Expire effects for current tick; return list of (player_id, effect_type) expired** (1 connections) — `server/async_persistence.py`
- **Create a new container.          Args:             source_type: Type of containe** (1 connections) — `server/async_persistence.py`
- **Async persistence layer using SQLAlchemy ORM for true async PostgreSQL operation** (1 connections) — `server/async_persistence.py`
- **Check if an item instance exists. Delegates to ItemRepository.** (1 connections) — `server/async_persistence.py`
- **Reset the global async persistence instance for testing.      DEPRECATED: Use Ap** (1 connections) — `server/async_persistence.py`

## Relationships

- [Async Persistence Layer](Async_Persistence_Layer.md) (17 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (13 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (13 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (4 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (3 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (3 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/commands/combat_handler.py`
- `server/npc/spawning_request_execution.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 165 (57%)
- INFERRED: 122 (43%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*