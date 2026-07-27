# Game Emote Service

> 4 nodes · cohesion 0.50

## Key Concepts

- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **Get the emote definition for a command.          Args:             command: The** (1 connections) — `server/game/emote_service.py`
- **Format emote messages for the player and room occupants.          Args:** (1 connections) — `server/game/emote_service.py`

## Relationships

- [[Chat Message Helpers]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Emote Schema Validator]] (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
