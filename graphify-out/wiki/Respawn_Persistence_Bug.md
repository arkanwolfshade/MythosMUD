# Respawn Persistence Bug

> 17 nodes

## Key Concepts

- **channel_broadcasting_strategies.py** (14 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **ChannelBroadcastingStrategy** (12 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **WhisperChannelStrategy** (8 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **SystemAdminChannelStrategy** (8 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **GlobalChannelStrategy** (7 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.__init__()** (7 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **ABC** (2 connections)
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Channel Broadcasting Strategies for NATS Message Handler.  This module implement** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Abstract base class for channel broadcasting strategies.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for global channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for whisper channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for system/admin channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize system/admin channel strategy.          Args:             channel_typ** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize the strategy factory.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test WhisperChannelStrategy.broadcast() sends personal message.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [Channel Broadcast Strategies](Channel_Broadcast_Strategies.md) (11 shared connections)
- [Transaction Boundaries Audit](Transaction_Boundaries_Audit.md) (5 shared connections)
- [Emotes JSON Schema](Emotes_JSON_Schema.md) (3 shared connections)
- [System Audit Status](System_Audit_Status.md) (3 shared connections)
- [Error Monitor Service](Error_Monitor_Service.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*