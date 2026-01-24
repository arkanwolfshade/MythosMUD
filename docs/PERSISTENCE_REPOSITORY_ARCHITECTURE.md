# Persistence Repository Architecture

**Last Updated**: December 2025
**Status**: ✅ Fully Async - PersistenceLayer Removed

## Overview

The persistence layer has been fully migrated to async. The legacy `PersistenceLayer` (synchronous shim) has been
removed. All code now uses `AsyncPersistenceLayer` with async repositories. This provides a modern async foundation with
no legacy sync code.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    async_persistence.py                          │
│              (Async Facade - Main Entry Point)                   │
│         Uses AsyncPersistenceLayer with repositories              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ Delegates to async repos
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────────┐       ┌──────────────────────┐
│  Async Repositories │       │  ApplicationContainer│
│  (1,185+ lines)     │       │  (Dependency Injection)│
├─────────────────────┤       ├──────────────────────┤
│• PlayerRepository   │       │• async_persistence    │
│• HealthRepository   │       │  (AsyncPersistenceLayer)│
│• ExperienceRepository│      └──────────────────────┘
│• RoomRepository     │
│• ProfessionRepository│
│• ContainerRepository│
│• ItemRepository     │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  SQLAlchemy Async   │
│  PostgreSQL via     │
│  asyncpg            │
└─────────────────────┘
```

## Repository Descriptions

### 1. PlayerRepository (400 lines)

**Purpose**: Player CRUD and query operations

**Key Methods**:

- `get_player_by_id(player_id)` - Fetch player by UUID
- `get_player_by_name(name)` - Fetch player by name
- `get_player_by_user_id(user_id)` - Fetch by auth user ID
- `save_player(player)` - Upsert player
- `save_players(players)` - Batch upsert
- `delete_player(player_id)` - Delete player
- `list_players()` - Get all players
- `get_players_in_room(room_id)` - Get players in specific room
- `get_players_batch(player_ids)` - Batch fetch by IDs
- `update_player_last_active(player_id, timestamp)` - Update activity timestamp
- `validate_and_fix_player_room(player)` - Ensure valid room placement

**Features**:

- Retry with exponential backoff
- Room validation and auto-fix
- Inventory integration
- SQLAlchemy async ORM

**Dependencies**:

- Room cache (for validation)
- EventBus (optional, for player events)

### 2. RoomRepository (60 lines)

**Purpose**: Room caching and retrieval

**Key Methods**:

- `get_room_by_id(room_id)` - Fetch cached room
- `list_rooms()` - Get all cached rooms

**Features**:

- Synchronous cache access (rooms loaded at startup)
- In-memory cache for fast lookup
- No database queries after startup

**Dependencies**:

- Shared room cache dictionary

### 3. HealthRepository (200 lines)

**Purpose**: Player health management

**Key Methods**:

- `damage_player(player, amount, damage_type)` - Apply damage atomically
- `heal_player(player, amount)` - Apply healing atomically
- `update_player_health(player_id, delta, reason)` - Atomic HP update

**Features**:

- Atomic JSONB field updates (prevents race conditions)
- EventBus integration for HP events
- Proper bounds checking (0-100 HP)
- Detailed logging for health changes

**Dependencies**:

- EventBus (optional, for HP change events)

**Design Pattern**: Atomic updates using PostgreSQL JSONB operations

### 4. ExperienceRepository (230 lines)

**Purpose**: Player XP and stat management

**Key Methods**:

- `gain_experience(player, amount, source)` - Award XP atomically
- `update_player_xp(player_id, delta, reason)` - Atomic XP update
- `update_player_stat_field(player_id, field, delta, reason)` - Atomic stat update

**Features**:

- Atomic field updates for race condition prevention
- Field name whitelisting (security)
- EventBus integration for XP events
- Supports all stat fields (strength, dexterity, etc.)

**Dependencies**:

- EventBus (optional, for XP/level events)

**Security**: Whitelist-based field validation prevents SQL injection

### 5. ProfessionRepository (90 lines)

**Purpose**: Profession queries

**Key Methods**:

- `get_all_professions()` - Fetch all professions
- `get_profession_by_id(profession_id)` - Fetch specific profession

**Features**:

- Simple async queries
- SQLAlchemy async ORM

**Dependencies**: None

### 6. ContainerRepository (110 lines)

**Purpose**: Container CRUD operations

**Key Methods**:

- `create_container(...)` - Create new container
- `get_container(container_id)` - Fetch container
- `get_containers_by_room_id(room_id)` - Room containers
- `get_containers_by_entity_id(entity_id)` - Entity containers
- `update_container(...)` - Update container
- `get_decayed_containers(current_time)` - Fetch decayed corpses
- `delete_container(container_id)` - Delete container

**Features**:

- Async wrappers via `asyncio.to_thread()`
- Delegates to existing `container_persistence.py`
- Non-blocking access to sync code

**Dependencies**:

- Uses `container_persistence.py` functions directly via sync connections

**Note**: Uses `asyncio.to_thread()` to wrap sync functions

### 7. ItemRepository (95 lines)

**Purpose**: Item instance operations

**Key Methods**:

- `create_item_instance(...)` - Create item instance
- `ensure_item_instance(...)` - Create if not exists
- `item_instance_exists(item_id)` - Check existence

**Features**:

- Async wrappers via `asyncio.to_thread()`
- Delegates to existing `item_instance_persistence.py`
- Non-blocking access to sync code

**Dependencies**:

- Uses `item_instance_persistence.py` functions directly via sync connections

**Note**: Uses `asyncio.to_thread()` to wrap sync functions

## Usage Examples

### Example 1: Direct Repository Usage

```python
from server.persistence.repositories import PlayerRepository, HealthRepository
from server.async_persistence import AsyncPersistenceLayer

