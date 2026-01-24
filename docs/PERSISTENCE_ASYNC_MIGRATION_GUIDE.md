# Persistence Layer Async Migration Guide

**Date**: December 5, 2025
**Status**: Phase 1 Complete - Async Repositories Extracted
**Migration Strategy**: Conservative - Gradual async adoption

## Executive Summary

The persistence layer has been refactored to extract async repositories while maintaining full backward compatibility
through the existing `persistence.py` synchronous interface. New async-first code can use the repositories directly,
while existing code continues working unchanged.

## What's Been Completed

### New Async Repository Architecture

```
server/persistence/
├── __init__.py                      # Exports async repositories
├── repositories/
│   ├── __init__.py                  # Repository exports
│   ├── player_repository.py         # ✅ Player CRUD + queries (async)
│   ├── room_repository.py           # ✅ Room caching (sync cache access)
│   ├── profession_repository.py     # ✅ Profession queries (async)
│   ├── health_repository.py         # ✅ Damage/healing operations (async)
│   ├── experience_repository.py     # ✅ XP/stats management (async)
│   ├── container_repository.py      # ✅ Container CRUD (async wrappers)
│   └── item_repository.py           # ✅ Item instances (async wrappers)
└── utils/
    └── __init__.py
```

### Repository Responsibilities

#### PlayerRepository (Fully Async)

Player CRUD: `get_player_by_id`, `get_player_by_name`, `get_player_by_user_id`, `save_player`, `delete_player`

- Batch operations: `list_players`, `get_players_in_room`, `save_players`, `get_players_batch`
- Utility: `update_player_last_active`, `validate_and_fix_player_room`
- Uses SQLAlchemy async ORM for true non-blocking operations

#### RoomRepository (Cache-Based)

Room retrieval: `get_room_by_id`, `list_rooms`

- Synchronous cache access (rooms loaded at startup)

#### HealthRepository (Fully Async)

Health management: `damage_player`, `heal_player`, `update_player_health`

- Atomic JSONB updates to prevent race conditions
- EventBus integration for HP change events

#### ExperienceRepository (Fully Async)

XP management: `gain_experience`, `update_player_xp`

- Stat updates: `update_player_stat_field`
- Atomic updates with field name whitelisting

#### ProfessionRepository (Fully Async)

Profession queries: `get_all_professions`, `get_profession_by_id`

- SQLAlchemy async ORM

#### ContainerRepository (Async Wrappers)

Container CRUD via `asyncio.to_thread()` wrappers

- Delegates to existing `container_persistence.py` module

#### ItemRepository (Async Wrappers)

Item instance operations via `asyncio.to_thread()` wrappers

- Delegates to existing `item_instance_persistence.py` module

## How to Use the New Async Repositories

### Option 1: Use Async Facade (Recommended for Async Code) ✅

```python
# AsyncPersistenceLayer now delegates to repositories!

from server.async_persistence import AsyncPersistenceLayer

# Initialize the facade

async_persistence = AsyncPersistenceLayer(event_bus=event_bus)

# All methods delegate to focused repositories

player = await async_persistence.get_player_by_id(player_id)
professions = await async_persistence.get_professions()
await async_persistence.save_player(player)
```

**Benefits:**

- Clean, familiar interface
- Automatic repository initialization
- Shared room cache
- EventBus integration

### Option 2: Direct Repository Usage (Maximum Flexibility)

```python
# Use repositories directly for fine-grained control

from server.persistence.repositories import PlayerRepository, HealthRepository
from server.async_persistence import AsyncPersistenceLayer

# Initialize

async_persistence = AsyncPersistenceLayer()
player_repo = PlayerRepository(
    room_cache=async_persistence._room_cache,
    event_bus=event_bus
)
health_repo = HealthRepository(event_bus=event_bus)

# Use async operations

player = await player_repo.get_player_by_id(player_id)
await health_repo.damage_player(player, amount=20, damage_type="combat")
await player_repo.save_player(player)
```

**Benefits:**

- Full control over repositories
- Can mix and match repositories
- Easier to test individual repositories

### Option 3: Continue Using Sync Interface (Existing Code)

```python
# Existing code continues working unchanged

from server.persistence import get_persistence

persistence = get_persistence()
player = persistence.get_player(player_id)  # Still synchronous
persistence.damage_player(player, 20, "combat")
persistence.save_player(player)
```

**Benefits:**

- Zero changes required
- Existing code continues working
- No migration pressure

## Migration Path for Existing Code

### Phase 1: Async Repository Extraction ✅ COMPLETE

[x] Extract PlayerRepository

- [x] Extract RoomRepository
- [x] Extract HealthRepository
- [x] Extract ExperienceRepository
- [x] Extract ProfessionRepository
- [x] Extract ContainerRepository (wrappers)
- [x] Extract ItemRepository (wrappers)

