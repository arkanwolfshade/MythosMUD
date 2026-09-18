# Community 544

> 31 nodes

## Key Concepts

- **admin_hallucinate_command.py** (29 connections) — `server/commands/admin_hallucinate_command.py`
- **resolve_hallucinate_target()** (10 connections) — `server/commands/admin_hallucinate_command.py`
- **get_player_service_from_app()** (9 connections) — `server/commands/admin_setlucidity_command.py`
- **get_current_lcd_or_error()** (8 connections) — `server/commands/admin_hallucinate_command.py`
- **HallucinateCommandError** (7 connections) — `server/commands/admin_hallucinate_command.py`
- **PlayerServiceLike** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **extract_args()** (5 connections) — `server/commands/admin_hallucinate_command.py`
- **_validate_target_and_type()** (5 connections) — `server/commands/admin_hallucinate_command.py`
- **PlayerLike** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **UUID** (4 connections)
- **_log_hallucinate_command()** (3 connections) — `server/commands/admin_hallucinate_command.py`
- **.resolve_player_name()** (3 connections) — `server/commands/admin_setlucidity_command.py`
- **test_extract_args_from_args_list()** (2 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_extract_args_from_fields()** (2 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_get_player_service_from_container()** (2 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_get_player_service_legacy_app_state()** (2 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_get_player_service_missing()** (2 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **Protocol** (2 connections)
- **.__init__()** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Exception** (1 connections)
- **Admin command to force a specific hallucination for QA/testing purposes (#714).…** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Resolve admin permissions, the target's id, and the target's current room;…** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Resolve the target's current LCD via a fresh DB session; raises if none is…** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Record the forced hallucination in the admin actions log (best-effort).** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Extract target_player and hallucination_type from command_data.** (1 connections) — `server/commands/admin_hallucinate_command.py`
- *... and 6 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [Community 235](Community_235.md) (10 shared connections)
- [Community 693](Community_693.md) (10 shared connections)
- [Community 464](Community_464.md) (6 shared connections)
- [Community 161](Community_161.md) (1 shared connections)
- [Community 160](Community_160.md) (1 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (1 shared connections)

## Source Files

- `server/commands/admin_hallucinate_command.py`
- `server/commands/admin_setlucidity_command.py`
- `server/tests/unit/commands/test_admin_hallucinate_command.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 77 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*