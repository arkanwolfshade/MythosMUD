# Combat Taunt

> 60 nodes

## Key Concepts

- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (22 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (11 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_apply_taunt_and_maybe_broadcast_publishes_target_switch_to_nats()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **asyncio** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- *... and 35 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (13 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (8 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (7 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (6 shared connections)
- [Combat Flee](Combat_Flee.md) (5 shared connections)
- [Test Aggro Threat](Test_Aggro_Threat.md) (5 shared connections)
- [Combat Events](Combat_Events.md) (4 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (4 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (4 shared connections)
- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Combat Handler](Combat_Handler.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 142 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*