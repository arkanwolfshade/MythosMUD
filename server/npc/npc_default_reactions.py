"""Register default event reactions for an NPC (greeting, farewell, retaliation, spoke response)."""

from typing import TYPE_CHECKING

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .event_reaction_system import NPCEventReactionSystem

logger: BoundLogger = get_logger(__name__)


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

        # #815: fallbacks for an NPC with no authored greeting/farewell of its own -- every one of
        # the ten seeded NPCs (data/db/mythos_*_dml.sql) sets its own greeting_message/
        # farewell_message, so these are rarely reached in practice. Kept in-tone regardless.
        if npc_type in ["shopkeeper", "passive_mob"]:
            greeting = str(behavior_config.get("greeting_message", "A wary nod is offered in greeting."))
            reactions.append(NPCEventReactionTemplates.player_entered_room_greeting(npc_id, greeting))

        if npc_type in ["shopkeeper", "passive_mob"]:
            farewell = str(behavior_config.get("farewell_message", "A wary nod, and nothing more, marks your leaving."))
            reactions.append(NPCEventReactionTemplates.player_left_room_farewell(npc_id, farewell))

        if npc_type == "aggressive_mob":
            reactions.append(NPCEventReactionTemplates.npc_attacked_retaliation(npc_id))

        if npc_type in ["shopkeeper", "passive_mob"]:
            response = str(behavior_config.get("response_message", "There is no answer, only silence."))
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
