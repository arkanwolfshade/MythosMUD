# server game magic mp regeneration

> 20 nodes

## Key Concepts

- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **MP regeneration service for passive and active magic point recovery. This…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Get MP regeneration multiplier based on player state. Args: stats: Player stats…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **# TODO: Check status effects for meditation when status effect system supports…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **# NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration). Args: player_id:…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from consuming an item. Args: player_id: Player ID amount: Amount of…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Service for managing MP regeneration. Handles passive regeneration over time…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Initialize the MP regeneration service. Args: player_service: Player service…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Process MP regeneration for a player on a game tick. Args: player_id: Player ID…** (1 connections) — `server/game/magic/mp_regeneration_service.py`

## Relationships

- [server tests unit game magic](server_tests_unit_game_magic.md) (5 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (3 shared connections)
- [server api players](server_api_players.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [leveluphook](leveluphook.md) (2 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server api character creation](server_api_character_creation.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 43 (90%)
- INFERRED: 5 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*