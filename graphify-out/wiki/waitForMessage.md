# waitForMessage

> 75 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (28 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (16 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (10 connections) — `server/commands/combat_helpers.py`
- **_PlayerForFlee** (8 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (8 connections) — `server/commands/combat_flee.py`
- **AppWithState** (7 connections) — `server/commands/combat_app_protocols.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **asyncio** (6 connections)
- **test_resolve_flee_preconditions_player_error()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_PlayerPositionServiceLike** (4 connections) — `server/commands/combat_flee.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- *... and 50 more nodes in this community*

## Relationships

- [User](User.md) (8 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_dependency_analysis.py](test_dependency_analysis.py.md) (2 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [analyze_log_file](analyze_log_file.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (1 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 149 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*