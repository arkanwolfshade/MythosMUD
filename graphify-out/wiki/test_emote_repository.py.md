# test_emote_repository.py

> 24 nodes

## Key Concepts

- **test_emote_repository.py** (15 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **EmoteRepository** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **emote_repository.py** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **.get_emote_aliases()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **.get_emotes()** (5 connections) — `server/persistence/repositories/emote_repository.py`
- **asyncio** (5 connections)
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emote_aliases()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emotes()** (4 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emote_aliases_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emotes_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **test_get_emotes_empty()** (3 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **_alias_row()** (2 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **_emote_row()** (2 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **Any** (2 connections)
- **fixture** (1 connections)
- **Emote repository for async persistence operations. This module provides async…** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Repository for predefined emote and emote-alias persistence operations.** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Initialize the emote repository.** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Get all predefined emotes from the database. Returns: list[dict]: Rows with…** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Get all emote aliases joined to their owning emote's stable_id. Returns:…** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Unit tests for EmoteRepository (#624).** (1 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (5 shared connections)
- [EmoteService](EmoteService.md) (3 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [error_logging.py](error_logging.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/emote_repository.py`
- `server/tests/unit/persistence/repositories/test_emote_repository.py`

## Audit Trail

- EXTRACTED: 56 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*