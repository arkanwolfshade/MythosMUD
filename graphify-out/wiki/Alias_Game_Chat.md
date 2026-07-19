# Alias Game Chat

> 5 nodes · cohesion 0.40

## Key Concepts

- **.model_dump()** (4 connections) — `server/models/alias.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **Convert alias to dictionary for JSON serialization.** (3 connections) — `server/models/alias.py`
- **Any** (1 connections) — `server/game/chat_message.py`
- **Any** (1 connections) — `server/models/alias.py`

## Relationships

- [[Chat Message Helpers]] (1 shared connections)
- [[Command Alias Model]] (1 shared connections)
- [[WebSocket Player Helpers]] (1 shared connections)
- [[Dead Letter Queue]] (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/models/alias.py`

## Audit Trail

- EXTRACTED: 11 (92%)
- INFERRED: 1 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
