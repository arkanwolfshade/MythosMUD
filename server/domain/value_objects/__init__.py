"""
Domain value objects for MythosMUD.

Value objects are immutable objects defined by their attributes, not identity.
Examples: Stats, Location, Coordinates, Health, etc.

Value objects should be:
- Immutable (use dataclasses with frozen=True or Pydantic)
- Validating (enforce invariants in __init__)
- Comparable by value equality
- Small and focused

Example:
    from server.domain.value_objects import Stats, Location

    stats = Stats(strength=10, dexterity=12, constitution=8)
    location = Location(zone="earth", subzone="arkhamcity", room="foyer_001")

    # Value objects are immutable
    # new_stats = stats.with_strength(15)  # Returns a new object
"""

__all__ = []
