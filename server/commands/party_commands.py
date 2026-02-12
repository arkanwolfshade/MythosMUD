"""
Party commands for MythosMUD.

Handlers for party, party invite <name>, party leave, party kick <name>, party list.
Uses TargetResolutionService for same-room player resolution on invite/kick.
"""

from __future__ import annotations

from typing import Any

from ..alias_storage import AliasStorage
from ..schemas.shared import TargetType as SchemaTargetType
from ..services.target_resolution_service import TargetResolutionService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_container(request: Any) -> Any:
    """Get application container from request."""
    app = getattr(request, "app", None) if request else None
    if not app or not hasattr(app, "state"):
        return None
    return getattr(app.state, "container", None)


async def _get_party_command_context(
    request: Any, current_user: dict[str, Any]
) -> dict[str, Any] | tuple[Any, Any, Any, Any, str, str]:
    """
    Resolve container, party service, persistence, and current player for party commands.
    Returns an error result dict on failure, or a tuple of (container, party_service,
    async_persistence, player_id, player_id_str, display_name) on success.
    """
    container = _get_container(request)
    if not container or not getattr(container, "party_service", None):
        logger.warning("Party command rejected: party service not available")
        return {"result": "Party is not available."}
    async_persistence = getattr(container, "async_persistence", None)
    if not async_persistence:
        logger.warning("Party command rejected: no persistence")
        return {"result": "Party is not available."}
    username = get_username_from_user(current_user)
    player = await async_persistence.get_player_by_name(username)
    if not player:
        logger.warning("Party command rejected: player not in game", username=username)
        return {"result": "You are not in the game."}
    player_id = getattr(player, "player_id", None)
    if not player_id:
        logger.warning("Party command rejected: could not resolve player id", username=username)
        return {"result": "Unable to identify you."}
    player_id_str = str(player_id)
    display_name = getattr(player, "name", username) or username
    return (container, container.party_service, async_persistence, player_id, player_id_str, display_name)


async def _handle_party_chat(
    container: Any,
    party_service: Any,
    player_id: Any,
    player_id_str: str,
    party_message: str,
) -> dict[str, Any]:
    """Handle party <message> (send to party chat)."""
    party = party_service.get_party_for_player(player_id)
    if not party:
        logger.debug("Party chat rejected: player not in party", player_id=player_id_str)
        return {"result": "You are not in a party. Use 'party invite <name>' to form one."}
    chat_service = getattr(container, "chat_service", None)
    if not chat_service:
        logger.warning("Party chat rejected: chat service not available")
        return {"result": "Party chat is not available."}
    outcome = await chat_service.send_party_message(player_id_str, party_message, party.party_id)
    if not outcome.get("success"):
        logger.warning(
            "Party chat send failed",
            player_id=player_id_str,
            party_id=party.party_id,
            error=outcome.get("error"),
        )
        return {"result": outcome.get("error", "Could not send party message.")}
    logger.info(
        "Party chat sent; published to NATS",
        player_id=player_id_str,
        party_id=party.party_id,
        member_count=len(party.member_ids),
    )
    return {"result": "Sent."}


async def handle_party_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """
    Handle party [invite|leave|kick|list]. No subcommand = party status/list.
    """
    _ = (alias_storage, player_name)
    context = await _get_party_command_context(request, current_user)
    if isinstance(context, dict):
        return context
    container, party_service, async_persistence, player_id, player_id_str, display_name = context

    subcommand = (command_data.get("subcommand") or "").strip().lower()
    target_name = (command_data.get("target") or "").strip() if command_data.get("target") else None
    party_message = (command_data.get("message") or "").strip() if command_data.get("message") else None

    if not subcommand and party_message:
        return await _handle_party_chat(container, party_service, player_id, player_id_str, party_message)
    if subcommand == "invite":
        return await _handle_party_invite(
            party_service, container, async_persistence, player_id, player_id_str, display_name, target_name
        )
    if subcommand == "leave":
        return _handle_party_leave(party_service, player_id)
    if subcommand == "kick":
        return await _handle_party_kick(
            party_service, container, async_persistence, player_id, player_id_str, target_name
        )
    if subcommand in ("list", ""):
        return await _handle_party_list(party_service, async_persistence, player_id, player_id_str, display_name)
    logger.debug("Party command unknown subcommand", subcommand=subcommand or "(empty)")
    return {"result": "Usage: party [invite|leave|kick|list] [target]"}


