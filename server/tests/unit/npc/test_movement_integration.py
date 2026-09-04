"""Unit tests for NPC movement integration."""

from unittest.mock import MagicMock, patch

import pytest

from server.npc.movement_integration import NPCMovementIntegration


@pytest.fixture
def persistence() -> MagicMock:
    return MagicMock()


def test_init_requires_persistence() -> None:
    with pytest.raises(ValueError, match="persistence"):
        NPCMovementIntegration(event_bus=None, persistence=None)


def test_validate_room_ids_rejects_empty_or_same(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration._validate_room_ids("npc-1", "", "room-b") is False
    assert integration._validate_room_ids("npc-1", "room-a", "room-a") is False
    assert integration._validate_room_ids("npc-1", "room-a", "room-b") is True


def test_move_npc_to_room_success(persistence: MagicMock) -> None:
    from_room = MagicMock()
    to_room = MagicMock()
    from_room.has_npc.return_value = True
    to_room.has_npc.return_value = False
    persistence.get_room_by_id.side_effect = [from_room, to_room]
    integration = NPCMovementIntegration(event_bus=MagicMock(), persistence=persistence)
    with patch.object(integration, "_is_npc_in_combat", return_value=False):
        assert integration.move_npc_to_room("npc-1", "room-a", "room-b") is True
    from_room.npc_left.assert_called_once()
    to_room.npc_entered.assert_called_once()


def test_move_npc_blocked_in_combat(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    with patch.object(integration, "_is_npc_in_combat", return_value=True):
        assert integration.move_npc_to_room("npc-1", "room-a", "room-b") is False


def test_get_room_objects_missing_room(persistence: MagicMock) -> None:
    persistence.get_room_by_id.return_value = None
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration._get_room_objects("npc-1", "room-a", "room-b") is None


def test_validate_npc_movement(persistence: MagicMock) -> None:
    from_room = MagicMock()
    to_room = MagicMock()
    from_room.has_npc.return_value = True
    persistence.get_room_by_id.side_effect = [from_room, to_room]
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.validate_npc_movement("npc-1", "room-a", "room-b") is True


def test_get_room_npcs_and_exits(persistence: MagicMock) -> None:
    room = MagicMock()
    room.get_npcs.return_value = ["npc-1"]
    room.exits = {"north": "room-n"}
    persistence.get_room_by_id.return_value = room
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.get_room_npcs("room-a") == ["npc-1"]
    assert integration.get_available_exits("room-a") == {"north": "room-n"}


def test_find_path_direct_connection(persistence: MagicMock) -> None:
    room = MagicMock()
    room.exits = {"east": "room-b"}
    persistence.get_room_by_id.return_value = room
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.find_path_between_rooms("room-a", "room-b") == ["room-a", "room-b"]


def test_validate_subzone_boundary(persistence: MagicMock) -> None:
    room = MagicMock()
    room.sub_zone = "arkham_downtown"
    persistence.get_room_by_id.return_value = room
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.validate_subzone_boundary("arkham_downtown", "room-a") is True
    assert integration.validate_subzone_boundary("innsmouth", "room-a") is False


def test_publish_movement_events(persistence: MagicMock) -> None:
    bus = MagicMock()
    integration = NPCMovementIntegration(event_bus=bus, persistence=persistence)
    integration._publish_movement_events("npc-1", "room-a", "room-b")
    assert bus.publish.call_count == 2


def test_get_npc_room_returns_none(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.get_npc_room("npc-1") is None


def test_get_room_objects_missing_destination(persistence: MagicMock) -> None:
    from_room = MagicMock()
    persistence.get_room_by_id.side_effect = [from_room, None]
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration._get_room_objects("npc-1", "room-a", "room-b") is None


def test_update_room_occupancy_skips_when_already_placed(persistence: MagicMock) -> None:
    from_room = MagicMock()
    to_room = MagicMock()
    from_room.has_npc.return_value = False
    to_room.has_npc.return_value = True
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    integration._update_room_occupancy("npc-1", from_room, to_room, "room-a", "room-b")
    from_room.npc_left.assert_not_called()
    to_room.npc_entered.assert_not_called()


def test_move_npc_exception_returns_false(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    with patch.object(integration, "_validate_room_ids", side_effect=RuntimeError("boom")):
        assert integration.move_npc_to_room("npc-1", "room-a", "room-b") is False


def test_publish_movement_events_skips_without_bus(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    integration._publish_movement_events("npc-1", "room-a", "room-b")


def test_publish_movement_events_handles_publish_error(persistence: MagicMock) -> None:
    bus = MagicMock()
    bus.publish.side_effect = RuntimeError("bus down")
    integration = NPCMovementIntegration(event_bus=bus, persistence=persistence)
    integration._publish_movement_events("npc-1", "room-a", "room-b")


def test_validate_npc_movement_npc_not_in_source(persistence: MagicMock) -> None:
    from_room = MagicMock()
    to_room = MagicMock()
    from_room.has_npc.return_value = False
    persistence.get_room_by_id.side_effect = [from_room, to_room]
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.validate_npc_movement("npc-1", "room-a", "room-b") is False


def test_find_path_returns_none_without_connection(persistence: MagicMock) -> None:
    room = MagicMock()
    room.exits = {"north": "room-other"}
    persistence.get_room_by_id.return_value = room
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.find_path_between_rooms("room-a", "room-b") is None


def test_get_destination_subzone_from_room_id(persistence: MagicMock) -> None:
    persistence.get_room_by_id.return_value = MagicMock(sub_zone=None)
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    with patch(
        "server.npc.movement_integration.extract_subzone_from_room_id",
        return_value="arkham_downtown",
    ):
        assert integration._get_destination_subzone("earth_arkham_downtown_001") == "arkham_downtown"


def test_validate_subzone_boundary_rejects_empty_ids(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.validate_subzone_boundary("", "room-a") is False
    assert integration.validate_subzone_boundary("arkham", "") is False


def test_validate_subzone_boundary_unknown_destination(persistence: MagicMock) -> None:
    persistence.get_room_by_id.return_value = None
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.validate_subzone_boundary("arkham", "missing-room") is False


def test_is_npc_in_combat_true(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    combat = MagicMock()
    combat.is_npc_in_combat_sync.return_value = True
    with patch("server.services.combat_service.get_combat_service", return_value=combat):
        assert integration._is_npc_in_combat("npc-1") is True


def test_update_npc_instance_room_tracking(persistence: MagicMock) -> None:
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    npc_instance = MagicMock(current_room="room-a")
    lifecycle_manager = MagicMock(active_npcs={"npc-1": npc_instance})
    svc = MagicMock(lifecycle_manager=lifecycle_manager)
    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        return_value=svc,
    ):
        integration._update_npc_instance_room_tracking("npc-1", "room-b")
    assert npc_instance.current_room == "room-b"


def test_get_room_npcs_empty_when_missing(persistence: MagicMock) -> None:
    persistence.get_room_by_id.return_value = None
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.get_room_npcs("missing") == []


def test_get_available_exits_empty_when_missing(persistence: MagicMock) -> None:
    persistence.get_room_by_id.return_value = None
    integration = NPCMovementIntegration(event_bus=None, persistence=persistence)
    assert integration.get_available_exits("missing") == {}
