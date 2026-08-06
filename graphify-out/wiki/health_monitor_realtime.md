# health monitor realtime

> 14 nodes

## Key Concepts

- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **chat_whisper_tracker.py** (5 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Chat whisper tracking utilities.  This module provides whisper tracking function** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player.          Args:             receiver_** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get the last whisper sender for a player.          Args:             player_name** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Clear the last whisper sender for a player.          Args:             player_na** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get all whisper trackings (for testing/debugging).          Returns:** (1 connections) — `server/game/chat_whisper_tracker.py`

## Relationships

- [chat game message](chat_game_message.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)

## Source Files

- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*