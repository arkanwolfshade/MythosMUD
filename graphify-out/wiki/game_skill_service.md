# game skill service

> 8 nodes

## Key Concepts

- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_processing.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_processing.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (6 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [subject admin controller](subject_admin_controller.md) (2 shared connections)
- [combat services service](combat_services_service.md) (2 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)
- [subject nats manager](subject_nats_manager.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [player look commands](player_look_commands.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*