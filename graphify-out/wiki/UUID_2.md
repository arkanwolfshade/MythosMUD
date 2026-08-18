# UUID

> 16 nodes

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

- [channel_broadcasting_strategies.py](channel_broadcasting_strategies.py.md) (4 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [RoomBasedChannelStrategy](RoomBasedChannelStrategy.md) (1 shared connections)
- [SystemAdminChannelStrategy](SystemAdminChannelStrategy.md) (1 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*