# AliasStorage

> God node · 248 connections · `server/alias_storage.py`

**Community:** [AliasStorage](AliasStorage.md)

## Connections by Relation

### calls
- _ensure_alias_storage() `EXTRACTED`
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`

### contains
- [alias_storage.py](alias_storage.py.md) `EXTRACTED`

### imports
- [command_service.py](command_service.py.md) `EXTRACTED`
- [admin_setstat_command.py](admin_setstat_command.py.md) `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- player_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- [rescue_commands.py](rescue_commands.py.md) `EXTRACTED`
- admin_commands.py `EXTRACTED`
- quest_commands.py `EXTRACTED`
- admin_shutdown_command.py `EXTRACTED`
- [catalog_commands.py](catalog_commands.py.md) `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- [combat_assist.py](combat_assist.py.md) `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`

### method
- ._fetch() `EXTRACTED`
- .create_alias() `EXTRACTED`
- ._call_scalar() `EXTRACTED`
- .get_player_aliases() `EXTRACTED`
- .get_alias() `EXTRACTED`
- .remove_alias() `EXTRACTED`
- .delete_player_aliases_by_id() `EXTRACTED`
- .validate_alias_name() `EXTRACTED`
- .validate_alias_command() `EXTRACTED`

### rationale_for
- Player alias persistence backed by the ``player_aliases`` table. Aliases are… `EXTRACTED`

### references
- _handle_admin_set_stat_command() `EXTRACTED`
- handle_ground_command() `EXTRACTED`
- handle_alias_command() `EXTRACTED`
- handle_logout_command() `EXTRACTED`
- handle_teleport_command() `EXTRACTED`
- handle_party_command() `EXTRACTED`
- handle_rest_command() `EXTRACTED`
- _handle_admin_hallucinate_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- handle_goto_command() `EXTRACTED`
- handle_quest_command() `EXTRACTED`
- handle_whisper_command() `EXTRACTED`
- handle_unequip_command() `EXTRACTED`
- handle_pray_command() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- _handle_admin_set_lucidity_command() `EXTRACTED`
- handle_deposit_command() `EXTRACTED`
- handle_debrief_command() `EXTRACTED`
- handle_follow_command() `EXTRACTED`
- handle_get_command() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- TestHelperFunctions `INFERRED`
- [MagicCommandHandler](MagicCommandHandler.md) `INFERRED`
- handle_read_command() `INFERRED`
- _prepare_command_for_processing() `INFERRED`
- handle_teach_command() `INFERRED`
- process_command_unified() `INFERRED`
- _handle_special_command_routing() `INFERRED`
- _process_alias_expansion() `INFERRED`
- run_handle_protect_command() `INFERRED`
- run_handle_assist_command() `INFERRED`
- run_handle_taunt_command() `INFERRED`
- _run_expanded_alias() `INFERRED`
- handle_kick_command() `INFERRED`
- handle_punch_command() `INFERRED`
- handle_strike_command() `INFERRED`
- handle_cast_command() `INFERRED`
- handle_learn_command() `INFERRED`
- handle_spell_command() `INFERRED`
- handle_spells_command() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*