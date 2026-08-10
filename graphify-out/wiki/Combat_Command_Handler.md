# Combat Command Handler

> 449 nodes

## Key Concepts

- **User** (314 connections) — `server/models/user.py`
- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (28 connections) — `server/auth/argon2_utils.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- *... and 424 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (111 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (81 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (32 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (25 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (23 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (15 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (14 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (11 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (11 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (9 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/professions.py`
- `server/async_persistence.py`
- `server/auth/argon2_utils.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 1785 (89%)
- INFERRED: 218 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*