async def _handle_party_invite(
    party_service: Any,
    container: Any,
    async_persistence: Any,
    player_id: Any,
    player_id_str: str,
    inviter_display_name: str,
    target_name: str | None,
) -> dict[str, Any]:
    """Handle party invite <name> logic. Uses confirmation pattern: target must accept."""
    if not target_name:
        logger.debug("Party invite rejected: no target name")
        return {"result": "Invite whom? Usage: party invite <player name>"}
    if not party_service.get_party_for_player(player_id):
        create = party_service.create_party(player_id)
        if not create["success"]:
            logger.warning("Party invite rejected: create party failed", result=create.get("result"))
            return {"result": create["result"]}
    party = party_service.get_party_for_player(player_id)
    if not party or not party_service.is_leader(player_id):
        logger.debug("Party invite rejected: not leader or no party")
        return {"result": "Only the party leader can invite members."}
    player_svc = getattr(container, "player_service", None)
    if not player_svc:
        logger.warning("Party invite rejected: player service not available")
        return {"result": "Party is not available."}
    target_resolution = TargetResolutionService(async_persistence, player_svc)
    target_result = await target_resolution.resolve_target(player_id_str, target_name)
    if not target_result.success:
        logger.debug(
            "Party invite rejected: target resolve failed", target=target_name, error=target_result.error_message
        )
        return {"result": target_result.error_message or "No such player here."}
    match = target_result.get_single_match()
    if not match or match.target_type != SchemaTargetType.PLAYER:
        logger.debug("Party invite rejected: target not a player", target=target_name)
        return {"result": "You can only invite players. No such player here."}
    result = await party_service.request_party_invite(player_id, inviter_display_name, party.party_id, match.target_id)
    if not result.get("success"):
        return {"result": result.get("result", "Could not send invite.")}
    logger.info(
        "Party invite sent (pending acceptance)",
        party_id=party.party_id,
        inviter_id=player_id_str,
        target_id=str(match.target_id),
    )
    return {"result": result.get("result", "Party invite sent. Waiting for them to accept.")}


def _handle_party_leave(party_service: Any, player_id: Any) -> dict[str, Any]:
    """Handle party leave."""
    party = party_service.get_party_for_player(player_id)
    if not party:
        logger.debug("Party leave rejected: not in party", player_id=str(player_id))
        return {"result": "You are not in a party."}
    result = party_service.remove_member(party.party_id, player_id)
    logger.info("Party leave succeeded", party_id=party.party_id, player_id=str(player_id))
    return {"result": result.get("result", "You have left the party.")}


async def _handle_party_kick(
    party_service: Any,
    container: Any,
    async_persistence: Any,
    player_id: Any,
    player_id_str: str,
    target_name: str | None,
) -> dict[str, Any]:
    """Handle party kick <name> logic."""
    if not target_name:
        logger.debug("Party kick rejected: no target name")
        return {"result": "Kick whom? Usage: party kick <player name>"}
    party = party_service.get_party_for_player(player_id)
    if not party or not party_service.is_leader(player_id):
        logger.debug("Party kick rejected: not leader or no party")
        return {"result": "Only the party leader can kick members."}
    player_svc = getattr(container, "player_service", None)
    if not player_svc:
        logger.warning("Party kick rejected: player service not available")
        return {"result": "Party is not available."}
    target_resolution = TargetResolutionService(async_persistence, player_svc)
    target_result = await target_resolution.resolve_target(player_id_str, target_name)
    if not target_result.success:
        logger.debug(
            "Party kick rejected: target resolve failed", target=target_name, error=target_result.error_message
        )
        return {"result": target_result.error_message or "No such player here."}
    match = target_result.get_single_match()
    if not match or match.target_type != SchemaTargetType.PLAYER:
        return {"result": "No such player in your party."}
    if match.target_id not in party.member_ids:
        return {"result": "That player is not in your party."}
    result = party_service.kick_member(party.party_id, match.target_id, player_id)
    logger.info(
        "Party kick succeeded",
        party_id=party.party_id,
        kicker_id=player_id_str,
        target_id=str(match.target_id),
    )
    return {"result": result.get("result", "Done.")}


async def _handle_party_list(
    party_service: Any,
    async_persistence: Any,
    player_id: Any,
    player_id_str: str,
    display_name: str,
) -> dict[str, Any]:
    """Handle party status/list output."""
    party = party_service.get_party_for_player(player_id)
    if not party:
        logger.debug("Party list rejected: not in party", player_id=player_id_str)
        return {"result": "You are not in a party. Use 'party invite <name>' to form one (you become leader)."}
    lines = ["Your party:"]
    for mid in sorted(party.member_ids):
        name = display_name if mid == player_id_str else await _get_member_display(mid, async_persistence)
        suffix = " (leader)" if mid == party.leader_id else ""
        lines.append(f"  - {name}{suffix}")
    return {"result": "\n".join(lines)}


async def _get_member_display(member_id: str, async_persistence: Any) -> str:
    """Get display name for a party member ID."""
    try:
        import uuid

        p = await async_persistence.get_player_by_id(uuid.UUID(member_id))
        return getattr(p, "name", member_id) if p else member_id
    except (ValueError, TypeError, AttributeError):
        return member_id
