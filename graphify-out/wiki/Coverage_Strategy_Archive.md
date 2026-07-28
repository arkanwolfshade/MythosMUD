# Coverage Strategy Archive

> 4 nodes · cohesion 0.50

## Key Concepts

- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **_FollowTargetValue** (1 connections)
- **TypeGuard** (1 connections)
- **True when v is the 3-tuple (target_id, 'npc', display_name).** (1 connections) — `server/game/follow_service.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Map Editing Hooks](Map_Editing_Hooks.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*