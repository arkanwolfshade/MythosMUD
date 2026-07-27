# Death Delirium UI Modals

> 17 nodes · cohesion 0.11

## Key Concepts

- **Any** (19 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **._build_room_objects()** (3 connections) — `server/async_persistence.py`
- **.ensure_item_instance()** (3 connections) — `server/async_persistence.py`
- **.get_containers_by_room_id()** (3 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence.py`
- **._process_exit_rows()** (3 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence.py`
- **.set_instance_manager()** (3 connections) — `server/async_persistence.py`
- **.update_container()** (3 connections) — `server/async_persistence.py`
- **._generate_room_id_from_zone_data()** (2 connections) — `server/async_persistence.py`
- **Set the instance manager for instanced room lookup (instance-first).** (1 connections) — `server/async_persistence.py`
- **Get all containers in a room.** (1 connections) — `server/async_persistence.py`
- **Ensure an item instance exists. Delegates to ItemRepository.          Accepts ke** (1 connections) — `server/async_persistence.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (13 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 62 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*