# extract_npc_metadata

> 12 nodes · cohesion 0.17

## Key Concepts

- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **test_extract_npc_metadata_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_non_string_type()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_none_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_truthy_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_valid()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Extract NPC type and required status from NPC instance.      Args:         npc_i** (1 connections) — `server/npc/npc_utils.py`
- **Test extract_npc_metadata() handles None is_required.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_npc_metadata() extracts valid metadata.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_npc_metadata() returns defaults when missing.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_npc_metadata() handles non-string npc_type.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_npc_metadata() converts truthy is_required.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (6 shared connections)
- [.despawn_npc](despawn_npc.md) (2 shared connections)
- [npc_utils.py](npc_utils.py.md) (1 shared connections)
- [extract_room_id_from_npc](extract_room_id_from_npc.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*