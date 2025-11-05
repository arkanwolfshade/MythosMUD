"""
Domain entities for MythosMUD.

Entities are objects with identity and lifecycle. They represent core concepts
in the game domain: Player, Room, NPC, Combat, etc.

Entities should be:
- Framework-agnostic (no SQLAlchemy, FastAPI, etc. dependencies)
- Rich in behavior (methods that encapsulate business rules)
- Focused on business logic, not infrastructure

Example:
    from server.domain.entities import PlayerEntity

    player = PlayerEntity(
        id="player-123",
        name="Investigator",
        stats=Stats(strength=10, dexterity=12, ...),
    )

    # Business logic lives in the entity
    player.take_damage(damage=5, source="deep_one")
    player.apply_sanity_loss(loss=10, source="non_euclidean_geometry")
"""

__all__ = []
