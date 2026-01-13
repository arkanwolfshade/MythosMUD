# AnyIO vs Asyncio: High-Level Comparison and Decision Guide

**Date**: 2026-01-13
**Context**: MythosMUD - FastAPI server with WebSockets, NATS, PostgreSQL

## What Are They?

### `asyncio` (Python Standard Library)

- **What**: Python's built-in asynchronous I/O library (since Python 3.4)
- **Nature**: Low-level, event loop-based concurrency
- **Backend**: Single backend (asyncio's event loop)
- **Philosophy**: "Give developers control, even if they can shoot themselves in the foot"

### `anyio` (Third-Party Library)

- **What**: Unified async API that works on top of asyncio OR Trio
- **Nature**: High-level abstraction layer with structured concurrency
- **Backend**: Backend-agnostic (can use asyncio, Trio, or uvloop)
- **Philosophy**: "Enforce good practices, prevent common mistakes"

## Core Architectural Differences

### 1. **Structured Concurrency**

**asyncio**:

```python
# Tasks can be "orphaned" - no guarantee they complete
task = asyncio.create_task(some_coro())
# If parent function exits, task might still be running
# No automatic cleanup or cancellation
```

**anyio**:

```python
# Tasks are scoped - guaranteed cleanup
async with create_task_group() as tg:
    tg.start_soon(some_coro)
# When scope exits, all tasks are cancelled/waited for
# No orphaned tasks possible
```

**Impact**: AnyIO prevents resource leaks and orphaned tasks that can cause memory issues in long-running servers.

### 2. **Backend Abstraction**

**asyncio**:

- Locked to asyncio's event loop
- To use uvloop (faster), must replace event loop manually
- No way to test with different backends

**anyio**:

- Can run on asyncio, Trio, or uvloop
- Easy backend switching for testing
- Automatic backend detection and optimization

### 3. **API Design Philosophy**

**asyncio**:

- Low-level primitives
- Many ways to do the same thing
- Requires deep understanding to use correctly
- "Power user" API

**anyio**:

- High-level, opinionated API
- Fewer ways to do things (reduces mistakes)
- Easier to learn and use correctly
- "Best practices enforced" API

## Detailed Feature Comparison

### Entry Points

| Feature           | asyncio                  | anyio                                   |
| ----------------- | ------------------------ | --------------------------------------- |
| Entry point       | `asyncio.run()`          | `anyio.run()`                           |
| Backend selection | Manual (if using uvloop) | Automatic or explicit                   |
| Backend detection | No                       | Yes (`sniffio.current_async_library()`) |
| Error handling    | Basic                    | Enhanced with structured concurrency    |

### Primitives

| Primitive     | asyncio                 | anyio                                    | Notes                                          |
| ------------- | ----------------------- | ---------------------------------------- | ---------------------------------------------- |
| Sleep         | `asyncio.sleep()`       | `anyio.sleep()`                          | Functionally identical                         |
| Lock          | `asyncio.Lock()`        | `anyio.Lock()`                           | Functionally identical                         |
| Event         | `asyncio.Event()`       | `anyio.Event()`                          | Functionally identical                         |
| Queue         | `asyncio.Queue()`       | `anyio.create_memory_object_stream()`    | **Different API** - streams vs queue           |
| Timeout       | `asyncio.wait_for()`    | `anyio.move_on_after()` / `fail_after()` | **Different pattern** - context managers       |
| Task creation | `asyncio.create_task()` | `anyio.create_task()` or `TaskGroup`     | AnyIO adds TaskGroup option                    |
| Gather        | `asyncio.gather()`      | `TaskGroup`                              | **Different pattern** - structured concurrency |

### Task Management

**asyncio**:

```python
# Fire-and-forget (can leak)
task = asyncio.create_task(coro)

# Gather (no automatic cancellation)
results = await asyncio.gather(*tasks, return_exceptions=True)
```

**anyio**:

```python
# Structured (automatic cleanup)
async with create_task_group() as tg:
    tg.start_soon(coro1)
    tg.start_soon(coro2)
# All tasks guaranteed to complete/cancel when scope exits

# Or for tracked tasks
task = anyio.create_task(coro)  # Same as asyncio, but backend-agnostic
```

## Pros and Cons

### asyncio Pros ✅

1. **Standard Library**: No external dependency
2. **Universal Compatibility**: Every Python async library supports it
3. **Mature & Stable**: Battle-tested, extensive documentation
4. **Direct Control**: Full access to event loop internals
5. **Performance**: Can be fast with uvloop (manual setup)
6. **Ecosystem**: All async libraries built for it
7. **Learning Resources**: Vast amount of tutorials and examples

### asyncio Cons ❌

1. **No Structured Concurrency**: Easy to create orphaned tasks
2. **Backend Lock-in**: Hard to switch backends or test alternatives
3. **Complex API**: Many ways to do things, easy to make mistakes
4. **Resource Leaks**: Tasks can outlive their creators
5. **Manual uvloop Setup**: Requires explicit event loop replacement
6. **No Built-in Best Practices**: Must know what you're doing

### anyio Pros ✅

1. **Structured Concurrency**: Prevents orphaned tasks and leaks
2. **Backend Agnostic**: Can switch between asyncio/Trio/uvloop
3. **Better Error Handling**: TaskGroup provides superior error propagation
4. **Cleaner API**: Fewer ways to make mistakes
5. **Automatic Optimizations**: Can leverage uvloop automatically
6. **Testing Flexibility**: Test with different backends
7. **Future-Proof**: If Trio becomes preferred, easy to switch
8. **Best Practices Enforced**: Harder to write buggy code

### anyio Cons ❌

1. **External Dependency**: Adds another package (though already transitive via httpx)
2. **API Differences**: Queue → Streams, wait_for → context managers (migration effort)
3. **Less Direct Control**: Abstraction layer hides some event loop details
4. **Smaller Ecosystem**: Some libraries may not have anyio examples
5. **Learning Curve**: Different patterns than "standard" asyncio
6. **Compatibility Concerns**: Must ensure all dependencies work with anyio

## Real-World Impact for MythosMUD

### Current Stack Compatibility

✅ **Compatible with anyio**:

- FastAPI (uses Starlette, which supports anyio)
- httpx (already uses anyio internally!)
- asyncpg (works with anyio)
- WebSockets (FastAPI handles this)
- NATS-py (should work, but verify)

⚠️ **Needs Verification**:

- pytest-asyncio (may need configuration)
- uvicorn (manages its own loop, but should be fine)
- Some test utilities

### Performance Considerations

**Current State** (asyncio):

- Using standard asyncio event loop
- Not using uvloop (faster, but requires manual setup)
- Performance is "good enough" for current load

**With anyio**:

- Can automatically use uvloop if available
- Potential 2-4x performance improvement for I/O-bound operations
- Better resource management = fewer leaks = more stable

### Migration Complexity

**Easy Wins** (Low Risk):

- Scripts: `asyncio.run()` → `anyio.run()` (21 files)
- `asyncio.sleep()` → `anyio.sleep()` (50+ files, drop-in replacement)
- `asyncio.Lock()` → `anyio.Lock()` (15+ files, drop-in replacement)
- `asyncio.Event()` → `anyio.Event()` (1 file, drop-in replacement)

**Medium Complexity** (Some Risk):

- `asyncio.wait_for()` → `anyio.move_on_after()` (10+ files, pattern change)
- `asyncio.create_task()` → `anyio.create_task()` (many files, mostly drop-in)

**High Complexity** (Significant Risk):

- `asyncio.Queue()` → `anyio.create_memory_object_stream()` (3 files, API change)
- `asyncio.gather()` → `TaskGroup` (7 files, pattern change)

## Recommendation for MythosMUD

### Option 1: Full Migration (Recommended for Long-Term)

**Pros**:

- Better code quality and maintainability
- Structured concurrency prevents bugs
- Backend flexibility for testing
- Performance improvements with uvloop
- Aligns with modern best practices

**Cons**:

- Significant migration effort (especially Queue → Streams)
- Testing required to ensure compatibility
- Team learning curve

**Best For**: If you want the best long-term architecture and are willing to invest in migration.

### Option 2: Hybrid Approach (Pragmatic)

**Strategy**:

1. Add `anyio` as explicit dependency
2. Migrate scripts (`asyncio.run()` → `anyio.run()`) - easy wins
3. Migrate simple primitives (`sleep`, `Lock`, `Event`) - low risk
4. Keep `asyncio.Queue()` and `asyncio.gather()` for now - too complex
5. Gradually adopt anyio patterns in new code

**Pros**:

- Immediate benefits (scripts, primitives)
- Low risk
- Incremental migration
- Can stop at any point

**Cons**:

- Mixed patterns in codebase
- Doesn't get full structured concurrency benefits
- Queue migration still needed eventually

**Best For**: If you want benefits without major refactoring risk.

### Option 3: Stay with asyncio (Status Quo)

**Pros**:

- No migration effort
- No risk of breaking changes
- Team already familiar
- All libraries guaranteed compatible

**Cons**:

- Missing structured concurrency benefits
- Harder to prevent resource leaks
- No backend flexibility
- Not following the `.cursor/rules/anyio.mdc` guidelines

**Best For**: If migration risk outweighs benefits, or if you're close to release.

## My Academic Opinion (Mythos Persona)

*Adjusts spectacles and peers at the codebase*

The ancient texts (your `.cursor/rules/anyio.mdc`) are quite clear: "AnyIO is the definitive choice for modern asynchronous Python development." However, as with all forbidden knowledge, one must weigh the cost of acquisition against the benefits.

**For MythosMUD specifically**:

1. **You're already using anyio** (via httpx) - it's a transitive dependency. Making it explicit costs nothing.

2. **Your EventBus and NATS service** would benefit significantly from structured concurrency - preventing orphaned tasks in a long-running MUD server is critical.

3. **The Queue → Streams migration** is the real challenge. Your EventBus is central to the architecture. This requires careful testing.

4. **Scripts migration is trivial** - 21 files, mostly find/replace. Do this regardless.

**My recommendation**: Start with **Option 2 (Hybrid)**:

- Add anyio dependency (no risk)
- Migrate scripts (low risk, high value)
- Migrate simple primitives (low risk)
- Leave Queue/gather for a dedicated refactoring sprint

This gives you 80% of the benefits with 20% of the effort. The remaining 20% (Queue/Streams) can be tackled when you have time for proper testing.

## Decision Matrix

| Factor                    | Weight | asyncio | anyio (Full) | anyio (Hybrid) |
| ------------------------- | ------ | ------- | ------------ | -------------- |
| Migration Effort          | High   | 0       | -10          | -3             |
| Code Quality              | High   | 0       | +8           | +5             |
| Performance               | Medium | 0       | +6           | +3             |
| Risk                      | High   | 0       | -5           | -1             |
| Long-term Maintainability | Medium | 0       | +7           | +4             |
| Team Familiarity          | Low    | +3      | -2           | 0              |
| **Total Score**           |        | **3**   | **4**        | **8** ⭐        |

**Winner**: Hybrid approach balances benefits with risk.

## Next Steps

If choosing **Hybrid Approach**:

1. Add `anyio>=4.0.0` to `pyproject.toml`
2. Create migration branch
3. Migrate scripts (Phase 1 from review doc)
4. Migrate simple primitives (Phase 2)
5. Test thoroughly
6. Document decision on Queue/gather for future

Would you like me to proceed with the hybrid migration, or do you prefer a different approach?
