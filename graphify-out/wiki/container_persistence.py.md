# container_persistence.py

> 85 nodes

## Key Concepts

- **UserManager** (67 connections) — `server/services/user_manager.py`
- **UUID** (37 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.mute_global()** (7 connections) — `server/services/user_manager.py`
- **.mute_player()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.is_admin()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- *... and 60 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [room_validator/schemas/unified_room_schema.json](room_validator-schemas-unified_room_schema.json.md) (7 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (5 shared connections)
- [properties](properties.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [npc_schedules.schema.json](npc_schedules.schema.json.md) (1 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)
- [ContainerRepository](ContainerRepository.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 214 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*