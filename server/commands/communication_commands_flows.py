"""
Room/global/system/whisper/reply flows for communication command handlers.

Extracted from communication_commands to satisfy Lizard file and function limits
without changing handler signatures or behavior.
"""

from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from .communication_commands_support import (
    ChatCommandsProtocol,
    PlayerResolutionProtocol,
    UserManagerProtocol,
    app_from_request,
    chat_result_map,
    get_services_from_container,
    message_id_from_result,
    primary_id,
)

logger: BoundLogger = get_logger(__name__)

CHAT_UNAVAILABLE: dict[str, str] = {"result": "Chat functionality is not available."}
ADMIN_UNAVAILABLE: dict[str, str] = {"result": "Admin functionality is not available."}

# Client-facing text when chat flows hit an unexpected exception; never echo str(e) (information leakage).
_GENERIC_UNEXPECTED_CHAT_FAILURE = "Something went wrong. Please try again later."


def _str_error_from_chat_result(result: Mapping[str, object]) -> str:
    error_raw = result.get("error", "Unknown error")
    return error_raw if isinstance(error_raw, str) else "Unknown error"


async def _room_player_bundle(
    player_service: PlayerResolutionProtocol,
    player_name: str,
) -> tuple[object, object, object] | str:
    player_obj = await player_service.resolve_player_name(player_name)
    if not player_obj:
        return "Player not found."
    current_room_id = getattr(player_obj, "current_room_id", None)
    if not current_room_id:
        return "You are not in a room."
    pid = primary_id(player_obj)
    if pid is None:
        return "Player ID not found."
    return (player_obj, current_room_id, pid)


async def _global_player_bundle(
    player_service: PlayerResolutionProtocol,
    player_name: str,
) -> tuple[object, int, object] | str:
    player_obj = await player_service.resolve_player_name(player_name)
    if not player_obj:
        return "Player not found."
    player_level = getattr(player_obj, "level", 0)
    if not isinstance(player_level, int):
        player_level = 0
    if player_level < 1:
        return "You must be at least level 1 to use global chat."
    pid = primary_id(player_obj)
    if pid is None:
        return "Player ID not found."
    return (player_obj, player_level, pid)


async def _player_id_bundle(
    player_service: PlayerResolutionProtocol,
    player_name: str,
) -> tuple[object, object] | str:
    player_obj = await player_service.resolve_player_name(player_name)
    if not player_obj:
        return "Player not found."
    pid = primary_id(player_obj)
    if pid is None:
        return "Player ID not found."
    return (player_obj, pid)


def _message_from_command(
    command_data: Mapping[str, object],
    player_name: str,
    *,
    strip: bool,
    usage: str,
    empty_log: str,
) -> str | dict[str, str]:
    message = command_data.get("message")
    if not isinstance(message, str):
        logger.warning(empty_log, player_name=player_name, command_data=command_data)
        return {"result": usage}
    text = message.strip() if strip else message
    if not text:
        logger.warning(empty_log, player_name=player_name, command_data=command_data)
        return {"result": usage}
    return text


def _require_chat_pair(
    request: object | None,
    player_name: str,
    *,
    fail_log: str,
) -> tuple[PlayerResolutionProtocol, ChatCommandsProtocol] | dict[str, str]:
    app = app_from_request(request)
    player_service, chat_service, _ = get_services_from_container(app)
    if not player_service:
        logger.warning(
            "Chat flow missing player service",
            fail_log=fail_log,
            player_name=player_name,
        )
        return CHAT_UNAVAILABLE
    if not chat_service:
        logger.warning(
            "Chat flow missing chat service",
            fail_log=fail_log,
            player_name=player_name,
        )
        return CHAT_UNAVAILABLE
    return player_service, chat_service


@dataclass(frozen=True)
class _RoomChannelOutcomeConfig:
    success_fmt: str
    success_log: str
    fail_log: str
    err_label: str


