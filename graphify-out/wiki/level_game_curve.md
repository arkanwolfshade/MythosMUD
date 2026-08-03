# level game curve

> 4 nodes

## Key Concepts

- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [game models player](game_models_player.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 7 (70%)
- INFERRED: 3 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*