# Initialize

async_persistence = AsyncPersistenceLayer()
player_repo = PlayerRepository(
    room_cache=async_persistence._room_cache,
    event_bus=event_bus
)
health_repo = HealthRepository(event_bus=event_bus)

# Use

async def process_combat(attacker_id: UUID, target_id: UUID, damage: int):
    attacker = await player_repo.get_player_by_id(attacker_id)
    target = await player_repo.get_player_by_id(target_id)

    await health_repo.damage_player(target, damage, "combat")
    await xp_repo.gain_experience(attacker, 50, "combat_victory")

    await player_repo.save_player(target)
```

### Example 2: FastAPI Dependency Injection

```python
from fastapi import APIRouter, Depends
from server.persistence.repositories import PlayerRepository
from server.async_persistence import AsyncPersistenceLayer

router = APIRouter()

# Dependency factory

async def get_player_repo():
    async_persistence = AsyncPersistenceLayer()
    return PlayerRepository(room_cache=async_persistence._room_cache)

# Route handler

@router.get("/players/{player_id}")
async def get_player(
    player_id: UUID,
    player_repo: PlayerRepository = Depends(get_player_repo)
):
    player = await player_repo.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
```

### Example 3: Service Layer Integration

```python
from server.persistence.repositories import HealthRepository, ExperienceRepository

class CombatService:
    def __init__(self, event_bus=None):
        self.health_repo = HealthRepository(event_bus=event_bus)
        self.xp_repo = ExperienceRepository(event_bus=event_bus)

    async def apply_combat_damage(
        self,
        attacker: Player,
        target: Player,
        damage: int
    ) -> dict:
        # Apply damage

        await self.health_repo.damage_player(target, damage, "combat")

        # Award XP if target died

        if target.get_stats()["current_health"] <= 0:
            await self.xp_repo.gain_experience(attacker, 100, "killed_enemy")

        return {"damage_dealt": damage, "target_alive": target.get_stats()["current_health"] > 0}
```

## Design Patterns

### Repository Pattern

Each repository encapsulates database access for a specific domain:

**Benefits**:

- Clear separation of concerns
- Testable in isolation
- Swappable implementations
- Focused interfaces

**Implementation**:

- One repository per domain (Player, Room, Health, etc.)
- Async methods for I/O operations
- Dependency injection for shared resources
- Error handling with context

### Dependency Injection

Repositories receive dependencies via constructor:

**Pattern**:

```python
class PlayerRepository:
    def __init__(self, room_cache: dict, event_bus=None):
        self._room_cache = room_cache
        self._event_bus = event_bus
```

**Benefits**:

- Easy to mock for testing
- Clear dependency graph
- Flexible configuration
- No hidden global state

### Atomic Updates

Health and XP repositories use atomic updates:

**Pattern**:

```python
# Update single JSONB field without loading entire object

UPDATE players
SET stats = jsonb_set(stats, '{current_health}', ...)
WHERE player_id = :player_id
```

**Benefits**:

- Prevents race conditions
- Better performance
- Stronger consistency
- Reduced lock contention

## Migration Status

### Completed ✅

[x] PlayerRepository extracted

- [x] RoomRepository extracted
- [x] HealthRepository extracted
- [x] ExperienceRepository extracted
- [x] ProfessionRepository extracted
- [x] ContainerRepository extracted (wrappers)
- [x] ItemRepository extracted (wrappers)
- [x] Documentation created
- [x] All tests passing
- [x] Backward compatibility maintained

### Migration Status

[x] Migrate API endpoints to use async_persistence ✅ **COMPLETE**

- [x] Migrate services to use async_persistence ✅ **COMPLETE**
- [x] Migrate real-time handlers to use async_persistence ✅ **COMPLETE**
- [x] Migrate game/NPC systems to use async_persistence ✅ **COMPLETE**
- [x] Migrate tests to async patterns ✅ **COMPLETE**
- [x] Remove sync persistence layer ✅ **COMPLETE**
- [x] Remove persistence.py ✅ **COMPLETE**

## References

**Repositories**: `server/persistence/repositories/`

**Migration Guide**: `docs/PERSISTENCE_ASYNC_MIGRATION_GUIDE.md`

**Migration Plan**: `docs/PERSISTENCE_ASYNC_MIGRATION_PLAN.md`

**Summary**: `PERSISTENCE_REFACTORING_SUMMARY.md`
