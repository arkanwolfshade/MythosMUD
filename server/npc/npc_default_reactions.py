"""Register default event reactions for an NPC (greeting, farewell, retaliation, spoke response)."""

from typing import TYPE_CHECKING

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int

if TYPE_CHECKING:
    from .event_reaction_system import NPCEventReactionSystem

logger: BoundLogger = get_logger(__name__)

# Gestures for an NPC with no authored lines; rendered as "<NPC name> <text>" (#1103).
DEFAULT_GREETING_EMOTE = "offers a wary nod in greeting."
DEFAULT_FAREWELL_EMOTE = "gives a wary nod, and nothing more, as someone leaves."
DEFAULT_SILENCE_EMOTE = "gives no answer, only silence."


def register_default_reactions_for_npc(
    npc_id: str,
    npc_type: str,
    behavior_config: dict[str, object],
    event_reaction_system: "NPCEventReactionSystem",
    stats: dict[str, object] | None = None,
) -> None:
    """Build and register default event reactions for this NPC (greeting, farewell, etc.)."""
    try:
        from .corruption_reactions import build_corruption_aware_greeting
        from .dialogue_reactions import build_dialogue_opening
        from .event_reaction_system import NPCEventReaction, NPCEventReactionTemplates

        reactions: list[NPCEventReaction] = []

        # #815: fallbacks for an NPC with no authored greeting/farewell of its own -- every one of
        # the ten seeded NPCs (data/db/seed.sql) sets its own greeting_message/
        # farewell_message, so these are rarely reached in practice. Kept in-tone regardless.
        # #1103: the fallbacks are gestures, so they go out as emotes ("<NPC> offers a wary nod..."); an authored
        # greeting/farewell/response is the NPC's own words and stays speech.
        if npc_type in ["shopkeeper", "passive_mob"]:
            if behavior_config.get("initiates_dialogue") is True:
                # An NPC that speaks first: opening the conversation IS its greeting (a variant, not an addition).
                reactions.append(build_dialogue_opening(npc_id, event_reaction_system.event_bus))
            else:
                authored_greeting = behavior_config.get("greeting_message")
                greeting = str(authored_greeting) if authored_greeting is not None else DEFAULT_GREETING_EMOTE
                # #815 PR-4: the greeting reaction is corruption-aware -- a variant, not an addition.
                npc_corruption = coerce_int((stats or {}).get("corruption", 0), default=0)
                reactions.append(
                    build_corruption_aware_greeting(
                        npc_id, npc_corruption, greeting, as_emote=authored_greeting is None
                    )
                )

        if npc_type in ["shopkeeper", "passive_mob"]:
            authored_farewell = behavior_config.get("farewell_message")
            reactions.append(
                NPCEventReactionTemplates.player_left_room_farewell(
                    npc_id,
                    str(authored_farewell) if authored_farewell is not None else DEFAULT_FAREWELL_EMOTE,
                    as_emote=authored_farewell is None,
                )
            )

        if npc_type == "aggressive_mob":
            reactions.append(NPCEventReactionTemplates.npc_attacked_retaliation(npc_id))

        if npc_type in ["shopkeeper", "passive_mob"]:
            authored_response = behavior_config.get("response_message")
            reactions.append(
                NPCEventReactionTemplates.player_spoke_response(
                    npc_id,
                    str(authored_response) if authored_response is not None else DEFAULT_SILENCE_EMOTE,
                    as_emote=authored_response is None,
                )
            )

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
