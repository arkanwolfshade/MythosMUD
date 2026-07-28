# Container Component Capacity

> 261 nodes · cohesion 0.01

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **container.py** (25 connections) — `server/models/container.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **ContainerLockState** (14 connections) — `server/models/container.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **environmental_container_loader.py** (13 connections) — `server/services/environmental_container_loader.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- *... and 236 more nodes in this community*

## Relationships

- [Container API Endpoints](Container_API_Endpoints.md) (60 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (27 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (25 shared connections)
- [Communication Command Handlers](Communication_Command_Handlers.md) (18 shared connections)
- [Persistence Refactoring Complete](Persistence_Refactoring_Complete.md) (16 shared connections)
- [Container Open Events](Container_Open_Events.md) (15 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (10 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (5 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 1020 (91%)
- INFERRED: 104 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*