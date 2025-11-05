"""
Domain repository interfaces for MythosMUD.

Repositories provide an abstraction for data persistence, allowing the domain
layer to remain independent of specific database implementations.

Repository interfaces should:
- Define the contract for data access
- Use domain entities as parameters and return types
- Not leak infrastructure details (no SQLAlchemy sessions, etc.)
- Be implemented in the infrastructure layer

Example:
    from server.domain.repositories import PlayerRepository
    from server.domain.entities import PlayerEntity

    class PlayerRepository(Protocol):
        async def get_by_id(self, player_id: str) -> PlayerEntity | None:
            ...

        async def save(self, player: PlayerEntity) -> None:
            ...

        async def delete(self, player_id: str) -> bool:
            ...

    # Implementation lives in infrastructure layer:
    # server/infrastructure/repositories/sqlalchemy_player_repository.py
"""

__all__ = []
