# schemas items item

> 6 nodes

## Key Concepts

- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **Resolve NPC instance display name from lifecycle manager, or derive from npc_id.** (1 connections) — `server/npc/combat_integration.py`
- **Best-effort lookup of NPC name from the lifecycle manager.** (1 connections) — `server/npc/combat_integration.py`
- **Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [services nats service](services_nats_service.md) (3 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*