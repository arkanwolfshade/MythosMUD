# NPCEnteredRoom

> 73 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **datetime** (15 connections)
- **get_mythos_chronicle()** (13 connections) — `server/time/time_service.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleLike** (9 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **cleanup_decayed_corpses()** (8 connections) — `server/app/game_tick_corpses.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_corpses.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- *... and 48 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (9 shared connections)
- [Memory Leak Prevention System - Implementation Summary](Memory_Leak_Prevention_System_-_Implementation_Summary.md) (7 shared connections)
- [Cursor Subagents Overview](Cursor_Subagents_Overview.md) (3 shared connections)
- [executeCommand](executeCommand.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_item_instance_persistence.py](test_item_instance_persistence.py.md) (2 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (2 shared connections)
- [RoomInfoPanel.tsx](RoomInfoPanel.tsx.md) (2 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 185 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*