# User

> God node · 217 connections · `server/models/user.py`

**Community:** [Container Exception Handling](Container_Exception_Handling.md)

## Connections by Relation

### calls
- quest_seed_data() `EXTRACTED`
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
- server/models/__init__.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- test_admin_auth_service.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- users.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- database_helpers.py `EXTRACTED`
- api/metrics.py `EXTRACTED`
- api/game.py `EXTRACTED`
- api/player_respawn.py `EXTRACTED`
- test_containers.py `EXTRACTED`
- dialogue_definitions_api.py `EXTRACTED`
- test_container_exception_handlers.py `EXTRACTED`

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
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- respawn_player() `EXTRACTED`
- create_dialogue_definition() `EXTRACTED`
- list_dialogue_definitions() `EXTRACTED`
- upsert_dialogue_definition() `EXTRACTED`
- get_npc_population_stats() `EXTRACTED`

### uses
- Base `INFERRED`
- Invite `INFERRED`
- _admin_user() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- test_add_player_effect_generates_id() `INFERRED`
- test_apply_exploration_filter_if_needed_calls_for_normal_user() `INFERRED`
- test_apply_exploration_filter_if_needed_skips_for_superuser() `INFERRED`
- test_db_connectivity_create_and_read_user() `INFERRED`
- test_get_ascii_minimap_success() `INFERRED`
- test_get_current_superuser_failure() `INFERRED`
- test_get_current_superuser_with_none_user() `INFERRED`
- test_get_current_verified_user_failure() `INFERRED`
- test_get_current_verified_user_with_none_user() `INFERRED`
- test_login_user_player_no_profession_id() `INFERRED`
- test_login_user_profession_lookup_error() `INFERRED`
- test_login_user_profession_lookup_none() `INFERRED`
- test_login_user_profession_lookup_success() `INFERRED`
- test_username_authentication_backend_login() `INFERRED`
- test_get_current_room_id_none_when_persistence_errors() `INFERRED`
- test_get_player_and_exploration_returns_none_when_no_player() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*