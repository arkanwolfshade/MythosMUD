"""
Contracts and helpers for admin set-stat command.

Split from admin_setstat_command to keep handler module file-nloc within tooling limits.
"""

# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings
# pylint: disable=too-many-return-statements  # Reason: Validation helpers return early for each invalid input case

from __future__ import annotations

import math
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Protocol, cast

from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

__all__ = [
    "AdminSetStatApplyContext",
    "AdminSetStatLogContext",
    "AdminSetStatNotifyContext",
    "STAT_NAME_MAPPING",
    "SetStatApp",
    "SetStatConnectionManager",
    "SetStatRequest",
    "SetStatTargetPlayer",
    "build_set_stat_error_response",
    "calculate_stat_warnings",
    "get_app_or_error",
    "log_admin_set_stat",
    "parse_set_stat_args",
    "resolve_admin_services_and_permissions",
    "stat_change_notification_text",
    "target_player_uuid",
    "validate_set_stat_inputs",
]


class SetStatConnectionManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Realtime connection manager surface for set-stat notifications."""

    sequence_counter: int

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, object]) -> object: ...


class SetStatAppState(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """FastAPI app.state fields required by admin set-stat."""

    connection_manager: SetStatConnectionManager | None
    user_manager: object | None
    player_service: object | None
    persistence: object | None


class SetStatApp(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """FastAPI app surface with typed state for set-stat."""

    state: SetStatAppState


class SetStatRequest(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Request surface exposing the app instance."""

    @property
    def app(self) -> object: ...


class ResolvedAdminPlayer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player identity returned by admin name resolution."""

    id: uuid.UUID | str


class SetStatTargetPlayer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Target player mutable for admin stat changes."""

    player_id: uuid.UUID | str
    name: str
    current_room_id: str | None

    def get_stats(self) -> dict[str, object]: ...

    def set_stats(self, stats: dict[str, object]) -> None: ...

    def apply_dp_change(self, new_dp: int) -> tuple[int, bool, bool]: ...


class SetStatUserManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """User manager surface for admin privilege checks."""

    async def is_admin(self, player_id: uuid.UUID | str) -> bool: ...


