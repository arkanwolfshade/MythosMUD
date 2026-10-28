"""The server's MessageCategory enum and the client's TS union must list the same categories."""

import re
from pathlib import Path

from server.constants.message_category import MessageCategory

_TS_UNION = Path(__file__).resolve().parents[4] / "client" / "src" / "types" / "messageCategory.ts"


def test_ts_union_matches_enum() -> None:
    """Drift between the Python enum and the hand-mirrored TS union fails here, not in a player's panel."""
    ts_values = re.findall(r"^\s*\|?\s*'([a-z]+\.[a-z_]+)'", _TS_UNION.read_text(encoding="utf-8"), re.MULTILINE)
    assert sorted(ts_values) == sorted(member.value for member in MessageCategory)


def test_category_names_are_dotted_domain_kind() -> None:
    """The client styles by domain prefix, so every category must be `domain.kind`."""
    assert all(re.fullmatch(r"[a-z]+\.[a-z_]+", member.value) for member in MessageCategory)
