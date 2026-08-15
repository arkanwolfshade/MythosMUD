# process_npc_maintenance

> 5 nodes

## Key Concepts

- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **test_process_npc_maintenance_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Check if NPC maintenance should run on this tick. Args: tick_count: Current…** (1 connections) — `server/config/npc_config.py`

## Relationships

- [asyncio](asyncio.md) (3 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*