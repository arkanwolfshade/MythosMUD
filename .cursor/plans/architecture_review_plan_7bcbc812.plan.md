---
name: Architecture Review Plan
overview: Comprehensive architectural review of MythosMUD codebase evaluating modern architecture patterns, clean architecture principles, distributed systems design, and identifying areas for improvement.
todos:
  - id: implement-client-updates-plan
    content: Implement Client Updates System (Option C) per client_updates_system_audit_628e3fef.plan.md before proceeding with remaining architecture review todos
    status: completed
  - id: review-event-duplication
    content: Review and consolidate event duplication (EventBus vs direct WebSocket sends) per EVENT_OWNERSHIP_MATRIX.md
    status: completed
  - id: analyze-container-structure
    content: Analyze ApplicationContainer structure and propose domain-specific container split
    status: completed
  - id: review-repository-wrappers
    content: Review ContainerRepository and ItemRepository async wrappers and plan full async migration
    status: completed
  - id: define-service-boundaries
    content: Define explicit bounded contexts and service boundaries with documentation
    status: completed
  - id: create-adrs
    content: Create Architecture Decision Records (ADRs) for major architectural decisions
    status: completed
  - id: evaluate-distributed-eventbus
    content: Evaluate distributed EventBus solution (NATS) for horizontal scalability
    status: completed
  - id: review-domain-models
    content: Review domain models for anemic domain model anti-pattern and move logic from services to models
    status: completed
  - id: document-api-contracts
    content: Document API contracts and service interfaces with OpenAPI/Swagger specifications
    status: completed
isProject: false
---

# MythosMUD Architectural Review Plan

## Implementation Order and Prerequisites

**The Client Updates System Audit plan must be completed before continuing with any further todos in this architecture review plan.**

- **Prerequisite plan:** [client_updates_system_audit_628e3fef.plan.md](client_updates_system_audit_628e3fef.plan.md) (Client Updates System Audit – Option C implementation).
- **Gate todo:** `implement-client-updates-plan` – Implement the replacement client updates system (event-sourced derivation, single-source room/combat state, request/response for critical handoffs) as specified in that plan.
- **Remaining architecture review todos** (review-repository-wrappers, define-service-boundaries, create-adrs, evaluate-distributed-eventbus, review-domain-models, document-api-contracts) should be started only after `implement-client-updates-plan` is completed.

## Executive Summary

This review evaluates MythosMUD's architecture against modern software architecture principles including Clean Architecture, Domain-Driven Design, Event-Driven Architecture, and distributed systems patterns. The codebase demonstrates strong foundational patterns with opportunities for refinement in service boundaries, event ownership, and architectural documentation.

## 1. Current Architecture Assessment

### 1.1 Overall System Architecture

**Architecture Style**: Layered Architecture with Event-Driven Components

**Technology Stack**:

- **Backend**: FastAPI (Python) with async/await
- **Frontend**: React 18+ with TypeScript
- **Database**: PostgreSQL with SQLAlchemy async ORM
- **Messaging**: NATS for pub/sub, EventBus for domain events
- **Real-time**: WebSocket-only architecture

**Strengths**:

- Clear separation between client, API, service, and persistence layers
- Modern async/await patterns throughout
- Comprehensive dependency injection via `ApplicationContainer`
- Repository pattern for data access abstraction

**Areas for Review**:

- Service boundary definitions and cohesion
- Event ownership and duplication (documented in `EVENT_OWNERSHIP_MATRIX.md`)
- Client architecture organization

### 1.2 Layered Architecture Analysis

**Current Layers**:

```
┌─────────────────────────────────────┐
│  Client (React/TypeScript)          │
└──────────────┬──────────────────────┘
               │ HTTP/WebSocket
┌──────────────▼──────────────────────┐
│  API Layer (FastAPI Routers)         │
│  - /api/players, /api/containers     │
│  - /api/real_time (WebSocket)        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Service Layer                       │
│  - PlayerService, CombatService      │
│  - ContainerService, ChatService    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Domain Layer                        │
│  - Models (Player, Room, NPC)        │
│  - EventBus (domain events)          │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Persistence Layer                   │
│  - AsyncPersistenceLayer (Facade)     │
│  - Repositories (Player, Health, etc)│
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Database (PostgreSQL)               │
└─────────────────────────────────────┘
```

**Assessment**:

- ✅ Clear layer separation
- ✅ Dependency direction follows Clean Architecture (outer layers depend on inner)
- ⚠️ Some services directly access repositories (bypassing persistence facade)
- ⚠️ Domain models have some persistence concerns mixed in

