# fixtures/auth.ts

> 180 nodes · cohesion 0.01

## Key Concepts

- **Player** (281 connections) — `server/models/player.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **CorruptionCooldown** (13 connections) — `server/models/corruption.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **CorruptionAdjustmentLog** (9 connections) — `server/models/corruption.py`
- **asyncio** (9 connections)
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.damage_player()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.heal_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (5 connections)
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_convert_legacy_stats_string()** (4 connections) — `server/models/player.py`
- *... and 155 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (45 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (17 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (13 shared connections)
- [FollowService](FollowService.md) (13 shared connections)
- [endpoints.py](endpoints.py.md) (12 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (12 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (12 shared connections)
- [test_party_service.py](test_party_service.py.md) (11 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (9 shared connections)
- [retry.py](retry.py.md) (8 shared connections)
- [TargetMatch](TargetMatch.md) (7 shared connections)

## Source Files

- `server/models/corruption.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 402 (74%)
- INFERRED: 140 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*