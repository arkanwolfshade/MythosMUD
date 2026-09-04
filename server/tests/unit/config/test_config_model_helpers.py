"""Unit tests for server.config.models._helpers."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from server.config.models import _helpers


def test_parse_list_from_string_json_and_csv() -> None:
    assert _helpers._parse_list_from_string('["a", "b"]') == ["a", "b"]
    assert _helpers._parse_list_from_string("x, y , ,z") == ["x", "y", "z"]


def test_parse_env_list_empty_and_none() -> None:
    assert _helpers._parse_env_list(None) == []
    assert _helpers._parse_env_list("   ") == []


def test_default_cors_origins_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CORS_ALLOW_ORIGINS", "https://a.example,https://b.example")
    assert _helpers._default_cors_origins() == ["https://a.example", "https://b.example"]


def test_default_cors_origins_fallback() -> None:
    with patch.dict("os.environ", {}, clear=True):
        origins = _helpers._default_cors_origins()
    assert "http://localhost:5173" in origins


def test_apply_url_fallback_from_npc_url() -> None:
    data: dict[str, object] = {"npc_url": "postgres://npc"}
    _helpers._apply_url_fallback(data)
    assert data["url"] == "postgres://npc"


def test_apply_url_fallback_keeps_existing_url() -> None:
    data: dict[str, object] = {"url": "postgres://main", "npc_url": "postgres://npc"}
    _helpers._apply_url_fallback(data)
    assert data["url"] == "postgres://main"


def test_apply_url_fallback_from_database_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DATABASE_NPC_URL", "postgres://env_npc")
    data: dict[str, object] = {}
    _helpers._apply_url_fallback(data)
    assert data["url"] == "postgres://env_npc"


def test_validate_tls_files_missing_cert_raises(tmp_path: Path) -> None:
    cert = tmp_path / "cert.pem"
    key = tmp_path / "key.pem"
    cert.write_text("cert", encoding="utf-8")
    config = SimpleNamespace(
        tls_cert_file=str(cert),
        tls_key_file=str(key),
        tls_ca_file=None,
        url="nats://localhost:4222",
    )
    with pytest.raises(ValueError, match="key file not found"):
        _helpers._validate_tls_files_and_maybe_update_url(config)


def test_validate_tls_updates_url_scheme(tmp_path: Path) -> None:
    cert = tmp_path / "cert.pem"
    key = tmp_path / "key.pem"
    cert.write_text("cert", encoding="utf-8")
    key.write_text("key", encoding="utf-8")
    config = SimpleNamespace(
        tls_cert_file=str(cert),
        tls_key_file=str(key),
        tls_ca_file=None,
        url="nats://localhost:4222",
    )
    _helpers._validate_tls_files_and_maybe_update_url(config)
    assert config.url == "tls://localhost:4222"
