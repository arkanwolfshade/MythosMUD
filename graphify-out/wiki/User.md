# User

> God node · 331 connections · `server/models/user.py`

**Community:** [LoggedHTTPException](LoggedHTTPException.md)

## Connections by Relation

### calls
- _admin_user() `EXTRACTED`
- _create_player() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- _create_player() `EXTRACTED`
- _create_user_object() `EXTRACTED`
- _user() `EXTRACTED`
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
- [test_message_category_invariants.py](test_message_category_invariants.py.md) `EXTRACTED`
- async_persistence.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- rooms.py `EXTRACTED`
- [endpoints.py](endpoints.py.md) `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- command_handler_unified.py `EXTRACTED`
- [test_admin_auth_service.py](test_admin_auth_service.py.md) `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_users.py `EXTRACTED`
- users.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- rooms_helpers.py `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`

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
- roll_character_stats() `EXTRACTED`
- handle_open_container_exceptions() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- close_container() `EXTRACTED`
- get_item_catalog() `EXTRACTED`
- handle_close_container_exceptions() `EXTRACTED`
- handle_loot_all_exceptions() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- update_room_exit() `EXTRACTED`
- broadcast_message() `EXTRACTED`
- _prepare_ascii_map_context() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- create_error_context() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- delete_room_exit() `EXTRACTED`

### uses
- [Player](Player.md) `INFERRED`
- Base `INFERRED`
- [Invite](Invite.md) `INFERRED`
- _admin_user() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- _drive_admin_broadcasts() `INFERRED`
- test_clear_player_inventory_empties_gear_and_leaves_stats_untouched() `INFERRED`
- test_cleanup_deletes_rows_from_mutable_tables() `INFERRED`
- test_add_player_effect_generates_id() `INFERRED`
- test_login_user_authenticate_raises_exception() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_admin_broadcast_event_is_system_info() `INFERRED`
- test_db_connectivity_create_and_read_user() `INFERRED`
- test_apply_exploration_filter_if_needed_calls_for_normal_user() `INFERRED`
- test_apply_exploration_filter_if_needed_skips_for_superuser() `INFERRED`
- test_login_user_authenticate_returns_none() `INFERRED`
- test_login_user_generic_exception() `INFERRED`
- test_login_user_id_mismatch() `INFERRED`
- test_login_user_invalid_credentials() `INFERRED`
- test_login_user_no_email() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*