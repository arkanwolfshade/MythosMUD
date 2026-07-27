# Rescue Service Tests

> 7 nodes · cohesion 0.04

## Key Concepts

- **Any** (7 connections) — `server/commands/rescue_commands.py`
- **Any** (6 connections) — `server/services/rescue_service.py`
- **UUID** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (4 connections) — `server/services/rescue_service.py`
- **AsyncSessionFactory** (3 connections) — `server/services/rescue_service.py`
- **EventDispatcher** (3 connections) — `server/services/rescue_service.py`
- **LucidityServiceFactory** (3 connections) — `server/services/rescue_service.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/rescue_service.py`

## Audit Trail

- EXTRACTED: 21 (68%)
- INFERRED: 10 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*