# Whisper Channel System

> 8 nodes

## Key Concepts

- **handle_explore_command()** (9 connections) — `server/commands/exploration_commands.py`
- **test_handle_explore_command()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **asyncio** (2 connections)
- **Any** (1 connections)
- **Handle exploration requests by returning a simple message. This lightweight…** (1 connections) — `server/commands/exploration_commands.py`
- **Test handle_explore_command() explores area.** (1 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **Test handle_explore_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_exploration_commands.py`

## Relationships

- [pytest.md](pytest.md.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`

## Audit Trail

- EXTRACTED: 13 (87%)
- INFERRED: 2 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*