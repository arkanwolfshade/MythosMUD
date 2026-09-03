# Emote Service

> 52 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (18 connections) — `server/tests/unit/game/test_emote_service.py`
- **emote_service.py** (16 connections) — `server/game/emote_service.py`
- **EmoteRepository** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **emote_repository.py** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **.get_emote_aliases()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **.get_emotes()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **test_load_emotes_handles_missing_table_gracefully()** (4 connections) — `server/tests/unit/game/test_emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.load_emotes()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **test_emote_service_init_does_not_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_load_emotes_populates_from_repository()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_reload_emotes_calls_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **asyncio** (3 connections)
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [Wearable Container Service](Wearable_Container_Service.md) (8 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (4 shared connections)
- [Alias Storage](Alias_Storage.md) (4 shared connections)
- [Test Emote Repository](Test_Emote_Repository.md) (3 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`
- `server/persistence/repositories/emote_repository.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 107 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*