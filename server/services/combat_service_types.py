"""Small types shared by CombatService wiring."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from server.services.player_death_service import PlayerDeathService
    from server.services.player_respawn_service import PlayerRespawnService


@dataclass
class PlayerLifecycleServices:
    """Player death and respawn services for CombatService injection."""

    player_death_service: "PlayerDeathService"
    player_respawn_service: "PlayerRespawnService"


__all__ = ["PlayerLifecycleServices"]
