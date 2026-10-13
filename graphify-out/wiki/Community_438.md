# Community 438

> 40 nodes

## Key Concepts

- **_handle_admin_hallucinate_command()** (19 connections) — `server/commands/admin_hallucinate_command.py`
- **test_admin_hallucinate_command.py** (19 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **asyncio** (14 connections)
- **deliver_forced_hallucination()** (12 connections) — `server/commands/admin_hallucinate_command.py`
- **get_current_lcd_or_error()** (8 connections) — `server/commands/admin_hallucinate_command.py`
- **HallucinateCommandError** (7 connections) — `server/commands/admin_hallucinate_command.py`
- **extract_args()** (5 connections) — `server/commands/admin_hallucinate_command.py`
- **_validate_target_and_type()** (5 connections) — `server/commands/admin_hallucinate_command.py`
- **_log_hallucinate_command()** (4 connections) — `server/commands/admin_hallucinate_command.py`
- **test_get_current_lcd_or_error_raises_when_session_unavailable()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_delivers_phantom()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_delivery_error()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_resolve_hallucinate_target_raises_when_current_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **UUID** (4 connections)
- **_async_session_gen()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_deliver_forced_hallucination_fake_tell()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_deliver_forced_hallucination_overlay()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_deliver_forced_hallucination_phantom()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_invalid_type()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_missing_app()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_missing_args()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_no_player_service()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_permission_denied()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_target_no_room()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_target_not_found()** (3 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- *... and 15 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (10 shared connections)
- [Community 156](Community_156.md) (5 shared connections)
- [Community 319](Community_319.md) (4 shared connections)
- [Community 301](Community_301.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)
- [Community 177](Community_177.md) (1 shared connections)
- [Community 673](Community_673.md) (1 shared connections)

## Source Files

- `server/commands/admin_hallucinate_command.py`
- `server/tests/unit/commands/test_admin_hallucinate_command.py`

## Audit Trail

- EXTRACTED: 92 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*