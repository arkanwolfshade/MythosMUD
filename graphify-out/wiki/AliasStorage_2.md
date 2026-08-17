# AliasStorage

> God node · 264 connections · `server/alias_storage.py`

**Community:** [AliasStorage](AliasStorage.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`

### contains
- [alias_storage.py](alias_storage.py.md) `EXTRACTED`

### imports
- [command_service.py](command_service.py.md) `EXTRACTED`
- test_alias_storage.py `EXTRACTED`
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [command_handler_unified.py](command_handler_unified.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- [inventory_equip_command.py](inventory_equip_command.py.md) `EXTRACTED`
- [quest_commands.py](quest_commands.py.md) `EXTRACTED`
- [admin_teleport_commands.py](admin_teleport_commands.py.md) `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- [admin_summon_command.py](admin_summon_command.py.md) `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- admin_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- rescue_commands.py `EXTRACTED`
- [websocket_handler_commands.py](websocket_handler_commands.py.md) `EXTRACTED`
- [combat_taunt.py](combat_taunt.py.md) `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`
- communication_commands.py `EXTRACTED`

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
- handle_look_command() `EXTRACTED`
- _handle_admin_set_lucidity_command() `EXTRACTED`
- handle_follow_command() `EXTRACTED`
- handle_pickup_command() `EXTRACTED`
- handle_npc_command() `EXTRACTED`

### uses
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- TestHelperFunctions `INFERRED`
- MagicCommandHandler `INFERRED`
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
- handle_cast_command() `INFERRED`
- handle_learn_command() `INFERRED`
- handle_spell_command() `INFERRED`
- handle_spells_command() `INFERRED`
- handle_stop_command() `INFERRED`
- process_command() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*