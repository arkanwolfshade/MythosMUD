# Any

> 13 nodes

## Key Concepts

- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (7 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (3 connections) — `server/realtime/player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **Any** (1 connections)
- **Check if a value is a valid non-empty string name.      Args:         name: Valu** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format.      Args:         value: String to check** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object.      Args:         player:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID.      Args:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Get player position from stats.      Args:         player: The player object** (1 connections) — `server/realtime/player_presence_utils.py`

## Relationships

- [Player](Player.md) (7 shared connections)
- [player presence tracker](player_presence_tracker.md) (5 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*