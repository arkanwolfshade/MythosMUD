# PlayerChannelPreferences

> 24 nodes

## Key Concepts

- **Any** (19 connections)
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.set_instance_manager()** (3 connections) — `server/async_persistence.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence.py`
- **._process_exit_rows()** (3 connections) — `server/async_persistence.py`
- **._build_room_objects()** (3 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence.py`
- **.get_containers_by_room_id()** (3 connections) — `server/async_persistence.py`
- **.update_container()** (3 connections) — `server/async_persistence.py`
- **.ensure_item_instance()** (3 connections) — `server/async_persistence.py`
- **Set the instance manager for instanced room lookup (instance-first).** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence.py`
- **Create a new container.          Args:             source_type: Type of containe** (1 connections) — `server/async_persistence.py`
- **Get all containers in a room.** (1 connections) — `server/async_persistence.py`
- **Ensure an item instance exists. Delegates to ItemRepository.          Accepts ke** (1 connections) — `server/async_persistence.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (12 shared connections)
- [init](init.md) (4 shared connections)
- [find dead connections()](find_dead_connections%28%29.md) (1 shared connections)
- [time commands](time_commands.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 64 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*