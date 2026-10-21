# test_channel_broadcasting_strategies.py

> 21 nodes · cohesion 0.10

## Key Concepts

- **async_persistence_types.py** (7 connections) — `server/async_persistence_types.py`
- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **ContainerCreateKwargs** (6 connections) — `server/async_persistence_types.py`
- **PlayerEffectOptions** (6 connections) — `server/async_persistence_types.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.ensure_item_instance()** (4 connections) — `server/async_persistence.py`
- **.set_instance_manager()** (3 connections) — `server/async_persistence.py`
- **Unpack** (2 connections)
- **.get_room_by_id()** (2 connections) — `server/async_persistence_types.py`
- **TypedDict** (2 connections)
- **Set the instance manager for instanced room lookup (instance-first).** (1 connections) — `server/async_persistence.py`
- **Add a player effect. Returns effect id.** (1 connections) — `server/async_persistence.py`
- **Create a new container. Args: source_type: Type of container source (required)…** (1 connections) — `server/async_persistence.py`
- **Ensure an item instance exists. Delegates to ItemRepository. Accepts keyword…** (1 connections) — `server/async_persistence.py`
- **Protocol** (1 connections)
- **Room** (1 connections)
- **Shared typing helpers for the async persistence facade.** (1 connections) — `server/async_persistence_types.py`
- **Minimal instance-manager surface used for instanced room lookup.** (1 connections) — `server/async_persistence_types.py`
- **Backward-compatible kwargs for create_container when params is omitted.** (1 connections) — `server/async_persistence_types.py`
- **Optional fields for add_player_effect beyond the required scalars.** (1 connections) — `server/async_persistence_types.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (7 shared connections)
- [Room](Room.md) (4 shared connections)
- [whisper-movement.spec.ts](whisper-movement.spec.ts.md) (1 shared connections)
- [.profession_to_dict](profession_to_dict.md) (1 shared connections)
- [command_result_text](command_result_text.md) (1 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_types.py`

## Audit Trail

- EXTRACTED: 34 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*