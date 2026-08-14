# register_default_reactions_for_npc

> 15 nodes

## Key Concepts

- **register_default_reactions_for_npc()** (15 connections) — `server/npc/npc_default_reactions.py`
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **test_register_handles_import_error()** (3 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_logs_debug()** (3 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_aggressive_mob_retaliation_only()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_passive_mob_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_unknown_type_no_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **patch** (2 connections)
- **Register default reactions, room context, and chat display name.** (1 connections) — `server/npc/npc_base.py`
- **Register default event reactions for an NPC (greeting, farewell, retaliation,…** (1 connections) — `server/npc/npc_default_reactions.py`
- **Build and register default event reactions for this NPC (greeting, farewell,…** (1 connections) — `server/npc/npc_default_reactions.py`
- **Unit tests for default NPC event reaction registration.** (1 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`

## Relationships

- [event_types.py](event_types.py.md) (7 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*