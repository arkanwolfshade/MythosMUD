# Community 214

> 71 nodes

## Key Concepts

- **test_room_furniture_loader.py** (26 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_PrototypeRegistry** (20 connections) — `server/commands/look_container.py`
- **sync_room_furniture()** (18 connections) — `server/services/room_furniture_loader.py`
- **FakePersistence** (12 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FakeStartupPersistence** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_foyer()** (11 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **FurniturePersistence** (10 connections) — `server/services/room_furniture_loader.py`
- **initialize_room_furniture()** (10 connections) — `server/services/room_furniture_loader.py`
- **test_furniture_container_created_once_then_refreshed_in_place()** (10 connections) — `server/tests/integration/test_room_furniture_persistence.py`
- **FurnitureStartupPersistence** (8 connections) — `server/services/room_furniture_loader.py`
- **_sync_entry()** (8 connections) — `server/services/room_furniture_loader.py`
- **asyncio** (8 connections)
- **test_initialize_room_furniture_survives_database_error()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_skips_template_rooms_bad_entries_and_non_container_prototypes()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_undeclared_furniture_container_is_kept()** (7 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_room()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_creates_missing_furniture_container()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_initialize_room_furniture_warms_cache_and_syncs()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_refreshes_existing_container_from_prototype_without_touching_items()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **test_up_to_date_container_is_left_alone()** (6 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_furniture_spec()** (5 connections) — `server/services/room_furniture_loader.py`
- **_refresh_container()** (5 connections) — `server/services/room_furniture_loader.py`
- **test_initialize_room_furniture_skips_without_registry()** (5 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- **_furniture_containers()** (4 connections) — `server/services/room_furniture_loader.py`
- **registry()** (4 connections) — `server/tests/unit/services/test_room_furniture_loader.py`
- *... and 46 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (25 shared connections)
- [Community 149](Community_149.md) (4 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (4 shared connections)
- [Community 317](Community_317.md) (3 shared connections)
- [Community 56](Community_56.md) (2 shared connections)
- [Community 253](Community_253.md) (2 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [Community 445](Community_445.md) (1 shared connections)
- [Community 674](Community_674.md) (1 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/game/items/item_factory.py`
- `server/services/room_furniture_loader.py`
- `server/tests/integration/test_room_furniture_persistence.py`
- `server/tests/unit/services/test_room_furniture_loader.py`

## Audit Trail

- EXTRACTED: 164 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*