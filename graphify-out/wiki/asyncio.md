# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (12 connections)
- **PartyChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_global_channel_strategy_broadcast()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_id()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_service_no_send()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_party_not_found_no_send()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_sends_only_to_party_members()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_personal_target()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast_no_target()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Strategy for party channel broadcasting. Delivers only to current party members.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **When party_service is missing on handler, no message is sent.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **When party does not exist, no message is sent.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test PartyChannelStrategy.broadcast() handles missing party_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test WhisperChannelStrategy.broadcast() sends personal message.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test WhisperChannelStrategy.broadcast() handles missing target_player_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Personal system messages deliver to target_player_id only.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test GlobalChannelStrategy.broadcast() broadcasts globally.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Party chat is delivered only to current party members (visibility).** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [test_channel_broadcasting_strategies.py](test_channel_broadcasting_strategies.py.md) (9 shared connections)
- [channel_broadcasting_strategies.py](channel_broadcasting_strategies.py.md) (6 shared connections)
- [SystemAdminChannelStrategy](SystemAdminChannelStrategy.md) (2 shared connections)
- [RoomBasedChannelStrategy](RoomBasedChannelStrategy.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 34 (81%)
- INFERRED: 8 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*