async def _chat_send_with_room_bundle(
    command_data: Mapping[str, object],
    player_name: str,
    player_service: PlayerResolutionProtocol,
    chat_service: ChatCommandsProtocol,
    message: str,
    send: Callable[[ChatCommandsProtocol, object, str], Awaitable[object]],
    cfg: _RoomChannelOutcomeConfig,
) -> dict[str, str]:
    try:
        bundle = await _room_player_bundle(player_service, player_name)
        if isinstance(bundle, str):
            return {"result": bundle}
        _player_obj, current_room_id, player_id = bundle
        result_raw = await send(chat_service, player_id, message)
        result = chat_result_map(result_raw)
        if result.get("success"):
            logger.info(
                cfg.success_log,
                player_name=player_name,
                room=current_room_id,
                message_id=message_id_from_result(result),
            )
            return {"result": cfg.success_fmt.format(message)}
        error_msg = _str_error_from_chat_result(result)
        logger.warning(cfg.fail_log, player_name=player_name, error=error_msg)
        return {"result": f"{cfg.err_label}{error_msg}"}
    except (AttributeError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "Chat send with room bundle raised",
            fail_log=cfg.fail_log,
            player=player_name,
            command_data=command_data,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"{cfg.err_label}{_GENERIC_UNEXPECTED_CHAT_FAILURE}"}


async def flow_say_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `say` command: broadcast speech to the current room."""
    logger.debug("Processing say command", player_name=player_name, command_data=command_data)
    msg_or_err = _message_from_command(
        command_data,
        player_name,
        strip=False,
        usage="Say what? Usage: say <message>",
        empty_log="Say command with no message",
    )
    if isinstance(msg_or_err, dict):
        return msg_or_err
    logger.debug("Player saying message", player_name=player_name, message=msg_or_err)
    svc = _require_chat_pair(request, player_name, fail_log="Say command failed")
    if isinstance(svc, dict):
        return svc
    ps, cs = svc

    async def _send(c: ChatCommandsProtocol, pid: object, m: str) -> object:
        return await c.send_say_message(pid, m)

    cfg = _RoomChannelOutcomeConfig(
        success_fmt="You say: {0}",
        success_log="Say message sent successfully",
        fail_log="Say command failed",
        err_label="Error sending message: ",
    )
    return await _chat_send_with_room_bundle(command_data, player_name, ps, cs, msg_or_err, _send, cfg)


async def flow_local_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `local` command: room-only speech (not global)."""
    logger.debug("Processing local command", player_name=player_name, command_data=command_data)
    msg_or_err = _message_from_command(
        command_data,
        player_name,
        strip=True,
        usage="Say what? Usage: local <message> or /l <message>",
        empty_log="Local command with no message",
    )
    if isinstance(msg_or_err, dict):
        return msg_or_err
    logger.debug("Player saying local message", player_name=player_name, message=msg_or_err)
    svc = _require_chat_pair(request, player_name, fail_log="Local command failed")
    if isinstance(svc, dict):
        return svc
    ps, cs = svc

    async def _send(c: ChatCommandsProtocol, pid: object, m: str) -> object:
        return await c.send_local_message(pid, m)

    cfg = _RoomChannelOutcomeConfig(
        success_fmt="You say locally: {0}",
        success_log="Local message sent successfully",
        fail_log="Local command failed",
        err_label="Error sending message: ",
    )
    return await _chat_send_with_room_bundle(command_data, player_name, ps, cs, msg_or_err, _send, cfg)


