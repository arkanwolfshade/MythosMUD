"""Unit tests for server.utils.int_coercion.coerce_int."""

from __future__ import annotations

import math

import pytest

from server.utils.int_coercion import coerce_int


@pytest.mark.parametrize(
    ("value", "default", "expected"),
    [
        (None, 7, 7),
        ("", 2, 2),
        ("   ", 2, 2),
        ("42", 0, 42),
        ("-3", 99, -3),
        ("abc", 5, 5),
        ("12x", 5, 5),
        ("3.14", 5, 5),
    ],
)
def test_coerce_int_string_parsing(value: object, default: int, expected: int) -> None:
    assert coerce_int(value, default=default) == expected


def test_coerce_int_bool_before_int() -> None:
    assert coerce_int(True, default=0) == 1
    assert coerce_int(False, default=0) == 0


def test_coerce_int_plain_int() -> None:
    assert coerce_int(100, default=0) == 100


def test_coerce_int_float() -> None:
    assert coerce_int(3.9, default=0) == 3


def test_coerce_int_float_nan_falls_back_to_default() -> None:
    assert coerce_int(float("nan"), default=11) == 11


def test_coerce_int_float_inf_falls_back_to_default() -> None:
    assert coerce_int(math.inf, default=11) == 11


def test_coerce_int_unknown_type() -> None:
    assert coerce_int([1], default=9) == 9


def test_stats_int_delegates_to_coerce_int() -> None:
    """JSONB stats use the same coercion as inventory command payloads."""
    from server.models.player import _stats_int

    assert _stats_int({"x": float("nan")}, "x", default=11) == 11
    assert _stats_int({"x": 3.9}, "x", default=0) == 3
    assert _stats_int({}, "missing", default=5) == 5
