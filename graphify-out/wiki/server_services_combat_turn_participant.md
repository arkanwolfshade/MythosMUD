# server services combat turn participant

> 7 nodes

## Key Concepts

- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **PrototypeRegistry** (2 connections)
- **Normalize full_player.get_stats() to a dict for damage math.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve rolled damage and type from main-hand weapon, or unarmed fallback.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Return (player_service, registry, async_persistence) from app container, or…** (1 connections) — `server/services/combat_turn_participant_actions.py`

## Relationships

- [server services aggro threat](server_services_aggro_threat.md) (7 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [server game items prototype registry](server_game_items_prototype_registry.md) (2 shared connections)
- [server config init](server_config_init.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (1 shared connections)
- [server game weapons](server_game_weapons.md) (1 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 16 (73%)
- INFERRED: 6 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*