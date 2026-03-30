"""Unit tests for inventory_command_coercion.coerce_int."""

from __future__ import annotations

import math

import pytest

from server.commands.inventory_command_coercion import coerce_int


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
