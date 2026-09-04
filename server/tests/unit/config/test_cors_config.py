"""Unit tests for CORS configuration parsing."""

import pytest

from server.config.models.cors import CORSConfig


def test_cors_defaults_include_local_dev_origins() -> None:
    config = CORSConfig()
    assert "http://localhost:5173" in config.allow_origins
    assert config.allow_credentials is True


def test_cors_parse_allow_origins_from_comma_separated_string() -> None:
    config = CORSConfig(allow_origins="https://a.example, https://b.example")
    assert config.allow_origins == ["https://a.example", "https://b.example"]


def test_cors_parse_allow_origins_from_json_array() -> None:
    config = CORSConfig(allow_origins='["https://json.example"]')
    assert config.allow_origins == ["https://json.example"]


def test_cors_parse_allow_methods_uppercases() -> None:
    config = CORSConfig(allow_methods="get, post")
    assert config.allow_methods == ["GET", "POST"]


def test_cors_parse_max_age_from_string() -> None:
    config = CORSConfig(max_age="120")
    assert config.max_age == 120


def test_cors_parse_max_age_invalid_string_uses_default() -> None:
    config = CORSConfig(max_age="not-a-number")
    assert config.max_age == 600


def test_cors_rejects_negative_max_age() -> None:
    with pytest.raises(ValueError, match="max_age"):
        CORSConfig(max_age=-1)


def test_cors_parse_expose_headers_allows_empty() -> None:
    config = CORSConfig(expose_headers="")
    assert config.expose_headers == []


def test_cors_rejects_empty_allow_origins() -> None:
    with pytest.raises(ValueError, match="At least one entry"):
        CORSConfig(allow_origins="")


def test_cors_wildcard_origin_accepted() -> None:
    config = CORSConfig(allow_origins="*")
    assert config.allow_origins == ["*"]
