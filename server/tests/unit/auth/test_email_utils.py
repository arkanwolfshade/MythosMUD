"""Unit tests for auth email utilities."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.auth.email_utils import (
    generate_unique_bogus_email,
    is_bogus_email,
    validate_bogus_email_format,
)


def test_is_bogus_email() -> None:
    assert is_bogus_email("user@wolfshade.org") is True
    assert is_bogus_email("user@gmail.com") is False


def test_validate_bogus_email_format_rejects_non_bogus() -> None:
    assert validate_bogus_email_format("user@gmail.com") is False


def test_validate_bogus_email_format_accepts_valid() -> None:
    assert validate_bogus_email_format("player.one@wolfshade.org") is True


def test_validate_bogus_email_format_rejects_bad_local() -> None:
    assert validate_bogus_email_format("bad space@wolfshade.org") is False
    assert validate_bogus_email_format("@wolfshade.org") is False


@pytest.mark.asyncio
async def test_generate_unique_bogus_email_base_available() -> None:
    session = AsyncMock()
    result = MagicMock()
    result.scalar_one_or_none.return_value = None
    session.execute.return_value = result
    email = await generate_unique_bogus_email("TestUser", session)
    assert email == "testuser@wolfshade.org"


@pytest.mark.asyncio
async def test_generate_unique_bogus_email_adds_suffix_when_taken() -> None:
    session = AsyncMock()
    taken = MagicMock()
    free = MagicMock()
    taken.scalar_one_or_none.side_effect = [MagicMock(), None]
    free.scalar_one_or_none.return_value = None
    session.execute.side_effect = [taken, free]
    email = await generate_unique_bogus_email("dup", session)
    assert email.endswith("@wolfshade.org")
    assert email.startswith("dup.")


@pytest.mark.asyncio
async def test_generate_unique_bogus_email_full_uuid_collision() -> None:
    session = AsyncMock()
    always_taken = MagicMock()
    always_taken.scalar_one_or_none.return_value = MagicMock()
    session.execute.return_value = always_taken
    email = await generate_unique_bogus_email("x", session)
    assert email.endswith("@wolfshade.org")
    assert email.count(".") >= 1
