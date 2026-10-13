# Community 387

> 45 nodes

## Key Concepts

- **test_alias_storage.py** (19 connections) — `server/tests/unit/test_alias_storage.py`
- **_Session** (13 connections) — `server/tests/unit/test_alias_storage.py`
- **._fetch()** (8 connections) — `server/alias_storage.py`
- **_use_session()** (8 connections) — `server/tests/unit/test_alias_storage.py`
- **MonkeyPatch** (8 connections)
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **test_create_alias_refused_at_limit()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_upserts_and_commits()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_calls_procedure_and_maps_row()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_returns_procedure_result()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **asyncio** (7 connections)
- **_Result** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **_row_to_alias()** (6 connections) — `server/alias_storage.py`
- **test_delete_player_aliases_by_id_binds_player_id()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **.get_player_aliases()** (5 connections) — `server/alias_storage.py`
- **_alias_row()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_rejects_invalid_input_without_touching_db()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_database_errors_degrade_to_no_alias()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **Alias** (5 connections)
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **_broken_session_maker()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **.execute()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_row_to_alias_stores_naive_utc()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 20 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (19 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 93 (89%)
- INFERRED: 11 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*