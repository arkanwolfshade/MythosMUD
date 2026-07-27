# Game Chat Whisper

> 14 nodes · cohesion 0.14

## Key Concepts

- **ChatWhisperTracker** (12 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (6 connections) — `server/game/chat_service.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize chat service.          Args:             persistence: Database persis** (1 connections) — `server/game/chat_service.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player.          Args:             receiver_** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get the last whisper sender for a player.          Args:             player_name** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Clear the last whisper sender for a player.          Args:             player_na** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get all whisper trackings (for testing/debugging).          Returns:** (1 connections) — `server/game/chat_whisper_tracker.py`

## Relationships

- [[Chat Mute Admin API]] (3 shared connections)
- [[Chat Service Whispers]] (2 shared connections)
- [[Chat Moderation Service]] (1 shared connections)
- [[Game Chat Pose]] (1 shared connections)
- [[Chat Message Helpers]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 32 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
