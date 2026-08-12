# AliasStorage

> God node · 217 connections · `server/alias_storage.py`

**Community:** [AliasStorage](AliasStorage.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`
- test_alias_storage_creates_directory() `EXTRACTED`
- test_alias_storage_init_with_env_var() `EXTRACTED`
- test_alias_storage_init_with_storage_dir() `EXTRACTED`
- test_alias_storage_init_without_env_var() `EXTRACTED`

### contains
- [alias_storage.py](alias_storage.py.md) `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- [test_alias_storage.py](test_alias_storage.py.md) `EXTRACTED`
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) `EXTRACTED`
- [command_handler_unified.py](command_handler_unified.py.md) `EXTRACTED`
- combat_handler.py `EXTRACTED`
- [inventory_equip_command.py](inventory_equip_command.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [admin_shutdown_command.py](admin_shutdown_command.py.md) `EXTRACTED`
- [inventory_pickup_command.py](inventory_pickup_command.py.md) `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- [quest_commands.py](quest_commands.py.md) `EXTRACTED`
- [websocket_handler_commands.py](websocket_handler_commands.py.md) `EXTRACTED`
- communication_commands.py `EXTRACTED`
- [admin_setlucidity_command.py](admin_setlucidity_command.py.md) `EXTRACTED`

### method
- .get_player_aliases() `EXTRACTED`
- .save_player_aliases() `EXTRACTED`
- .create_alias() `EXTRACTED`
- ._validate_alias_payload() `EXTRACTED`
- ._get_alias_file_path() `EXTRACTED`
- ._save_alias_data() `EXTRACTED`
- .add_alias() `EXTRACTED`
- ._load_alias_data() `EXTRACTED`
- .remove_alias() `EXTRACTED`
- .get_alias() `EXTRACTED`
- .get_alias_count() `EXTRACTED`
- .backup_aliases() `EXTRACTED`
- .clear_aliases() `EXTRACTED`
- .validate_alias_name() `EXTRACTED`
- .validate_alias_command() `EXTRACTED`
- .delete_player_aliases() `EXTRACTED`
- .list_alias_files() `EXTRACTED`
- .__init__() `EXTRACTED`

### rationale_for
- Manages player alias storage in JSON files. Each player's aliases are stored in… `EXTRACTED`

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
- _process_alias_expansion() `EXTRACTED`
- process_command_unified() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- handle_teleport_command() `EXTRACTED`
- handle_follow_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- handle_pickup_command() `EXTRACTED`
- _handle_special_command_routing() `EXTRACTED`
- handle_say_command() `EXTRACTED`
- handle_npc_command() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- MagicCommandHandler `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TauntCommandHandler `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- [SchemaValidator](SchemaValidator.md) `INFERRED`
- _NpcWithLife `INFERRED`
- SpellCommandError `INFERRED`
- [CommandRequest](CommandRequest.md) `INFERRED`
- TestHandleSpecialCommandRouting `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*