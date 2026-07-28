# Command Integration Summary

> 15 nodes · cohesion 0.12

## Key Concepts

- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (7 connections) — `server/game/chat_service.py`
- **chat_whisper_tracker.py** (5 connections) — `server/game/chat_whisper_tracker.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Chat whisper tracking utilities.  This module provides whisper tracking function** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player.          Args:             receiver_** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get the last whisper sender for a player.          Args:             player_name** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Clear the last whisper sender for a player.          Args:             player_na** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Get all whisper trackings (for testing/debugging).          Returns:** (1 connections) — `server/game/chat_whisper_tracker.py`

## Relationships

- [Command Factory Creators](Command_Factory_Creators.md) (2 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (1 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (1 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (1 shared connections)
- [Services Npc Startup](Services_Npc_Startup.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 37 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*