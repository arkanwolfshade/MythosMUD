# Persistence Layer Async Migration Plan

**Created**: December 5, 2025
**Status**: Ready for Implementation
**Strategy**: Gradual, file-by-file async migration

## Phase 1: Foundation Complete ✅

The async repository foundation has been established:

- ✅ 7 async repositories extracted
- ✅ Backward compatibility maintained
- ✅ All tests passing
- ✅ Linting clean
- ✅ Documentation created

## Migration Roadmap

This plan outlines the step-by-step migration of 41 files from sync `persistence.py` to async repositories.

### Phase 2: API Endpoints (Priority 1) 🎯

**Rationale**: FastAPI endpoints are already async, making conversion straightforward with immediate performance benefits.

#### Files to Migrate (6 total)

1. **`server/api/players.py`**
   - **Complexity**: Low
   - **Effort**: 15 minutes
   - **Dependencies**: PlayerRepository
   - **Benefits**: Faster player API responses
   - **Risk**: Low

2. **`server/api/rooms.py`**
   - **Complexity**: Low
   - **Effort**: 10 minutes
   - **Dependencies**: RoomRepository
   - **Benefits**: Faster room queries
   - **Risk**: Low

3. **`server/api/containers.py`**
   - **Complexity**: Medium
   - **Effort**: 20 minutes
   - **Dependencies**: ContainerRepository
   - **Benefits**: Non-blocking container operations
   - **Risk**: Low

4. **`server/api/monitoring.py`**
   - **Complexity**: Low
   - **Effort**: 15 minutes
   - **Dependencies**: PlayerRepository
   - **Benefits**: Non-blocking stats queries
   - **Risk**: Low

5. **`server/api/real_time.py`**
   - **Complexity**: Medium
   - **Effort**: 20 minutes
   - **Dependencies**: PlayerRepository
   - **Benefits**: Better WebSocket performance
   - **Risk**: Medium

6. **`server/auth/endpoints.py`**
   - **Complexity**: Medium
   - **Effort**: 20 minutes
   - **Dependencies**: PlayerRepository
   - **Benefits**: Non-blocking auth operations
   - **Risk**: Low

**Phase 2 Total**: ~100 minutes (1.7 hours)

### Phase 3: Real-Time Handlers (Priority 2) 🚀

**Rationale**: High-traffic, latency-sensitive components benefit most from async.

#### Files to Migrate (2 total)

1. **`server/realtime/integration/game_state_provider.py`**
   - **Complexity**: High
   - **Effort**: 45 minutes
   - **Dependencies**: PlayerRepository, RoomRepository
   - **Benefits**: Faster game state loading
   - **Risk**: Medium - complex async flow

2. **`server/realtime/websocket_handler.py`**
   - **Complexity**: High
   - **Effort**: 30 minutes
   - **Dependencies**: PlayerRepository
   - **Benefits**: Better WebSocket responsiveness
   - **Risk**: Medium - critical path

**Phase 3 Total**: ~75 minutes (1.25 hours)

### Phase 4: High-Impact Services (Priority 3) ⚡

**Rationale**: Services with frequent database access benefit from async.

#### Files to Migrate (11 total)

**Easy Wins** (30-40 min total):

1. **`server/services/health_service.py`**
   - Complexity: Low | Effort: 10 min | Repo: HealthRepository

2. **`server/services/user_manager.py`**
   - Complexity: Low | Effort: 15 min | Repo: PlayerRepository

3. **`server/services/player_position_service.py`**
   - Complexity: Low | Effort: 15 min | Repo: RoomRepository, PlayerRepository

**Moderate** (90-120 min total):
4. **`server/services/exploration_service.py`**

- Complexity: Medium | Effort: 25 min | Repo: RoomRepository, PlayerRepository

5. **`server/services/environmental_container_loader.py`**
   - Complexity: Medium | Effort: 20 min | Repo: ContainerRepository

6. **`server/services/corpse_lifecycle_service.py`**
   - Complexity: Medium | Effort: 25 min | Repo: ContainerRepository

