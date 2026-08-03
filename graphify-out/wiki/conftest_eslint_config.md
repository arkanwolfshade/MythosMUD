# conftest eslint config

> 12 nodes

## Key Concepts

- **register_default_reactions_for_npc()** (15 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **test_register_passive_mob_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_aggressive_mob_retaliation_only()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_unknown_type_no_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_logs_debug()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_handles_import_error()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **Register default reactions, room context, and chat display name.** (1 connections) — `server/npc/npc_base.py`
- **Build and register default event reactions for this NPC (greeting, farewell, etc** (1 connections) — `server/npc/npc_default_reactions.py`
- **Unit tests for default NPC event reaction registration.** (1 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*