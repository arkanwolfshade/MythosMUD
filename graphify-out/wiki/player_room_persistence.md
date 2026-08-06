# player room persistence

> 8 nodes

## Key Concepts

- **WhisperChannelStrategy** (8 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.__init__()** (7 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast_no_target()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Strategy for whisper channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize the strategy factory.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test WhisperChannelStrategy.broadcast() sends personal message.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test WhisperChannelStrategy.broadcast() handles missing target_player_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [channel realtime broadcasting](channel_realtime_broadcasting.md) (4 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (3 shared connections)
- [realtime channel broadcasting](realtime_channel_broadcasting.md) (1 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)
- [world loader rationale](world_loader_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*