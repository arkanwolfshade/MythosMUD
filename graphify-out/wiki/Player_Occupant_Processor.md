# Player Occupant Processor

> 34 nodes

## Key Concepts

- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager.py** (12 connections) — `server/game/instance_manager.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **spawn_defaults.py** (4 connections) — `server/constants/spawn_defaults.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **UUID** (2 connections)
- **datetime** (2 connections)
- **room_cache()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_first_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_exit_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_none_for_non_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_room_when_in_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Connection** (1 connections)
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.** (1 connections) — `server/constants/spawn_defaults.py`
- **InstanceManager for MythosMUD.  Manages instanced rooms: creates, stores, and de** (1 connections) — `server/game/instance_manager.py`
- **Unit tests for InstanceManager.  Tests instance creation, destruction, room clon** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 9 more nodes in this community*

## Relationships

- [Command Factory Tests](Command_Factory_Tests.md) (4 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/constants/spawn_defaults.py`
- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 90 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*