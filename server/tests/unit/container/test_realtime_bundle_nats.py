"""RealtimeBundle NATS connect policy: e2e hard-fails; soft fail only for non-e2e."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.container.bundles.realtime import RealtimeBundle


def _config(*, environment: str, nats_enabled: bool = True) -> Any:
    return SimpleNamespace(
        logging=SimpleNamespace(environment=environment),
        nats=SimpleNamespace(
            enabled=nats_enabled,
            connect_timeout=1,
            url="nats://localhost:4222",
        ),
    )


@pytest.mark.asyncio
async def test_connect_nats_e2e_raises_when_connect_returns_false() -> None:
    """e2e_test must not soft-mock missing NATS (avoids silent chat failures in Playwright)."""
    bundle = RealtimeBundle()
    event_bus: MagicMock = MagicMock()
    mock_service: MagicMock = MagicMock()
    mock_service.connect = AsyncMock(return_value=False)

    with patch("server.services.nats_service.NATSService", return_value=mock_service):
        with pytest.raises(RuntimeError, match="NATS is mandatory"):
            await bundle._connect_nats(_config(environment="e2e_test"), event_bus)


@pytest.mark.asyncio
async def test_connect_nats_e2e_raises_on_timeout() -> None:
    """e2e_test hard-fails when NATS connect times out (e.g. TLS mismatch)."""
    bundle = RealtimeBundle()
    event_bus: MagicMock = MagicMock()
    mock_service: MagicMock = MagicMock()
    mock_service.connect = AsyncMock(side_effect=TimeoutError())

    with patch("server.services.nats_service.NATSService", return_value=mock_service):
        with pytest.raises(RuntimeError, match="NATS is mandatory"):
            await bundle._connect_nats(_config(environment="e2e_test"), event_bus)


@pytest.mark.asyncio
async def test_connect_nats_local_continues_without_nats_on_timeout() -> None:
    """Non-e2e local may soft-continue without NATS when connect fails."""
    bundle = RealtimeBundle()
    event_bus: MagicMock = MagicMock()
    mock_service: MagicMock = MagicMock()
    mock_service.connect = AsyncMock(side_effect=TimeoutError())

    with patch("server.services.nats_service.NATSService", return_value=mock_service):
        result = await bundle._connect_nats(_config(environment="local"), event_bus)
    assert result is None


@pytest.mark.asyncio
async def test_handle_nats_unavailable_unit_test_soft() -> None:
    """unit_test combat path still soft-mocks unavailable NATS."""
    from server.container.bundles.combat import CombatBundle

    combat = CombatBundle()
    combat.combat_service = MagicMock()
    combat._handle_nats_unavailable(is_testing=True)
    assert combat.combat_service is None


def test_handle_nats_unavailable_e2e_raises() -> None:
    """e2e_test combat path raises when NATS is unavailable (is_testing=False)."""
    from server.container.bundles.combat import CombatBundle

    combat = CombatBundle()
    with pytest.raises(RuntimeError, match="NATS is mandatory"):
        combat._handle_nats_unavailable(is_testing=False)
