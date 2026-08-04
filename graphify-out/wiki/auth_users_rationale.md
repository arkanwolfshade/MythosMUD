# auth users rationale

> 144 nodes

## Key Concepts

- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (15 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **test_email_utils.py** (12 connections) — `server/tests/unit/auth/test_email_utils.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **email_utils.py** (10 connections) — `server/auth/email_utils.py`
- **UsernameAuthenticationBackend** (9 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **generate_unique_bogus_email()** (8 connections) — `server/auth/email_utils.py`
- **is_bogus_email()** (7 connections) — `server/auth/email_utils.py`
- **validate_bogus_email_format()** (7 connections) — `server/auth/email_utils.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- *... and 119 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (39 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (5 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (4 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [player preferences services](player_preferences_services.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)

## Source Files

- `server/auth/email_utils.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_email_utils.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 506 (96%)
- INFERRED: 21 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*