# Logging File Setup

> 10 nodes · cohesion 0.04

## Key Concepts

- **Queue** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **Handler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **RotatingFileHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LogRecord** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **Path** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **Formatter** (4 connections) — `server/structured_logging/logging_file_setup.py`
- **QueueListener** (4 connections) — `server/structured_logging/logging_file_setup.py`
- **Logger** (3 connections) — `server/structured_logging/logging_file_setup.py`
- **_PlayerGuidFormatterType** (2 connections) — `server/structured_logging/logging_utilities.py`
- **BoundLogger** (2 connections) — `server/structured_logging/logging_utilities.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`

## Audit Trail

- EXTRACTED: 34 (68%)
- INFERRED: 16 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*