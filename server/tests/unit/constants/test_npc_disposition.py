"""NpcDisposition must stay in step with NPCDefinitionType and with the npc.* message categories (#1025)."""

from server.constants.message_category import MessageCategory
from server.constants.npc_disposition import NpcDisposition
from server.models.npc import NPCDefinitionType


def test_dispositions_mirror_npc_definition_types() -> None:
    """The wire vocabulary is the definition type, word for word, so deriving one needs no translation table."""
    assert sorted(d.value for d in NpcDisposition) == sorted(t.value for t in NPCDefinitionType)


def test_every_disposition_has_an_npc_category() -> None:
    """The client colours an NPC through ``npc.<disposition>``; a disposition without one would render unstyled."""
    npc_categories = {member.value for member in MessageCategory if member.value.startswith("npc.")}
    assert npc_categories == {f"npc.{d.value}" for d in NpcDisposition}
