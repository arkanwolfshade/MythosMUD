# User

> God node · 297 connections · `server/models/user.py`

**Community:** [User](User.md)

## Connections by Relation

### calls
- test_add_player_effect_generates_id() `EXTRACTED`
- test_lucidity_adjustment_round_trip() `EXTRACTED`
- test_db_connectivity_create_and_read_user() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- test_login_user_authenticate_raises_exception() `EXTRACTED`
- test_login_user_authenticate_returns_none() `EXTRACTED`
- test_login_user_generic_exception() `EXTRACTED`
- test_login_user_http_exception_re_raised() `EXTRACTED`
- test_login_user_id_mismatch() `EXTRACTED`
- test_login_user_invalid_credentials() `EXTRACTED`
- test_login_user_no_email() `EXTRACTED`
- test_login_user_player_no_profession_id() `EXTRACTED`
- test_login_user_profession_lookup_error() `EXTRACTED`
- test_login_user_profession_lookup_none() `EXTRACTED`
- test_login_user_profession_lookup_success() `EXTRACTED`
- test_login_user_success() `EXTRACTED`
- test_login_user_with_characters() `EXTRACTED`
- test_register_user_duplicate_username() `EXTRACTED`
- test_register_user_success() `EXTRACTED`
- test_get_current_superuser_failure() `EXTRACTED`

### contains
- models/user.py `EXTRACTED`

### imports
- models/player.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- [players.py](players.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [test_users.py](test_users.py.md) `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- [test_admin_auth_service.py](test_admin_auth_service.py.md) `EXTRACTED`
- endpoints.py `EXTRACTED`
- test_endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- users.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- [test_async_persistence_core.py](test_async_persistence_core.py.md) `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`
- [rooms.py](rooms.py.md) `EXTRACTED`
- [test_maps.py](test_maps.py.md) `EXTRACTED`
- test_container_exception_handlers.py `EXTRACTED`
- test_containers.py `EXTRACTED`

### inherits
- Base `EXTRACTED`
- SQLAlchemyBaseUserTableUUID `EXTRACTED`

### method
- .is_authenticated() `EXTRACTED`
- .get_display_name() `EXTRACTED`
- .__repr__() `EXTRACTED`

### rationale_for
- User model for FastAPI Users v14+ with SQLAlchemy 2.0 typing. Extends… `EXTRACTED`

### references
- validate_admin_permission() `EXTRACTED`
- handle_transfer_items_exceptions() `EXTRACTED`
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- handle_open_container_exceptions() `EXTRACTED`
- roll_character_stats() `EXTRACTED`
- handle_close_container_exceptions() `EXTRACTED`
- handle_loot_all_exceptions() `EXTRACTED`
- close_container() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- _prepare_ascii_map_context() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- _execute_create_character() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- _roll_stats_with_profession_preview() `EXTRACTED`
- validate_character_stats() `EXTRACTED`

### uses
- [Player](Player.md) `INFERRED`
- Base `INFERRED`
- [Invite](Invite.md) `INFERRED`
- PlayerInventory `INFERRED`
- PlayerChannelPreferences `INFERRED`
- TestTransferAllItemsFromContainer `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- PlayerExploration `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestCloseContainer `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- TestRequestModels `INFERRED`
- TestHandleContainerServiceErrorEdgeCases `INFERRED`
- TestExceptionChaining `INFERRED`
- TestExceptionHandlerContext `INFERRED`
- TestExceptionHandlerLoggerCalls `INFERRED`
- TestHandleCloseContainerExceptions `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*