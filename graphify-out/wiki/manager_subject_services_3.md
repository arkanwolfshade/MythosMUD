# manager subject services

> 18 nodes

## Key Concepts

- **logging_utilities.py** (18 connections) — `server/structured_logging/logging_utilities.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **_setup_console_handler()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **Formatter** (2 connections)
- **Configuration for console handler setup (reduces parameter count).** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Set up console handler with structured output.      Returns:         Console han** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Create formatter (with or without PlayerGuidFormatter).** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **BoundLogger** (1 connections)
- **_PlayerGuidFormatterType** (1 connections)
- **Logging utilities for directory management, path resolution, and environment det** (1 connections) — `server/structured_logging/logging_utilities.py`
- **Structlog logger for rotate_log_files (cast silences basedpyright Any from get_l** (1 connections) — `server/structured_logging/logging_utilities.py`
- **Return PlayerGuidFormatter without a static import from caller modules.      Imp** (1 connections) — `server/structured_logging/logging_utilities.py`
- **# NOTE: Infrastructure files may use structlog.get_logger() directly to avoid** (1 connections) — `server/structured_logging/logging_utilities.py`
- **# NOTE: Using structlog directly here to avoid circular import.** (1 connections) — `server/structured_logging/logging_utilities.py`
- **# NOTE: Using structlog directly here to avoid circular import.** (1 connections) — `server/structured_logging/logging_utilities.py`

## Relationships

- [logging setup structured](logging_setup_structured.md) (9 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (6 shared connections)
- [player guid formatter](player_guid_formatter.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (4 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`

## Audit Trail

- EXTRACTED: 62 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*