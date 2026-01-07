# Persistence Repositories

Async repository modules for domain-specific database operations.

## Overview

This directory contains focused async repositories that handle database
operations for specific domains (players, rooms, health, etc.). These
repositories use SQLAlchemy async ORM with PostgreSQL for true non-blocking
database access.

## Quick Start

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
player = await player_repo.get_player_by_id(player_id)
await health_repo.damage_player(player, 20, "combat")
```

## Available Repositories

- **PlayerRepository**: Player CRUD + queries (400 lines, fully async)
- **RoomRepository**: Room caching (60 lines, sync cache access)
- **HealthRepository**: Damage/healing/HP (200 lines, fully async)
- **ExperienceRepository**: XP/stats (230 lines, fully async)
- **ProfessionRepository**: Profession queries (90 lines, fully async)
- **ContainerRepository**: Container CRUD (110 lines, async wrappers)
- **ItemRepository**: Item instances (95 lines, async wrappers)

## Documentation

See:
- **Architecture**: `docs/PERSISTENCE_REPOSITORY_ARCHITECTURE.md`
- **Migration Guide**: `docs/PERSISTENCE_ASYNC_MIGRATION_GUIDE.md`
- **Migration Plan**: `docs/PERSISTENCE_ASYNC_MIGRATION_PLAN.md`
