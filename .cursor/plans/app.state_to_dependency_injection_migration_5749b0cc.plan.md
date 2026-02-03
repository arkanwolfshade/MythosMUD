---
name: app.state to dependency injection migration
overview: Migrate all services from app.state to ApplicationContainer-based dependency injection, eliminating the dual storage pattern and updating all 500+ access points throughout the codebase to use proper dependency injection.
# Note: ApplicationContainer is now implemented in server/container/ package (main.py, utils.py, bundles/). See ADR-002 and docs/APPLICATION_CONTAINER_ANALYSIS.md.
todos:

  - id: phase1-container-extend

    content: Extend ApplicationContainer with all missing services (combat, magic, NPC, chat, etc.)
    status: completed

  - id: phase1-container-init

    content: Move service initialization logic from lifespan_startup.py into container.initialize()
    status: completed

  - id: phase1-legacy-compat

    content: Update initialize_container_and_legacy_services() to store in container first, then app.state for backward compatibility
    status: completed

  - id: phase2-di-functions

    content: Create dependency injection functions in dependencies.py for all new services (~18 functions)
    status: completed

  - id: phase2-di-aliases

    content: Create Depends() aliases for all new dependency functions
    status: completed

  - id: phase3-api-routes

    content: Migrate API route handlers in server/api/*.py to use dependency injection
    status: completed

  - id: phase4-game-tick

    content: Migrate game_tick_processing.py to use container instead of app.state
    status: completed

  - id: phase4-shutdown-command

    content: Migrate admin_shutdown_command.py to use container for shutdown state
    status: completed

  - id: phase5-command-handlers

    content: Migrate all command handlers in server/commands/*.py to use dependency injection
    status: completed

  - id: phase6-websocket-handlers

    content: Migrate WebSocket and real-time handlers to use container
    status: completed

  - id: phase7-remove-dual-storage

    content: Remove dual storage pattern - stop copying services to app.state
    status: completed

  - id: phase8-test-fixtures

    content: Update test fixtures in conftest.py to use container-based dependency injection
    status: completed

  - id: phase8-migrate-tests

    content: Migrate all 445+ test instances across 35+ test files to use container
    status: completed

  - id: phase9-cleanup

    content: Remove deprecated code, update documentation, add linting rules
    status: completed

  - id: phase9-verification

    content: Run full test suite, verify zero app.state.* access, check coverage
    status: completed
---

# App.State to Dependency Injection Migration Plan

## Overview

This plan addresses the migration from `app.state` global state access to proper dependency injection using `ApplicationContainer`. Currently, the codebase has 502+ instances of `app.state` access, with many services stored in both `app.state` AND `ApplicationContainer` for backward compatibility. This creates maintenance burden, testability issues, and violates clean architecture principles.

## Current State Analysis

### Services Currently ONLY in app.state

Combat services: `player_combat_service`, `player_death_service`, `player_respawn_service`, `combat_service`

- Magic services: `magic_service`, `spell_registry`, `spell_targeting_service`, `spell_effects`, `spell_learning_service`, `mp_regeneration_service`
- NPC services: `npc_lifecycle_manager`, `npc_spawning_service`, `npc_population_controller`
- Other services: `catatonia_registry`, `passive_lucidity_flux_service`, `mythos_time_consumer`, `chat_service`
- Infrastructure: `nats_service`, `nats_message_handler` (also in container but accessed via app.state)
- State flags: `server_shutdown_pending`, `shutdown_data`, `tick_task`, `mythos_tick_scheduler`, `db_session_maker`

### Services in BOTH container and app.state (duplicated)

Core: `container`, `task_registry`, `event_bus`, `event_handler`, `persistence`, `connection_manager`

- Game: `player_service`, `room_service`, `user_manager`, `container_service`
- Temporal: `holiday_service`, `schedule_service`
- Caching: `room_cache_service`, `profession_cache_service`
- Items: `prototype_registry`, `item_factory`

### Access Patterns

**502+ instances** of `app.state.` access across production code

**274+ instances** of `request.app.state` access in route handlers

**Hundreds of test files** mocking `app.state` directly

- Mixed patterns: some code uses `get_container(request)`, others use direct `app.state` access

## Migration Strategy

### Phase 1: Extend ApplicationContainer (8-12 hours)

**Goal**: Add all missing services to `ApplicationContainer`

1. **Add service attributes to `ApplicationContainer.__init__`** in `server/container/main.py` (or appropriate bundle):

   - Combat: `player_combat_service`, `player_death_service`, `player_respawn_service`, `combat_service`
   - Magic: `magic_service`, `spell_registry`, `spell_targeting_service`, `spell_effects`, `spell_learning_service`, `mp_regeneration_service`
   - NPC: `npc_lifecycle_manager`, `npc_spawning_service`, `npc_population_controller`
   - Other: `catatonia_registry`, `passive_lucidity_flux_service`, `mythos_time_consumer`, `chat_service`
   - State: `server_shutdown_pending`, `shutdown_data`, `tick_task`

2. **Update `container.initialize()`** to initialize these services in proper dependency order:

   - Move initialization logic from `server/app/lifespan_startup.py` into container
   - Maintain initialization order: infrastructure → game services → specialized services

3. **Update `initialize_container_and_legacy_services()`** in `server/app/lifespan_startup.py`:

   - Store services in container first
   - Then copy to `app.state` for backward compatibility (temporary)
   - Add deprecation warnings when services are accessed via `app.state`

### Phase 2: Create Dependency Injection Functions (4-6 hours)

**Goal**: Add DI functions for all services in `server/dependencies.py`

1. **Add dependency functions** for each new service:

   ```python
   def get_player_combat_service(request: Request) -> PlayerCombatService:
       container = get_container(request)
       if container.player_combat_service is None:
           raise RuntimeError("PlayerCombatService not initialized")
       return container.player_combat_service
   ```

2. **Create dependency aliases**:

   ```python
   PlayerCombatServiceDep = Depends(get_player_combat_service)
   ```

3. **Services to add DI functions for**:

   - All combat services (4 functions)
   - All magic services (6 functions)
   - All NPC services (3 functions)
   - Other services (5 functions)
   - Total: ~18 new dependency functions

### Phase 3: Migrate Route Handlers and API Endpoints (12-16 hours)

**Goal**: Update all FastAPI route handlers to use dependency injection

1. **Identify route handlers** using `request.app.state`:

   - `server/api/*.py` files
   - `server/commands/*.py` files
   - WebSocket handlers in `server/realtime/*.py`

2. **Migration pattern**:

   ```python
   # BEFORE:

   async def some_endpoint(request: Request):
       service = request.app.state.some_service

   # AFTER:

   async def some_endpoint(service: SomeService = SomeServiceDep):
       # Use service directly

   ```

3. **Files to migrate** (priority order):

   - `server/api/metrics.py` (already partially migrated)
   - `server/api/monitoring.py`
   - `server/api/players.py`
   - `server/api/real_time.py`
   - Command handlers in `server/commands/`

### Phase 4: Migrate Background Tasks and Game Tick Processing (8-10 hours)

**Goal**: Update background processing to use container instead of app.state

1. **Update `server/app/game_tick_processing.py`**:

   - Replace `app.state.*` access with `container.*`
   - Pass container as parameter instead of app
   - Update all service access patterns

2. **Update shutdown command** in `server/commands/admin_shutdown_command.py`:

   - Migrate `app.state.server_shutdown_pending` to container
   - Update shutdown state management

3. **Update lifespan tick scheduler**:

   - Store `tick_task` reference in container
   - Access via container instead of app.state

### Phase 5: Migrate Command Handlers (16-20 hours)

**Goal**: Update all command handlers to use dependency injection

1. **Command handler pattern migration**:

   ```python
   # BEFORE:

   async def handle_command(request: Request, ...):
       service = request.app.state.some_service

   # AFTER:

   async def handle_command(
       service: SomeService = SomeServiceDep,
       ...
   ):
   ```

2. **Files to migrate**:

   - `server/commands/admin_*.py`
   - `server/commands/combat.py`
   - `server/commands/go_command.py`
   - `server/commands/inventory_commands.py`
   - `server/commands/magic_commands.py`
   - `server/commands/npc_admin_commands.py`
   - `server/commands/status_commands.py`
   - `server/commands/teleport_helpers.py`
   - `server/commands/who_commands.py`
   - All other command files

3. **Special cases**:

   - Commands that access multiple services
   - Commands with conditional service access
   - Commands that need `app` for WebSocket broadcasting

### Phase 6: Migrate WebSocket and Real-time Handlers (8-10 hours)

**Goal**: Update WebSocket handlers and real-time event processing

1. **Update `server/realtime/websocket_handler.py`**:

   - Migrate service access from `app.state` to container
   - Update connection manager access patterns

2. **Update `server/realtime/connection_helpers.py`**:

   - Migrate service dependencies
   - Update helper functions to accept services as parameters

3. **Update `server/realtime/request_context.py`**:

   - Migrate `WebSocketRequestContext` to use container
   - Update context creation to inject services

4. **Update `server/command_handler_unified.py`**:

   - Migrate command handler to use dependency injection
   - Update service resolution logic

### Phase 7: Remove Dual Storage Pattern (4-6 hours)

**Goal**: Stop storing services in both container and app.state

1. **Update `initialize_container_and_legacy_services()`**:

   - Remove code that copies services to `app.state`
   - Keep only `app.state.container = container` for backward compatibility

2. **Add deprecation warnings**:

   - Create wrapper functions that log warnings when `app.state.*` is accessed
   - Guide developers to use dependency injection

3. **Update `get_container()` dependency**:

   - Ensure it works for both `request.app.state.container` and direct container access
   - Add fallback logic if needed

### Phase 8: Migrate Test Suite (20-30 hours)

**Goal**: Update all tests to use container-based dependency injection

1. **Update test fixtures** in `server/tests/conftest.py`:

   - Create container fixture that initializes all services
   - Update app fixture to use container
   - Remove `app.state.*` mocking patterns

2. **Migration pattern for tests**:

   ```python
   # BEFORE:

   mock_app.state.service = mock_service

   # AFTER:

   container = app.state.container
   container.service = mock_service
   # OR

   container = ApplicationContainer()
   container.service = mock_service
   await container.initialize()
   ```

3. **Files to migrate** (445+ instances across 35+ test files):

   - All `server/tests/unit/commands/test_*.py`
   - All `server/tests/unit/api/test_*.py`
   - All `server/tests/unit/realtime/test_*.py`
   - Integration and e2e tests

4. **Test helper utilities**:

   - Create `create_test_container()` helper function
   - Create `mock_container_services()` utility
   - Update test base classes

### Phase 9: Cleanup and Documentation (4-6 hours)

**Goal**: Remove legacy code and update documentation

1. **Remove deprecated code**:

   - Remove `app.state.*` assignment code from `lifespan_startup.py`
   - Remove wrapper functions if no longer needed
   - Clean up unused imports

2. **Update documentation**:

   - Update `docs/CONTAINER_SYSTEM_ARCHITECTURE.md`
   - Add migration guide for developers
   - Update API documentation

3. **Add linting rules**:

   - Add pylint rule to warn on `app.state.*` access (except `app.state.container`)
   - Add mypy type checking for container services

4. **Verification**:

   - Run full test suite
   - Verify no `app.state.*` access (except `app.state.container`)
   - Check code coverage maintained

## Implementation Guidelines

### Dependency Injection Pattern

**For Route Handlers**:

```python
from server.dependencies import ContainerDep, PlayerServiceDep

@app.get("/endpoint")
async def my_endpoint(
    container: ApplicationContainer = ContainerDep,
    player_service: PlayerService = PlayerServiceDep,
):
    # Use injected services

    pass
```

**For Command Handlers**:

```python
async def handle_command(
    command_data: dict,
    current_user: dict,
    player_service: PlayerService = PlayerServiceDep,
    connection_manager: ConnectionManager = ConnectionManagerDep,
) -> dict:
    # Use injected services

    pass
```

**For Background Tasks**:

```python
async def background_task(container: ApplicationContainer):
    # Access services via container

    service = container.some_service
```

### Service Initialization Order

1. Configuration
2. Database infrastructure
3. Task management
4. Event system
5. Persistence layer
6. Real-time communication
7. Game services (player, room, movement)
8. Combat services
9. Magic services
10. NPC services
11. Specialized services (chat, time, etc.)

### Testing Strategy

1. **Unit Tests**: Use `ApplicationContainer()` directly with mocked services
2. **Integration Tests**: Use container fixture with real services
3. **E2E Tests**: Use full container initialization via lifespan

## Risk Mitigation

1. **Incremental Migration**: Migrate one service category at a time
2. **Backward Compatibility**: Keep `app.state.container` during transition
3. **Comprehensive Testing**: Run full test suite after each phase
4. **Code Review**: Review each phase before proceeding
5. **Rollback Plan**: Keep old code commented during migration

## Success Criteria

Zero direct `app.state.*` access (except `app.state.container`)

- All services accessible via `ApplicationContainer`
- All route handlers use dependency injection
- All tests use container-based dependency injection
- 100% test coverage maintained
- No performance regressions
- All linter checks pass

## Estimated Effort

**Phase 1**: 8-12 hours

**Phase 2**: 4-6 hours

**Phase 3**: 12-16 hours

- **Phase 4**: 8-10 hours
- **Phase 5**: 16-20 hours
- **Phase 6**: 8-10 hours
- **Phase 7**: 4-6 hours
- **Phase 8**: 20-30 hours
- **Phase 9**: 4-6 hours

**Total**: 84-116 hours (~40-60 hours as originally estimated, but expanded scope requires more time)

## Dependencies

ApplicationContainer must be fully initialized before any service access

- All services must be properly typed in container
- Dependency injection functions must handle None cases gracefully
- Test fixtures must support both old and new patterns during migration
