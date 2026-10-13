# User

> God node · 215 connections · `server/models/user.py`

**Community:** [Auth Dependencies & Users](Auth_Dependencies_&_Users.md)

## Connections by Relation

### calls
- _admin_user() `EXTRACTED`
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
- test_admin_auth_service.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- users.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- subject_controller.py `EXTRACTED`
- api/metrics.py `EXTRACTED`
- database_helpers.py `EXTRACTED`
- test_endpoints_register.py `EXTRACTED`
- api/player_respawn.py `EXTRACTED`
- dialogue_definitions_api.py `EXTRACTED`
- test_containers.py `EXTRACTED`
- npc_population_api.py `EXTRACTED`
- npc_spawn_rules_api.py `EXTRACTED`
- test_auth_dependencies.py `EXTRACTED`

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
- roll_character_stats() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- get_npc_definitions() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- get_npc_spawn_rules() `EXTRACTED`
- respawn_player() `EXTRACTED`
- create_dialogue_definition() `EXTRACTED`
- list_dialogue_definitions() `EXTRACTED`
- upsert_dialogue_definition() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- get_npc_definition() `EXTRACTED`
- get_npc_population_stats() `EXTRACTED`
- replay_dlq_message() `EXTRACTED`
- apply_lucidity_loss() `EXTRACTED`
- get_dialogue_definition() `EXTRACTED`
- get_admin_sessions() `EXTRACTED`
- _execute_create_character() `EXTRACTED`

### uses
- Invite `INFERRED`
- Base `INFERRED`
- _admin_user() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_db_connectivity_create_and_read_user() `INFERRED`
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

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*