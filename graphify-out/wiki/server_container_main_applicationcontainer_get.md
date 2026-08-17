# server container main applicationcontainer get

> 99 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
- **UUID** (37 connections)
- **.get_instance()** (32 connections) — `server/container/main.py`
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **.is_admin()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **.add_admin()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- *... and 74 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (4 shared connections)
- [server container main applicationcontainer reset](server_container_main_applicationcontainer_reset.md) (4 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (3 shared connections)
- [server services npc startup service](server_services_npc_startup_service.md) (3 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (2 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (2 shared connections)
- [healthstatus](healthstatus.md) (2 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 250 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*