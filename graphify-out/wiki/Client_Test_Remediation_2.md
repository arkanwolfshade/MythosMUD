# Client Test Remediation

> 10 nodes · cohesion 0.20

## Key Concepts

- **.__init__()** (5 connections) — `server/models/invite.py`
- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **.is_active()** (4 connections) — `server/models/game.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Any** (1 connections)
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **setter** (1 connections)
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (1 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 11 (73%)
- INFERRED: 4 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*