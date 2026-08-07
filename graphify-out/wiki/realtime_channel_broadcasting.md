# realtime channel broadcasting

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
- **Broadcast message according to channel strategy.          Args:             chat** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast room-based message with server-side filtering.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast global message to all connected players.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast party message to party members only, with dampening and mute checks.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Send whisper message to specific player with communication dampening.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Broadcast system/admin message; personal when target_player_id is set.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Handle unknown channel type.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`

## Relationships

- [channel broadcasting strategies](channel_broadcasting_strategies.md) (4 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)
- [channel realtime broadcasting](channel_realtime_broadcasting.md) (1 shared connections)
- [player room persistence](player_room_persistence.md) (1 shared connections)
- [world loader rationale](world_loader_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*