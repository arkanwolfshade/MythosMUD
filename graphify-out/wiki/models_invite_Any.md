# models invite Any

> 11 nodes

## Key Concepts

- **.is_active()** (5 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Get all currently active status effects.          Args:             current_tick** (1 connections) — `server/models/game.py`
- **Any** (1 connections)
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 21 (78%)
- INFERRED: 6 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*