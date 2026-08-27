# Cursor Subagents Overview

> 12 nodes

## Key Concepts

- **TimeConfig** (7 connections) — `server/config/models/chat_time.py`
- **ChatConfig** (5 connections) — `server/config/models/chat_time.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.validate_rate_limits()** (3 connections) — `server/config/models/chat_time.py`
- **.validate_compression_ratio()** (3 connections) — `server/config/models/chat_time.py`
- **BaseSettings** (2 connections)
- **field_validator** (2 connections)
- **Path** (1 connections)
- **Chat system configuration.** (1 connections) — `server/config/models/chat_time.py`
- **Validate rate limits are reasonable.** (1 connections) — `server/config/models/chat_time.py`
- **Temporal compression configuration for the MythosChronicle.** (1 connections) — `server/config/models/chat_time.py`
- **Ensure we never divide by zero or run the chronicle backward.** (1 connections) — `server/config/models/chat_time.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (3 shared connections)

## Source Files

- `server/config/models/chat_time.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*