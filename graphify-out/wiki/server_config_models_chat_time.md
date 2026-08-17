# server config models chat time

> 5 nodes

## Key Concepts

- **.validate_rate_limits()** (3 connections) — `server/config/models/chat_time.py`
- **.validate_compression_ratio()** (3 connections) — `server/config/models/chat_time.py`
- **field_validator** (2 connections)
- **Validate rate limits are reasonable.** (1 connections) — `server/config/models/chat_time.py`
- **Ensure we never divide by zero or run the chronicle backward.** (1 connections) — `server/config/models/chat_time.py`

## Relationships

- [server config init create config](server_config_init_create_config.md) (1 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)

## Source Files

- `server/config/models/chat_time.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*