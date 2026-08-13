# .is_alive

> 10 nodes

## Key Concepts

- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **.is_active()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **Any** (1 connections)
- **setter** (1 connections)
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [StatusEffect](StatusEffect.md) (1 shared connections)
- [Invite](Invite.md) (1 shared connections)
- [.execute_idle_movement](execute_idle_movement.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 11 (79%)
- INFERRED: 3 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*