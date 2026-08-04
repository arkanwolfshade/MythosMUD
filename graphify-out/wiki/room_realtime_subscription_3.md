# room realtime subscription

> 2 nodes

## Key Concepts

- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **_publish_attack_event forwards to event bus when configured.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (1 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 4 (80%)
- INFERRED: 1 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*