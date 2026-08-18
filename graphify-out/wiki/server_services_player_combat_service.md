# server services player combat service

> 29 nodes

## Key Concepts

- **UUID** (15 connections)
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **Track a player's combat state. Args: player_id: ID of the player player_name:…** (1 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state. Args: player_id: ID of the player** (1 connections) — `server/services/player_combat_service.py`
- **Synchronously check if a player is currently in combat. This is the preferred…** (1 connections) — `server/services/player_combat_service.py`
- **Check if a player is currently in combat. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Get all players currently in combat. Returns: List of player IDs currently in…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat start for a player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat end by clearing all players in the combat. Args: combat_id: ID of…** (1 connections) — `server/services/player_combat_service.py`
- **Handle NPC death and award XP to the player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Return True if the NPC rewards path handled the award (success or logged…** (1 connections) — `server/services/player_combat_service.py`
- **Fallback: load player, add XP, save, publish (used without integration in…** (1 connections) — `server/services/player_combat_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [server game magic spell targeting](server_game_magic_spell_targeting.md) (16 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (1 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server services player position service](server_services_player_position_service.md) (1 shared connections)
- [jsondict](jsondict.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 52 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*