# AliasStorage

> God node · 132 connections · `server/alias_storage.py`

**Community:** [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md)

## Connections by Relation

### calls
- _ensure_alias_storage() `EXTRACTED`
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
- inventory_equip_command.py `EXTRACTED`
- look_command.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- player_service.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- router.py `EXTRACTED`
- admin_mute_commands.py `EXTRACTED`
- inventory_get_command.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`
- combat_handler.py `EXTRACTED`

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

### uses
- CombatCommandHandler `INFERRED`
- MagicCommandHandler `INFERRED`
- TestHelperFunctions `INFERRED`
- SchemaValidator `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- Any `INFERRED`
- TauntCommandHandler `INFERRED`
- Any `INFERRED`
- _NpcWithLife `INFERRED`
- [AliasStorage](AliasStorage.md) `INFERRED`
- AppWithState `INFERRED`
- [AliasStorage](AliasStorage.md) `INFERRED`
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- CombatService `INFERRED`
- TargetMatch `INFERRED`
- Any `INFERRED`
- ConnectionManager `INFERRED`
- EventBus `INFERRED`
- PlayerCombatService `INFERRED`
- TargetResolutionResult `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*