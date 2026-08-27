# test_connection_helpers_impl.py

> 120 nodes

## Key Concepts

- **PlayerPositionService** (45 connections) — `server/services/player_position_service.py`
- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (28 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (23 connections) — `server/commands/rest_command.py`
- **asyncio** (22 connections)
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **asyncio** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_restores_standing()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_no_service()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_true()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 95 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (29 shared connections)
- [character-cleanup.ts](character-cleanup.ts.md) (17 shared connections)
- [LogAnalyzer](LogAnalyzer.md) (10 shared connections)
- [room_validator/tests/conftest.py](room_validator-tests-conftest.py.md) (6 shared connections)
- [ChatPanelRuntimeViewParts.tsx](ChatPanelRuntimeViewParts.tsx.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (5 shared connections)
- [NATSService](NATSService.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [chatPanelRuntimeUtils.ts](chatPanelRuntimeUtils.ts.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (2 shared connections)

## Source Files

- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 291 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*