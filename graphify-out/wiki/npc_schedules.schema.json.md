# npc_schedules.schema.json

> 16 nodes

## Key Concepts

- **PlayerService** (6 connections)
- **.__init__()** (5 connections) — `server/game/chat_service.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **player_service()** (4 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **player_service()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **fixture** (2 connections)
- **fixture** (2 connections)
- **fixture** (1 connections)
- **Initialize chat service. Args: persistence: Database persistence layer…** (1 connections) — `server/game/chat_service.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Create a PlayerService instance.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/game/test_player_service.py`
- **Create a PlayerService instance.** (1 connections) — `server/tests/unit/game/test_player_service.py`
- **Create a RateLimiter instance for testing.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`

## Relationships

- [._create_tracked_task](_create_tracked_task.md) (3 shared connections)
- [useAsciiMapState.ts](useAsciiMapState.ts.md) (2 shared connections)
- [container_persistence.py](container_persistence.py.md) (1 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (1 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [Commands](Commands.md) (1 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (1 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/utils/test_rate_limiter_utils.py`

## Audit Trail

- EXTRACTED: 19 (73%)
- INFERRED: 7 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*