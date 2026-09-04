"""Unit tests for NATSMessageHandlerMixinBase stubs."""

from __future__ import annotations

import pytest

from server.realtime.nats_message_handler_base import NATSMessageHandlerMixinBase


class _Handler(NATSMessageHandlerMixinBase):
    """Concrete subclass for testing mixin stubs."""


@pytest.mark.asyncio
async def test_subscribe_stub_returns_false() -> None:
    handler = _Handler()
    assert await handler._subscribe_to_subject("room.events") is False


@pytest.mark.asyncio
async def test_unsubscribe_stub_returns_false() -> None:
    handler = _Handler()
    assert await handler._unsubscribe_from_subject("room.events") is False
