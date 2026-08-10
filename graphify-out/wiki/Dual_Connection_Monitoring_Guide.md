# Dual Connection Monitoring Guide

> 25 nodes

## Key Concepts

- **idle_movement.py** (17 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **NPC Idle Movement Handler for MythosMUD.  This module provides idle movement f** (1 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement.          Checks multiple con** (1 connections) — `server/npc/idle_movement.py`
- **Get exits from current room that stay within subzone boundaries.          Args** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities.          Args:             exit_** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn ro** (1 connections) — `server/npc/idle_movement.py`
- **Execute idle movement for an NPC.          This method orchestrates the full i** (1 connections) — `server/npc/idle_movement.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [Cursor Bug Agents](Cursor_Bug_Agents.md) (9 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (1 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Cursor Skills Arrange](Cursor_Skills_Arrange.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 89 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*