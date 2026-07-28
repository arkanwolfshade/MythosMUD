# Realtime Statistics Aggregator

> 6 nodes · cohesion 0.20

## Key Concepts

- **ChannelBroadcastingStrategyFactory** (11 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.register_strategy()** (3 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_init()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_register_strategy()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_global_channel_strategy_factory_instance()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns UnknownChannelStr** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [Validation Rule Base](Validation_Rule_Base.md) (4 shared connections)
- [Phase Three Complete Summary](Phase_Three_Complete_Summary.md) (3 shared connections)
- [Npc Config Parsing](Npc_Config_Parsing.md) (3 shared connections)
- [Planning Contingency Plans](Planning_Contingency_Plans.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 22 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*