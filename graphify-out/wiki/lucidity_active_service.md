# lucidity active service

> 31 nodes

## Key Concepts

- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **test_player_spell_repository.py** (19 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_mock_session_with_rows()** (9 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **.get_player_spells()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.update_mastery()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **UUID** (7 connections)
- **_spell_row()** (6 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_found()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell_no_row_raises()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_record_spell_cast()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **Any** (2 connections)
- **test_row_to_player_spell_maps_fields()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells_db_error()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_missing()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery_not_found()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **Player spell repository for async persistence operations.  This module provides** (1 connections) — `server/persistence/repositories/player_spell_repository.py`
- **Map procedure result row to PlayerSpell model.** (1 connections) — `server/persistence/repositories/player_spell_repository.py`
- *... and 6 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (11 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (9 shared connections)
- [player room realtime](player_room_realtime.md) (8 shared connections)
- [add used user](add_used_user.md) (7 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (1 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)
- [room occupant manager](room_occupant_manager.md) (1 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 142 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*