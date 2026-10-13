# Community 632

> 27 nodes

## Key Concepts

- **idle_movement.py** (19 connections) — `server/npc/idle_movement.py`
- **is_npc_in_combat()** (10 connections) — `server/npc/movement_integration.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **_npc_alive_and_active()** (3 connections) — `server/npc/idle_movement.py`
- **test_is_npc_in_combat_fails_closed_on_lookup_error()** (3 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **test_is_npc_in_combat_false_without_combat_service()** (3 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **setter** (1 connections)
- **NPC Idle Movement Handler for MythosMUD. This module provides idle movement…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn. Args:…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities. Args: exit_weights: List of…** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn…** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms. This is a simplified distance…** (1 connections) — `server/npc/idle_movement.py`
- **True if the NPC is in combat. Fails closed: a lookup error counts as in combat…** (1 connections) — `server/npc/movement_integration.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 160](Community_160.md) (15 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (4 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (4 shared connections)
- [Community 248](Community_248.md) (2 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_idle_movement_combat_gate.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*