### Phase 2: High-Impact Services (Future)

**Services to Migrate** (11 files):

1. `server/services/combat_service.py` - Use HealthRepository
2. `server/services/player_death_service.py` - Use HealthRepository
3. `server/services/user_manager.py` - Use PlayerRepository
4. `server/services/npc_combat_integration_service.py` - Use HealthRepository
5. `server/services/corpse_lifecycle_service.py` - Use ContainerRepository
6. `server/services/wearable_container_service.py` - Use ContainerRepository
7. `server/services/player_position_service.py` - Use RoomRepository
8. `server/services/npc_startup_service.py` - Use PlayerRepository
9. `server/services/health_service.py` - Use HealthRepository
10. `server/services/environmental_container_loader.py` - Use ContainerRepository
11. `server/services/exploration_service.py` - Use RoomRepository

**Migration Pattern**:

```python
# Before (sync)

from server.persistence import get_persistence

class CombatService:
    def __init__(self):
        self.persistence = get_persistence()

    def apply_damage(self, player, amount):
        self.persistence.damage_player(player, amount)

# After (async)

from server.persistence.repositories import HealthRepository

class CombatService:
    def __init__(self, event_bus=None):
        self.health_repo = HealthRepository(event_bus=event_bus)

    async def apply_damage(self, player, amount):
        await self.health_repo.damage_player(player, amount)
```

### Phase 3: API Endpoints (Future)

**API Files to Migrate** (6 files):

- `server/api/real_time.py` - Use PlayerRepository
- `server/api/containers.py` - Use ContainerRepository
- `server/api/players.py` - Use PlayerRepository
- `server/api/rooms.py` - Use RoomRepository
- `server/api/monitoring.py` - Use PlayerRepository
- `server/auth/endpoints.py` - Use PlayerRepository

**Migration Pattern**:

```python
# Before (sync dependency injection)

@router.get("/players/{player_id}")
def get_player(player_id: UUID, persistence: PersistenceLayer = Depends(get_persistence)):
    player = persistence.get_player(player_id)
    return player

# After (async dependency injection)

async def get_player_repo(event_bus=Depends(get_event_bus)):
    return PlayerRepository(room_cache=..., event_bus=event_bus)

@router.get("/players/{player_id}")
async def get_player(
    player_id: UUID,
    player_repo: PlayerRepository = Depends(get_player_repo)
):
    player = await player_repo.get_player_by_id(player_id)
    return player
```

### Phase 4: Real-Time Integration (Future)

**Realtime Files to Migrate** (2 files):

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/websocket_handler.py`

### Phase 5: Game & NPC Systems (Future)

**Game/NPC Files to Migrate** (11 files):

- Game: `movement_service.py`, `stats_generator.py`

- NPC: `spawning_service.py`, `lifecycle_manager.py`, `movement_integration.py`, `behaviors.py`,

  `combat_integration.py`, `communication_integration.py`, `idle_movement.py`

- Commands: `combat.py`

### Phase 6: Test Migration (Future)

**Test Files to Migrate** (17 files):

- Update fixtures to use async repositories
- Convert sync assertions to async
- Migrate database setup/teardown to async

## Benefits of Async Repositories

### Performance

**Non-blocking I/O**: True async database operations (no thread pool overhead)

**Connection Pooling**: SQLAlchemy async connection pooling

**Better Concurrency**: Handle more simultaneous operations

**Reduced Latency**: Async operations complete faster under load

### Maintainability

**Focused Responsibilities**: Each repository handles one domain

**Easier Testing**: Mock async sessions, test repositories in isolation

**Clear Interfaces**: Well-defined async methods per domain

**Self-Documenting**: Repository names and methods describe their purpose

### Architecture

**Modern Patterns**: Async/await throughout

**Repository Pattern**: Clean separation of data access

**Dependency Injection**: Clear dependency graphs

**Scalability Foundation**: Ready for distributed architecture

## Migration Decision Tree

### When to Use Async Repositories Directly?

**YES - Use async repositories directly when:**

- Writing NEW features or services
- Service is already async (FastAPI endpoints, WebSocket handlers)
- Performance is critical (high-throughput operations)
- Working on a file that's being refactored anyway

**NO - Keep using sync persistence when:**

- Code is stable and working (don't fix what isn't broken)
- File is low-priority for async migration
- Risk of introducing bugs outweighs benefits
- Team velocity is more important than incremental improvements

### Migration Priority Matrix

| Priority   | Component Type     | Reason                                          |
| ---------- | ------------------ | ----------------------------------------------- |
| **HIGH**   | API Endpoints      | Already async (FastAPI), easy conversion        |
| **HIGH**   | Real-time handlers | Already async (WebSocket), performance critical |
| **MEDIUM** | Services           | Mixed sync/async, moderate effort               |
| **LOW**    | Game logic         | Stable code, low traffic                        |
| **LOW**    | NPC systems        | Background operations, not latency-sensitive    |

## Testing the New Repositories

### Unit Testing Repositories

```python
import pytest
from unittest.mock import AsyncMock, MagicMock
from server.persistence.repositories import PlayerRepository

