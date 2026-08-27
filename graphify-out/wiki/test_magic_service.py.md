# test_magic_service.py

> 83 nodes

## Key Concepts

- **look_command.py** (45 connections) — `server/commands/look_command.py`
- **test_look_command.py** (26 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (17 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (13 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (12 connections) — `server/commands/look_command.py`
- **_route_look_command()** (12 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (10 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (10 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (10 connections) — `server/commands/look_command.py`
- **FastAPI** (10 connections)
- **asyncio** (10 connections)
- **_LookPersistence** (9 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (9 connections) — `server/commands/look_command.py`
- **CommandResponse** (9 connections)
- **LookRouteCtx** (8 connections) — `server/commands/look_command.py`
- **_as_response()** (8 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (8 connections) — `server/commands/look_command.py`
- **_LookRoom** (7 connections) — `server/commands/look_command.py`
- **_connection_manager_from_app()** (7 connections) — `server/commands/look_command.py`
- **_container_from_app()** (7 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (7 connections) — `server/commands/look_command.py`
- **_prototype_registry_from_app()** (6 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (6 connections) — `server/commands/look_command.py`
- **test_handle_look_command_accepts_websocket_request_context()** (5 connections) — `server/tests/unit/commands/test_look_command.py`
- *... and 58 more nodes in this community*

## Relationships

- [test_manager.py](test_manager.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [ChatMessage](ChatMessage.md) (2 shared connections)
- [FastAPI Code Review - Anti-Patterns and Best Practices](FastAPI_Code_Review_-_Anti-Patterns_and_Best_Practices.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [Test Value Distribution Chart](Test_Value_Distribution_Chart.md) (1 shared connections)
- [10 Concurrent Players Load Test](10_Concurrent_Players_Load_Test.md) (1 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (1 shared connections)
- [ClientLogger](ClientLogger.md) (1 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (1 shared connections)
- [useStatsRollingActions.ts](useStatsRollingActions.ts.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*