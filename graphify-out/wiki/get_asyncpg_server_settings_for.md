# get asyncpg server settings for

> 10 nodes

## Key Concepts

- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle_npc_attack()** (4 connections) — `server/npc/combat_integration_base.py`
- **Return the live NPC combat integration service for delegation.      Prefer ``C** (1 connections) — `server/npc/combat_integration_base.py`
- **Handle an NPC attack on a target.          This is a thin wrapper around _hand** (1 connections) — `server/npc/combat_integration_base.py`
- **Core implementation for handling an NPC attack on a target.          When the** (1 connections) — `server/npc/combat_integration_base.py`
- **Prefer full combat codepath (same as player-initiated combat) when available.** (1 connections) — `server/npc/combat_integration_base.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [PanelManager](PanelManager.md) (5 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [init](init.md) (1 shared connections)
- [process dead players()](process_dead_players%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [MessageHandlerFactory](MessageHandlerFactory.md) (1 shared connections)
- [processing](processing.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 26 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*