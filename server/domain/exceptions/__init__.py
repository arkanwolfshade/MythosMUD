"""
Domain-specific exceptions for MythosMUD.

These exceptions represent business rule violations and domain errors,
not infrastructure or technical failures.

Domain exceptions should:
- Have descriptive names that communicate the business rule violation
- Contain relevant domain context
- Be independent of infrastructure concerns
- Not inherit from HTTP exceptions or database exceptions

Example:
    from server.domain.exceptions import InvalidMovementError

    class InvalidMovementError(DomainError):
        '''Raised when a player attempts an invalid room transition.'''

        def __init__(self, player_id: str, from_room: str, to_room: str, reason: str):
            self.player_id = player_id
            self.from_room = from_room
            self.to_room = to_room
            self.reason = reason
            super().__init__(
                f"Player {player_id} cannot move from {from_room} to {to_room}: {reason}"
            )
"""


class DomainError(Exception):
    """Base exception for all domain errors."""

    pass


__all__ = ["DomainError"]
