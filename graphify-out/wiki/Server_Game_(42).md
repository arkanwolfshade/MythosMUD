# Server Game (42)

> 12 nodes

## Key Concepts

- **ChatWhisperTracker** (7 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player.          Args:             receiver_** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get the last whisper sender for a player.          Args:             player_name** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Clear the last whisper sender for a player.          Args:             player_na** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get all whisper trackings (for testing/debugging).          Returns:** (1 connections) — `server/game/chat_whisper_tracker.py`

## Relationships

- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*