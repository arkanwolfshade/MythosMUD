# Semgrep Configuration

> 15 nodes · cohesion 0.13

## Key Concepts

- **.shutdown_all()** (8 connections) — `server/app/task_registry.py`
- **Event** (4 connections)
- **.__init__()** (4 connections) — `server/events/event_bus.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.__init__()** (3 connections) — `server/app/task_registry.py`
- **._wait_for_task_completion()** (3 connections) — `server/app/task_registry.py`
- **Cancel lifecycle/critical tasks first (Phase 1).** (1 connections) — `server/app/task_registry.py`
- **Cancel remaining active tasks (Phase 2).** (1 connections) — `server/app/task_registry.py`
- **Wait for task completion with timeout.** (1 connections) — `server/app/task_registry.py`
- **Forcibly cancel any lingering tasks that didn't respond to graceful…** (1 connections) — `server/app/task_registry.py`
- **Gracefully shutdown all tracked tasks with timeout coordination. Implements…** (1 connections) — `server/app/task_registry.py`
- **Initialize TaskRegistry with empty task collections.** (1 connections) — `server/app/task_registry.py`
- **Initialize the pure async event bus.** (1 connections) — `server/events/event_bus.py`

## Relationships

- [command_error](command_error.md) (7 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 21 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*