# game rationale schemas

> 22 nodes

## Key Concepts

- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_container_no_holiday_service_attribute()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_logs_debug()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_different_calendar_components()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Return the current Mythos calendar metadata for HUD initialization.      In-memo** (1 connections) — `server/api/game.py`
- **Response model for Mythos calendar time endpoint.** (1 connections) — `server/schemas/game/game.py`
- **Test get_mythos_time returns time data.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles missing holiday service.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles holiday service errors gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles None container.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles upcoming holidays error gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test edge cases for get_mythos_time.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles container without holiday_service attribute.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time logs debug message.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time with different calendar component values.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [realtime player presence](realtime_player_presence.md) (6 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (3 shared connections)
- [invite models create](invite_models_create.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 62 (81%)
- INFERRED: 15 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*