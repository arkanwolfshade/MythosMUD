# MemoryProfiler

> 67 nodes

## Key Concepts

- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **.state()** (31 connections) — `server/realtime/connection_state_machine.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (15 connections) — `server/commands/rescue_commands.py`
- **Any** (9 connections)
- **_run_ground_session()** (8 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **_get_ground_services()** (6 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **UUID** (6 connections)
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- *... and 42 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (13 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (5 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (4 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [SchemaValidator](SchemaValidator.md) (3 shared connections)
- [login_grace_period.py](login_grace_period.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 164 (81%)
- INFERRED: 38 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*