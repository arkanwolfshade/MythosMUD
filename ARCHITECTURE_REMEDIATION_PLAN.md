# MythosMUD Architecture Remediation Plan

**Document Version:** 1.0
**Date:** November 3, 2025
**Status:** Active Implementation
**Author:** Miskatonic University Development Team

## Overview

This plan addresses 10 critical architectural issues identified in the comprehensive architecture review. Issues are prioritized by severity and dependency order. Each phase must be completed and tested before proceeding to the next.

## Phase 1: Critical Foundation Fixes (Week 1-2)

### 1.1 Dependency Injection Container Implementation

**Priority: CRITICAL** - Eliminates 19+ global singletons

**Approach:**
- Create `server/container.py` with `ApplicationContainer` class
- Inject dependencies through constructors instead of global state
- Maintain singleton behavior through container, not global variables

**Key Changes:**
- New file: `server/container.py` - DI container implementation
- Refactor: `server/app/factory.py` - Use container for service initialization
- Refactor: `server/app/lifespan.py` - Initialize container during startup
- Update: All service files to accept dependencies via constructor

**Files Affected:**
- `server/persistence.py` (remove `_persistence_instance` global)
- `server/database.py` (remove `_db_manager` global)
- `server/config/__init__.py` (remove `_config_instance` global)
- `server/logging/enhanced_logging_config.py` (remove global flags)
- `server/app/tracked_task_manager.py` (remove global manager)
- 14+ other singleton instances

**Success Criteria:**
- Zero module-level global state variables (except constants)
- All services accept dependencies through `__init__`
- Tests can create isolated service instances without reset functions

### 1.2 EventBus Consolidation & Event Source Deduplication

**Priority: CRITICAL** - Fixes duplicate game messages to players

**Approach:**
- Establish single authoritative EventBus instance
- Define canonical events for each domain action
- Eliminate duplicate event publishers (Connection + Room events)

**Key Changes:**
- Audit: Map all event publishers and identify duplicates
- Design: Create event ownership matrix (who publishes what)
- Refactor: `server/realtime/connection_manager.py` - Remove duplicate events
- Refactor: `server/models/room.py` - Use canonical event names
- Update: All event handlers to listen to single event source

**Event Ownership Rules:**
```
Player Connection → PlayerConnectionEvents (connected, disconnected)
Room Movement → RoomMovementEvents (entered, left, moved)
Combat → CombatEvents (started, attacked, ended)
Chat → ChatEvents (message_sent, whisper_sent)
```

**Files Affected:**
- `server/events/event_types.py` - Define canonical event taxonomy
- `server/realtime/connection_manager.py` - Remove `player_entered_game`/`player_left_game`
- `server/models/room.py` - Use only `PlayerEnteredRoom`/`PlayerLeftRoom`
- `server/persistence.py` - Remove event publishing during sync operations
- All event handlers - Update to listen for canonical events only

**Success Criteria:**
- Each game action produces exactly ONE event type
- Zero duplicate messages received by players
- Event flow clearly documented and traceable

### 1.3 Async Migration Strategy for PersistenceLayer

**Priority: CRITICAL** - Eliminates event loop blocking

**Approach:**
- Migrate `PersistenceLayer` to use `AsyncSession` instead of `sqlite3`
- Replace `threading.RLock` with `asyncio.Lock`
- Update all persistence methods to async

**Key Changes:**
- Refactor: `server/persistence.py` - Convert to async operations
- Update: All callers to `await` persistence operations
- Remove: All `threading.RLock` usage in persistence
- Add: Proper async context managers

**Files Affected:**
- `server/persistence.py` - Complete async migration (~1293 lines)
- `server/game/player_service.py` - Update all persistence calls
- `server/game/room_service.py` - Update all persistence calls
- `server/commands/*.py` - Update command handlers to async persistence
- 50+ test files - Update to async test patterns

**Migration Phases:**
1. Create `AsyncPersistenceLayer` alongside existing (parallel implementation)
2. Migrate high-traffic paths first (player updates, room queries)
3. Update all callers incrementally
4. Remove sync `PersistenceLayer` after complete migration
5. Update all tests to use async patterns

**Success Criteria:**
- Zero synchronous database operations in async request handlers
- All persistence operations use `async/await`
- No `threading.Lock` usage in persistence layer
- Tests pass with async-only operations

## Phase 2: Architecture Cleanup (Week 3-4)

### 2.1 CORS Middleware Consolidation

**Priority: HIGH** - Reduces configuration complexity

**Approach:**
- Merge `AllowedCORSMiddleware` functionality into FastAPI's `CORSMiddleware`
- Simplify environment variable override logic
- Single source of truth for CORS configuration

**Key Changes:**
- Remove: `server/middleware/allowed_cors.py` (custom middleware)
- Update: `server/app/factory.py` - Use single CORS middleware
- Simplify: `server/config/models.py` - Remove complex override logic
- Update: Tests to not depend on specific middleware presence

