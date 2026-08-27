# utils/layout.ts

> 41 nodes

## Key Concepts

- **player_connection_setup.py** (26 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (19 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup.py** (18 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (11 connections) — `server/realtime/player_connection_setup.py`
- **_manager()** (11 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **asyncio** (11 connections)
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (8 connections) — `server/realtime/player_connection_setup.py`
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_add_player_to_room_silently()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **test_player_connection_setup_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_broadcast_player_entered_game_success_and_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_send_room_occupants_update_paths()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_database_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **_stable_room_id_for_quest()** (4 connections) — `server/realtime/player_connection_setup.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_add_player_to_room_silently_paths()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_ends_combat_on_login()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_room_none_early_return()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_no_service()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_success_and_failure()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- *... and 16 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [chatPanelRuntimeUtils.ts](chatPanelRuntimeUtils.ts.md) (3 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (1 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [Reporter](Reporter.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 118 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*