7. **`server/services/wearable_container_service.py`**
   - Complexity: Medium | Effort: 20 min | Repo: ContainerRepository

**Complex** (120-150 min total):
8. **`server/services/combat_service.py`**

- Complexity: High | Effort: 40 min | Repo: HealthRepository, ExperienceRepository

9. **`server/services/player_death_service.py`**
   - Complexity: High | Effort: 30 min | Repo: HealthRepository, PlayerRepository

10. **`server/services/npc_combat_integration_service.py`**
    - Complexity: High | Effort: 35 min | Repo: HealthRepository

11. **`server/services/npc_startup_service.py`**
    - Complexity: Medium | Effort: 25 min | Repo: PlayerRepository

**Phase 4 Total**: ~260 minutes (4.3 hours)

### Phase 5: Game & NPC Systems (Priority 4) 🎮

**Rationale**: Stable code, lower traffic, can be migrated when convenient.

#### Game Systems (3 files)

1. **`server/game/movement_service.py`**
   - Complexity: Medium | Effort: 20 min | Repo: RoomRepository, PlayerRepository

2. **`server/game/stats_generator.py`**
   - Complexity: Low | Effort: 15 min | Repo: PlayerRepository

3. **`server/commands/combat.py`**
   - Complexity: High | Effort: 35 min | Repo: HealthRepository, PlayerRepository

#### NPC Systems (7 files)

4. **`server/npc/spawning_service.py`**
   - Complexity: Medium | Effort: 20 min | Repo: PlayerRepository

5. **`server/npc/lifecycle_manager.py`**
   - Complexity: Medium | Effort: 25 min | Repo: PlayerRepository

6. **`server/npc/movement_integration.py`**
   - Complexity: Medium | Effort: 20 min | Repo: RoomRepository

7. **`server/npc/behaviors.py`**
   - Complexity: Medium | Effort: 20 min | Repo: PlayerRepository

8. **`server/npc/combat_integration.py`**
   - Complexity: High | Effort: 30 min | Repo: HealthRepository

9. **`server/npc/communication_integration.py`**
   - Complexity: Low | Effort: 15 min | Repo: PlayerRepository

10. **`server/npc/idle_movement.py`**
    - Complexity: Low | Effort: 15 min | Repo: RoomRepository

**Phase 5 Total**: ~215 minutes (3.6 hours)

### Phase 6: Test Migration (Priority 5) 🧪

**Rationale**: Migrate tests after their corresponding code is migrated.

#### Test Files (17 total)

**Unit Tests** (8 files):

- Effort: ~10-15 min each = 80-120 min total
- Update mocks to async patterns
- Convert sync assertions to async
- Update fixtures

**Integration Tests** (6 files):

- Effort: ~15-20 min each = 90-120 min total
- Async test clients
- Async database fixtures
- E2E flow conversion

**Verification/Security Tests** (3 files):

- Effort: ~10-15 min each = 30-45 min total
- Async security tests
- Async operation verification
- Conftest.py async fixtures

**Phase 6 Total**: ~200-285 minutes (3.3-4.75 hours)

## Total Migration Effort

| Phase               | Files  | Effort (hours)  | Cumulative |
| ------------------- | ------ | --------------- | ---------- |
| Phase 1 (Complete)  | -      | -               | ✅ Done     |
| Phase 2 (API)       | 6      | 1.7             | 1.7        |
| Phase 3 (Real-time) | 2      | 1.25            | 2.95       |
| Phase 4 (Services)  | 11     | 4.3             | 7.25       |
| Phase 5 (Game/NPC)  | 11     | 3.6             | 10.85      |
| Phase 6 (Tests)     | 17     | 3.3-4.75        | 14.15-15.6 |
| **TOTAL**           | **47** | **14-16 hours** | -          |

## Migration Workflow (Per File)

### Step 1: Pre-Migration Assessment

```bash
# Identify all persistence calls in the file
grep -n "persistence\." server/path/to/file.py

# Check if file is already async
grep -n "async def" server/path/to/file.py

# Review dependencies
grep -r "from.*your_file import" server/
```

### Step 2: Create Async Repository Instances

