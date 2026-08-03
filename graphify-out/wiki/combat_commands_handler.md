# combat commands handler

> 52 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **Any** (6 connections)
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (6 connections) — `server/commands/combat_handler.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_handler.py`
- **.room_forbids_combat()** (3 connections) — `server/commands/combat_handler.py`
- **.get_room_data()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_combat_action()** (3 connections) — `server/commands/combat_handler.py`
- **test_attack_command_allowed_after_grace_period()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_when_incapacitated()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **Handler for combat-related commands.     Processes combat commands and integrat** (1 connections) — `server/commands/combat_handler.py`
- **Movement service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- *... and 27 more nodes in this community*

## Relationships

- [combat commands handler](combat_commands_handler.md) (9 shared connections)
- [combat helpers commands](combat_helpers_commands.md) (7 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [container helpers loot](container_helpers_loot.md) (6 shared connections)
- [grace period login](grace_period_login.md) (4 shared connections)
- [spell game magic](spell_game_magic.md) (3 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [game weapon player](game_weapon_player.md) (2 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 141 (81%)
- INFERRED: 33 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*