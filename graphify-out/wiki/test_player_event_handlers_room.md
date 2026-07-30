# test player event handlers room

> 56 nodes

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
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_taunt.py`
- *... and 31 more nodes in this community*

## Relationships

- [.end combat()](end_combat%28%29.md) (12 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (6 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (6 shared connections)
- [test magic commands](test_magic_commands.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [close db()](close_db%28%29.md) (5 shared connections)
- [combat](combat.md) (3 shared connections)
- [test command service](test_command_service.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*