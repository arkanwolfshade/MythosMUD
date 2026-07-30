# channel broadcasting strategies

> 14 nodes

## Key Concepts

- **test_channel_broadcasting_strategies.py** (26 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **PartyChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_global_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_sends_only_to_party_members()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_service_no_send()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_party_not_found_no_send()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_party_channel_strategy_broadcast_no_party_id()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Strategy for party channel broadcasting. Delivers only to current party members.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Unit tests for channel broadcasting strategies.  Tests the channel_broadcasting_** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test GlobalChannelStrategy.broadcast() broadcasts globally.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Party chat is delivered only to current party members (visibility).** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **When party_service is missing on handler, no message is sent.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **When party does not exist, no message is sent.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test PartyChannelStrategy.broadcast() handles missing party_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [add fastapi users columns](add_fastapi_users_columns.md) (7 shared connections)
- [PartyService](PartyService.md) (5 shared connections)
- [test inventory mutation guard internal](test_inventory_mutation_guard_internal.md) (4 shared connections)
- [admin summon command](admin_summon_command.md) (4 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [.broadcast()](broadcast%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*