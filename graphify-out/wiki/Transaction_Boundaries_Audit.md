# Transaction Boundaries Audit

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
- **Broadcast system/admin message to all players.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Handle unknown channel type.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`

## Relationships

- [Respawn Persistence Bug](Respawn_Persistence_Bug.md) (5 shared connections)
- [System Audit Status](System_Audit_Status.md) (1 shared connections)
- [Channel Broadcast Strategies](Channel_Broadcast_Strategies.md) (1 shared connections)
- [Error Monitor Service](Error_Monitor_Service.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*