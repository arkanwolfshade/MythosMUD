# NPC Utility Functions

> 13 nodes · cohesion 0.15

## Key Concepts

- **extract_room_id_from_npc()** (11 connections) — `server/npc/npc_utils.py`
- **Any** (3 connections)
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Extract room ID from NPC instance with fallback logic.      Args:         npc_in** (1 connections) — `server/npc/npc_utils.py`
- **Test extract_room_id_from_npc() extracts from current_room.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() extracts from current_room_id.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() extracts from room_id.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() returns 'unknown' when not found.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() returns 'unknown' for non-string value.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Facades Implementation Summary](Facades_Implementation_Summary.md) (1 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (1 shared connections)
- [E 2 E Scenario Whisper](E_2_E_Scenario_Whisper.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*