class SetStatPlayerService(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player service surface for resolving display names."""

    async def resolve_player_name(self, player_name: str) -> ResolvedAdminPlayer | None: ...


class SetStatPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Persistence surface for loading and saving set-stat targets."""

    async def get_player_by_name(self, name: str) -> SetStatTargetPlayer | None: ...

    async def save_player(self, player: SetStatTargetPlayer) -> None: ...


@dataclass(frozen=True)
class AdminSetStatLogContext:
    """Context for logging an admin set-stat command (reduces parameter count)."""

    stat_name_input: str
    target_player: str
    value_input: str | int | None
    target_player_obj: SetStatTargetPlayer | None
    stat_key: str
    old_value: object
    value: int


@dataclass(frozen=True)
class AdminSetStatApplyContext:
    """Context for applying an admin set-stat change (reduces parameter count)."""

    app: SetStatApp
    persistence: SetStatPersistence
    target_player_obj: SetStatTargetPlayer
    stat_name_input: str
    target_player: str
    stat_key: str
    value: int
    value_input: str | int | None
    player_name: str


@dataclass(frozen=True)
class AdminSetStatNotifyContext:
    """Context for notifying a player about an admin set-stat change."""

    app: SetStatApp
    target_player_obj: SetStatTargetPlayer
    stat_name_input: str
    old_value: object
    value: int
    warning_message: str
    range_warning: str
    stat_key: str
    previous_position: str | None = None


STAT_NAME_MAPPING: dict[str, str] = {
    "STR": "strength",
    "CON": "constitution",
    "INT": "intelligence",
    "EDU": "education",
    "LUCK": "luck",
    "DEX": "dexterity",
    "SIZ": "size",
    "POW": "power",
    "CHA": "charisma",
    "DP": "current_dp",
    "MP": "magic_points",
    "LCD": "lucidity",
    "str": "strength",
    "con": "constitution",
    "int": "intelligence",
    "edu": "education",
    "luck": "luck",
    "dex": "dexterity",
    "siz": "size",
    "pow": "power",
    "cha": "charisma",
    "dp": "current_dp",
    "mp": "magic_points",
    "lcd": "lucidity",
    "strength": "strength",
    "constitution": "constitution",
    "intelligence": "intelligence",
    "education": "education",
    "dexterity": "dexterity",
    "power": "power",
    "charisma": "charisma",
    "current_dp": "current_dp",
    "magic_points": "magic_points",
    "lucidity": "lucidity",
    "occult": "occult",
    "corruption": "corruption",
    "Occult": "occult",
    "Corruption": "corruption",
}

_PRIMARY_STATS = frozenset(
    {"strength", "dexterity", "constitution", "size", "intelligence", "power", "education", "charisma", "luck"}
)
_OCCULT_RANGE_STATS = frozenset({"occult", "corruption", "lucidity"})


def _as_int(value: object, default: int) -> int:
    """Coerce stats JSON values to int without accepting bool as int."""
    if isinstance(value, bool) or value is None:
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _optional_str(value: object | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return str(value)


def _optional_str_or_int(value: object | None) -> str | int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return value
    return str(value)


def _args_as_strings(raw_args: object) -> list[str]:
    if not isinstance(raw_args, list):
        return []
    return [str(item) for item in cast(list[object], raw_args)]


def _parse_value_from_args(value_input: str | int | None, args: list[str]) -> str | int | None:
    """Parse value from args[2] when value_input is None and args has at least 3 elements."""
    if value_input is not None or len(args) < 3:
        return value_input
    try:
        return int(args[2])
    except (ValueError, TypeError):
        return args[2]


def parse_set_stat_args(command_data: Mapping[str, object]) -> tuple[str | None, str | None, str | int | None]:
    """Parse stat name, target player, and value from command data."""
    args = _args_as_strings(command_data.get("args", []))
    stat_name_input = _optional_str(command_data.get("stat_name"))
    target_player = _optional_str(command_data.get("target_player")) or _optional_str(command_data.get("target_name"))
    value_input = _optional_str_or_int(command_data.get("value"))

    if not stat_name_input and len(args) >= 1:
        stat_name_input = args[0]
    if not target_player and len(args) >= 2:
        target_player = args[1]
    value_input = _parse_value_from_args(value_input, args)

    return stat_name_input, target_player, value_input


def validate_set_stat_inputs(
    stat_name_input: str | None, target_player: str | None, value_input: str | int | None, player_name: str
) -> tuple[str, int] | dict[str, str]:
    """Validate stat name and value inputs."""
    if not stat_name_input:
        logger.warning("Admin set command with no stat name", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    if not target_player:
        logger.warning("Admin set command with no target player", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    if value_input is None:
        logger.warning("Admin set command with no value", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    stat_name_lower = stat_name_input.lower()
    stat_key = STAT_NAME_MAPPING.get(stat_name_input) or STAT_NAME_MAPPING.get(stat_name_lower)

    if not stat_key:
        logger.warning("Admin set command with invalid stat name", player_name=player_name, stat_name=stat_name_input)
        valid_stats = ", ".join(sorted(set(STAT_NAME_MAPPING.values())))
        return {
            "result": (
                f"Invalid stat name '{stat_name_input}'. Valid stats: {valid_stats}\n"
                "Usage: admin set <stat_name> <target_player> <value>"
            )
        }

    try:
        value = int(value_input)
    except (ValueError, TypeError):
        logger.warning("Admin set command with invalid value", player_name=player_name, value=value_input)
        return {"result": f"Invalid value '{value_input}'. Value must be an integer."}

    return stat_key, value


def _warning_for_cap_stat(stat_key: str, value: int, stats: Mapping[str, object]) -> str:
    """Return warning message if value exceeds DP or MP calculated maximum; else empty string."""
    if stat_key == "current_dp":
        con = _as_int(stats.get("constitution", 50), 50)
        siz = _as_int(stats.get("size", 50), 50)
        max_dp = (con + siz) // 5
        if value > max_dp:
            return f" Warning: DP value {value} exceeds calculated maximum {max_dp} (based on CON {con} + SIZ {siz})."
    elif stat_key == "magic_points":
        pow_val = _as_int(stats.get("power", 50), 50)
        max_mp = math.ceil(pow_val * 0.2)
        if value > max_mp:
            return f" Warning: MP value {value} exceeds calculated maximum {max_mp} (based on POW {pow_val})."
    return ""


def _warning_for_stat_range(stat_key: str, value: int) -> str:
    """Return warning message if value is outside normal range for stat; else empty string."""
    if stat_key in _PRIMARY_STATS:
        if value < 1 or value > 100:
            return f" Warning: {stat_key} value {value} is outside normal range (1-100)."
    elif stat_key in _OCCULT_RANGE_STATS:
        if value < 0 or value > 100:
            return f" Warning: {stat_key} value {value} is outside normal range (0-100)."
    return ""


def calculate_stat_warnings(stat_key: str, value: int, stats: Mapping[str, object]) -> tuple[str, str]:
    """Calculate warnings for stat values that exceed maximums or normal ranges."""
    return _warning_for_cap_stat(stat_key, value, stats), _warning_for_stat_range(stat_key, value)


def target_player_uuid(target_player_obj: SetStatTargetPlayer) -> uuid.UUID | None:
    raw_id: object | None = getattr(target_player_obj, "player_id", None)
    if raw_id is None:
        raw_id = getattr(target_player_obj, "id", None)
    if raw_id is None:
        return None
    if isinstance(raw_id, uuid.UUID):
        return raw_id
    if isinstance(raw_id, str):
        return uuid.UUID(raw_id)
    return uuid.UUID(str(raw_id))


def stat_change_notification_text(
    stat_name_input: str, old_value: object, value: int, warning_message: str, range_warning: str
) -> str:
    message = f"An administrator has set your {stat_name_input} from {old_value} to {value}."
    return message + warning_message + range_warning


async def resolve_admin_services_and_permissions(
    app: SetStatApp, player_name: str, target_player: str
) -> tuple[SetStatPersistence, SetStatTargetPlayer] | dict[str, str]:
    """Resolve required services and check admin permissions."""
    user_manager_raw = app.state.user_manager
    if user_manager_raw is None:
        logger.warning("Admin set command failed - no user manager", player_name=player_name)
        return {"result": "Admin set functionality is not available."}
    user_manager = cast(SetStatUserManager, user_manager_raw)

    player_service_raw = app.state.player_service
    if player_service_raw is None:
        return {"result": "Player service not available."}
    player_service = cast(SetStatPlayerService, player_service_raw)

    persistence_raw = app.state.persistence
    if persistence_raw is None:
        return {"result": "Persistence layer not available."}
    persistence = cast(SetStatPersistence, persistence_raw)

    current_player_obj = await player_service.resolve_player_name(player_name)
    if not current_player_obj:
        return {"result": "Current player not found."}

    current_user_id = str(current_player_obj.id)
    if not await user_manager.is_admin(current_user_id):
        logger.debug("Admin set command denied - not admin", player_name=player_name)
        return {"result": "You do not have permission to use this command."}

    target_player_obj = await persistence.get_player_by_name(target_player)
    if not target_player_obj:
        return {"result": f"Player '{target_player}' not found."}

    return persistence, target_player_obj


def log_admin_set_stat(
    player_name: str,
    ctx: AdminSetStatLogContext,
    success: bool = True,
    error: str | None = None,
) -> None:
    """Log admin set stat command."""
    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_admin_command(
            admin_name=player_name,
            command=f"admin set {ctx.stat_name_input} {ctx.target_player} {ctx.value_input}",
            success=success,
            additional_data={
                "target_player": ctx.target_player,
                "target_player_id": str(ctx.target_player_obj.player_id) if ctx.target_player_obj else None,
                "stat_name": ctx.stat_key,
                "old_value": ctx.old_value,
                "new_value": ctx.value,
                "error": error,
                "error_type": type(error).__name__ if error else None,
            }
            if success
            else {"error": str(error), "error_type": type(error).__name__ if error else None},
        )
    except (OSError, AttributeError, TypeError) as log_exc:
        logger.warning("Failed to log admin set command", player_name=player_name, error=str(log_exc))


def build_set_stat_error_response(
    player_name: str,
    stat_name_input: str | None,
    target_player: str | None,
    value_input: str | int | None,
    error: BaseException,
) -> dict[str, str]:
    """Log error and admin action failure, return error result dict."""
    stat_s = stat_name_input or "unknown"
    target_s = target_player or "unknown"
    logger.error(
        "Admin set command error",
        admin_name=player_name,
        target_player=target_s,
        stat_name=stat_s,
        error=str(error),
        error_type=type(error).__name__,
    )
    log_admin_set_stat(
        player_name,
        AdminSetStatLogContext(stat_s, target_s, value_input, None, "", None, 0),
        success=False,
        error=str(error),
    )
    return {"result": f"Error setting {stat_s} for {target_s}: {str(error)}"}


def get_app_or_error(
    request: SetStatRequest | None, player_name: str
) -> tuple[SetStatApp | None, dict[str, str] | None]:
    """Return (app, None) if request has app, else (None, error_dict)."""
    if request is None:
        return None, {"result": "Admin set functionality is not available."}
    app_raw = getattr(request, "app", None)
    if app_raw is None:
        logger.warning("Admin set command failed - no application context", player_name=player_name)
        return None, {"result": "Admin set functionality is not available."}
    return cast(SetStatApp, app_raw), None
