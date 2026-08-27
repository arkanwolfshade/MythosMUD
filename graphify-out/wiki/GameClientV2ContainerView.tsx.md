# GameClientV2ContainerView.tsx

> 56 nodes

## Key Concepts

- **combat_taunt.py** (27 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (25 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (12 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **_validate_taunt_context()** (11 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (8 connections) — `server/commands/combat_taunt.py`
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
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **asyncio** (4 connections)
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- **test_resolve_taunt_room_and_player_uses_room_id_attr()** (3 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 31 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (12 shared connections)
- [User](User.md) (7 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [Test Value Distribution Chart](Test_Value_Distribution_Chart.md) (3 shared connections)
- [.get_instance](get_instance.md) (3 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [waitForMessage](waitForMessage.md) (1 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 136 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*