**Before**:

```python
from server.persistence import get_persistence

class MyService:
    def __init__(self):
        self.persistence = get_persistence()
```

**After**:

```python
from server.persistence.repositories import PlayerRepository, HealthRepository
from server.async_persistence import AsyncPersistenceLayer

class MyService:
    def __init__(self, event_bus=None):
        async_persistence = AsyncPersistenceLayer(event_bus=event_bus)
        self.player_repo = PlayerRepository(
            room_cache=async_persistence._room_cache,
            event_bus=event_bus
        )
        self.health_repo = HealthRepository(event_bus=event_bus)
```

### Step 3: Convert Methods to Async

**Before**:

```python
def process_player(self, player_id: UUID) -> Player:
    player = self.persistence.get_player(player_id)
    self.persistence.damage_player(player, 20)
    return player
```

**After**:

```python
async def process_player(self, player_id: UUID) -> Player:
    player = await self.player_repo.get_player_by_id(player_id)
    await self.health_repo.damage_player(player, 20)
    return player
```

### Step 4: Update All Callers

**Before**:

```python
# Caller code
result = my_service.process_player(player_id)
```

**After**:

```python
# Caller code (must also be async!)
result = await my_service.process_player(player_id)
```

### Step 5: Test Migration

```bash
# Run specific file tests
pytest server/tests/unit/path/to/test_your_file.py -v

# Run integration tests
pytest server/tests/integration/ -k "your_feature" -v

# Run full test suite
make test
```

### Step 6: Validate Performance

```python
# Add performance logging
import time

start = time.time()
result = await my_service.process_player(player_id)
elapsed = time.time() - start

logger.info("Operation completed", elapsed_ms=elapsed * 1000)
```

## Common Conversion Patterns

### Pattern 1: Simple Query

**Before**:

```python
def get_player_stats(self, player_id: UUID) -> dict:
    player = self.persistence.get_player(player_id)
    return player.get_stats() if player else {}
```

**After**:

```python
async def get_player_stats(self, player_id: UUID) -> dict:
    player = await self.player_repo.get_player_by_id(player_id)
    return player.get_stats() if player else {}
```

### Pattern 2: Batch Operations

**Before**:

```python
def update_all_players(self, players: list[Player]) -> None:
    for player in players:
        self.persistence.save_player(player)
```

**After**:

```python
async def update_all_players(self, players: list[Player]) -> None:
    await self.player_repo.save_players(players)  # Single transaction!
```

### Pattern 3: Health Operations

**Before**:

```python
def apply_combat_damage(self, player: Player, damage: int) -> None:
    self.persistence.damage_player(player, damage, "combat")
    self.persistence.save_player(player)
```

**After**:

```python
async def apply_combat_damage(self, player: Player, damage: int) -> None:
    await self.health_repo.damage_player(player, damage, "combat")
    # No need to save - damage_player handles persistence atomically!
```

### Pattern 4: FastAPI Dependency Injection

**Before**:

```python
from fastapi import Depends
from server.persistence import get_persistence, PersistenceLayer

@router.get("/players/{player_id}")
def get_player(
    player_id: UUID,
    persistence: PersistenceLayer = Depends(get_persistence)
):
    return persistence.get_player(player_id)
```

**After**:

```python
from fastapi import Depends
from server.persistence.repositories import PlayerRepository
from server.async_persistence import AsyncPersistenceLayer

# Dependency factory
async def get_player_repo():
    async_persistence = AsyncPersistenceLayer()
    return PlayerRepository(room_cache=async_persistence._room_cache)

@router.get("/players/{player_id}")
async def get_player(
    player_id: UUID,
    player_repo: PlayerRepository = Depends(get_player_repo)
):
    return await player_repo.get_player_by_id(player_id)
```

## Detailed File Migration Instructions

### API Endpoints (Phase 2)

#### `server/api/players.py`

**Current Imports**:

```python
from server.persistence import get_persistence, PersistenceLayer
```

**New Imports**:

```python
from server.persistence.repositories import PlayerRepository
from server.async_persistence import AsyncPersistenceLayer
```

