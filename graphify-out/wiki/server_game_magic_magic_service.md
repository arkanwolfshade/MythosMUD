# server game magic magic service

> 8 nodes

## Key Concepts

- **_StatsPlayer** (5 connections) — `server/game/magic/magic_service.py`
- **_PlayerPersistence** (4 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **_CombatTickState** (3 connections) — `server/game/magic/magic_service.py`
- **.get_player_by_id()** (3 connections) — `server/game/magic/magic_service.py`
- **Protocol** (3 connections)
- **.get_stats()** (1 connections) — `server/game/magic/magic_service.py`
- **Calculate next initiative tick for combat casting. In round-based combat,…** (1 connections) — `server/game/magic/magic_service.py`

## Relationships

- [magicservicecompletionmixin](magicservicecompletionmixin.md) (5 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*