# .start()

> 4 nodes

## Key Concepts

- **.start()** (4 connections) — `server/services/game_tick_service.py`
- **._tick_loop()** (3 connections) — `server/services/game_tick_service.py`
- **Start the game tick service.          Returns:             bool: True if started** (1 connections) — `server/services/game_tick_service.py`
- **Main tick loop that runs at the specified interval.** (1 connections) — `server/services/game_tick_service.py`

## Relationships

- [GameTickService](GameTickService.md) (2 shared connections)
- [test command parser](test_command_parser.md) (1 shared connections)

## Source Files

- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*