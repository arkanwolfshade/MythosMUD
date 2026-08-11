# Game Client Container

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

- [Magic Service Bundle](Magic_Service_Bundle.md) (21 shared connections)
- [Container Open Events](Container_Open_Events.md) (7 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (7 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (6 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (4 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Health Check Models](Health_Check_Models.md) (1 shared connections)

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