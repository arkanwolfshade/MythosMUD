# EmoteService

> 63 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (17 connections) — `server/tests/unit/game/test_emote_service.py`
- **emote_service.py** (16 connections) — `server/game/emote_service.py`
- **test_emote_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **EmoteRepository** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **.get_emote_aliases()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **.get_emotes()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **asyncio** (5 connections)
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **test_load_emotes_handles_missing_table_gracefully()** (4 connections) — `server/tests/unit/game/test_emote_service.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emote_aliases()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emotes()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.load_emotes()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **test_emote_service_init_does_not_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_load_emotes_populates_from_repository()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (8 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (7 shared connections)
- [ValidationError](ValidationError.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)

## Source Files

- `server/game/emote_service.py`
- `server/persistence/repositories/emote_repository.py`
- `server/tests/unit/game/test_emote_service.py`
- `server/tests/unit/persistence/repositories/test_emote_repository.py`

## Audit Trail

- EXTRACTED: 119 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*