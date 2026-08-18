# server game magic spell targeting

> 78 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **test_award_xp_on_npc_death_delegates_to_rewards_when_available()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_error()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_no_player_combat_service()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_success()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_default()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_database()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_mapping()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_clear_player_combat_state()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats_multiple_combats()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_players_in_combat()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 53 more nodes in this community*

## Relationships

- [server services player combat service](server_services_player_combat_service.md) (16 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (5 shared connections)
- [server events combat events](server_events_combat_events.md) (5 shared connections)
- [server game mechanics](server_game_mechanics.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server game movement helpers](server_game_movement_helpers.md) (2 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (2 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (1 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/realtime/connection_manager.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 153 (80%)
- INFERRED: 38 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*