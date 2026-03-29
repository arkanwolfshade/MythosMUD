# pyright: reportPrivateUsage=false
# Unit tests intentionally import metrics module-private helpers for direct coverage.
"""Unit tests for server.api.metrics (admin gate, helpers, and key routes)."""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException, Request, status

from server.api.metrics import (
    _get_nats_handler,
    _handle_replay_error,
    _load_dlq_message,
    delete_dlq_message,
    get_dlq_messages,
    get_metrics,
    get_metrics_summary,
    replay_dlq_message,
    reset_circuit_breaker,
    reset_metrics,
    verify_admin_access,
)
from server.exceptions import LoggedHTTPException
from server.models.user import User


def _admin_user() -> MagicMock:
    u: MagicMock = MagicMock(spec=User)
    u.id = uuid.uuid4()
    u.username = "admin"
    u.is_admin = True
    u.is_superuser = False
    return u


def _plain_user() -> MagicMock:
    u: MagicMock = MagicMock(spec=User)
    u.id = uuid.uuid4()
    u.username = "u"
    u.is_admin = False
    u.is_superuser = False
    return u


def test_verify_admin_access_rejects_anonymous() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _ = verify_admin_access(MagicMock(spec=Request), None)
    assert ei.value.status_code == status.HTTP_401_UNAUTHORIZED


def test_verify_admin_access_rejects_non_admin() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _ = verify_admin_access(MagicMock(spec=Request), _plain_user())
    assert ei.value.status_code == status.HTTP_403_FORBIDDEN


def test_verify_admin_access_accepts_admin() -> None:
    u = _admin_user()
    out = verify_admin_access(MagicMock(spec=Request), u)
    assert out is u


def test_get_nats_handler_raises_when_missing() -> None:
    with pytest.raises(HTTPException) as ei:
        _get_nats_handler(None)
    assert ei.value.status_code == status.HTTP_503_SERVICE_UNAVAILABLE


def test_handle_replay_error_returns_failed_payload() -> None:
    u = _admin_user()
    resp = _handle_replay_error(RuntimeError("secret"), "path/to/file", u)
    assert resp.status == "failed"
    assert "Replay failed" in resp.message


@pytest.mark.asyncio
async def test_load_dlq_message_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "nope.json"
    with pytest.raises(HTTPException) as ei:
        _ = await _load_dlq_message(missing)
    assert ei.value.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_load_dlq_message_reads_data_key(tmp_path: Path) -> None:
    p = tmp_path / "e.json"
    _ = p.write_text(json.dumps({"data": {"message_id": "m1", "subject": "s"}}), encoding="utf-8")
    data = await _load_dlq_message(p)
    assert data["message_id"] == "m1"


@pytest.mark.asyncio
async def test_load_dlq_message_accepts_legacy_message_key(tmp_path: Path) -> None:
    p = tmp_path / "legacy.json"
    _ = p.write_text(json.dumps({"message": {"k": 1}}), encoding="utf-8")
    data = await _load_dlq_message(p)
    assert data == {"k": 1}


@pytest.mark.asyncio
async def test_load_dlq_message_rejects_bad_payload(tmp_path: Path) -> None:
    p = tmp_path / "bad.json"
    _ = p.write_text(json.dumps({"data": "not-a-dict"}), encoding="utf-8")
    with pytest.raises(HTTPException) as ei:
        _ = await _load_dlq_message(p)
    assert ei.value.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_metrics_merges_nats_and_handler() -> None:
    base: dict[str, object] = {
        "uptime_seconds": 1.0,
        "messages": cast(dict[str, object], {}),
        "circuit_breaker": cast(
            dict[str, object],
            {"open_count": 0, "recent_state_changes": cast(list[object], [])},
        ),
        "performance": cast(dict[str, object], {}),
        "collection_period": cast(dict[str, object], {"start": "a", "end": "b"}),
    }
    circuit_breaker_m: MagicMock = MagicMock()
    get_stats_m: MagicMock = MagicMock(return_value={"extra": 1})
    circuit_breaker_m.get_stats = get_stats_m
    dlq_m: MagicMock = MagicMock()
    get_dlq_stats_m: MagicMock = MagicMock(return_value={"total_messages": 0})
    dlq_m.get_statistics = get_dlq_stats_m
    handler: MagicMock = MagicMock()
    handler.circuit_breaker = circuit_breaker_m
    handler.dead_letter_queue = dlq_m

    conn_m: MagicMock = MagicMock(return_value={"ok": True})
    subs_m: MagicMock = MagicMock(return_value=["a"])
    mock_ns: MagicMock = MagicMock()
    mock_ns.get_connection_stats = conn_m
    mock_ns.get_active_subscriptions = subs_m

    with (
        patch("server.api.metrics.metrics_collector") as mc_raw,
        patch("server.services.nats_service.nats_service", mock_ns),
    ):
        coll: MagicMock = mc_raw
        get_met: MagicMock = MagicMock(return_value=base)
        coll.get_metrics = get_met
        out = await get_metrics(MagicMock(spec=Request), _admin_user(), handler)
    assert "dead_letter_queue" in out.metrics.model_dump()
    assert out.metrics.nats_connection == {"ok": True}


