# countdown rest task

> 33 nodes

## Key Concepts

- **UUID** (15 connections)
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **Get base stats as dictionary.** (1 connections) — `server/models/npc.py`
- **Track a player's combat state.          Args:             player_id: ID of th** (1 connections) — `server/services/player_combat_service.py`
- **Get a player's combat state.          Args:             player_id: ID of the** (1 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state.          Args:             player_id: ID of th** (1 connections) — `server/services/player_combat_service.py`
- **Synchronously check if a player is currently in combat.          This is the p** (1 connections) — `server/services/player_combat_service.py`
- **Check if a player is currently in combat.          Args:             player_i** (1 connections) — `server/services/player_combat_service.py`
- **Get all players currently in combat.          Returns:             List of pl** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat start for a player.          Args:             player_id: ID of** (1 connections) — `server/services/player_combat_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (16 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)
- [position player service](position_player_service.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 96 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*