# NATSMetrics

> 75 nodes

## Key Concepts

- **test_admin_setlucidity_command.py** (45 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **admin_setlucidity_command.py** (31 connections) — `server/commands/admin_setlucidity_command.py`
- **asyncio** (24 connections)
- **_handle_admin_set_lucidity_command()** (17 connections) — `server/commands/admin_setlucidity_command.py`
- **_execute_lucidity_change()** (14 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **LucidityChangeCtx** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_check_admin_permissions()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_resolve_target_player()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_command_context()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_player_service_from_app()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **LucidityUpdateResult** (5 connections) — `server/services/lucidity_helpers.py`
- **_log_lucidity_success()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **test_apply_lucidity_change_adjustment_error()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_admin_logger_failure()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_success()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **UUID** (5 connections)
- **test_execute_lucidity_change_success()** (4 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_check_admin_permissions_current_player_missing()** (3 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (4 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)
- [Memory Leak Audit Report](Memory_Leak_Audit_Report.md) (1 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 194 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*