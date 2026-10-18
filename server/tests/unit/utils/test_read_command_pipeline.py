"""`read <item>` keeps its arguments all the way from the typed line to the handler's command_data.

Regression: the parser built a bare ReadCommand and discarded the arguments, so ``handle_read_command`` always saw an
empty ``args`` and answered "Usage: /read <item_name> [spell_name]" for every real ``read``. The handler's own tests
passed because they hand-build ``command_data``; this runs a real command line through the real pipeline.
"""

from __future__ import annotations

import pytest

from server.utils.command_processor import CommandProcessor


@pytest.mark.parametrize(
    ("line", "expected_args"),
    [
        ("read advertiser", ["advertiser"]),
        ("read arkham advertiser", ["arkham", "advertiser"]),
        ("read spellbook fireball", ["spellbook", "fireball"]),
    ],
)
def test_read_arguments_reach_command_data(line: str, expected_args: list[str]) -> None:
    processor = CommandProcessor()

    validated, error, command_type = processor.process_command_string(line, "Tester")

    assert error is None
    assert command_type == "read"
    assert validated is not None
    assert processor.extract_command_data(validated)["args"] == expected_args


def test_a_bare_read_still_reaches_the_handlers_usage_message() -> None:
    processor = CommandProcessor()

    validated, error, _ = processor.process_command_string("read", "Tester")

    assert error is None
    assert validated is not None
    assert processor.extract_command_data(validated)["args"] == []
