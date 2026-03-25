"""Register default event reactions for an NPC (greeting, farewell, retaliation, spoke response)."""

from typing import TYPE_CHECKING, cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .event_reaction_system import NPCEventReactionSystem

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def register_default_reactions_for_npc(
    npc_id: str,
    npc_type: str,
    behavior_config: dict[str, object],
    event_reaction_system: "NPCEventReactionSystem",
) -> None:
    """Build and register default event reactions for this NPC (greeting, farewell, etc.)."""
    try:
        from .event_reaction_system import NPCEventReaction, NPCEventReactionTemplates

        reactions: list[NPCEventReaction] = []

        if npc_type in ["shopkeeper", "passive_mob"]:
            greeting = str(behavior_config.get("greeting_message", "Hello there!"))
            reactions.append(NPCEventReactionTemplates.player_entered_room_greeting(npc_id, greeting))

        if npc_type in ["shopkeeper", "passive_mob"]:
            farewell = str(behavior_config.get("farewell_message", "Goodbye!"))
            reactions.append(NPCEventReactionTemplates.player_left_room_farewell(npc_id, farewell))

        if npc_type == "aggressive_mob":
            reactions.append(NPCEventReactionTemplates.npc_attacked_retaliation(npc_id))

        if npc_type in ["shopkeeper", "passive_mob"]:
            response = str(behavior_config.get("response_message", "I heard you!"))
            reactions.append(NPCEventReactionTemplates.player_spoke_response(npc_id, response))

        if reactions:
            event_reaction_system.register_npc_reactions(npc_id, reactions)
            logger.debug(
                "Registered default reactions",
                npc_id=npc_id,
                reaction_count=len(reactions),
            )
    except (ImportError, AttributeError, TypeError) as e:
        logger.error(
            "Error registering default reactions",
            npc_id=npc_id,
            error=str(e),
            error_type=type(e).__name__,
        )