@pytest.mark.asyncio
async def test_get_metrics_wraps_unexpected_errors() -> None:
    with patch("server.api.metrics.metrics_collector") as mc_raw:
        coll: MagicMock = mc_raw
        get_met: MagicMock = MagicMock(side_effect=RuntimeError("boom"))
        coll.get_metrics = get_met
        with pytest.raises(LoggedHTTPException) as ei:
            _ = await get_metrics(MagicMock(spec=Request), _admin_user(), None)
    assert ei.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


@pytest.mark.asyncio
async def test_get_metrics_summary_adds_dlq_and_circuit() -> None:
    dlq_m: MagicMock = MagicMock()
    get_dlq_stats_m: MagicMock = MagicMock(return_value={"total_messages": 3})
    dlq_m.get_statistics = get_dlq_stats_m
    circuit_breaker_m: MagicMock = MagicMock()
    get_state_m: MagicMock = MagicMock(return_value=MagicMock(value="open"))
    circuit_breaker_m.get_state = get_state_m
    handler: MagicMock = MagicMock()
    handler.dead_letter_queue = dlq_m
    handler.circuit_breaker = circuit_breaker_m
    with patch("server.api.metrics.metrics_collector") as mc_raw:
        coll: MagicMock = mc_raw
        get_sum: MagicMock = MagicMock(return_value={"total_messages": 1})
        coll.get_summary = get_sum
        out = await get_metrics_summary(MagicMock(spec=Request), _admin_user(), handler)
    assert out.dlq_pending == 3
    assert out.circuit_state == "open"


@pytest.mark.asyncio
async def test_reset_metrics_success() -> None:
    with patch("server.api.metrics.metrics_collector") as mc_raw:
        coll: MagicMock = mc_raw
        reset_m: MagicMock = MagicMock()
        coll.reset_metrics = reset_m
        out = await reset_metrics(MagicMock(spec=Request), _admin_user())
        reset_m.assert_called_once()
    assert out.status == "success"


@pytest.mark.asyncio
async def test_get_dlq_messages_empty_when_no_handler() -> None:
    out = await get_dlq_messages(MagicMock(spec=Request), 10, _admin_user(), None)
    assert out.messages == []
    assert out.count == 0


@pytest.mark.asyncio
async def test_reset_circuit_breaker_503_without_handler() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await reset_circuit_breaker(MagicMock(spec=Request), _admin_user(), None)
    assert ei.value.status_code == status.HTTP_503_SERVICE_UNAVAILABLE


@pytest.mark.asyncio
async def test_reset_circuit_breaker_calls_reset() -> None:
    reset_cb: MagicMock = MagicMock()
    circuit_breaker_m: MagicMock = MagicMock()
    circuit_breaker_m.reset = reset_cb
    handler: MagicMock = MagicMock()
    handler.circuit_breaker = circuit_breaker_m
    out = await reset_circuit_breaker(MagicMock(spec=Request), _admin_user(), handler)
    reset_cb.assert_called_once()
    assert out.status == "success"


@pytest.mark.asyncio
async def test_delete_dlq_message_404_when_missing_file(tmp_path: Path) -> None:
    dlq_m: MagicMock = MagicMock()
    dlq_m.storage_dir = tmp_path
    handler: MagicMock = MagicMock()
    handler.dead_letter_queue = dlq_m
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await delete_dlq_message("missing.json", MagicMock(spec=Request), _admin_user(), handler)
    assert ei.value.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_dlq_message_success(tmp_path: Path) -> None:
    delete_msg: MagicMock = MagicMock()
    dlq_m: MagicMock = MagicMock()
    dlq_m.storage_dir = tmp_path
    dlq_m.delete_message = delete_msg
    handler: MagicMock = MagicMock()
    handler.dead_letter_queue = dlq_m
    target = tmp_path / "a.json"
    _ = target.write_text("{}", encoding="utf-8")
    out = await delete_dlq_message("a.json", MagicMock(spec=Request), _admin_user(), handler)
    assert "deleted" in out.message.lower()
    delete_msg.assert_called_once()


@pytest.mark.asyncio
async def test_replay_dlq_message_success_removes_from_dlq(tmp_path: Path) -> None:
    delete_msg: MagicMock = MagicMock()
    dlq_m: MagicMock = MagicMock()
    dlq_m.storage_dir = tmp_path
    dlq_m.delete_message = delete_msg
    handler: MagicMock = MagicMock()
    handler.dead_letter_queue = dlq_m
    rel = "msg.json"
    fp = tmp_path / rel
    _ = fp.write_text(json.dumps({"data": {"message_id": "1"}}), encoding="utf-8")
    handler._process_single_message = AsyncMock()  # noqa: SLF001

    out = await replay_dlq_message(rel, MagicMock(spec=Request), _admin_user(), handler)
    assert out.status == "success"
    delete_msg.assert_called_once()
