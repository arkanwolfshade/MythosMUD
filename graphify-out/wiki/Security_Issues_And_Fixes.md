# Security Issues And Fixes

> 14 nodes · cohesion 0.14

## Key Concepts

- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_has_definition_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_definition()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_record()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_no_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_non_int()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Extract definition ID from NPC instance or lifecycle record.      Args:** (1 connections) — `server/npc/npc_utils.py`
- **Test extract_definition_id_from_npc() extracts from NPC instance.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_definition_id_from_npc() returns None for non-int.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_definition_id_from_npc() extracts from lifecycle manager.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_definition_id_from_npc() returns None when no lifecycle record.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_definition_id_from_npc() returns None when record has no definition** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_definition_id_from_npc() returns None when no manager and no defini** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (7 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Facades Implementation Summary](Facades_Implementation_Summary.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*