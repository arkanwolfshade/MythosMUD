# session

> 82 nodes · cohesion 0.04

## Key Concepts

- **OccupantFormatter** (42 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter.py** (33 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **NpcOccupant** (28 connections) — `server/constants/npc_disposition.py`
- **occupant_formatter.py** (10 connections) — `server/realtime/occupant_formatter.py`
- **._is_uuid_string()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **.separate_occupants_by_type()** (6 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_valid()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_chars()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_dashes()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_length()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_valid()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_fallback_name()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_player()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_unknown_disposition_falls_back_to_passive()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._add_valid_name_to_lists()** (3 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **Any** (3 connections)
- **NpcOccupant** (3 connections)
- *... and 57 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (12 shared connections)
- [ChatHistoryPanel.tsx](ChatHistoryPanel.tsx.md) (5 shared connections)
- [security.ts](security.ts.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [SystemAdminChannelStrategy](SystemAdminChannelStrategy.md) (1 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (1 shared connections)

## Source Files

- `server/constants/npc_disposition.py`
- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 154 (90%)
- INFERRED: 18 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*