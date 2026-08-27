# User

> God node · 255 connections · `server/models/user.py`

**Community:** [NATSServicePoolMixin](NATSServicePoolMixin.md)

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
- models/player.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- test_maps.py `EXTRACTED`
- [test_users.py](test_users.py.md) `EXTRACTED`
- users.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`
- [api/player_effects.py](api-player_effects.py.md) `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- database_helpers.py `EXTRACTED`
- [subject_controller.py](subject_controller.py.md) `EXTRACTED`
- api/metrics.py `EXTRACTED`

### inherits
- [Base](Base.md) `EXTRACTED`
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
- [Base](Base.md) `INFERRED`
- [Invite](Invite.md) `INFERRED`
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
- test_username_authentication_backend_login() `INFERRED`
- test_get_current_room_id_none_when_persistence_errors() `INFERRED`
- test_get_player_and_exploration_returns_none_when_no_player() `INFERRED`
- test_set_map_origin_success() `INFERRED`
- test_get_all_professions_requires_auth() `INFERRED`
- test_get_current_superuser_success() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*