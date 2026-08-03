# combat models rationale

> 54 nodes

## Key Concepts

- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **test_validate_and_fix_player_room_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_lucidity_loss_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_fear_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_corruption_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_heal_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_heal_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_damage_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_damage_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_async_persistence_creates_instance()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_async_persistence_returns_same_instance()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_reset_async_persistence()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_player_by_user_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_container_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_containers_by_room_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_containers_by_entity_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_update_container_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_decayed_containers_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_decayed_containers_none_time()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_delete_container_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_item_instance_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_ensure_item_instance_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_item_instance_exists_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_soft_delete_player_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- *... and 29 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (23 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (10 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (4 shared connections)
- [persistence container item](persistence_container_item.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 144 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*