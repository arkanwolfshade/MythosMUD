# End-to-End Validation

> 26 nodes · cohesion 0.08

## Key Concepts

- **UUID** (21 connections)
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.add_player_effect()** (3 connections) — `server/async_persistence.py`
- **.delete_player()** (3 connections) — `server/async_persistence.py`
- **.get_player_effect_remaining_ticks()** (3 connections) — `server/async_persistence.py`
- **.has_player_effect()** (3 connections) — `server/async_persistence.py`
- **.remove_player_effect_by_id()** (3 connections) — `server/async_persistence.py`
- **.soft_delete_player()** (3 connections) — `server/async_persistence.py`
- **.delete_container()** (2 connections) — `server/async_persistence.py`
- **Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Delete a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Apply lucidity loss to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Apply fear to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Apply corruption to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Add a player effect. Returns effect id.** (1 connections) — `server/async_persistence.py`
- **Remove a player effect by id.** (1 connections) — `server/async_persistence.py`
- **Get active effects for a player (remaining_ticks > 0). Returns list of PlayerEff** (1 connections) — `server/async_persistence.py`
- **Return True if player has an active effect of the given type.** (1 connections) — `server/async_persistence.py`
- **Return remaining ticks for the effect, or None.** (1 connections) — `server/async_persistence.py`
- **Get a container by ID.** (1 connections) — `server/async_persistence.py`
- *... and 1 more nodes in this community*

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (13 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (5 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 74 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*