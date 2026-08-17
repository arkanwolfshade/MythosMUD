# User

> God node · 293 connections · `server/models/user.py`

**Community:** [claude rules fastapi](claude_rules_fastapi.md)

## Connections by Relation

### calls
- quest_seed_data() `EXTRACTED`
- .create_user() `INFERRED`
- .verify_token() `INFERRED`
- .verify_token() `INFERRED`

### contains
- models/user.py `EXTRACTED`

### imports
- models/player.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- test_admin_auth_service.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- users.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`

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
- _prepare_ascii_map_context() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- get_ascii_map() `EXTRACTED`
- get_ascii_minimap() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`

### uses
- [Player](Player.md) `INFERRED`
- Base `INFERRED`
- Invite `INFERRED`
- _admin_user() `INFERRED`
- _admin_user() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- test_add_player_effect_generates_id() `INFERRED`
- test_apply_exploration_filter_if_needed_calls_for_normal_user() `INFERRED`
- test_apply_exploration_filter_if_needed_skips_for_superuser() `INFERRED`
- test_login_user_authenticate_raises_exception() `INFERRED`
- test_login_user_authenticate_returns_none() `INFERRED`
- test_login_user_generic_exception() `INFERRED`
- test_login_user_id_mismatch() `INFERRED`
- test_login_user_invalid_credentials() `INFERRED`
- test_login_user_no_email() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_db_connectivity_create_and_read_user() `INFERRED`
- test_get_ascii_minimap_success() `INFERRED`
- test_get_current_superuser_failure() `INFERRED`
- test_get_current_superuser_with_none_user() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*