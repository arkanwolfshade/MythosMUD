"""NPC disengage: an NPC that breaks off a fight once its target is hurt enough.

Content sets ``behavior_config.disengage_at_target_dp_ratio`` (a fraction in (0, 1]) and, optionally,
``behavior_config.disengage_line`` (the clause after the NPC's name in the room line). On its turn, when its target's
DP has fallen to that fraction of max, the NPC announces it, the combat ends, and the NPC is despawned. That is a
despawn, not a death: no kill is recorded and no respawn is queued (respawns only come from the death handler).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from server.models.combat import CombatInstance, CombatParticipant
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger = get_logger(__name__)

DISENGAGE_RATIO_KEY = "disengage_at_target_dp_ratio"
DISENGAGE_LINE_KEY = "disengage_line"
DEFAULT_DISENGAGE_LINE = "breaks off the attack and withdraws."
DESPAWN_REASON = "disengaged"


class NpcDespawner(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub; mirrors NPCLifecycleManager
    """The slice of NPCLifecycleManager that disengage drives."""

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        """Despawn an NPC instance by its string id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


def disengage_ratio(npc: CombatParticipant) -> float | None:
    """The NPC's configured disengage fraction, or None when absent or not a number in (0, 1]."""
    raw = (npc.npc_behavior_config or {}).get(DISENGAGE_RATIO_KEY)
    if isinstance(raw, bool) or not isinstance(raw, int | float):
        return None
    return float(raw) if 0 < raw <= 1 else None


def should_disengage(npc: CombatParticipant, target: CombatParticipant) -> bool:
    """True when the NPC has a disengage ratio and its target's DP is at or below that fraction of max."""
    ratio = disengage_ratio(npc)
    if ratio is None or target.max_dp <= 0:
        return False
    return target.current_dp <= ratio * target.max_dp


def npc_lifecycle_manager(config: object) -> NpcDespawner | None:
    """The NPC lifecycle manager from the app container the combat config points at, if wired."""
    app = cast(object | None, getattr(config, "_app_instance", None))
    state = cast(object | None, getattr(app, "state", None))
    container = cast(object | None, getattr(state, "container", None))
    return cast(NpcDespawner | None, getattr(container, "npc_lifecycle_manager", None))


async def _announce(combat_service: CombatService, combat: CombatInstance, npc: CombatParticipant) -> None:
    npc_service = combat_service.get_npc_combat_integration_service()
    if npc_service is None:
        return
    line = (npc.npc_behavior_config or {}).get(DISENGAGE_LINE_KEY)
    _ = await npc_service.get_messaging_integration().broadcast_npc_disengage(
        combat.room_id,
        str(combat.combat_id),
        npc.name,
        line if isinstance(line, str) and line else DEFAULT_DISENGAGE_LINE,
        npc_disposition=npc_service.get_npc_disposition(npc.participant_id),
    )


def _despawn(combat_service: CombatService, npc: CombatParticipant, lifecycle: NpcDespawner | None) -> None:
    npc_service = combat_service.get_npc_combat_integration_service()
    npc_id = npc_service.get_original_string_id(npc.participant_id) if npc_service is not None else None
    if lifecycle is None or npc_id is None:
        logger.warning("Disengaged NPC could not be despawned", npc_name=npc.name, has_lifecycle=lifecycle is not None)
        return
    _ = lifecycle.despawn_npc(npc_id, reason=DESPAWN_REASON)


async def disengage(
    combat_service: CombatService, combat: CombatInstance, npc: CombatParticipant, lifecycle: NpcDespawner | None
) -> None:
    """Announce, end the combat, and despawn the NPC.

    ponytail: ends the whole combat, so in a multi-foe fight the other foes stop too; removing only this NPC from the
    roster needs an NPC counterpart of CombatService.remove_participant.
    """
    await _announce(combat_service, combat, npc)
    await combat_service.end_combat(combat.combat_id, f"{npc.name} disengaged")
    _despawn(combat_service, npc, lifecycle)
