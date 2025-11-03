"""
Domain services for MythosMUD.

Domain services contain business logic that doesn't naturally belong to any single
entity. They orchestrate operations across multiple entities or value objects.

Examples:
- Combat resolution logic
- Room transition validation
- NPC spawning rules
- Experience calculation

Domain services should:
- Be stateless (no instance variables beyond dependencies)
- Focus on business logic, not infrastructure
- Depend only on domain layer and infrastructure interfaces
- Not depend on application layer or frameworks

Example:
    from server.domain.services import CombatService
    from server.domain.repositories import PlayerRepository

    class CombatService:
        def __init__(self, player_repo: PlayerRepository):
            self._player_repo = player_repo

        def resolve_attack(
            self,
            attacker: PlayerEntity,
            defender: PlayerEntity
        ) -> CombatResult:
            # Pure business logic for combat resolution
            ...
"""

__all__ = []