**Files Affected:**
- `server/middleware/allowed_cors.py` - DELETE
- `server/app/factory.py` - Simplify CORS setup
- `server/config/models.py` - Simplify CORSConfig validation
- `server/tests/*/test_cors_*.py` - Update test expectations

**Success Criteria:**
- Single CORS middleware in middleware stack
- Clear configuration precedence (env > config > defaults)
- All CORS tests pass with simplified configuration

### 2.2 Message Broker Abstraction Layer

**Priority: HIGH** - Removes NATS vendor lock-in

**Approach:**
- Define `MessageBroker` Protocol (abstract interface)
- Implement `NATSMessageBroker` concrete implementation
- Update services to depend on abstraction, not NATS directly

**Key Changes:**
- New: `server/infrastructure/message_broker.py` - Protocol definition
- New: `server/infrastructure/nats_broker.py` - NATS implementation
- Refactor: `server/services/nats_service.py` - Wrap in abstraction
- Update: All services to use `MessageBroker` interface

**Files Affected:**
- `server/services/nats_service.py` - Implement MessageBroker protocol
- `server/services/combat_event_publisher.py` - Use abstraction
- `server/realtime/nats_message_handler.py` - Use abstraction
- All services using NATS - Update to use abstraction

**Success Criteria:**
- Zero direct `import nats` in service layer
- Can swap message broker implementation without changing services
- Tests can mock message broker interface

### 2.3 Complete Error Handler Migration

**Priority: HIGH** - Eliminates legacy code

**Approach:**
- Migrate remaining legacy error handlers to modular system
- Remove `server/legacy_error_handlers.py`
- Consolidate error response creation

**Key Changes:**
- Audit: Find all usages of legacy error handlers
- Migrate: Update to use `StandardizedErrorResponse`
- Remove: `server/legacy_error_handlers.py`
- Update: All imports and references

**Files Affected:**
- `server/legacy_error_handlers.py` - DELETE after migration
- All API endpoints - Use modular error handlers
- `server/error_handlers/__init__.py` - Remove legacy imports
- Tests - Update error response expectations

**Success Criteria:**
- `legacy_error_handlers.py` deleted
- All errors use standardized response format
- All tests pass with new error handlers

## Phase 3: Code Quality Improvements (Week 5)

### 3.1 Circular Dependency Elimination

**Priority: MEDIUM** - Improves maintainability

**Approach:**
- Analyze import graph to identify circular dependencies
- Refactor to establish proper layered dependencies
- Remove `server/models/relationships.py` workaround

**Key Changes:**
- Analyze: Run dependency analysis tool
- Refactor: Move relationships into model definitions
- Update: Module imports to follow dependency rule
- Remove: Late relationship binding workaround

**Files Affected:**
- `server/models/relationships.py` - DELETE after refactoring
- `server/models/*.py` - Define relationships inline
- Various modules with circular imports - Refactor

**Success Criteria:**
- No circular imports detected by analysis tools
- Relationships defined directly in model files
- No late-binding relationship setup required

### 3.2 Client Path Aliases Configuration

**Priority: MEDIUM** - Improves developer experience

**Approach:**
- Configure TypeScript path aliases
- Replace all relative imports with absolute aliases
- Update ESLint to enforce alias usage

**Key Changes:**
- Update: `client/tsconfig.json` - Add path mappings
- Update: `client/vite.config.ts` - Configure Vite aliases
- Refactor: All `.tsx`/`.ts` files - Replace `../../../` with `@/`
- Update: `client/eslint.config.js` - Enforce alias usage

**Path Aliases:**
```json
{
  "@components/*": ["src/components/*"],
  "@utils/*": ["src/utils/*"],
  "@config/*": ["src/config/*"],
  "@stores/*": ["src/stores/*"],
  "@hooks/*": ["src/hooks/*"],
  "@theme/*": ["src/theme/*"],
  "@contexts/*": ["src/contexts/*"]
}
```

**Files Affected:**
- `client/tsconfig.json` - Add path mappings
- `client/vite.config.ts` - Add resolve aliases
- 174+ client files - Update imports

**Success Criteria:**
- Zero imports using `../../../` pattern
- All imports use `@alias/` pattern
- ESLint passes with alias enforcement

### 3.3 Domain Layer Introduction

**Priority: MEDIUM** - Enables clean architecture

**Approach:**
- Create `server/domain/` directory structure
- Move business logic from services to domain layer
- Establish clear layer boundaries

**Key Changes:**
- New: `server/domain/player/` - Player domain logic
- New: `server/domain/room/` - Room domain logic
- New: `server/domain/combat/` - Combat domain logic
- New: `server/domain/chat/` - Chat domain logic
- Refactor: Move business rules from services to domain
- Update: Services to orchestrate domain operations

