# test_nats_message_handler_subzone_events.py

> 65 nodes

## Key Concepts

- **NPCThreadManager** (59 connections) — `server/npc/threading.py`
- **test_npc_thread_manager_internals.py** (33 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **asyncio** (17 connections)
- **._parse_behavior_config()** (7 connections) — `server/npc/threading.py`
- **test_bridge_send_message_to_npc_swallows_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_no_instance_service()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_npc_not_active()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_success()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_inner_execute_error()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_outer_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_dict_attr()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_invalid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_json_non_dict()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_valid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_process_wander_action_handles_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_process_wander_action_returns_early_when_unresolved()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_restart_npc_thread_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_start_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_stop_cancels_active_threads_via_gather()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_stop_npc_thread_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_stop_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_worker_handles_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_worker_processes_message_and_executes_behavior_then_stops()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_worker_stops_cleanly_on_cancellation()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_wander_movement_no_async_persistence_logs_and_returns()** (3 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- *... and 40 more nodes in this community*

## Relationships

- [player_service](player_service.md) (12 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Mansions_of_Madness__Vol_1_-_Behind_Closed_Doors__2026-08-12.md) (8 shared connections)
- [Respawn Death Screen Loop Limbo ID Mismatch](Respawn_Death_Screen_Loop_Limbo_ID_Mismatch.md) (5 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [fixtures/shared/__init__.py](fixtures-shared-__init__.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_thread_manager_internals.py`

## Audit Trail

- EXTRACTED: 113 (79%)
- INFERRED: 30 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*