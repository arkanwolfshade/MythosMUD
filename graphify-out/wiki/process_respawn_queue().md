# .process respawn queue()

> 13 nodes

## Key Concepts

- **lifecycle_respawn.py** (9 connections) — `server/npc/lifecycle_respawn.py`
- **process_respawn_queue_impl()** (7 connections) — `server/npc/lifecycle_respawn.py`
- **_process_respawn_queue_entry()** (5 connections) — `server/npc/lifecycle_respawn.py`
- **Any** (4 connections)
- **_cleanup_respawn_queue()** (4 connections) — `server/npc/lifecycle_respawn.py`
- **_attempt_respawn_impl()** (4 connections) — `server/npc/lifecycle_respawn.py`
- **.process_respawn_queue()** (3 connections) — `server/npc/lifecycle_manager.py`
- **Process the respawn queue and spawn NPCs that are ready (delegates to lifecycle_** (1 connections) — `server/npc/lifecycle_manager.py`
- **Respawn queue processing for NPC lifecycle.  Extracted from lifecycle_manager to** (1 connections) — `server/npc/lifecycle_respawn.py`
- **Process the respawn queue and spawn NPCs that are ready.      Args:         mana** (1 connections) — `server/npc/lifecycle_respawn.py`
- **Process a single respawn queue entry. Returns (should_remove, was_respawned).** (1 connections) — `server/npc/lifecycle_respawn.py`
- **Remove processed NPCs from respawn queue.** (1 connections) — `server/npc/lifecycle_respawn.py`
- **Attempt to respawn an NPC. Returns True if respawn was successful.** (1 connections) — `server/npc/lifecycle_respawn.py`

## Relationships

- [parse jsonb column()](parse_jsonb_column%28%29.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_respawn.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*