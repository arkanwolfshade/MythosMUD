# User

> God node · 325 connections · `server/models/user.py`

**Community:** [Exception Containers](Exception_Containers.md)

## Connections by Relation

### calls
- test_lucidity_adjustment_round_trip() `EXTRACTED`
- test_add_player_effect_generates_id() `EXTRACTED`
- test_login_user_authenticate_raises_exception() `EXTRACTED`
- test_login_user_authenticate_returns_none() `EXTRACTED`
- test_login_user_generic_exception() `EXTRACTED`
- test_login_user_id_mismatch() `EXTRACTED`
- test_login_user_invalid_credentials() `EXTRACTED`
- test_login_user_no_email() `EXTRACTED`
- test_register_user_duplicate_username() `EXTRACTED`
- test_login_user_player_no_profession_id() `EXTRACTED`
- test_login_user_profession_lookup_error() `EXTRACTED`
- test_login_user_profession_lookup_none() `EXTRACTED`
- test_login_user_profession_lookup_success() `EXTRACTED`
- test_login_user_http_exception_re_raised() `EXTRACTED`
- test_login_user_success() `EXTRACTED`
- test_login_user_with_characters() `EXTRACTED`
- test_register_user_success() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- test_get_current_superuser_failure() `EXTRACTED`
- test_get_current_superuser_with_none_user() `EXTRACTED`

### contains
- user.py `EXTRACTED`

### imports
- player.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- __init__.py `EXTRACTED`
- players.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- test_admin_auth_service.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- users.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_container_exception_handlers.py `EXTRACTED`
- test_containers.py `EXTRACTED`

### indirect_call
- _admin_user() `INFERRED`
- generate_unique_bogus_email() `INFERRED`
- _check_username_exists() `INFERRED`
- test_apply_exploration_filter_if_needed_calls_for_normal_user() `INFERRED`
- test_apply_exploration_filter_if_needed_skips_for_superuser() `INFERRED`
- test_get_ascii_minimap_success() `INFERRED`
- test_db_connectivity_create_and_read_user() `INFERRED`
- test_get_current_room_id_none_when_persistence_errors() `INFERRED`
- test_get_player_and_exploration_returns_none_when_no_player() `INFERRED`
- test_set_map_origin_success() `INFERRED`
- test_get_all_professions_requires_auth() `INFERRED`
- mock_user_and_player() `INFERRED`
- test_get_current_room_id_from_player() `INFERRED`
- test_get_current_room_id_from_query_param() `INFERRED`
- test_get_minimap_player_and_room_id_success() `INFERRED`
- test_recalculate_coordinates_admin() `INFERRED`
- _plain_user() `INFERRED`
- mock_user() `INFERRED`
- mock_user() `INFERRED`
- mock_user() `INFERRED`

### inherits
- Base `EXTRACTED`
- SQLAlchemyBaseUserTableUUID `EXTRACTED`

### method
- .get_display_name() `EXTRACTED`
- .is_authenticated() `EXTRACTED`
- .__repr__() `EXTRACTED`

### rationale_for
- User model for FastAPI Users v14+ with SQLAlchemy 2.0 typing.      Extends SQLAl `EXTRACTED`

### references
- loot_all_items() `EXTRACTED`
- validate_admin_permission() `EXTRACTED`
- handle_transfer_items_exceptions() `EXTRACTED`
- handle_open_container_exceptions() `EXTRACTED`
- transfer_items() `EXTRACTED`
- handle_loot_all_exceptions() `EXTRACTED`
- roll_character_stats() `EXTRACTED`
- open_container() `EXTRACTED`
- handle_close_container_exceptions() `EXTRACTED`
- close_container() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _prepare_ascii_map_context() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- _ensure_coordinates_generated() `EXTRACTED`
- get_ascii_minimap() `EXTRACTED`

### uses
- [Player](Player.md) `INFERRED`
- Base `INFERRED`
- Invite `INFERRED`
- PlayerChannelPreferences `INFERRED`
- PlayerInventory `INFERRED`
- TestTransferAllItemsFromContainer `INFERRED`
- TestHelperFunctions `INFERRED`
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