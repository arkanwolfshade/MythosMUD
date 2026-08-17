# AliasStorage

> God node · 250 connections · `server/alias_storage.py`

**Community:** [server alias storage aliasstorage](server_alias_storage_aliasstorage.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`

### contains
- alias_storage.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- test_alias_storage.py `EXTRACTED`
- test_admin_shutdown_command.py `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- player_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- quest_commands.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`
- communication_commands.py `EXTRACTED`
- go_command.py `EXTRACTED`

### method
- .get_player_aliases() `EXTRACTED`
- .get_alias_file_path() `EXTRACTED`
- ._load_alias_data() `EXTRACTED`
- ._save_alias_data() `EXTRACTED`
- .save_player_aliases() `EXTRACTED`
- .create_alias() `EXTRACTED`
- ._validate_alias_payload() `EXTRACTED`
- .add_alias() `EXTRACTED`
- .remove_alias() `EXTRACTED`
- .get_alias() `EXTRACTED`
- .get_alias_count() `EXTRACTED`
- .backup_aliases() `EXTRACTED`
- ._resolved_alias_open_path() `EXTRACTED`
- .clear_aliases() `EXTRACTED`
- .validate_alias_name() `EXTRACTED`
- .validate_alias_command() `EXTRACTED`
- .delete_player_aliases() `EXTRACTED`
- .__init__() `EXTRACTED`
- .list_alias_files() `EXTRACTED`

### rationale_for
- Manages player alias storage in JSON files. Each player's aliases are stored in… `EXTRACTED`

### references
- _handle_admin_set_stat_command() `EXTRACTED`
- handle_teleport_command() `EXTRACTED`
- handle_ground_command() `EXTRACTED`
- handle_alias_command() `EXTRACTED`
- handle_logout_command() `EXTRACTED`
- handle_pray_command() `EXTRACTED`
- handle_party_command() `EXTRACTED`
- handle_rest_command() `EXTRACTED`
- handle_goto_command() `EXTRACTED`
- handle_whisper_command() `EXTRACTED`
- handle_debrief_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- handle_quest_command() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- handle_unequip_command() `EXTRACTED`
- _handle_admin_set_lucidity_command() `EXTRACTED`
- handle_follow_command() `EXTRACTED`
- handle_pickup_command() `EXTRACTED`
- handle_npc_command() `EXTRACTED`
- handle_say_command() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- TestHelperFunctions `INFERRED`
- handle_read_command() `INFERRED`
- _prepare_command_for_processing() `INFERRED`
- _process_alias_expansion() `INFERRED`
- process_command_unified() `INFERRED`
- handle_teach_command() `INFERRED`
- _handle_special_command_routing() `INFERRED`
- run_handle_taunt_command() `INFERRED`
- _ensure_alias_storage() `INFERRED`
- handle_kick_command() `INFERRED`
- handle_punch_command() `INFERRED`
- handle_strike_command() `INFERRED`
- process_command() `INFERRED`
- handle_attack_command() `INFERRED`
- handle_flee_command() `INFERRED`
- handle_taunt_command() `INFERRED`
- alias_storage() `INFERRED`
- test_alias_storage_init_with_env_var() `INFERRED`
- test_backup_aliases_custom_dir() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*