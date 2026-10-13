"""NPC disposition helpers and the phantom tag (#1025, ADR-024)."""

from unittest.mock import MagicMock, patch

from server.constants.npc_disposition import DEFAULT_NPC_DISPOSITION, NpcDisposition
from server.realtime import connection_utils
from server.realtime.connection_utils import (
    get_npc_disposition_from_instance,
    npc_disposition_from_row,
    npc_disposition_from_type,
    npc_occupant,
)
from server.services.phantom_visibility import get_viewer_phantom_occupants


def test_npc_disposition_from_type_maps_every_definition_type() -> None:
    for disposition in NpcDisposition:
        assert npc_disposition_from_type(disposition.value) is disposition


def test_npc_disposition_from_type_falls_back_to_passive_with_a_warning() -> None:
    with patch.object(connection_utils.logger, "warning") as warning:
        assert npc_disposition_from_type("friendly", "npc_1") is DEFAULT_NPC_DISPOSITION
        assert npc_disposition_from_type(None, "npc_2") is DEFAULT_NPC_DISPOSITION
    assert warning.call_count == 2


def test_npc_disposition_from_row_reads_the_row() -> None:
    assert npc_disposition_from_row({"disposition": "shopkeeper"}) is NpcDisposition.SHOPKEEPER
    assert npc_disposition_from_row({"npc_name": "No tag"}) is DEFAULT_NPC_DISPOSITION


def test_npc_occupant_shape() -> None:
    assert npc_occupant("Rat", NpcDisposition.AGGRESSIVE_MOB) == {"name": "Rat", "disposition": "aggressive_mob"}


def test_get_npc_disposition_from_instance_reads_the_live_npc() -> None:
    npc = MagicMock(npc_type="quest_giver")
    service = MagicMock(lifecycle_manager=MagicMock(active_npcs={"npc_1": npc}))
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=service):
        assert get_npc_disposition_from_instance("npc_1") is NpcDisposition.QUEST_GIVER
        assert get_npc_disposition_from_instance("missing") is DEFAULT_NPC_DISPOSITION


def test_get_npc_disposition_from_instance_defaults_when_service_is_unavailable() -> None:
    with patch("server.services.npc_instance_service.get_npc_instance_service", side_effect=RuntimeError("no service")):
        assert get_npc_disposition_from_instance("npc_1") is DEFAULT_NPC_DISPOSITION


def test_every_phantom_is_tagged_aggressive_mob() -> None:
    """ADR-024: a phantom must carry exactly the tag a real hostile does, whatever its tier or damage."""
    with patch(
        "server.services.phantom_visibility.get_viewer_phantom_names",
        return_value=["Shambling Horror", "Pale Thing"],
    ):
        assert get_viewer_phantom_occupants("viewer", "room_1") == [
            {"name": "Shambling Horror", "disposition": NpcDisposition.AGGRESSIVE_MOB},
            {"name": "Pale Thing", "disposition": NpcDisposition.AGGRESSIVE_MOB},
        ]


def test_no_viewer_means_no_phantoms() -> None:
    assert get_viewer_phantom_occupants(None, "room_1") == []