async def flow_global_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `global` command: server-wide chat when permitted."""
    logger.debug("Processing global command", player_name=player_name, command_data=command_data)
    msg_or_err = _message_from_command(
        command_data,
        player_name,
        strip=True,
        usage="Say what? Usage: global <message> or /g <message>",
        empty_log="Global command with no message",
    )
    if isinstance(msg_or_err, dict):
        return msg_or_err
    logger.debug("Player saying global message", player_name=player_name, message=msg_or_err)
    svc = _require_chat_pair(request, player_name, fail_log="Global command failed")
    if isinstance(svc, dict):
        return svc
    ps, cs = svc
    try:
        bundle = await _global_player_bundle(ps, player_name)
        if isinstance(bundle, str):
            return {"result": bundle}
        player_obj, player_level, player_id = bundle
        logger.debug("Player resolved player_obj", player_name=player_name, player_obj=player_obj)
        result_raw = await cs.send_global_message(player_id, msg_or_err)
        result = chat_result_map(result_raw)
        if result.get("success"):
            logger.info(
                "Global message sent successfully",
                player_name=player_name,
                player_level=player_level,
                message_id=message_id_from_result(result),
            )
            return {"result": f"You say (global): {msg_or_err}"}
        error_msg = _str_error_from_chat_result(result)
        logger.warning("Global command failed", player_name=player_name, error_msg=error_msg)
        return {"result": f"Error sending message: {error_msg}"}
    except (AttributeError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "Global command error",
            player_name=player_name,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error sending message: {_GENERIC_UNEXPECTED_CHAT_FAILURE}"}


def _system_services_triple(
    request: object | None,
    player_name: str,
) -> tuple[PlayerResolutionProtocol, ChatCommandsProtocol, UserManagerProtocol] | dict[str, str]:
    app = app_from_request(request)
    player_service, chat_service, user_manager = get_services_from_container(app)
    if not player_service:
        logger.warning("System command failed - no player service", player_name=player_name)
        return CHAT_UNAVAILABLE
    if not chat_service:
        logger.warning("System command failed - no chat service", player_name=player_name)
        return CHAT_UNAVAILABLE
    if not user_manager:
        logger.warning("System command failed - no user manager", player_name=player_name)
        return ADMIN_UNAVAILABLE
    return player_service, chat_service, user_manager


async def _system_send_if_admin(
    player_service: PlayerResolutionProtocol,
    chat_service: ChatCommandsProtocol,
    user_manager: UserManagerProtocol,
    player_name: str,
    message: str,
) -> dict[str, str]:
    bundle = await _player_id_bundle(player_service, player_name)
    if isinstance(bundle, str):
        return {"result": bundle}
    _, player_id = bundle
    if not user_manager.is_admin(player_id):
        logger.warning("Non-admin player attempted to use system command", player_name=player_name)
        return {"result": "You must be an admin to send system messages."}
    result_raw = await chat_service.send_system_message(player_id, message)
    result = chat_result_map(result_raw)
    if result.get("success"):
        logger.info(
            "System message sent successfully",
            player_name=player_name,
            message_id=message_id_from_result(result),
        )
        return {"result": f"You system: {message}"}
    error_msg = _str_error_from_chat_result(result)
    logger.warning("System command failed", player_name=player_name, error_msg=error_msg)
    return {"result": f"Error sending system message: {error_msg}"}


async def flow_system_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `system` command: admin-only system channel message."""
    logger.debug("Processing system command", player_name=player_name, command_data=command_data)
    msg_or_err = _message_from_command(
        command_data,
        player_name,
        strip=True,
        usage="System what? Usage: system <message>",
        empty_log="System command with no message",
    )
    if isinstance(msg_or_err, dict):
        return msg_or_err
    logger.debug("Player sending system message", player_name=player_name, message=msg_or_err)
    triple = _system_services_triple(request, player_name)
    if isinstance(triple, dict):
        return triple
    ps, cs, um = triple
    try:
        return await _system_send_if_admin(ps, cs, um, player_name, msg_or_err)
    except (AttributeError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "System command error",
            player_name=player_name,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error sending system message: {_GENERIC_UNEXPECTED_CHAT_FAILURE}"}


def _whisper_id_pair_or_error(sender_obj: object, target_obj: object) -> tuple[object, object] | dict[str, str]:
    """Resolve primary IDs for whisper; return error dict if self-whisper or missing ID."""
    sender_id = primary_id(sender_obj)
    target_id = primary_id(target_obj)
    if sender_id is not None and target_id is not None and sender_id == target_id:
        return {"result": "You cannot whisper to yourself"}
    if sender_id is None or target_id is None:
        return {"result": "Player ID not found."}
    return (sender_id, target_id)


async def _deliver_whisper_message(
    ps: PlayerResolutionProtocol,
    cs: ChatCommandsProtocol,
    player_name: str,
    target: str,
    message: str,
) -> dict[str, str]:
    sender_obj = await ps.resolve_player_name(player_name)
    if not sender_obj:
        return {"result": "Player not found."}
    target_obj = await ps.resolve_player_name(target)
    if not target_obj:
        return {"result": "You whisper into the aether."}
    ids = _whisper_id_pair_or_error(sender_obj, target_obj)
    if isinstance(ids, dict):
        return ids
    sender_id, target_id = ids
    result_raw = await cs.send_whisper_message(sender_id, target_id, message)
    result = chat_result_map(result_raw)
    if result.get("success"):
        logger.info(
            "Whisper message sent successfully",
            player_name=player_name,
            target=target,
            message_id=message_id_from_result(result),
        )
        return {"result": f"You whisper to {target}: {message}"}
    error_msg = _str_error_from_chat_result(result)
    logger.warning("Whisper command failed", player_name=player_name, error_msg=error_msg)
    return {"result": f"Error sending whisper: {error_msg}"}


async def flow_whisper_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle `whisper`: send a private message to a named online player."""
    logger.debug("Processing whisper command", player_name=player_name, command_data=command_data)
    target = command_data.get("target")
    message = command_data.get("message")
    if not isinstance(target, str) or not target or not isinstance(message, str) or not message:
        logger.warning(
            "Whisper command with missing target or message",
            player_name=player_name,
            command_data=command_data,
        )
        return {"result": "Say what? Usage: whisper <player> <message>"}
    svc = _require_chat_pair(request, player_name, fail_log="Whisper command failed")
    if isinstance(svc, dict):
        return svc
    ps, cs = svc
    try:
        return await _deliver_whisper_message(ps, cs, player_name, target, message)
    except (AttributeError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "Whisper command error",
            player_name=player_name,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error sending whisper: {_GENERIC_UNEXPECTED_CHAT_FAILURE}"}


async def _deliver_reply_to_last_whisper(
    ps: PlayerResolutionProtocol,
    cs: ChatCommandsProtocol,
    player_name: str,
    message: str,
) -> dict[str, str]:
    sender_obj = await ps.resolve_player_name(player_name)
    if not sender_obj:
        return {"result": "Player not found."}
    last_whisper_sender = cs.get_last_whisper_sender(player_name)
    if not last_whisper_sender:
        return {"result": "No one has whispered to you recently."}
    last_str = last_whisper_sender if isinstance(last_whisper_sender, str) else str(last_whisper_sender)
    target_obj = await ps.resolve_player_name(last_str)
    if not target_obj:
        return {"result": "The player you're trying to reply to is no longer available."}
    sender_id = primary_id(sender_obj)
    target_id = primary_id(target_obj)
    if sender_id is None or target_id is None:
        return {"result": "Player ID not found."}
    result_raw = await cs.send_whisper_message(sender_id, target_id, message)
    result = chat_result_map(result_raw)
    if result.get("success"):
        logger.info(
            "Reply message sent successfully",
            player_name=player_name,
            last_whisper_sender=last_str,
            message_id=message_id_from_result(result),
        )
        return {"result": f"You whisper to {last_str}: {message}"}
    error_msg = _str_error_from_chat_result(result)
    logger.warning("Reply command failed", player_name=player_name, error_msg=error_msg)
    return {"result": f"Error sending reply: {error_msg}"}


async def flow_reply_command(
    command_data: Mapping[str, object],
    request: object | None,
    player_name: str,
) -> dict[str, str]:
    """Handle `reply`: whisper back to the last player who whispered to you."""
    logger.debug("Processing reply command", player_name=player_name, command_data=command_data)
    msg_or_err = _message_from_command(
        command_data,
        player_name,
        strip=False,
        usage="Say what? Usage: reply <message>",
        empty_log="Reply command with no message",
    )
    if isinstance(msg_or_err, dict):
        return msg_or_err
    logger.debug("Player replying to last whisper", player_name=player_name, message=msg_or_err)
    svc = _require_chat_pair(request, player_name, fail_log="Reply command failed")
    if isinstance(svc, dict):
        return svc
    ps, cs = svc
    try:
        return await _deliver_reply_to_last_whisper(ps, cs, player_name, msg_or_err)
    except (AttributeError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "Reply command error",
            player_name=player_name,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error sending reply: {_GENERIC_UNEXPECTED_CHAT_FAILURE}"}
