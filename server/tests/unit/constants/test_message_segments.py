"""The segment contract: segments always join back to message, and NPC names carry npc.<disposition> (#1025)."""

from server.constants.message_category import MessageCategory
from server.constants.message_segments import (
    join_parts,
    message_with_segments,
    npc_name_segment,
)
from server.constants.npc_disposition import NpcDisposition


def test_npc_name_segment_uses_the_disposition_category() -> None:
    for disposition in NpcDisposition:
        segment = npc_name_segment("Rat", disposition)
        assert segment == {"text": "Rat", "category": f"npc.{disposition.value}"}
        assert MessageCategory(segment.get("category", ""))  # a real category, not just a string


def test_segments_join_back_to_message() -> None:
    parts = ["You attack ", npc_name_segment("Rat", NpcDisposition.AGGRESSIVE_MOB), " for 5 damage."]
    built = message_with_segments(parts)
    assert built["message"] == "You attack Rat for 5 damage."
    assert "".join(segment["text"] for segment in built["segments"]) == built["message"]
    assert built["segments"] == [
        {"text": "You attack "},
        {"text": "Rat", "category": "npc.aggressive_mob"},
        {"text": " for 5 damage."},
    ]


def test_adjacent_plain_strings_merge_and_empties_drop() -> None:
    built = message_with_segments(["a", "b", "", npc_name_segment("Rat", NpcDisposition.PASSIVE_MOB), "", "c"])
    assert built["message"] == "abRatc"
    assert built["segments"] == [
        {"text": "ab"},
        {"text": "Rat", "category": "npc.passive_mob"},
        {"text": "c"},
    ]


def test_name_first_line_has_no_leading_empty_span() -> None:
    built = message_with_segments([npc_name_segment("Rat", NpcDisposition.SHOPKEEPER), " appears."])
    assert built["segments"][0] == {"text": "Rat", "category": "npc.shopkeeper"}
    assert join_parts([npc_name_segment("Rat", NpcDisposition.SHOPKEEPER), " appears."]) == "Rat appears."