**Architecture:**
```
Presentation (API) → Application (Services) → Domain (Business Logic) → Infrastructure (DB/NATS)
```

**Files Affected:**
- New directory structure under `server/domain/`
- `server/services/*.py` - Extract business logic to domain
- `server/game/*.py` - Move to domain layer
- Tests - Add domain layer tests

**Success Criteria:**
- Business logic isolated in domain layer
- Services only orchestrate, don't contain business rules
- Domain layer has no infrastructure dependencies

### 3.4 Configuration Override Simplification

**Priority: LOW** - Reduces complexity

**Approach:**
- Simplify CORS configuration override logic
- Establish clear precedence: env > file > defaults
- Remove complex parsing logic

**Key Changes:**
- Simplify: `server/config/models.py` - CORSConfig parsing
- Remove: Complex JSON/CSV/list parsing logic
- Document: Configuration precedence rules

**Files Affected:**
- `server/config/models.py` - Simplify CORSConfig (lines 388-641)
- `server/app/factory.py` - Simplify CORS setup
- Environment files - Standardize format

**Success Criteria:**
- Single parsing method for environment variables
- Clear documentation of override precedence
- Reduced configuration code by 50%

## Implementation Strategy

### Risk Mitigation

1. **Incremental Changes**: Each phase can be implemented incrementally
2. **Parallel Implementation**: Keep old code working while new code is added
3. **Feature Flags**: Use feature flags for major migrations
4. **Comprehensive Testing**: Run full test suite after each change
5. **Rollback Plan**: Git branches for each phase with clear rollback points

### Testing Requirements

Each phase requires:
- All existing tests continue to pass
- New tests for refactored code
- Integration tests for changed components
- E2E tests for critical paths
- Performance benchmarks to ensure no regression

### Documentation Updates

Each phase requires updating:
- Architecture documentation (`docs/REAL_TIME_ARCHITECTURE.md`)
- Development guides (`docs/DEVELOPMENT_AI.md`)
- Code comments and docstrings
- Test documentation

## Success Metrics

**Phase 1 Complete:**
- Zero module-level globals (except constants)
- Single authoritative event source
- All persistence operations async

**Phase 2 Complete:**
- Single CORS middleware
- Message broker abstraction in place
- Zero legacy error handlers

**Phase 3 Complete:**
- Zero circular imports
- Client uses path aliases
- Clear domain layer boundaries

**Overall Success:**
- Architecture score improves from 6.5/10 to 8.5/10
- Test coverage remains >80%
- No performance regression
- All existing features continue working
- Foundation ready for advanced features

## Timeline Estimate

- **Phase 1**: 2 weeks (80 hours)
- **Phase 2**: 2 weeks (80 hours)
- **Phase 3**: 1 week (40 hours)
- **Total**: 5 weeks (200 hours)

Note: Timeline assumes focused work without feature development in parallel.

## Critical Architectural Issues Summary

### Issue Severity Breakdown

| Severity | Count | Issues |
|----------|-------|--------|
| 🔴 CRITICAL | 4 | Global Singletons, Circular Dependencies, Async/Sync Mix, EventBus Duplication |
| 🟡 HIGH | 3 | CORS Middleware, NATS Coupling, Error Handler Migration |
| 🟢 MEDIUM | 3 | Client Imports, Domain Layer, Configuration Complexity |

### Architectural Quality Metrics (Current State)

| Quality Attribute | Score | Target |
|-------------------|-------|--------|
| Maintainability | 6/10 | 9/10 |
| Testability | 7/10 | 9/10 |
| Scalability | 7/10 | 8/10 |
| Security | 8/10 | 9/10 |
| Performance | 6/10 | 8/10 |
| Reliability | 7/10 | 9/10 |
| Modularity | 5/10 | 9/10 |
| **Overall** | **6.5/10** | **8.5/10** |

## Implementation Status

- [ ] Phase 1.1: Dependency Injection Container
- [ ] Phase 1.2: EventBus Consolidation
- [ ] Phase 1.3: Async Persistence Migration
- [ ] Phase 2.1: CORS Consolidation
- [ ] Phase 2.2: Message Broker Abstraction
- [ ] Phase 2.3: Error Handler Migration
- [ ] Phase 3.1: Circular Dependency Elimination
- [ ] Phase 3.2: Client Path Aliases
- [ ] Phase 3.3: Domain Layer Introduction
- [ ] Phase 3.4: Configuration Simplification

## Next Steps

Begin with Phase 1.1 (Dependency Injection Container) as it unblocks all subsequent refactoring work.

---

**References:**
- Architecture Review: Internal documentation
- Clean Architecture: Robert C. Martin
- Domain-Driven Design: Eric Evans
- Patterns of Enterprise Application Architecture: Martin Fowler
