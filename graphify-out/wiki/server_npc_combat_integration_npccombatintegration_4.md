# server npc combat integration npccombatintegration

> 6 nodes

## Key Concepts

- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **._get_npc_stats()** (2 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (2 connections) — `server/npc/combat_integration.py`
- **Publish NPC attack event to event bus.** (1 connections) — `server/npc/combat_integration.py`
- **Handle NPC death and related effects. Args: npc_id: ID of the dead NPC room_id:…** (1 connections) — `server/npc/combat_integration.py`
- **Get NPC stats or use defaults.** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (3 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*