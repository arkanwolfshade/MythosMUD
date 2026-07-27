# User

> God node · 184 connections · `server/models/user.py`

**Community:** [[API Test Fixtures]]

## Connections by Relation

### calls
- [[_create_user_object()]] `EXTRACTED`
- [[test_add_player_effect_generates_id()]] `EXTRACTED`
- [[test_login_user_generic_exception()]] `EXTRACTED`
- [[test_lucidity_adjustment_round_trip()]] `EXTRACTED`
- [[test_login_user_authenticate_raises_exception()]] `EXTRACTED`
- [[test_login_user_authenticate_returns_none()]] `EXTRACTED`
- [[test_login_user_http_exception_re_raised()]] `EXTRACTED`
- [[test_login_user_id_mismatch()]] `EXTRACTED`
- [[test_login_user_invalid_credentials()]] `EXTRACTED`
- [[test_login_user_no_email()]] `EXTRACTED`
- [[test_login_user_player_no_profession_id()]] `EXTRACTED`
- [[test_login_user_profession_lookup_error()]] `EXTRACTED`
- [[test_login_user_profession_lookup_none()]] `EXTRACTED`
- [[test_login_user_profession_lookup_success()]] `EXTRACTED`
- [[test_login_user_success()]] `EXTRACTED`
- [[test_login_user_with_characters()]] `EXTRACTED`
- [[test_register_user_duplicate_username()]] `EXTRACTED`
- [[test_register_user_success()]] `EXTRACTED`
- [[quest_seed_data()]] `EXTRACTED`
- [[test_get_current_superuser_failure()]] `EXTRACTED`

### contains
- [[user.py]] `EXTRACTED`

### imports
- [[async_persistence.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[players.py]] `EXTRACTED`
- [[test_users.py]] `EXTRACTED`
- [[player.py]] `EXTRACTED`
- [[test_admin_auth_service.py]] `EXTRACTED`
- [[maps.py]] `EXTRACTED`
- [[container_endpoints_basic.py]] `EXTRACTED`
- [[endpoints.py]] `EXTRACTED`
- [[test_endpoints.py]] `EXTRACTED`
- [[character_creation.py]] `EXTRACTED`
- [[users.py]] `EXTRACTED`
- [[container_helpers.py]] `EXTRACTED`
- [[test_container_helpers.py]] `EXTRACTED`
- [[test_async_persistence_core.py]] `EXTRACTED`
- [[container_endpoints_loot.py]] `EXTRACTED`
- [[test_metrics_endpoints.py]] `EXTRACTED`
- [[rooms.py]] `EXTRACTED`
- [[database_helpers.py]] `EXTRACTED`
- [[npc_definitions_api.py]] `EXTRACTED`

### inherits
- [[Base]] `EXTRACTED`
- [[SQLAlchemyBaseUserTableUUID]] `EXTRACTED`

### method
- [[.get_display_name()]] `EXTRACTED`
- [[.is_authenticated()]] `EXTRACTED`
- [[.__repr__()]] `EXTRACTED`

### rationale_for
- [[User model for FastAPI Users v14+ with SQLAlchemy 2.0 typing.      Extends SQLAl]] `EXTRACTED`

### references
- [[set_display_name_default()]] `EXTRACTED`

### uses
- [[Player]] `INFERRED`
- [[Base]] `INFERRED`
- [[Invite]] `INFERRED`
- [[PlayerInventory]] `INFERRED`
- [[PlayerChannelPreferences]] `INFERRED`
- [[TestTransferAllItemsFromContainer]] `INFERRED`
- [[TestHelperFunctions]] `INFERRED`
- [[TestOpenContainer]] `INFERRED`
- [[TestTransferItems]] `INFERRED`
- [[PlayerExploration]] `INFERRED`
- [[TestHandleTransferItemsExceptions]] `INFERRED`
- [[TestCloseContainer]] `INFERRED`
- [[TestHandleLootAllExceptions]] `INFERRED`
- [[TestHandleOpenContainerExceptions]] `INFERRED`
- [[TestRequestModels]] `INFERRED`
- [[TestHandleContainerServiceErrorEdgeCases]] `INFERRED`
- [[TestGetMythosTime]] `INFERRED`
- [[TestRollCharacterStats]] `INFERRED`
- [[TestExceptionChaining]] `INFERRED`
- [[TestExceptionHandlerContext]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