### 1.3 Dependency Injection Architecture

**Implementation**: `ApplicationContainer` pattern in `server/container.py`

**Analysis and proposal:** See `docs/APPLICATION_CONTAINER_ANALYSIS.md` for a full structure analysis, attribute inventory by domain, initialization order, and a proposed domain-specific split using internal bundles (Option A) with backward-compatible migration path.

**Strengths**:

- Eliminated 19+ global singletons
- Explicit dependency graph
- Thread-safe initialization
- Proper lifecycle management

**Pattern Compliance**:

- ✅ Dependency Inversion Principle (DIP) - depends on abstractions
- ✅ Single Responsibility - container manages dependencies only
- ⚠️ Container is large (1,200+ lines) - consider splitting by domain
- ⚠️ Some circular dependencies handled with `TYPE_CHECKING` blocks

**Recommendations**:

- Consider domain-specific containers (GameContainer, RealtimeContainer)
- Extract service factories for complex initialization
- Document dependency graph and initialization order

### 1.4 Repository Pattern Implementation

**Current State**: 9 specialized repositories in `server/persistence/repositories/`

**Repositories**:

- `PlayerRepository` (664 lines)
- `HealthRepository` (atomic JSONB updates)
- `ExperienceRepository` (atomic stat updates)
- `RoomRepository` (cache-based)
- `ContainerRepository`, `ItemRepository` (async wrappers)
- `ProfessionRepository`, `SpellRepository`, `PlayerSpellRepository`

**Strengths**:

- ✅ Clear separation of data access concerns
- ✅ Atomic operations for race condition prevention
- ✅ Async-first design
- ✅ Testable in isolation

**Areas for Improvement**:

- Some repositories use `asyncio.to_thread()` wrappers (ContainerRepository, ItemRepository)
- Consider Unit of Work pattern for transaction management
- Repository interfaces could be more explicit (protocols/interfaces)

### 1.5 Event-Driven Architecture

**Dual Event Systems**:

1. **EventBus** (Domain Events) - `server/events/event_bus.py`

- In-memory pub/sub for domain events
- Pure asyncio implementation
- Events: `PlayerEnteredRoom`, `CombatStartedEvent`, etc.

1. **NATS** (Inter-Service Communication) - `server/services/nats_service.py`

- Distributed pub/sub for real-time events
- Subject-based routing (`chat.say.{room_id}`, `events.player_entered.{room_id}`)
- Used for chat, combat events, game ticks

**Critical Issue Identified**: Event duplication documented in `EVENT_OWNERSHIP_MATRIX.md`

- Player movement events published to both EventBus AND sent directly via WebSocket
- Recommendation: Single source of truth - EventBus → RealTimeEventHandler → WebSocket

**Event Flow**:

```
Domain Layer (Room, Combat)
    ↓ publishes
EventBus (Domain Events)
    ↓ notifies
RealTimeEventHandler (Event → Message Transformer)
    ↓ sends
WebSocket (Client Delivery)
```

**Parallel Path (Chat)**:

```
ChatService
    ↓ publishes
NATS (chat.* subjects)
    ↓ subscribes
NATSMessageHandler
    ↓ sends
WebSocket
```

**Assessment**:

- ✅ Clear separation between domain events (EventBus) and messaging (NATS)
- ⚠️ Event duplication needs consolidation
- ✅ Event ownership matrix documents current state
- ⚠️ Consider event sourcing for critical game state changes

### 1.6 Real-Time Communication Architecture

**Architecture**: WebSocket-only (no SSE)

**Components**:

- `ConnectionManager` (facade pattern, 2,382 lines - refactored from 3,653)
- `RealTimeEventHandler` (EventBus → WebSocket)
- `NATSMessageHandler` (NATS → WebSocket)
- `EventPublisher` (standardized NATS publishing)

**Strengths**:

- ✅ Modular architecture (7 specialized modules)
- ✅ Circuit breaker pattern for resilience
- ✅ Connection health monitoring
- ✅ Room-based subscription management

**Areas for Review**:

- Message ordering and sequence numbers
- Reconnection strategy (exponential backoff)
- Dead letter queue implementation
- Performance under high concurrency

### 1.7 Security Architecture

**Implemented Security Features**:

- ✅ Argon2 password hashing
- ✅ JWT token authentication
- ✅ Rate limiting (per-user, per-endpoint)
- ✅ Input validation (Pydantic models)
- ✅ Command injection prevention
- ✅ Security headers middleware
- ✅ COPPA compliance considerations

