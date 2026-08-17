# NPCAttacked

> 14 nodes

## Key Concepts

- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **._attack_target_impl()** (6 connections) — `server/npc/aggressive_mob_npc.py`
- **.attack_target()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._attack_via_combat_integration()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._get_attack_damage()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_attack_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **Event fired when an NPC attacks a target. This event is triggered when an NPC…** (1 connections) — `server/events/event_types.py`
- **Resolve attack_damage from behavior config with robust typing.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Try to handle the attack via combat integration. Returns: True/False if…** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Internal implementation for attacking a target.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Attack a specific target.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle attacking target action.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Publish NPC attack event to event bus.** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (5 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [combat_integration.py](combat_integration.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*