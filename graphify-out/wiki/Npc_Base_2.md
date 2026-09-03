# Npc Base

> 10 nodes

## Key Concepts

- **.__init__()** (5 connections) — `server/models/invite.py`
- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **.is_active()** (4 connections) — `server/models/game.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **Any** (1 connections)
- **setter** (1 connections)
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [Test Game Status Effect](Test_Game_Status_Effect.md) (1 shared connections)
- [Test Invite](Test_Invite.md) (1 shared connections)
- [Test Container Helpers Inventory Ops](Test_Container_Helpers_Inventory_Ops.md) (1 shared connections)
- [Test Idle Movement](Test_Idle_Movement.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Npc Base](Npc_Base.md) (1 shared connections)

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