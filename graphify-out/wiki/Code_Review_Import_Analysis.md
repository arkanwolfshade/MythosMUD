# Code Review Import Analysis

> 7 nodes

## Key Concepts

- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via UUID lookup.          Args:             npc_id:** (1 connections) — `server/npc/idle_movement.py`
- **Check if NPC is in combat via string ID mapping.          Args:             n** (1 connections) — `server/npc/idle_movement.py`
- **Check if an NPC is currently in combat.          Args:             npc_instan** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [datetime](datetime.md) (4 shared connections)
- [.get explored rooms()](get_explored_rooms%28%29.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*