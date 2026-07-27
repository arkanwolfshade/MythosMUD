# Catatonia Check Logic

> 6 nodes · cohesion 0.04

## Key Concepts

- **CommandExecutionRequest** (11 connections) — `server/command_handler/command_execution_request.py`
- **UUID** (8 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections) — `server/command_handler/alias_expansion.py`
- **Any** (2 connections) — `server/command_handler/alias_expansion.py`
- **AsyncSession** (2 connections) — `server/command_handler/catatonia_check.py`

## Relationships

- [Realtime Message Formatters](Realtime_Message_Formatters.md) (3 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`

## Audit Trail

- EXTRACTED: 15 (50%)
- INFERRED: 15 (50%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*