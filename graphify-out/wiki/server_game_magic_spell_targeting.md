# server game magic spell targeting

> 114 nodes

## Key Concepts

- **PlayerCombatService** (74 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **test_award_xp_on_npc_death_delegates_to_rewards_when_available()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_error()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 89 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (6 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (3 shared connections)
- [server services player combat service](server_services_player_combat_service.md) (3 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (3 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server commands combat](server_commands_combat.md) (2 shared connections)
- [server game movement helpers](server_game_movement_helpers.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 188 (79%)
- INFERRED: 49 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*