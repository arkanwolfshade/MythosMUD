# usePanelContext.ts

> 16 nodes · cohesion 0.17

## Key Concepts

- **UUID** (8 connections)
- **Any** (7 connections)
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.broadcast()** (4 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast party message to party members only, with dampening and mute checks.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Send whisper message to specific player with communication dampening.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast system/admin message; personal when target_player_id is set.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Handle unknown channel type.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast message according to channel strategy. Args: chat_event: WebSocket…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast room-based message with server-side filtering.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast global message to all connected players.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`

## Relationships

- [Test Server Remediation Prompt - Cursor Executable Version](Test_Server_Remediation_Prompt_-_Cursor_Executable_Version.md) (4 shared connections)
- [fix_markdown_line_length.py](fix_markdown_line_length.py.md) (1 shared connections)
- [TestCheckCastingState](TestCheckCastingState.md) (1 shared connections)
- [zone_and_subzone](zone_and_subzone.md) (1 shared connections)
- [test_db_connectivity_create_and_read_user](test_db_connectivity_create_and_read_user.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*