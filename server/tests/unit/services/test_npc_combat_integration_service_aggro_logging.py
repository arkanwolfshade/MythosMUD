"""Log-level tests for NPCCombatIntegrationService.handle_npc_attack_on_player.

Expected combat contention must not be logged as an error. These tests assert the log level
directly; checking only the False return value cannot tell a routine skip from the error branch,
since both return False.
"""

# pyright: reportPrivateUsage=false
# Replacing the underscore-prefixed combat collaborator is how these tests isolate the handler.

from typing import TYPE_CHECKING

import pytest

from server.services import npc_combat_integration_service as integration_module

from .test_npc_combat_integration_service import (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)

if TYPE_CHECKING:
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService

# pylint: disable=redefined-outer-name  # pytest injects fixtures by parameter name

# Pytest registers imported @pytest.fixture callables; the tuple keeps the imports "used".
_PYTEST_SERVICE_FIXTURES: tuple[object, ...] = (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)


class _RecordingLogger:
    """Typed stand-in that records (level, event) for each log call."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []

    def debug(self, event: str, **_fields: object) -> None:
        """Record a debug call."""
        self.calls.append(("debug", event))

    def info(self, event: str, **_fields: object) -> None:
        """Record an info call."""
        self.calls.append(("info", event))

    def warning(self, event: str, **_fields: object) -> None:
        """Record a warning call."""
        self.calls.append(("warning", event))

    def error(self, event: str, **_fields: object) -> None:
        """Record an error call."""
        self.calls.append(("error", event))

    def levels(self) -> list[str]:
        """Levels logged, in order."""
        return [level for level, _ in self.calls]


async def _attack_raising(
    service: "NPCCombatIntegrationService", monkeypatch: pytest.MonkeyPatch, message: str
) -> tuple[bool, _RecordingLogger]:
    recorder = _RecordingLogger()
    monkeypatch.setattr(integration_module, "logger", recorder)

    def not_in_login_grace(_player_uuid: object) -> bool:
        return False

    monkeypatch.setattr(integration_module, "is_npc_attack_on_player_blocked_by_login_grace_period", not_in_login_grace)

    async def raise_from_combat_path(*_args: object, **_kwargs: object) -> bool:
        raise ValueError(message)

    monkeypatch.setattr(service, "_run_npc_attack_on_player_after_grace", raise_from_combat_path)
    result = await service.handle_npc_attack_on_player(
        npc_id="npc_001",
        target_id="00000000-0000-0000-0000-000000000001",
        room_id="room_1",
        attack_damage=10,
    )
    return result, recorder


@pytest.mark.asyncio
async def test_already_in_combat_is_a_debug_skip_not_an_error(
    integration_service: "NPCCombatIntegrationService", monkeypatch: pytest.MonkeyPatch
) -> None:
    """Regression: a second aggressive NPC refused because the player is already fighting.

    validate_combat_can_start raises this whenever a participant is already in a combat, which is
    routine when several aggressive NPCs share a room. It used to be logged at ERROR on every
    aggro attempt.
    """
    result, recorder = await _attack_raising(
        integration_service, monkeypatch, "One or both participants are already in combat"
    )

    assert result is False
    assert recorder.levels() == ["debug"]


@pytest.mark.asyncio
async def test_already_dead_is_a_debug_skip_not_an_error(
    integration_service: "NPCCombatIntegrationService", monkeypatch: pytest.MonkeyPatch
) -> None:
    """The pre-existing sibling case: attacking an already-dead player is also a routine skip."""
    result, recorder = await _attack_raising(integration_service, monkeypatch, "Target is already dead")

    assert result is False
    assert recorder.levels() == ["debug"]


@pytest.mark.asyncio
async def test_unexpected_value_error_is_still_logged_as_error(
    integration_service: "NPCCombatIntegrationService", monkeypatch: pytest.MonkeyPatch
) -> None:
    """Narrowing the skip must not swallow genuine failures from the combat path."""
    result, recorder = await _attack_raising(integration_service, monkeypatch, "Target is not in this combat")

    assert result is False
    assert recorder.levels() == ["error"]
