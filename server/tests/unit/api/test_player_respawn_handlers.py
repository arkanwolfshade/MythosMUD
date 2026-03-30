# pyright: reportPrivateUsage=false
# Tests call player_respawn validation helpers that are module-private by convention.
"""Unit tests for server.api.player_respawn validation mappers."""

import uuid
from unittest.mock import MagicMock

import pytest
from fastapi import Request

from server.api.player_respawn import _handle_delirium_respawn_validation_error, _handle_respawn_validation_error
from server.exceptions import LoggedHTTPException, ValidationError


def _user() -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    return u


def test_handle_respawn_validation_not_found() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_respawn_validation_error(ValidationError("Player not found"), MagicMock(spec=Request), _user())
    assert ei.value.status_code == 404


def test_handle_respawn_validation_must_be_dead() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_respawn_validation_error(
            ValidationError("Player must be dead to respawn"),
            MagicMock(spec=Request),
            _user(),
        )
    assert ei.value.status_code == 403


def test_handle_respawn_validation_generic_500() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_respawn_validation_error(ValidationError("other"), MagicMock(spec=Request), _user())
    assert ei.value.status_code == 500


def test_handle_delirium_validation_not_found() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_delirium_respawn_validation_error(
            ValidationError("not found in list"),
            MagicMock(spec=Request),
            _user(),
        )
    assert ei.value.status_code == 404


def test_handle_delirium_validation_must_be_delirious() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_delirium_respawn_validation_error(
            ValidationError("must be delirious"),
            MagicMock(spec=Request),
            _user(),
        )
    assert ei.value.status_code == 403


def test_handle_delirium_validation_lucidity_keyword() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_delirium_respawn_validation_error(
            ValidationError("lucidity too high"),
            MagicMock(spec=Request),
            _user(),
        )
    assert ei.value.status_code == 403


def test_handle_delirium_validation_generic_500() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_delirium_respawn_validation_error(
            ValidationError("unknown failure"),
            MagicMock(spec=Request),
            _user(),
        )
    assert ei.value.status_code == 500
