# User

> God node · 287 connections · `server/models/user.py`

**Community:** [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md)

## Connections by Relation

### calls
- _admin_user() `EXTRACTED`
- _create_user_object() `EXTRACTED`
- test_user_get_display_name_all_empty() `EXTRACTED`
- test_user_get_display_name_falls_back_to_id() `EXTRACTED`
- test_user_get_display_name_with_display_name() `EXTRACTED`
- test_user_get_display_name_with_empty_display_name() `EXTRACTED`
- test_user_get_display_name_without_display_name() `EXTRACTED`
- test_user_is_authenticated_when_active() `EXTRACTED`
- test_user_is_authenticated_when_inactive() `EXTRACTED`
- test_user_repr() `EXTRACTED`
- .create_user() `INFERRED`
- .verify_token() `INFERRED`
- .verify_token() `INFERRED`

### contains
- models/user.py `EXTRACTED`

### imports
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- rooms.py `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- test_admin_auth_service.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- subject_controller.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`

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
- transfer_items() `EXTRACTED`
- handle_transfer_items_exceptions() `EXTRACTED`
- open_container() `EXTRACTED`
- roll_character_stats() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- close_container() `EXTRACTED`
- handle_open_container_exceptions() `EXTRACTED`
- handle_close_container_exceptions() `EXTRACTED`
- handle_loot_all_exceptions() `EXTRACTED`
- create_room_exit() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- update_room() `EXTRACTED`
- update_room_exit() `EXTRACTED`
- _prepare_ascii_map_context() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- delete_room_exit() `EXTRACTED`

### uses
- Base `INFERRED`
- Invite `INFERRED`
- _admin_user() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_apply_exploration_filter_if_needed_calls_for_normal_user() `INFERRED`
- test_apply_exploration_filter_if_needed_skips_for_superuser() `INFERRED`
- test_login_user_authenticate_raises_exception() `INFERRED`
- test_login_user_authenticate_returns_none() `INFERRED`
- test_login_user_generic_exception() `INFERRED`
- test_login_user_id_mismatch() `INFERRED`
- test_login_user_invalid_credentials() `INFERRED`
- test_login_user_no_email() `INFERRED`
- test_get_ascii_minimap_success() `INFERRED`
- test_get_current_superuser_failure() `INFERRED`
- test_get_current_superuser_with_none_user() `INFERRED`
- test_get_current_verified_user_failure() `INFERRED`
- test_get_current_verified_user_with_none_user() `INFERRED`
- test_login_user_player_no_profession_id() `INFERRED`
- test_login_user_profession_lookup_error() `INFERRED`
- test_login_user_profession_lookup_none() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*