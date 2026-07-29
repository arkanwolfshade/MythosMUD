# channel broadcasting strategies

> 59 nodes

## Key Concepts

- **test_channel_broadcasting_strategies.py** (26 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **channel_broadcasting_strategies.py** (14 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **ChannelBroadcastingStrategy** (12 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **ChannelBroadcastingStrategyFactory** (11 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **RoomBasedChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **PartyChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **SystemAdminChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **UnknownChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **WhisperChannelStrategy** (8 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **GlobalChannelStrategy** (7 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.__init__()** (7 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_known()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_unknown()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.register_strategy()** (3 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_global_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_sends_only_to_party_members()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_service_no_send()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_party_not_found_no_send()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_id()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_whisper_channel_strategy_broadcast_no_target()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_personal_target()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- *... and 34 more nodes in this community*

## Relationships

- [.broadcast()](broadcast%28%29.md) (8 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [Initialize room based channel strategy.](Initialize_room_based_channel_strategy.md) (1 shared connections)
- [Initialize system/admin channel strategy. Args:](Initialize_system-admin_channel_strategy._Args-.md) (1 shared connections)
- [Initialize unknown channel strategy. Args:](Initialize_unknown_channel_strategy._Args-.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 204 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*