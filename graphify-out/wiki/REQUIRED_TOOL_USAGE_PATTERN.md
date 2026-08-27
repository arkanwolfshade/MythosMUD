# REQUIRED TOOL USAGE PATTERN

> 12 nodes

## Key Concepts

- **ChatWhisperTracker** (7 connections) — `server/game/chat_whisper_tracker.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player. Args: receiver_name: Name of the…** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get the last whisper sender for a player. Args: player_name: Name of the player…** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Clear the last whisper sender for a player. Args: player_name: Name of the…** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get all whisper trackings (for testing/debugging). Returns: Dictionary mapping…** (1 connections) — `server/game/chat_whisper_tracker.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*