**Methods to Convert**:

- `create_player` → `await player_repo.save_player(player)`
- `get_player` → `await player_repo.get_player_by_id(player_id)`
- `list_players` → `await player_repo.list_players()`
- `delete_player` → `await player_repo.delete_player(player_id)`

**Dependency Injection Change**:

```python
# Add at module level
async def get_player_repository():
    async_persistence = AsyncPersistenceLayer()
    return PlayerRepository(room_cache=async_persistence._room_cache)

# Update each route
async def endpoint(player_repo: PlayerRepository = Depends(get_player_repository)):
    ...
```

#### `server/api/rooms.py`

**Methods to Convert**:

- Room queries → `room_repo.get_room_by_id(room_id)`
- Room listings → `room_repo.list_rooms()`

**Note**: Room operations are mostly synchronous (cache access), minimal changes needed.

#### `server/api/containers.py`

**Methods to Convert**:

- Container CRUD → All methods already have async wrappers
- Just change `persistence.method()` → `await container_repo.method()`

### Services (Phase 4)

#### `server/services/combat_service.py`

**Key Changes**:

- Replace `persistence.damage_player()` → `await health_repo.damage_player()`
- Replace `persistence.heal_player()` → `await health_repo.heal_player()`
- Replace `persistence.gain_experience()` → `await xp_repo.gain_experience()`

**Initialization**:

```python
class CombatService:
    def __init__(self, event_bus=None):
        self.health_repo = HealthRepository(event_bus=event_bus)
        self.xp_repo = ExperienceRepository(event_bus=event_bus)
```

**Method Signatures**:

- All combat methods become `async def`
- Add `await` to all repository calls
- Update callers to use `await`

#### `server/services/user_manager.py`

**Key Changes**:

- Replace all `persistence.get_player*()` → `await player_repo.get_player*()`
- Replace `persistence.save_player()` → `await player_repo.save_player()`
- Replace `persistence.delete_player()` → `await player_repo.delete_player()`

**Testing Priority**: HIGH - User management is critical

## Testing Strategy

### Per-File Testing

After migrating each file:

```bash
# 1. Run file-specific tests
pytest server/tests/unit/path/test_your_file.py -v

# 2. Run integration tests for that domain
pytest server/tests/integration/ -k "related_feature" -v

# 3. Run fast test suite
make test

# 4. If all pass, commit
git add server/path/to/migrated_file.py
git commit -m "Migrate file.py to async repositories"
```

### Regression Testing

After each phase (2-6):

```bash
# Run comprehensive test suite
make test-comprehensive

# Run E2E multiplayer scenarios
# (Follow e2e-tests/MULTIPLAYER_TEST_RULES.md)

# Performance testing
# Monitor response times, ensure no degradation
```

## Rollback Procedures

### Individual File Rollback

```bash
# If a specific file migration causes issues
git checkout HEAD -- server/path/to/problematic_file.py

# Re-run tests
make test
```

### Phase Rollback

```bash
# If an entire phase needs rollback
git revert --no-commit <phase_start_commit>..<phase_end_commit>
git commit -m "Rollback Phase X migration due to <reason>"
```

### Emergency Rollback

```bash
# Nuclear option - revert all async migrations
git checkout <pre-migration-commit>

# Or use feature flag
export USE_SYNC_PERSISTENCE=true
```

## Success Metrics

### Per-File Metrics

- [ ] All tests passing
- [ ] No linting errors
- [ ] Async signatures correctly typed
- [ ] No performance regressions
- [ ] Documentation updated

### Per-Phase Metrics

- [ ] All files in phase migrated
- [ ] Comprehensive tests passing
- [ ] E2E scenarios validated
- [ ] Performance benchmarks green
- [ ] Migration documented

### Overall Migration Metrics

- **Files Migrated**: 0/41 (track progress)
- **Test Pass Rate**: 100% maintained
- **Coverage**: 82%+ maintained
- **Performance**: No regressions
- **Breaking Changes**: None (all backward compatible)

## Migration Timeline

### Conservative Timeline (Gradual Migration)

