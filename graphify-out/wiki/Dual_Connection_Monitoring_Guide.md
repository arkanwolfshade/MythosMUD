# Dual Connection Monitoring Guide

> 16 nodes

## Key Concepts

- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement.          Checks multiple con** (1 connections) — `server/npc/idle_movement.py`
- **Check if an NPC is currently in combat.          Args:             npc_instan** (1 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries.          Args** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC.          This method orchestrates the full i** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Cursor Skills Arrange](Cursor_Skills_Arrange.md) (2 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*