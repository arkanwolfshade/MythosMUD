"""
Unit tests for room data cache.

Tests the RoomDataCache class for caching and freshness management.
"""

from unittest.mock import patch

from server.services.room_data_cache import RoomDataCache


class TestRoomDataCache:
    """Test suite for RoomDataCache class."""

    def test_init_default_threshold(self):
        """Test RoomDataCache initialization with default threshold."""
        cache = RoomDataCache()
        assert cache._freshness_threshold_seconds == 5
        assert cache._room_data_cache == {}

    def test_init_custom_threshold(self):
        """Test RoomDataCache initialization with custom threshold."""
        cache = RoomDataCache(freshness_threshold_seconds=10)
        assert cache._freshness_threshold_seconds == 10

    def test_is_room_data_fresh_fresh(self):
        """Test is_room_data_fresh returns True for fresh data."""
        cache = RoomDataCache(freshness_threshold_seconds=5)
        current_time = 1000.0
        room_data = {"id": "test_room_1", "timestamp": 999.0}  # 1 second old
        assert cache.is_room_data_fresh(room_data, current_time=current_time) is True

    def test_is_room_data_fresh_stale(self):
        """Test is_room_data_fresh returns False for stale data."""
        cache = RoomDataCache(freshness_threshold_seconds=5)
        current_time = 1000.0
        room_data = {"id": "test_room_1", "timestamp": 990.0}  # 10 seconds old
        assert cache.is_room_data_fresh(room_data, current_time=current_time) is False

    def test_is_room_data_fresh_no_timestamp(self):
        """Test is_room_data_fresh returns False when no timestamp."""
        cache = RoomDataCache()
        room_data = {"id": "test_room_1"}
        assert cache.is_room_data_fresh(room_data) is False

    def test_is_room_data_fresh_custom_threshold(self):
        """Test is_room_data_fresh with custom threshold parameter."""
        cache = RoomDataCache(freshness_threshold_seconds=5)
        current_time = 1000.0
        room_data = {"id": "test_room_1", "timestamp": 990.0}  # 10 seconds old
        # With custom threshold of 15 seconds, should be fresh
        assert cache.is_room_data_fresh(room_data, current_time=current_time, threshold_seconds=15) is True

    def test_is_room_data_fresh_exactly_at_threshold(self):
        """Test is_room_data_fresh at exactly threshold boundary."""
        cache = RoomDataCache(freshness_threshold_seconds=5)
        current_time = 1000.0
        room_data = {"id": "test_room_1", "timestamp": 995.0}  # Exactly 5 seconds old
        # Should be stale (not < threshold)
        assert cache.is_room_data_fresh(room_data, current_time=current_time) is False

    def test_is_room_data_fresh_invalid_input(self):
        """Test is_room_data_fresh handles invalid input."""
        cache = RoomDataCache()
        assert cache.is_room_data_fresh(None) is False

    def test_get_cache_not_found(self):
        """Test get_cache returns None for non-existent room."""
        cache = RoomDataCache()
        assert cache.get_cache("nonexistent_room") is None

    def test_get_cache_found(self):
        """Test get_cache returns cached data."""
        cache = RoomDataCache()
        room_data = {"id": "test_room_1", "name": "Test Room"}
        cache.set_cache("test_room_1", room_data)
        assert cache.get_cache("test_room_1") == room_data

    def test_set_cache(self):
        """Test set_cache stores room data."""
        cache = RoomDataCache()
        room_data = {"id": "test_room_1", "name": "Test Room"}
        cache.set_cache("test_room_1", room_data)
        assert cache._room_data_cache["test_room_1"] == room_data

    def test_set_cache_overwrites(self):
        """Test set_cache overwrites existing data."""
        cache = RoomDataCache()
        room_data1 = {"id": "test_room_1", "name": "Old Name"}
        room_data2 = {"id": "test_room_1", "name": "New Name"}
        cache.set_cache("test_room_1", room_data1)
        cache.set_cache("test_room_1", room_data2)
        assert cache.get_cache("test_room_1")["name"] == "New Name"

    def test_clear_cache_specific_room(self):
        """Test clear_cache clears specific room."""
        cache = RoomDataCache()
        cache.set_cache("room1", {"id": "room1"})
        cache.set_cache("room2", {"id": "room2"})
        cache.clear_cache("room1")
        assert cache.get_cache("room1") is None
        assert cache.get_cache("room2") is not None

    def test_clear_cache_all(self):
        """Test clear_cache clears all rooms when room_id is None."""
        cache = RoomDataCache()
        cache.set_cache("room1", {"id": "room1"})
        cache.set_cache("room2", {"id": "room2"})
        cache.clear_cache()
        assert cache.get_cache("room1") is None
        assert cache.get_cache("room2") is None

    def test_clear_cache_nonexistent_room(self):
        """Test clear_cache handles nonexistent room gracefully."""
        cache = RoomDataCache()
        cache.clear_cache("nonexistent_room")  # Should not raise

    def test_get_cache_stats_empty(self):
        """Test get_cache_stats with empty cache."""
        cache = RoomDataCache()
        stats = cache.get_cache_stats(cache.is_room_data_fresh)
        assert stats["total_rooms_cached"] == 0
        assert stats["fresh_rooms"] == 0
        assert stats["stale_rooms"] == 0

    def test_get_cache_stats_with_fresh_and_stale(self):
        """Test get_cache_stats with mix of fresh and stale data."""
        cache = RoomDataCache(freshness_threshold_seconds=5)
        current_time = 1000.0

        # Fresh data (1 second old)
        fresh_data = {"id": "fresh_room", "timestamp": 999.0}
        cache.set_cache("fresh_room", fresh_data)

        # Stale data (10 seconds old)
        stale_data = {"id": "stale_room", "timestamp": 990.0}
        cache.set_cache("stale_room", stale_data)

        with patch("time.time", return_value=current_time):
            stats = cache.get_cache_stats(cache.is_room_data_fresh)
            assert stats["total_rooms_cached"] == 2
            assert stats["fresh_rooms"] == 1
            assert stats["stale_rooms"] == 1

    def test_merge_room_data_newer_timestamp(self):
        """Test merge_room_data merges with newer data taking precedence."""
        cache = RoomDataCache()
        old_data = {"id": "test_room_1", "name": "Old Name", "timestamp": 100.0}
        new_data = {"id": "test_room_1", "name": "New Name", "timestamp": 200.0}
        merged = cache.merge_room_data(old_data, new_data)
        assert merged["name"] == "New Name"
        assert merged["timestamp"] == 200.0

    def test_merge_room_data_older_timestamp(self):
        """Test merge_room_data keeps old data when new is older, but uses new timestamp."""
        cache = RoomDataCache()
        old_data = {"id": "test_room_1", "name": "Old Name", "timestamp": 200.0}
        new_data = {"id": "test_room_1", "name": "New Name", "timestamp": 100.0}
        merged = cache.merge_room_data(old_data, new_data)
        assert merged["name"] == "Old Name"  # Old data kept because it's newer
        assert merged["timestamp"] == 100.0  # Always uses new timestamp (code behavior)

    def test_merge_room_data_new_field(self):
        """Test merge_room_data adds new fields from new data."""
        cache = RoomDataCache()
        old_data = {"id": "test_room_1", "name": "Test Room"}
        new_data = {"id": "test_room_1", "name": "Test Room", "description": "New Description"}
        merged = cache.merge_room_data(old_data, new_data)
        assert merged["description"] == "New Description"

    def test_merge_room_data_preserves_old_data(self):
        """Test merge_room_data does not modify original data."""
        cache = RoomDataCache()
        old_data = {"id": "test_room_1", "name": "Old Name"}
        new_data = {"id": "test_room_1", "name": "New Name"}
        merged = cache.merge_room_data(old_data, new_data)
        assert old_data["name"] == "Old Name"  # Original not modified
        assert merged["name"] == "New Name"  # Merged has new name

    def test_merge_room_data_invalid_input(self):
        """Test merge_room_data handles invalid input."""
        cache = RoomDataCache()
        new_data = {"id": "test_room_1", "name": "Test Room"}
        result = cache.merge_room_data(None, new_data)
        assert result == new_data  # Should return new data as fallback

    def test_is_newer_data_new_has_timestamp_old_doesnt(self):
        """Test _is_newer_data when new has timestamp but old doesn't."""
        cache = RoomDataCache()
        old_data = {"name": "Old"}
        new_data = {"name": "New", "timestamp": 100.0}
        assert cache._is_newer_data(old_data, new_data, "name") is True

    def test_is_newer_data_both_have_timestamps(self):
        """Test _is_newer_data when both have timestamps."""
        cache = RoomDataCache()
        old_data = {"name": "Old", "timestamp": 100.0}
        new_data = {"name": "New", "timestamp": 200.0}
        assert cache._is_newer_data(old_data, new_data, "name") is True

    def test_is_newer_data_old_newer_than_new(self):
        """Test _is_newer_data when old is newer than new."""
        cache = RoomDataCache()
        old_data = {"name": "Old", "timestamp": 200.0}
        new_data = {"name": "New", "timestamp": 100.0}
        assert cache._is_newer_data(old_data, new_data, "name") is False