@pytest.mark.asyncio
async def test_player_repository_get_by_id(mock_async_session):
    # Arrange

    player_repo = PlayerRepository(room_cache={}, event_bus=None)
    expected_player = Player(player_id=uuid4(), name="TestPlayer")

    # Mock async session

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(return_value=MagicMock(scalar_one_or_none=lambda: expected_player))

    # Act

    player = await player_repo.get_player_by_id(expected_player.player_id)

    # Assert

    assert player == expected_player
```

## Common Pitfalls & Solutions

### Pitfall 1: Mixing Sync and Async Code

**Problem**:

```python
# This won't work - can't await in sync function

def my_function():
    player = await player_repo.get_player_by_id(player_id)  # ERROR!
```

**Solution**:

```python
# Convert function to async

async def my_function():
    player = await player_repo.get_player_by_id(player_id)  # OK!

# OR use asyncio.run() for one-off calls

def my_function():
    player = asyncio.run(player_repo.get_player_by_id(player_id))  # OK but not ideal
```

### Pitfall 2: Forgetting to Initialize Room Cache

**Problem**:

```python
player_repo = PlayerRepository()  # room_cache is empty!
player = await player_repo.get_player_by_id(player_id)
# Player validation will fail - missing rooms

```

**Solution**:

```python
# Use AsyncPersistenceLayer for room cache

async_persistence = AsyncPersistenceLayer()
player_repo = PlayerRepository(
    room_cache=async_persistence._room_cache,
    event_bus=event_bus
)
```

### Pitfall 3: Not Handling Async Exceptions

**Problem**:

```python
try:
    player = await player_repo.get_player_by_id(player_id)
except Exception:  # Too broad!
    pass
```

**Solution**:

```python
from server.exceptions import DatabaseError

try:
    player = await player_repo.get_player_by_id(player_id)
except DatabaseError as e:
    logger.error("Database error loading player", error=str(e))
    # Handle appropriately

```

## Performance Comparison

### Sync Persistence (Current)

```python
# Uses psycopg2 + RLock + thread pool

persistence = get_persistence()
player = persistence.get_player(player_id)  # Blocks thread
```

**Characteristics**:

- Thread-safe with RLock overhead
- Blocks thread during database I/O
- Connection pooling via psycopg2
- Suitable for low-concurrency scenarios

### Async Repositories (New)

```python
# Uses SQLAlchemy async + asyncpg

player_repo = PlayerRepository(room_cache=room_cache)
player = await player_repo.get_player_by_id(player_id)  # Non-blocking
```

**Characteristics**:

- No thread synchronization overhead
- Non-blocking event loop friendly
- Connection pooling via SQLAlchemy async
- Scales better under high concurrency

**Benchmark Results** (Estimated):

- Single operation: ~5-10% faster (async overhead minimal)
- 100 concurrent operations: ~50-100% faster (async shines)
- 1000 concurrent operations: ~200-400% faster (async dominates)

## Migration Checklist (Per File)

Use this checklist when migrating a file to async repositories:

### Pre-Migration

[ ] Identify all persistence operations in file

- [ ] Check if file is already async (FastAPI routes are!)
- [ ] Review dependencies (other files that call this one)
- [ ] Create test cases for current behavior

### Migration Steps

[ ] Change imports from `persistence` to `persistence.repositories`

- [ ] Initialize repository instances (inject dependencies)
- [ ] Convert sync function signatures to `async def`
- [ ] Add `await` to all repository calls
- [ ] Update return types (add `Awaitable` if needed)
- [ ] Handle async exceptions properly

### Post-Migration

[ ] Run tests - verify behavior unchanged

- [ ] Check linting - ensure async signatures correct
- [ ] Performance test - verify no regressions
- [ ] Update dependent files (if they call this file)

### Example Migration

**Before** (`server/services/user_manager.py`):

```python
from server.persistence import get_persistence

class UserManager:
    def __init__(self):
        self.persistence = get_persistence()

    def create_player(self, name: str, user_id: str) -> Player:
        player = Player(name=name, user_id=user_id)
        self.persistence.save_player(player)
        return player

    def get_player(self, player_id: UUID) -> Player | None:
        return self.persistence.get_player(player_id)
