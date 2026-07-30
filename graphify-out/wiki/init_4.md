# init

> 20 nodes

## Key Concepts

- **UUID** (21 connections)
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.soft_delete_player()** (3 connections) — `server/async_persistence.py`
- **.delete_player()** (3 connections) — `server/async_persistence.py`
- **.add_player_effect()** (3 connections) — `server/async_persistence.py`
- **.remove_player_effect_by_id()** (3 connections) — `server/async_persistence.py`
- **.has_player_effect()** (3 connections) — `server/async_persistence.py`
- **.get_player_effect_remaining_ticks()** (3 connections) — `server/async_persistence.py`
- **.delete_container()** (2 connections) — `server/async_persistence.py`
- **Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Delete a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Add a player effect. Returns effect id.** (1 connections) — `server/async_persistence.py`
- **Remove a player effect by id.** (1 connections) — `server/async_persistence.py`
- **Get active effects for a player (remaining_ticks > 0). Returns list of PlayerEff** (1 connections) — `server/async_persistence.py`
- **Return True if player has an active effect of the given type.** (1 connections) — `server/async_persistence.py`
- **Return remaining ticks for the effect, or None.** (1 connections) — `server/async_persistence.py`
- **Get a container by ID.** (1 connections) — `server/async_persistence.py`
- **Get all containers owned by an entity.** (1 connections) — `server/async_persistence.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (10 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (5 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [find dead connections()](find_dead_connections%28%29.md) (1 shared connections)
- [time commands](time_commands.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 59 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*