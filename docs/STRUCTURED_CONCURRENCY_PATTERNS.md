# Structured Concurrency Patterns

This document outlines the structured concurrency patterns used in the MythosMUD codebase, based on AnyIO best practices adapted for asyncio.

## Overview

Structured concurrency ensures that all async tasks are properly managed, tracked, and cleaned up. This prevents resource leaks, orphaned tasks, and difficult-to-debug issues.

## Core Principles

1. **Task Tracking**: All background tasks should be tracked for proper lifecycle management
2. **Structured Cleanup**: Tasks should be properly cancelled and cleaned up during shutdown
3. **Exception Handling**: Exceptions in concurrent tasks should be properly aggregated and handled
4. **No Orphaned Tasks**: All tasks should complete or be cancelled before their parent context ends

## Patterns

### Pattern 1: Structured Concurrency for Multiple Async Operations

**Use Case**: When you need to run multiple async operations concurrently and ensure all complete.

**Implementation**: Use `asyncio.gather()` with `return_exceptions=True` to ensure all tasks complete even if some fail.

**Example** (EventBus):

```python
# Process async subscribers with structured concurrency
if async_subscribers:
    tasks: list[asyncio.Task] = []
    subscriber_names: dict[asyncio.Task, str] = {}

    for subscriber in async_subscribers:
        task = asyncio.create_task(subscriber(event))
        tasks.append(task)
        subscriber_names[task] = subscriber_name
        self._active_tasks.add(task)

    # Wait for all tasks with structured concurrency pattern
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Log any exceptions from subscribers
    for task, result in zip(tasks, results):
        if isinstance(result, Exception):
            self._logger.error("Error in async subscriber", ...)
```

**Benefits**:
- All tasks complete even if some fail
- Exceptions are properly logged
- Tasks are tracked for cleanup

### Pattern 2: Tracked Background Tasks

**Use Case**: Long-running background tasks that need lifecycle management.

**Implementation**: Create a helper method to track all background tasks.

**Example** (NATS Service):

```python
def _create_tracked_task(
    self, coro, task_name: str = "nats_background", task_type: str = "background"
) -> asyncio.Task:
    """
    Create a tracked background task with proper lifecycle management.

    AnyIO Pattern: Track all background tasks for proper cleanup and monitoring.
    """
    try:
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)

        # Remove from tracking when complete
        def remove_task(t: asyncio.Task) -> None:
            self._background_tasks.discard(t)

        task.add_done_callback(remove_task)
        return task
    except RuntimeError as e:
        logger.error("Failed to create tracked task", ...)
        raise
```

**Benefits**:
- All background tasks are tracked
- Automatic cleanup on completion
- Proper error handling

### Pattern 3: Structured Cleanup on Shutdown

**Use Case**: Cancelling all background tasks during service shutdown.

**Implementation**: Cancel all tracked tasks and wait for them to complete.

**Example** (NATS Service):

```python
async def _cancel_background_tasks(self):
    """
    Cancel all tracked background tasks for proper cleanup.

    AnyIO Pattern: Structured cleanup of all background tasks ensures
    no orphaned tasks remain after shutdown.
    """
    if not self._background_tasks:
        return

    # Cancel all background tasks
    for task in list(self._background_tasks):
        if not task.done():
            task.cancel()

    # Wait for tasks to complete with timeout
    if self._background_tasks:
        done, pending = await asyncio.wait(
            self._background_tasks, timeout=2.0, return_when=asyncio.ALL_COMPLETED
        )

        # Force cancel any remaining tasks
        if pending:
            for task in pending:
                if not task.done():
                    task.cancel()
            await asyncio.wait_for(
                asyncio.gather(*pending, return_exceptions=True), timeout=0.5
            )

    self._background_tasks.clear()
```

**Benefits**:
- All tasks are properly cancelled
- Timeout prevents hanging
- Clean state after shutdown

### Pattern 4: Fire-and-Forget with Error Logging

**Use Case**: Tasks that should run independently but need error logging.

**Implementation**: Create task with error logging callback.

**Example** (Catatonia Registry):

```python
if asyncio.iscoroutine(result):
    try:
        task = asyncio.create_task(result)
        # Add a callback to log if it fails
        def log_failover_error(t: asyncio.Task) -> None:
            try:
                t.result()  # This will raise if task failed
            except Exception as e:
                logger.error("Failover callback task failed", ...)
        task.add_done_callback(log_failover_error)
    except RuntimeError:
        logger.warning("Failover callback requires event loop", ...)
```

**Benefits**:
- Tasks run independently
- Errors are logged
- No blocking of main flow

## When to Use Each Pattern

### Use Pattern 1 (Structured Concurrency) when:
- You have multiple async operations that should all complete
- You want to ensure all operations run even if some fail
- You need to aggregate results or exceptions

### Use Pattern 2 (Tracked Background Tasks) when:
- You have long-running background tasks
- Tasks need lifecycle management
- You need to cancel tasks during shutdown

### Use Pattern 3 (Structured Cleanup) when:
- You're implementing service shutdown
- You need to ensure all tasks are cancelled
- You want to prevent resource leaks

### Use Pattern 4 (Fire-and-Forget) when:
- Tasks should run independently
- Tasks are intentionally decoupled
- You still want error logging

## Anti-Patterns to Avoid

### ❌ Creating tasks without tracking

```python
# BAD: Task is not tracked
asyncio.create_task(background_operation())
```

### ❌ Creating tasks in loops without structured concurrency

```python
# BAD: Tasks created without proper coordination
for item in items:
    asyncio.create_task(process_item(item))
```

### ❌ Not cleaning up tasks on shutdown

```python
# BAD: Tasks may be orphaned
async def shutdown(self):
    self._running = False
    # Missing: Cancel and wait for tasks
```

### ❌ Blocking operations in async context

```python
# BAD: Blocks event loop
async def process_data(self):
    time.sleep(1)  # Should use asyncio.sleep() or asyncio.to_thread()
```

## Testing Structured Concurrency

When testing structured concurrency patterns:

1. **Verify task completion**: Ensure all tasks complete or are properly cancelled
2. **Test exception handling**: Verify exceptions are properly logged and don't crash the system
3. **Test cleanup**: Ensure tasks are cleaned up after completion or cancellation
4. **Test shutdown**: Verify all tasks are cancelled during shutdown

Example test:

```python
@pytest.mark.asyncio
async def test_structured_concurrency_task_cleanup(self):
    """Test that tasks are properly cleaned up after structured concurrency execution."""
    service = MyService()

    # Create tasks
    task1 = service._create_tracked_task(background_task1())
    task2 = service._create_tracked_task(background_task2())

    # Verify tasks are tracked
    assert len(service._background_tasks) == 2

    # Shutdown should clean up
    await service.shutdown()

    # Verify cleanup
    assert len(service._background_tasks) == 0
    assert task1.done()
    assert task2.done()
```

## References

- [AnyIO Best Practices](.cursor/rules/anyio.mdc)
- [Python asyncio.TaskGroup](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup) (Python 3.11+)
- [Structured Concurrency](https://en.wikipedia.org/wiki/Structured_concurrency)

## Implementation Status

- ✅ EventBus: Uses structured concurrency for async subscribers
- ✅ NATS Service: Tracks all background tasks with proper cleanup
- ✅ Connection Manager: Health check tasks properly managed
- ✅ Catatonia Registry: Fire-and-forget tasks with error logging
