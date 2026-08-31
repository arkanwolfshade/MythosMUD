# test_room_write_procedures.py

> 31 nodes

## Key Concepts

- **test_room_write_procedures.py** (15 connections) — `server/tests/integration/test_room_write_procedures.py`
- **async_sessionmaker** (12 connections)
- **AsyncSession** (12 connections)
- **asyncio** (11 connections)
- **integration** (11 connections)
- **test_create_room_link_duplicate_direction_raises_integrity_error()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_create_room_link_unknown_room_returns_false()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_create_room_link_writes_a_single_row()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_delete_room_link_missing_exit_returns_false()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_delete_room_link_removes_the_row()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_link_changes_target_and_attributes()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_link_missing_exit_returns_false()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_properties_clears_environment_to_null()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_properties_leaves_environment_alone_when_not_set()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_properties_unknown_room_returns_false()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **test_update_room_properties_writes_and_reads_back()** (7 connections) — `server/tests/integration/test_room_write_procedures.py`
- **room_pair()** (6 connections) — `server/tests/integration/test_room_write_procedures.py`
- **fixture** (1 connections)
- **Integration tests for the room-editor write procedures…** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **update_room_properties() with p_set_environment=TRUE and NULL clears the…** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **p_set_environment=FALSE leaves attributes.environment untouched, regardless of…** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **update_room_properties() on a nonexistent stable_id returns FALSE, no exception.** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **create_room_link() writes exactly one room_links row for the given direction.** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **Create a zone, subzone, and two rooms (source, target) with unique stable_ids.…** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- **A second create_room_link() for the same (from_room, direction) hits the UNIQUE…** (1 connections) — `server/tests/integration/test_room_write_procedures.py`
- *... and 6 more nodes in this community*

## Relationships

- [session_factory](session_factory.md) (12 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_room_write_procedures.py`

## Audit Trail

- EXTRACTED: 74 (86%)
- INFERRED: 12 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*