# AliasStorage

> God node · 230 connections · `server/alias_storage.py`

**Community:** [Client Event Store](Client_Event_Store.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`
- test_alias_storage_creates_directory() `EXTRACTED`
- test_alias_storage_init_with_env_var() `EXTRACTED`
- test_alias_storage_init_with_storage_dir() `EXTRACTED`
- test_alias_storage_init_without_env_var() `EXTRACTED`

### contains
- alias_storage.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- test_alias_storage.py `EXTRACTED`
- test_admin_shutdown_command.py `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- player_service.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`
- look_command.py `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- quest_commands.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- communication_commands.py `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`

### indirect_call
- .test_ensure_alias_storage_provided() `INFERRED`

### method
- .get_player_aliases() `EXTRACTED`
- .create_alias() `EXTRACTED`
- ._get_alias_file_path() `EXTRACTED`
- .save_player_aliases() `EXTRACTED`
- ._validate_alias_payload() `EXTRACTED`
- .add_alias() `EXTRACTED`
- ._load_alias_data() `EXTRACTED`
- ._save_alias_data() `EXTRACTED`
- .backup_aliases() `EXTRACTED`
- .get_alias() `EXTRACTED`
- .get_alias_count() `EXTRACTED`
- .remove_alias() `EXTRACTED`
- .clear_aliases() `EXTRACTED`
- .delete_player_aliases() `EXTRACTED`
- .validate_alias_command() `EXTRACTED`
- .validate_alias_name() `EXTRACTED`
- .__init__() `EXTRACTED`
- .list_alias_files() `EXTRACTED`

### rationale_for
- Manages player alias storage in JSON files.      Each player's aliases are store `EXTRACTED`

### references
- _handle_admin_set_stat_command() `EXTRACTED`
- handle_ground_command() `EXTRACTED`
- handle_alias_command() `EXTRACTED`
- handle_logout_command() `EXTRACTED`
- handle_read_command() `EXTRACTED`
- handle_pray_command() `EXTRACTED`
- handle_rest_command() `EXTRACTED`
- _prepare_command_for_processing() `EXTRACTED`
- handle_whisper_command() `EXTRACTED`
- handle_quest_command() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- handle_teleport_command() `EXTRACTED`
- _process_alias_expansion() `EXTRACTED`
- process_command_unified() `EXTRACTED`
- _handle_special_command_routing() `EXTRACTED`
- handle_follow_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- handle_pickup_command() `EXTRACTED`
- handle_say_command() `EXTRACTED`
- handle_npc_command() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- MagicCommandHandler `INFERRED`
- TestHelperFunctions `INFERRED`
- SchemaValidator `INFERRED`
- TauntCommandHandler `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- Any `INFERRED`
- _NpcWithLife `INFERRED`
- Any `INFERRED`
- SpellCommandError `INFERRED`
- CommandRequest `INFERRED`
- CommandExecutionRequest `INFERRED`
- Any `INFERRED`
- TestHandleSpecialCommandRouting `INFERRED`
- Any `INFERRED`
- UUID `INFERRED`
- Path `INFERRED`
- AppWithState `INFERRED`
- Any `INFERRED`
- AppWithState `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*