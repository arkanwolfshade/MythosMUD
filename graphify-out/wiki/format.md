# .format

> 6 nodes

## Key Concepts

- **.format()** (5 connections) — `server/structured_logging/player_guid_formatter.py`
- **_canonical_ip()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **._convert_player_guids()** (3 connections) — `server/structured_logging/player_guid_formatter.py`
- **LogRecord** (1 connections)
- **Format a log record with enhanced player GUID display. Args: record: The log…** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Convert player GUIDs in message to enhanced format. Args: message: The log…** (1 connections) — `server/structured_logging/player_guid_formatter.py`

## Relationships

- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (1 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/structured_logging/player_guid_formatter.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*