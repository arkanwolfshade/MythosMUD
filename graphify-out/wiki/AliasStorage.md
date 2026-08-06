# AliasStorage

> God node · 283 connections · `server/alias_storage.py`

**Community:** [alias storage rationale](alias_storage_rationale.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`
- test_alias_storage_init_with_env_var() `EXTRACTED`
- test_alias_storage_creates_directory() `EXTRACTED`
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
- quest_commands.py `EXTRACTED`
- look_command.py `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- communication_commands.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- inventory_get_command.py `EXTRACTED`

### indirect_call
- .test_ensure_alias_storage_provided() `INFERRED`

### method
- .get_player_aliases() `EXTRACTED`
- ._load_alias_data() `EXTRACTED`
- .create_alias() `EXTRACTED`
- .get_alias_file_path() `EXTRACTED`
- ._save_alias_data() `EXTRACTED`
- .save_player_aliases() `EXTRACTED`
- ._validate_alias_payload() `EXTRACTED`
- .add_alias() `EXTRACTED`
- ._resolved_alias_open_path() `EXTRACTED`
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
- handle_teleport_command() `EXTRACTED`
- handle_ground_command() `EXTRACTED`
- handle_read_command() `EXTRACTED`
- handle_logout_command() `EXTRACTED`
- handle_alias_command() `EXTRACTED`
- _prepare_command_for_processing() `EXTRACTED`
- handle_goto_command() `EXTRACTED`
- handle_pray_command() `EXTRACTED`
- handle_party_command() `EXTRACTED`
- handle_rest_command() `EXTRACTED`
- handle_whisper_command() `EXTRACTED`
- handle_quest_command() `EXTRACTED`
- _process_alias_expansion() `EXTRACTED`
- process_command_unified() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- handle_debrief_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- _handle_special_command_routing() `EXTRACTED`
- handle_follow_command() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- MagicCommandHandler `INFERRED`
- TestHelperFunctions `INFERRED`
- TauntCommandHandler `INFERRED`
- SchemaValidator `INFERRED`
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
- AppWithState `INFERRED`
- AppWithState `INFERRED`
- UUID `INFERRED`
- Request `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*