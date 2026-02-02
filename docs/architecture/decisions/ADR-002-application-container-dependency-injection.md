# ADR-002: ApplicationContainer for Dependency Injection

**Status:** Accepted
**Date:** 2026-02-02

## Context

Before the ApplicationContainer refactor, MythosMUD used 19+ global singletons for services such as PlayerService, RoomService, ConnectionManager, and EventBus. Global singletons cause tight coupling, make unit testing difficult (services cannot be mocked or replaced), and obscure the dependency graph. Test setup required mutating global state, leading to fragile, order-dependent tests.

## Decision

Implement a single **ApplicationContainer** class in `server/container.py` that:

- Manages all service lifecycle and dependency resolution
- Provides thread-safe initialization with explicit phases
- Exposes services as attributes (e.g., `container.player_service`)
- Replaces all global singleton access with container injection
- Ensures dependency inversion: services depend on abstractions, container wires concrete implementations

The container is initialized once at application startup and passed (or accessed via a single accessor) where services are needed.

## Alternatives Considered

1. **Continue with global singletons** - Rejected: testing and maintainability suffer
2. **Third-party DI framework (e.g., dependency-injector, injector)** - Rejected: ApplicationContainer provides sufficient control; avoids extra dependency; custom phases (e.g., warm room cache before starting real-time) are explicit
3. **Domain-specific sub-containers** - Deferred: documented in APPLICATION_CONTAINER_ANALYSIS.md as future refinement; current single container is acceptable

## Consequences

- **Positive**: Eliminated global singletons; explicit dependency graph; testable services via mock injection; proper lifecycle management
- **Negative**: Container is large (~1,200+ lines); some circular dependencies handled with TYPE_CHECKING; splitting by domain requires migration
- **Neutral**: Initialization order is explicit but complex; document initialization phases for maintainers

## Related ADRs

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-005: Repository Pattern for Data Access

## References

- [ApplicationContainer Analysis](../../APPLICATION_CONTAINER_ANALYSIS.md)
- [Bounded Contexts and Service Boundaries](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
