# websocket handler realtime

> 58 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **UUID** (6 connections)
- **_validate_taunt_target_name()** (6 connections) — `server/commands/combat_taunt.py`
- **_RoomWithIdOnly** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_taunt.py`
- **AppWithState** (4 connections)
- **.resolve_combat_target()** (4 connections) — `server/commands/combat_taunt.py`
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_taunt.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- *... and 33 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (13 shared connections)
- [spell game magic](spell_game_magic.md) (12 shared connections)
- [Item Instances](Item_Instances.md) (7 shared connections)
- [command factories exploration](command_factories_exploration.md) (6 shared connections)
- [commands npc admin](commands_npc_admin.md) (5 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (2 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 244 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*