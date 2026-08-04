# services nats service

> 31 nodes

## Key Concepts

- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_display_name_prefers_lifecycle()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_display_name_falls_back_to_id()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_from_config()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_missing_app()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_swallows_errors()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_after_npc_damage()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_skips_without_player_or_bus()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_swallows_errors()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields_non_dict_stats()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_event_noop_without_bus()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_success()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_no_publisher()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_swallows_errors()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_event_publisher_from_container()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_event_publisher_missing_pieces()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_and_stats_for_nats_missing_player()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_build_player_attacked_event_uses_dp_fallback()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_invalid_killer_returns_false()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_max_health()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_combat_stats_string_and_invalid_dp()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_from_dp()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 6 more nodes in this community*

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (26 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [chat game service](chat_game_service.md) (2 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [game room service](game_room_service.md) (1 shared connections)
- [tick services game](tick_services_game.md) (1 shared connections)
- [models invite Any](models_invite_Any.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*