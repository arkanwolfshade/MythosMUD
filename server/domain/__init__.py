"""
Domain layer for MythosMUD.

This package contains the core business logic and domain entities of the application,
independent of infrastructure concerns like databases, messaging, or web frameworks.

Following hexagonal architecture principles, the domain layer defines what the
application does, while infrastructure layers define how it's done.

As noted in the restricted archives: "The essence of the game - the rules, the
mechanics, the eldritch truths - must remain pure and untainted by the
ephemeral concerns of storage and transmission."

Domain Structure:
- entities/ - Core domain entities (Player, Room, NPC, etc.)
- value_objects/ - Immutable value objects (Stats, Location, etc.)
- services/ - Domain services (business logic not belonging to entities)
- events/ - Domain events (state change notifications)
- repositories/ - Repository interfaces (implemented by infrastructure)
- exceptions/ - Domain-specific exceptions

Architecture Principles:
- Domain entities are framework-agnostic
- Domain logic doesn't depend on infrastructure
- Domain defines interfaces; infrastructure implements them
- Domain events communicate state changes
"""

__all__ = []
