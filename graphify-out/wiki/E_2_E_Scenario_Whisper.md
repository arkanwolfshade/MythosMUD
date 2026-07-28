# E 2 E Scenario Whisper

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

- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [Facades Implementation Summary](Facades_Implementation_Summary.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*