**Week 1**:

- Phase 2 (API Endpoints) - 6 files
- Expected: 1-2 hours of work

**Week 2**:

- Phase 3 (Real-time) - 2 files
- Expected: 1-2 hours of work

**Weeks 3-4**:

- Phase 4 (Services, easy wins) - 3-4 files
- Expected: 1 hour per week

**Weeks 5-8**:

- Phase 4 (Services, moderate/complex) - 7-8 files
- Expected: 1-2 hours per week

**Weeks 9-12**:

- Phase 5 (Game/NPC) - 11 files
- Expected: 1 hour per week

**Weeks 13-16**:

- Phase 6 (Tests) - 17 files
- Expected: 1-2 hours per week

**Total**: ~3-4 months of gradual migration

### Aggressive Timeline (Focused Migration)

If migration is prioritized:

- **Week 1**: Phases 2-3 (API + Real-time) = ~3 hours
- **Week 2**: Phase 4 (Easy services) = ~2 hours
- **Week 3**: Phase 4 (Moderate services) = ~3 hours
- **Week 4**: Phase 4 (Complex services) = ~3 hours
- **Week 5**: Phase 5 (Game/NPC) = ~4 hours
- **Week 6**: Phase 6 (Tests) = ~4 hours

**Total**: ~6 weeks of focused work (~20 hours total)

## Monitoring & Validation

### Metrics to Track

**Performance Metrics**:

- API endpoint response times
- Database query latencies
- WebSocket message delivery times
- Concurrent operation throughput

**Quality Metrics**:

- Test pass rate (must stay 100%)
- Code coverage (must stay ≥82%)
- Linting errors (must stay 0)
- Type checking errors (must stay 0)

**Migration Progress**:

- Files migrated per week
- Tests migrated per week
- Cumulative effort hours
- Issues encountered

### Performance Validation

```python
# Add performance tracking to migrated code
import time
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

async def migrated_operation():
    start = time.perf_counter()

    # Async operation
    result = await some_async_operation()

    elapsed_ms = (time.perf_counter() - start) * 1000
    logger.info("Async operation completed", elapsed_ms=elapsed_ms)

    return result
```

## Gotchas & Solutions

### Gotcha 1: Async Propagation

**Problem**: Converting one method to async requires converting all callers.

**Solution**: Start with leaf nodes (methods that don't call other methods) and work up the call stack.

### Gotcha 2: Mixing Sync and Async

**Problem**: Can't call async from sync without `asyncio.run()`.

**Solution**: Convert entire call chain to async, or use `asyncio.create_task()` for fire-and-forget.

### Gotcha 3: Transaction Management

**Problem**: SQLAlchemy async sessions use different transaction semantics.

**Solution**: Use `async with get_async_session()` consistently, commit in repositories.

### Gotcha 4: Testing Async Code

**Problem**: Regular pytest doesn't handle async tests.

**Solution**: Use `@pytest.mark.asyncio` and `pytest-asyncio` plugin (already installed).

## Decision Points

### When NOT to Migrate

Don't migrate a file if:

- File is rarely executed (< 10 times/day)
- File is scheduled for deprecation/removal
- File has complex legacy logic that's fragile
- Migration risk exceeds performance benefit
- Team lacks async expertise for that domain

### When TO Migrate

Do migrate a file if:

- File is a FastAPI endpoint (already async!)
- File handles high-traffic operations
- File has performance bottlenecks
- File is being refactored anyway
- Clear performance benefits expected

## References

- **Async Repositories**: `server/persistence/repositories/`
- **Migration Guide**: `docs/PERSISTENCE_ASYNC_MIGRATION_GUIDE.md`
- **Refactoring Summary**: `PERSISTENCE_REFACTORING_SUMMARY.md`
- **Async Best Practices**: `docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md`

## Conclusion

This migration plan provides a **gradual, low-risk path** to async persistence adoption. Each file can be migrated **independently** based on **priority and need**, without breaking existing functionality.

**Migration is optional** - files can remain on sync persistence indefinitely if preferred. The async repositories provide benefits for those who choose to adopt them.
