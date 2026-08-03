# npc aggressive mob

> 2 nodes

## Key Concepts

- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **Publish NPC attack event to event bus.** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*