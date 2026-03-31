"""
Typed helpers and Protocols for communication command handlers.

Split from communication_commands to keep handler module size and complexity
within tooling limits without changing runtime behavior.
"""

# pylint: disable=missing-function-docstring
# Protocol method stubs intentionally omit per-method docstrings; contracts are in class docstrings.

from collections.abc import Mapping
from typing import Protocol, cast


class PlayerResolutionProtocol(Protocol):  # pylint: disable=too-few-public-methods
    """Resolve display names to player objects for chat and command routing."""

    async def resolve_player_name(self, name: str) -> object | None: ...


class ChatCommandsProtocol(Protocol):
    """Chat service (say, local, global, system, whisper, reply metadata)."""

    async def send_say_message(self, player_id: object, message: object) -> object: ...

    async def send_local_message(self, player_id: object, message: object) -> object: ...

    async def send_global_message(self, player_id: object, message: object) -> object: ...

    async def send_system_message(self, player_id: object, message: object) -> object: ...

    async def send_whisper_message(self, sender_id: object, target_id: object, message: object) -> object: ...

    def get_last_whisper_sender(self, player_name: str) -> object | None: ...


class UserManagerProtocol(Protocol):  # pylint: disable=too-few-public-methods
    """User/role checks (e.g. admin) for gated chat commands."""

    def is_admin(self, player_id: object) -> bool: ...


class AsyncPersistenceForPose(Protocol):  # pylint: disable=too-few-public-methods
    """Minimal persistence for pose read/write in emote/pose flows."""

    async def get_player_by_name(self, name: str) -> object | None: ...

    async def save_player(self, player: object) -> object: ...


class PlayerWithPose(Protocol):  # pylint: disable=too-few-public-methods
    """Player-like object exposing an optional ``pose`` string (structural typing)."""

    pose: object | None


def app_from_request(request: object | None) -> object | None:
    """Return ``request.app`` if present, else None."""
    if request is None:
        return None
    return cast(object | None, getattr(request, "app", None))


def primary_id(entity: object) -> object | None:
    """Resolve id or player_id from a player-like object without propagating Any."""
    left = cast(object | None, getattr(entity, "id", None))
    if left is not None:
        return left
    return cast(object | None, getattr(entity, "player_id", None))


def get_services_from_container(
    app: object | None,
) -> tuple[
    PlayerResolutionProtocol | None,
    ChatCommandsProtocol | None,
    UserManagerProtocol | None,
]:
    """
    Get services from container with backward compatibility fallback.

    Args:
        app: FastAPI app instance (or any ASGI app exposing state / container).

    Returns:
        Tuple of (player_service, chat_service, user_manager)
    """
    if app is None:
        return None, None, None

    state_raw = getattr(app, "state", None)
    if state_raw is None:
        return None, None, None
    state: object = cast(object, state_raw)

    container_raw = getattr(state, "container", None)
    if container_raw:
        container: object = cast(object, container_raw)
        return (
            cast(PlayerResolutionProtocol | None, getattr(container, "player_service", None)),
            cast(ChatCommandsProtocol | None, getattr(container, "chat_service", None)),
            cast(UserManagerProtocol | None, getattr(container, "user_manager", None)),
        )

    return (
        cast(PlayerResolutionProtocol | None, getattr(state, "player_service", None)),
        cast(ChatCommandsProtocol | None, getattr(state, "chat_service", None)),
        cast(UserManagerProtocol | None, getattr(state, "user_manager", None)),
    )


def get_pose_persistence(app: object | None) -> AsyncPersistenceForPose | None:
    """Resolve async persistence from app state or container for pose commands."""
    if app is None:
        return None
    state_raw = getattr(app, "state", None)
    if state_raw is None:
        return None
    state: object = cast(object, state_raw)
    container_raw = getattr(state, "container", None)
    if container_raw:
        container: object = cast(object, container_raw)
        ap = getattr(container, "async_persistence", None)
        if ap is not None:
            return cast(AsyncPersistenceForPose, ap)
    persistence = getattr(state, "persistence", None)
    if persistence is not None:
        return cast(AsyncPersistenceForPose, persistence)
    return None


def chat_result_map(result: object) -> Mapping[str, object]:
    """Normalize chat service return values to a string-keyed mapping."""
    if isinstance(result, dict):
        return cast(Mapping[str, object], result)
    return cast(Mapping[str, object], {})


def message_id_from_result(result: Mapping[str, object]) -> object | None:
    """Extract nested message id from a chat result payload, if present."""
    inner = result.get("message")
    if isinstance(inner, dict):
        inner_map = cast(Mapping[str, object], inner)
        return inner_map.get("id")
    return None