```

**After** (`server/services/user_manager.py`):

```python
from server.persistence.repositories import PlayerRepository
from server.async_persistence import AsyncPersistenceLayer

class UserManager:
    def __init__(self, event_bus=None):
        async_persistence = AsyncPersistenceLayer(event_bus=event_bus)
        self.player_repo = PlayerRepository(
            room_cache=async_persistence._room_cache,
            event_bus=event_bus
        )

    async def create_player(self, name: str, user_id: str) -> Player:
        player = Player(name=name, user_id=user_id)
        await self.player_repo.save_player(player)
        return player

    async def get_player(self, player_id: UUID) -> Player | None:
        return await self.player_repo.get_player_by_id(player_id)
```

## File-by-File Migration Priority

### Priority 1: API Endpoints (Easiest - Already Async!)

FastAPI endpoints are already async, making them the easiest to migrate:

**Files**:

1. `server/api/players.py` - Player API
2. `server/api/rooms.py` - Room API
3. `server/api/containers.py` - Container API
4. `server/api/monitoring.py` - Stats API
5. `server/api/real_time.py` - WebSocket API
6. `server/auth/endpoints.py` - Auth API

**Effort**: ~10-15 minutes per file
**Benefit**: Immediate performance improvement for API calls
**Risk**: Low - FastAPI handles async natively

### Priority 2: Real-Time Handlers (High Impact)

WebSocket and real-time handlers benefit most from async:

**Files**:

1. `server/realtime/integration/game_state_provider.py`
2. `server/realtime/websocket_handler.py`

**Effort**: ~30 minutes per file
**Benefit**: Better real-time responsiveness, reduced latency
**Risk**: Medium - complex async flow, test thoroughly

### Priority 3: Services (Moderate Effort)

Services have mixed sync/async patterns:

**Files** (by complexity, easiest first):

1. `server/services/health_service.py` - Simple health operations
2. `server/services/user_manager.py` - Player CRUD
3. `server/services/player_position_service.py` - Room management
4. `server/services/exploration_service.py` - Room navigation
5. `server/services/environmental_container_loader.py` - Container loading
6. `server/services/combat_service.py` - Combat state management
7. `server/services/player_death_service.py` - Death handling
8. `server/services/corpse_lifecycle_service.py` - Corpse containers
9. `server/services/wearable_container_service.py` - Equipment
10. `server/services/npc_combat_integration_service.py` - NPC combat
11. `server/services/npc_startup_service.py` - NPC spawning

**Effort**: ~20-45 minutes per file depending on complexity
**Benefit**: Gradual performance improvement
**Risk**: Medium - ensure proper async conversion

### Priority 4: Game & NPC Systems (Lower Priority)

These are stable and low-traffic:

**Files**:

- `server/commands/combat.py`
- `server/game/movement_service.py`
- `server/game/stats_generator.py`
- `server/npc/*.py` (7 files)

**Effort**: ~15-30 minutes per file
**Benefit**: Code modernization
**Risk**: Low - stable code, infrequent changes

### Priority 5: Tests (After Code Migration)

Migrate tests after their corresponding code is migrated:

**Effort**: ~10-20 minutes per test file
**Benefit**: Test async behavior properly
**Risk**: Low - tests should guide migration

## Rollback Strategy

If issues arise during migration:

1. **Individual File Rollback**: Revert specific file to sync version
2. **Keep Both Versions**: Maintain sync and async paths temporarily
3. **Feature Flags**: Use environment variable to toggle async/sync
4. **No Breaking Changes**: Existing code continues working throughout migration

## Success Metrics

### Per-File Migration Metrics

[ ] All tests passing

- [ ] No linting errors
- [ ] No performance regressions
- [ ] Async signatures correctly typed

### Overall Migration Metrics

Current: 0/41 files migrated to async repositories

- Target: Gradual migration over time (no deadline)
- Test Coverage: Maintain 82%+ throughout migration
- Performance: No regressions, potential improvements

## Next Steps

1. **Start with API endpoints** - Easiest wins, immediate performance benefits
2. **Migrate high-traffic services** - Combat, player management
3. **Update real-time handlers** - WebSocket responsiveness
4. **Gradually convert remaining services** - As time permits
5. **Migrate tests** - After corresponding code is migrated
6. **Eventually deprecate sync layer** - When all code is async

## References

**Async Repositories**: `server/persistence/repositories/`

**Async Persistence Layer**: `server/async_persistence.py`

**SQLAlchemy Async Best Practices**: `docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md`

**Async Remediation Summary**: `docs/ASYNC_REMEDIATION_SUMMARY_2025-12-03.md`

## Questions?

This migration is **entirely optional** and can proceed at whatever pace makes sense for the project. The async
repositories are available for use, but existing sync code continues working indefinitely.
