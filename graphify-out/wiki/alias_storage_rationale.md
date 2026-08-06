# alias storage rationale

> 186 nodes

## Key Concepts

- **AliasStorage** (283 connections) — `server/alias_storage.py`
- **test_alias_storage.py** (67 connections) — `server/tests/unit/test_alias_storage.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (20 connections)
- **magic_service()** (13 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **Path** (11 connections)
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **Any** (6 connections)
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- **._resolve_learn_context()** (5 connections) — `server/commands/magic_commands.py`
- **test_alias_storage_init_with_env_var()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 161 more nodes in this community*

## Relationships

- [alias models rationale](alias_models_rationale.md) (33 shared connections)
- [realtime real time](realtime_real_time.md) (24 shared connections)
- [commands npc admin](commands_npc_admin.md) (23 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (17 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (16 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (15 shared connections)
- [player model models](player_model_models.md) (13 shared connections)
- [commands admin mute](commands_admin_mute.md) (11 shared connections)
- [rest grace period](rest_grace_period.md) (9 shared connections)
- [rescue service services](rescue_service_services.md) (8 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (8 shared connections)
- [commands whisper command](commands_whisper_command.md) (7 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/combat_handler.py`
- `server/commands/magic_commands.py`
- `server/realtime/request_context.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 863 (94%)
- INFERRED: 57 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*