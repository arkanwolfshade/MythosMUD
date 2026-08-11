# Auth Token Utilities

> 252 nodes

## Key Concepts

- **AuthenticationError** (64 connections) — `server/exceptions.py`
- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **real_time.py** (34 connections) — `server/api/real_time.py`
- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **hash_password()** (28 connections) — `server/auth/argon2_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **argon2_utils.py** (19 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **auth_utils.py** (16 connections) — `server/auth_utils.py`
- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **PresenceStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **Any** (9 connections)
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- *... and 227 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (40 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (22 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (16 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (3 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 960 (90%)
- INFERRED: 107 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*