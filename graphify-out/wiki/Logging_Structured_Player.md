# Logging Structured Player

> 25 nodes · cohesion 0.09

## Key Concepts

- **PlayerGuidFormatter** (16 connections) — `server/structured_logging/player_guid_formatter.py`
- **logging_utilities.py** (10 connections) — `server/structured_logging/logging_utilities.py`
- **load_player_guid_formatter_class()** (10 connections) — `server/structured_logging/logging_utilities.py`
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **.format()** (4 connections) — `server/structured_logging/player_guid_formatter.py`
- **._convert_player_guids()** (3 connections) — `server/structured_logging/player_guid_formatter.py`
- **_PlayerGuidFormatterType** (2 connections) — `server/structured_logging/logging_utilities.py`
- **BoundLogger** (2 connections) — `server/structured_logging/logging_utilities.py`
- **player_guid_formatter.py** (2 connections) — `server/structured_logging/player_guid_formatter.py`
- **._get_player_name()** (2 connections) — `server/structured_logging/player_guid_formatter.py`
- **.__init__()** (2 connections) — `server/structured_logging/player_guid_formatter.py`
- **._is_likely_player_id()** (2 connections) — `server/structured_logging/player_guid_formatter.py`
- **LogRecord** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Logging utilities for directory management, path resolution, and environment det** (1 connections) — `server/structured_logging/logging_utilities.py`
- **# NOTE: Using structlog directly here to avoid circular import.** (1 connections) — `server/structured_logging/logging_utilities.py`
- **# NOTE: Infrastructure files may use structlog.get_logger() directly to avoid** (1 connections) — `server/structured_logging/logging_utilities.py`
- **Return PlayerGuidFormatter without a static import from caller modules.      Imp** (1 connections) — `server/structured_logging/logging_utilities.py`
- **Structlog logger for rotate_log_files (cast silences basedpyright Any from get_l** (1 connections) — `server/structured_logging/logging_utilities.py`
- **Player GUID Formatter for MythosMUD logging system.  This module provides a cust** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Determine if a GUID is likely to be a player ID based on context.          Args:** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Get player name for GUID from in-memory data.          Args:             guid: T** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Custom formatter that converts player GUIDs to "<name>: <GUID>" format.      Thi** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Initialize the PlayerGuidFormatter.          Args:             player_service: S** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Format a log record with enhanced player GUID display.          Args:** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Convert player GUIDs in message to enhanced format.          Args:             m** (1 connections) — `server/structured_logging/player_guid_formatter.py`

## Relationships

- [[Logging Path Utilities]] (6 shared connections)
- [[Player GUID Formatter]] (5 shared connections)
- [[Logging File Setup]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Logging Rotating Handlers]] (2 shared connections)

## Source Files

- `server/structured_logging/logging_utilities.py`
- `server/structured_logging/player_guid_formatter.py`

## Audit Trail

- EXTRACTED: 66 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