**Security Layers**:

1. Input validation (Pydantic, command validators)
2. Authentication (JWT, Bearer tokens)
3. Authorization (role-based, admin actions)
4. Rate limiting (command rate limiter)
5. Audit logging (security events)

**Assessment**:

- ✅ Defense in depth approach
- ✅ Security-first mindset in codebase
- ⚠️ Consider adding API key rotation
- ⚠️ Review secret management (currently environment variables)

### 1.8 Error Handling Architecture

**Error Handling Strategy**:

- Custom exception hierarchy (`MythosMUDError` base class)
- Structured error logging with context
- Standardized error responses
- Error handling middleware (ASGI-based)

**Components**:

- `StandardizedErrorResponse` - consistent error format
- `ErrorHandlingMiddleware` - catches all exceptions
- `ErrorContext` - rich context for debugging
- Enhanced logging with correlation IDs

**Strengths**:

- ✅ Comprehensive error context
- ✅ User-friendly error messages
- ✅ Security-aware (no sensitive data in logs)
- ✅ Correlation IDs for request tracking

### 1.9 Client Architecture

**Frontend Structure**:

- React 18+ with TypeScript
- Lazy loading for code splitting
- Zustand for state management (some components)
- WebSocket client for real-time communication

**Areas for Review**:

- State management patterns (mix of useState, Zustand)
- Component organization
- Error boundary implementation
- Type safety between client/server

## 2. Architectural Patterns Evaluation

### 2.1 SOLID Principles Compliance

**Single Responsibility Principle (SRP)**:

- ✅ Repositories have focused responsibilities
- ✅ Services are domain-specific
- ⚠️ Some services are large (ConnectionManager was 3,653 lines, now refactored)
- ⚠️ ApplicationContainer is large (split proposed in `docs/APPLICATION_CONTAINER_ANALYSIS.md`)

**Open/Closed Principle (OCP)**:

- ✅ Command pattern for extensible commands
- ✅ Event system allows new handlers without modification
- ✅ Repository pattern allows different implementations

**Liskov Substitution Principle (LSP)**:

- ✅ Repository interfaces are consistent
- ✅ Service interfaces follow contracts

**Interface Segregation Principle (ISP)**:

- ✅ Focused repository interfaces
- ⚠️ Some services have large interfaces (could be split)

**Dependency Inversion Principle (DIP)**:

- ✅ ApplicationContainer provides abstractions
- ✅ Services depend on repository interfaces
- ⚠️ Some direct database access (should go through repositories)

### 2.2 Design Patterns Used

**Implemented Patterns**:

- ✅ Repository Pattern (data access)
- ✅ Facade Pattern (AsyncPersistenceLayer, ConnectionManager)
- ✅ Factory Pattern (ItemFactory, Command factories)
- ✅ Observer Pattern (EventBus subscribers)
- ✅ Strategy Pattern (channel broadcasting strategies)
- ✅ Circuit Breaker Pattern (connection resilience)
- ✅ Dependency Injection (ApplicationContainer)

**Patterns to Consider**:

- Unit of Work (transaction management)
- Specification Pattern (complex queries)
- CQRS (Command Query Responsibility Segregation) for read/write separation
- Saga Pattern (distributed transactions if needed)

### 2.3 Domain-Driven Design (DDD) Assessment

**Current State**:

- Domain models exist (`Player`, `Room`, `NPC`, `Container`)
- Domain events (`PlayerEnteredRoom`, `CombatStartedEvent`)
- Some domain logic in services (could be in domain models)

**Areas for Improvement**:

- ⚠️ Bounded contexts not explicitly defined
- ⚠️ Ubiquitous language could be more consistent
- ⚠️ Some anemic domain models (logic in services)
- Consider aggregate roots and value objects

## 3. Scalability and Performance

### 3.1 Horizontal Scalability

**Current Limitations**:

- In-memory EventBus (not distributed)
- Room cache in memory (single instance)
- ConnectionManager state in memory

**Scalability Considerations**:

- ✅ NATS enables horizontal scaling for messaging
- ⚠️ EventBus is single-instance (consider Redis pub/sub)
- ⚠️ Room cache needs distributed solution for multi-instance
- ✅ Database connection pooling (SQLAlchemy)

**Recommendations**:

- Consider Redis for distributed EventBus
- Implement distributed room cache (Redis or database)
- Session affinity for WebSocket connections (sticky sessions)

