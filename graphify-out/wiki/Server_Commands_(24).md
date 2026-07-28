# Server Commands (24)

> 62 nodes

## Key Concepts

- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
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
- *... and 37 more nodes in this community*

## Relationships

- [Server Game (2)](Server_Game_%282%29.md) (20 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (13 shared connections)
- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (7 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (6 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (6 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (5 shared connections)
- [Server Services (11)](Server_Services_%2811%29.md) (4 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (4 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (3 shared connections)
- [Server Commands (20)](Server_Commands_%2820%29.md) (2 shared connections)
- [Server Commands (30)](Server_Commands_%2830%29.md) (2 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 308 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*