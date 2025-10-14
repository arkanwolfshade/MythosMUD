"""
Tests for NATS message handler sub-zone subscription functionality.

These tests cover the dynamic subscription management for local channels
when players move between sub-zones.
"""

from unittest.mock import AsyncMock, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


class TestNATSMessageHandlerSubZoneSubscriptions:
    """Test sub-zone subscription management in NATS message handler."""

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = AsyncMock(spec=NATSService)
        mock_service.subscribe = AsyncMock(return_value=True)
        mock_service.unsubscribe = AsyncMock(return_value=True)
        return mock_service

    @pytest.fixture
    def nats_handler(self, mock_nats_service):
        """Create NATS message handler with mock service."""
        handler = NATSMessageHandler(mock_nats_service)
        # Initialize subscriptions dict to track subscribed subjects
        handler.subscriptions = {}

        # Create mock functions that track calls
        handler._subscribe_calls = []
        handler._unsubscribe_calls = []

        async def mock_subscribe(subject):
            handler._subscribe_calls.append(subject)
            handler.subscriptions[subject] = True
            return True

        async def mock_unsubscribe(subject):
            handler._unsubscribe_calls.append(subject)
            if subject in handler.subscriptions:
                del handler.subscriptions[subject]
            return True

        handler._subscribe_to_subject = mock_subscribe
        handler._unsubscribe_from_subject = mock_unsubscribe
        return handler

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_new_subscription(self, nats_handler):
        """Test subscribing to a new sub-zone."""
        subzone = "docks"

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is True
        assert subzone in nats_handler.subzone_subscriptions
        assert nats_handler.subzone_subscriptions[subzone] == 1
        assert "chat.local.subzone.docks" in nats_handler._subscribe_calls

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_existing_subscription(self, nats_handler):
        """Test subscribing to an already subscribed sub-zone."""
        subzone = "docks"

        # First subscription
        result1 = await nats_handler.subscribe_to_subzone(subzone)
        assert result1 is True
        assert nats_handler.subzone_subscriptions[subzone] == 1

        # Second subscription (should increase count)
        result2 = await nats_handler.subscribe_to_subzone(subzone)
        assert result2 is True
        assert nats_handler.subzone_subscriptions[subzone] == 2

        # Should only call _subscribe_to_subject once
        assert nats_handler._subscribe_calls.count("chat.local.subzone.docks") == 1

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_failure(self, nats_handler):
        """Test subscribing to sub-zone when NATS subscription fails."""
        subzone = "docks"

        # Override the mock to return False
        async def mock_subscribe_fail(subject):
            return False

        nats_handler._subscribe_to_subject = mock_subscribe_fail

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is False
        assert subzone not in nats_handler.subzone_subscriptions

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_decrease_count(self, nats_handler):
        """Test unsubscribing from sub-zone decreases count but doesn't unsubscribe from NATS."""
        subzone = "docks"

        # Subscribe twice
        await nats_handler.subscribe_to_subzone(subzone)
        await nats_handler.subscribe_to_subzone(subzone)
        assert nats_handler.subzone_subscriptions[subzone] == 2

        # Unsubscribe once
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is True
        assert nats_handler.subzone_subscriptions[subzone] == 1
        # Should not call _unsubscribe_from_subject yet
        assert "chat.local.subzone.docks" not in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_final_unsubscribe(self, nats_handler):
        """Test unsubscribing from sub-zone when count reaches zero."""
        subzone = "docks"

        # Subscribe once
        await nats_handler.subscribe_to_subzone(subzone)
        assert nats_handler.subzone_subscriptions[subzone] == 1

        # Unsubscribe (should remove from NATS)
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is True
        assert subzone not in nats_handler.subzone_subscriptions
        assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_not_subscribed(self, nats_handler):
        """Test unsubscribing from a sub-zone that's not subscribed."""
        subzone = "docks"

        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_nats_failure(self, nats_handler):
        """Test unsubscribing from sub-zone when NATS unsubscribe fails."""
        subzone = "docks"

        # Override the mock to return False
        async def mock_unsubscribe_fail(subject):
            return False

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_fail

        # Subscribe once
        await nats_handler.subscribe_to_subzone(subzone)

        # Try to unsubscribe
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        # Should still be in subscriptions since NATS unsubscribe failed
        assert subzone in nats_handler.subzone_subscriptions

    def test_track_player_subzone_subscription_new_player(self, nats_handler):
        """Test tracking a new player's sub-zone subscription."""
        player_id = "player1"
        subzone = "docks"

        nats_handler.track_player_subzone_subscription(player_id, subzone)

        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_track_player_subzone_subscription_same_subzone(self, nats_handler):
        """Test tracking player movement within same sub-zone."""
        player_id = "player1"
        subzone = "docks"

        # Initial subscription
        nats_handler.track_player_subzone_subscription(player_id, subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

        # Move within same sub-zone
        nats_handler.track_player_subzone_subscription(player_id, subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_track_player_subzone_subscription_different_subzone(self, nats_handler):
        """Test tracking player movement to different sub-zone."""
        player_id = "player1"
        old_subzone = "docks"
        new_subzone = "warehouse"

        # Subscribe to old sub-zone
        nats_handler.subzone_subscriptions[old_subzone] = 2

        # Initial subscription
        nats_handler.track_player_subzone_subscription(player_id, old_subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == old_subzone
        assert nats_handler.subzone_subscriptions[old_subzone] == 2

        # Move to different sub-zone
        nats_handler.track_player_subzone_subscription(player_id, new_subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == new_subzone
        # Should decrease count for old sub-zone
        assert nats_handler.subzone_subscriptions[old_subzone] == 1

    def test_get_players_in_subzone(self, nats_handler):
        """Test getting players in a specific sub-zone."""
        # Set up player subscriptions
        nats_handler.player_subzone_subscriptions = {
            "player1": "docks",
            "player2": "docks",
            "player3": "warehouse",
            "player4": "docks",
        }

        players = nats_handler.get_players_in_subzone("docks")

        assert set(players) == {"player1", "player2", "player4"}

    def test_get_players_in_subzone_empty(self, nats_handler):
        """Test getting players in a sub-zone with no players."""
        nats_handler.player_subzone_subscriptions = {"player1": "docks", "player2": "warehouse"}

        players = nats_handler.get_players_in_subzone("northside")

        assert players == []

    @pytest.mark.asyncio
    async def test_handle_player_movement_same_subzone(self, nats_handler):
        """Test handling player movement within same sub-zone."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_docks_warehouse_2"

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = lambda x: "docks" if "docks" in x else None

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should not subscribe/unsubscribe since same sub-zone
            assert len(nats_handler._subscribe_calls) == 0
            assert len(nats_handler._unsubscribe_calls) == 0

            # Should track the subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "docks"

    @pytest.mark.asyncio
    async def test_handle_player_movement_different_subzone(self, nats_handler):
        """Test handling player movement between different sub-zones."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_northside_mansion_1"

        # Set up initial state - player is already in docks sub-zone
        nats_handler.subzone_subscriptions["docks"] = 1
        nats_handler.player_subzone_subscriptions[player_id] = "docks"
        nats_handler.subscriptions["chat.local.subzone.docks"] = True

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = lambda x: "docks" if "docks" in x else "northside"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should unsubscribe from old sub-zone and subscribe to new one
            assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
            assert "chat.local.subzone.northside" in nats_handler._subscribe_calls

            # Should track the new subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "northside"

    @pytest.mark.asyncio
    async def test_handle_player_movement_from_no_room(self, nats_handler):
        """Test handling player movement from no room to a room."""
        player_id = "player1"
        old_room_id = None
        new_room_id = "earth_arkham_docks_warehouse_1"

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.return_value = "docks"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should only subscribe to new sub-zone
            assert "chat.local.subzone.docks" in nats_handler._subscribe_calls
            assert len(nats_handler._unsubscribe_calls) == 0

            # Should track the subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "docks"

    @pytest.mark.asyncio
    async def test_handle_player_movement_to_no_room(self, nats_handler):
        """Test handling player movement from a room to no room."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = None

        # Set up initial state - player is already in docks sub-zone
        nats_handler.subzone_subscriptions["docks"] = 1
        nats_handler.player_subzone_subscriptions[player_id] = "docks"
        nats_handler.subscriptions["chat.local.subzone.docks"] = True

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.return_value = "docks"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should only unsubscribe from old sub-zone
            assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
            assert len(nats_handler._subscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions(self, nats_handler):
        """Test cleaning up empty sub-zone subscriptions."""
        # Set up sub-zones with different states
        nats_handler.subzone_subscriptions = {
            "docks": 0,  # Empty, should be cleaned up
            "warehouse": 1,  # Has players, should not be cleaned up
            "northside": -1,  # Negative count, should be cleaned up
        }

        # Set up player subscriptions
        nats_handler.player_subzone_subscriptions = {
            "player1": "warehouse"  # Only player is in warehouse
        }

        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should unsubscribe from empty sub-zones
        assert len(nats_handler._unsubscribe_calls) == 2
        assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
        assert "chat.local.subzone.northside" in nats_handler._unsubscribe_calls

        # Should not unsubscribe from warehouse (has players)
        assert "chat.local.subzone.warehouse" not in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions_no_cleanup_needed(self, nats_handler):
        """Test cleanup when no sub-zones need cleaning up."""
        # Set up sub-zones with active players
        nats_handler.subzone_subscriptions = {"docks": 1, "warehouse": 2}

        nats_handler.player_subzone_subscriptions = {"player1": "docks", "player2": "warehouse", "player3": "warehouse"}

        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should not unsubscribe from any sub-zones
        assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_exception_handling(self, nats_handler):
        """Test exception handling in subscribe_to_subzone."""
        subzone = "docks"

        # Override the mock to raise exception
        async def mock_subscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._subscribe_to_subject = mock_subscribe_exception

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is False
        assert subzone not in nats_handler.subzone_subscriptions

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_exception_handling(self, nats_handler):
        """Test exception handling in unsubscribe_from_subzone."""
        subzone = "docks"
        nats_handler.subzone_subscriptions[subzone] = 1

        # Override the mock to raise exception
        async def mock_unsubscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_exception

        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        # Should still be in subscriptions since unsubscribe failed
        assert subzone in nats_handler.subzone_subscriptions

    def test_track_player_subzone_subscription_exception_handling(self, nats_handler):
        """Test exception handling in track_player_subzone_subscription."""
        player_id = "player1"
        subzone = "docks"

        # Cause an exception by making subzone_subscriptions a non-dict
        nats_handler.subzone_subscriptions = None

        # Should not raise exception
        nats_handler.track_player_subzone_subscription(player_id, subzone)

        # Should still track the player subscription
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_get_players_in_subzone_exception_handling(self, nats_handler):
        """Test exception handling in get_players_in_subzone."""
        subzone = "docks"

        # Cause an exception by making player_subzone_subscriptions a non-dict
        nats_handler.player_subzone_subscriptions = None

        players = nats_handler.get_players_in_subzone(subzone)

        assert players == []

    @pytest.mark.asyncio
    async def test_handle_player_movement_exception_handling(self, nats_handler):
        """Test exception handling in handle_player_movement."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_northside_mansion_1"

        # Mock sub-zone extraction to raise exception
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = Exception("Room parsing error")

            # Should not raise exception
            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should not make any subscription calls
            assert len(nats_handler._subscribe_calls) == 0
            assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions_exception_handling(self, nats_handler):
        """Test exception handling in cleanup_empty_subzone_subscriptions."""
        nats_handler.subzone_subscriptions = {"docks": 0}

        # Override the mock to raise exception
        async def mock_unsubscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_exception

        # Should not raise exception
        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should still be in subscriptions since cleanup failed
        assert "docks" in nats_handler.subzone_subscriptions
