# .move_to_room

> 8 nodes

## Key Concepts

- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **Return True if NPC is in combat (blocks movement); False on lookup failure.** (1 connections) — `server/npc/npc_base.py`
- **Move NPC using movement integration; return True if successful.** (1 connections) — `server/npc/npc_base.py`
- **Move NPC without integration (simple room update).** (1 connections) — `server/npc/npc_base.py`
- **Move NPC to a room; blocked in combat. Return True if successful.** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*