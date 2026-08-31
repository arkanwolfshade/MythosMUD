# EmoteService

> 41 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (18 connections) — `server/tests/unit/game/test_emote_service.py`
- **emote_service.py** (16 connections) — `server/game/emote_service.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **test_load_emotes_handles_missing_table_gracefully()** (4 connections) — `server/tests/unit/game/test_emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.load_emotes()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **test_emote_service_init_does_not_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_load_emotes_populates_from_repository()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_reload_emotes_calls_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **asyncio** (3 connections)
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **test_format_emote_messages()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_is_emote_alias_and_get_definition()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_list_available_emotes()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_no_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_with_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [test_emote_repository.py](test_emote_repository.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [error_logging.py](error_logging.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 78 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*