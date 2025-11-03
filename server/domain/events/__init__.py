"""
Domain events for MythosMUD.

Domain events represent significant state changes in the domain that other parts
of the system may need to react to. They are the primary mechanism for
communicating between bounded contexts.

Domain events should:
- Be immutable
- Contain all relevant information about the state change
- Have past-tense names (PlayerDied, RoomEntered, etc.)
- Not contain business logic

Example:
    from server.domain.events import PlayerDiedEvent

    @dataclass(frozen=True)
    class PlayerDiedEvent:
        player_id: str
        room_id: str
        killer_id: str | None
        timestamp: datetime
        death_type: DeathType

    # Events are published through the event bus
    # event_bus.publish(PlayerDiedEvent(...))
"""

__all__ = []