### 3.2 Performance Optimizations

**Implemented**:

- ✅ Async/await throughout
- ✅ Connection pooling
- ✅ Room caching
- ✅ Lazy loading (client code splitting)
- ✅ Atomic database operations

**Areas for Review**:

- Database query optimization (N+1 queries?)
- Caching strategy (what's cached, TTLs)
- Message batching for WebSocket
- Database indexing strategy

## 4. Testing Architecture

**Test Organization**:

- Unit tests: `server/tests/unit/`
- Integration tests: `server/tests/integration/`
- Test fixtures: `server/tests/fixtures/`

**Coverage Requirements**:

- Minimum 70% overall coverage
- Critical files: 90% minimum
- Test execution: `make test` (fast suite), `make test-comprehensive` (full suite)

**Assessment**:

- ✅ Comprehensive test structure
- ✅ Test fixtures for common scenarios
- ✅ Mock helpers for isolation
- ⚠️ Review test coverage reports for gaps

## 5. Documentation Architecture

**Current Documentation**:

- Architecture docs in `docs/` directory
- Event ownership matrix
- Persistence architecture docs
- Real-time architecture docs
- Security guides

**Strengths**:

- ✅ Comprehensive architecture documentation
- ✅ Event flow diagrams
- ✅ Security guidelines

**Recommendations**:

- Create Architecture Decision Records (ADRs)
- Document service boundaries and contracts
- API documentation (OpenAPI/Swagger)
- Deployment architecture diagrams

## 6. Critical Issues and Recommendations

### 6.1 High Priority

1. **Event Duplication** (Documented in `EVENT_OWNERSHIP_MATRIX.md`)

- **Issue**: Player movement events published to both EventBus and sent directly
- **Impact**: Potential inconsistencies, harder to maintain
- **Recommendation**: Consolidate to single path: EventBus → RealTimeEventHandler → WebSocket

1. **ApplicationContainer Size**

- **Issue**: 1,200+ lines managing all dependencies
- **Impact**: Harder to maintain, test, and understand
- **Recommendation**: Split into domain-specific containers

1. **Repository Wrappers**

- **Issue**: ContainerRepository and ItemRepository use `asyncio.to_thread()` wrappers
- **Impact**: Performance overhead, complexity
- **Recommendation**: Migrate underlying code to async

### 6.2 Medium Priority

1. **Service Boundaries**

- Define explicit bounded contexts
- Document service contracts
- Consider microservices boundaries (if scaling)

1. **Event Sourcing Consideration**

- For critical game state (player actions, combat)
- Audit trail and replay capability
- Event store implementation

1. **CQRS Pattern**

- Separate read/write models
- Optimize queries independently
- Consider read replicas for scaling

### 6.3 Low Priority

1. **Architecture Decision Records (ADRs)**

- Document major architectural decisions
- Rationale and trade-offs
- Future reference

1. **API Versioning**

- Plan for API evolution
- Versioning strategy
- Backward compatibility

1. **Monitoring and Observability**

- Distributed tracing
- Performance metrics
- Business metrics

## 7. Implementation Plan

### Phase 1: Critical Fixes (Immediate)

1. Consolidate event duplication (EventBus → RealTimeEventHandler only)
2. Review and optimize ApplicationContainer structure
3. Migrate repository wrappers to full async

### Phase 2: Architecture Improvements (Short-term)

1. Define bounded contexts and service boundaries
2. Create ADRs for major decisions
3. Improve domain model richness (move logic from services to models)

### Phase 3: Scalability Preparation (Medium-term)

1. Evaluate distributed EventBus (Redis)
2. Implement distributed room cache
3. Plan for horizontal scaling architecture

### Phase 4: Advanced Patterns (Long-term)

1. Consider event sourcing for critical paths
2. Evaluate CQRS implementation
3. Advanced monitoring and observability

## 8. Success Metrics

**Architectural Quality**:

- Reduced code duplication
- Clear service boundaries
- Improved testability
- Better documentation

**Performance**:

- Response time improvements
- Throughput increases
- Resource utilization optimization

**Maintainability**:

- Reduced complexity metrics
- Improved code organization
- Better developer experience

## Conclusion

MythosMUD demonstrates a solid architectural foundation with modern patterns, comprehensive dependency injection, and clear layer separation. The primary areas for improvement are event consolidation, container organization, and preparing for horizontal scalability. The codebase shows strong engineering practices with room for refinement in service boundaries and distributed systems patterns.
