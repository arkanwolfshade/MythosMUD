# PlayerLucidity

> 88 nodes · cohesion 0.04

## Key Concepts

- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **handle_ground_command()** (32 connections) — `server/commands/rescue_commands.py`
- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **Any** (7 connections)
- **.rescue()** (7 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections)
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **Any** (4 connections)
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 63 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (15 shared connections)
- [AliasStorage](AliasStorage.md) (14 shared connections)
- [lucidity_service.py](lucidity_service.py.md) (14 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (11 shared connections)
- [Player](Player.md) (10 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [lucidity.py](lucidity.py.md) (4 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (4 shared connections)
- [PassiveLucidityFluxService](PassiveLucidityFluxService.md) (4 shared connections)
- [get_async_session](get_async_session.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/models/lucidity.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 351 (89%)
- INFERRED: 44 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*