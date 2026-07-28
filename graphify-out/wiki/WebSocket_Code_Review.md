# WebSocket Code Review

> 17 nodes · cohesion 0.12

## Key Concepts

- **Profession** (54 connections) — `server/models/profession.py`
- **test_get_profession_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession_get_stat_requirements_invalid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_repr()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_set_mechanical_effects()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **.is_available_for_selection()** (2 connections) — `server/models/profession.py`
- **.__repr__()** (2 connections) — `server/models/profession.py`
- **Base** (1 connections)
- **Check if profession is available for player selection.** (1 connections) — `server/models/profession.py`
- **Profession model for game data.      Stores profession information including nam** (1 connections) — `server/models/profession.py`
- **String representation of the profession.** (1 connections) — `server/models/profession.py`
- **Test get_professions with successful query.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **Test get_profession_by_id delegates to ProfessionRepository.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **Test set_mechanical_effects stores dict as JSON string.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_profession.py`
- **Test get_stat_requirements returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [Async Persistence Migration](Async_Persistence_Migration.md) (13 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (2 shared connections)
- [Metadata Npc](Metadata_Npc.md) (1 shared connections)
- [Cursor Plans Gladiator](Cursor_Plans_Gladiator.md) (1 shared connections)
- [Services Feature Flag](Services_Feature_Flag.md) (1 shared connections)

## Source Files

- `server/models/profession.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 75 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*