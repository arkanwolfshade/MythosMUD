"""
Unit tests for NPC combat UUID mapping.

Tests the NPCCombatUUIDMapping class for managing UUID-to-string ID and UUID-to-XP mappings.
"""

from uuid import UUID, uuid4

from server.services.npc_combat_uuid_mapping import NPCCombatUUIDMapping


class TestNPCCombatUUIDMapping:
    """Test suite for NPCCombatUUIDMapping class."""

    def test_init(self):
        """Test NPCCombatUUIDMapping initialization."""
        mapping = NPCCombatUUIDMapping()
        assert mapping._uuid_to_string_id_mapping == {}
        assert mapping._uuid_to_xp_mapping == {}

    def test_is_valid_uuid_valid(self):
        """Test is_valid_uuid returns True for valid UUID."""
        mapping = NPCCombatUUIDMapping()
        valid_uuid = str(uuid4())
        assert mapping.is_valid_uuid(valid_uuid) is True

    def test_is_valid_uuid_invalid(self):
        """Test is_valid_uuid returns False for invalid UUID."""
        mapping = NPCCombatUUIDMapping()
        assert mapping.is_valid_uuid("not-a-uuid") is False
        assert mapping.is_valid_uuid("12345") is False
        assert mapping.is_valid_uuid("") is False

    def test_convert_to_uuid_from_uuid_string(self):
        """Test convert_to_uuid returns UUID when given UUID string."""
        mapping = NPCCombatUUIDMapping()
        uuid_str = str(uuid4())
        result = mapping.convert_to_uuid(uuid_str)
        assert isinstance(result, UUID)
        assert str(result) == uuid_str

    def test_convert_to_uuid_from_string_id(self):
        """Test convert_to_uuid creates new UUID when given string ID."""
        mapping = NPCCombatUUIDMapping()
        string_id = "npc_guard_001"
        result = mapping.convert_to_uuid(string_id)
        assert isinstance(result, UUID)
        # Should be a different UUID each time
        result2 = mapping.convert_to_uuid(string_id)
        assert result != result2

    def test_store_string_id_mapping(self):
        """Test store_string_id_mapping stores mapping."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        string_id = "npc_guard_001"
        mapping.store_string_id_mapping(uuid_id, string_id)
        assert mapping._uuid_to_string_id_mapping[uuid_id] == string_id

    def test_store_string_id_mapping_overwrites(self):
        """Test store_string_id_mapping overwrites existing mapping."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        mapping.store_string_id_mapping(uuid_id, "original_id")
        mapping.store_string_id_mapping(uuid_id, "new_id")
        assert mapping._uuid_to_string_id_mapping[uuid_id] == "new_id"

    def test_store_xp_mapping(self):
        """Test store_xp_mapping stores XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        xp_value = 100
        mapping.store_xp_mapping(uuid_id, xp_value)
        assert mapping._uuid_to_xp_mapping[uuid_id] == xp_value

    def test_store_xp_mapping_overwrites(self):
        """Test store_xp_mapping overwrites existing XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        mapping.store_xp_mapping(uuid_id, 50)
        mapping.store_xp_mapping(uuid_id, 100)
        assert mapping._uuid_to_xp_mapping[uuid_id] == 100

    def test_get_original_string_id_found(self):
        """Test get_original_string_id returns stored string ID."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        string_id = "npc_guard_001"
        mapping.store_string_id_mapping(uuid_id, string_id)
        result = mapping.get_original_string_id(uuid_id)
        assert result == string_id

    def test_get_original_string_id_not_found(self):
        """Test get_original_string_id returns None when not found."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        result = mapping.get_original_string_id(uuid_id)
        assert result is None

    def test_get_xp_value_found(self):
        """Test get_xp_value returns stored XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        xp_value = 150
        mapping.store_xp_mapping(uuid_id, xp_value)
        result = mapping.get_xp_value(uuid_id)
        assert result == xp_value

    def test_get_xp_value_not_found(self):
        """Test get_xp_value returns None when not found."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        result = mapping.get_xp_value(uuid_id)
        assert result is None

    def test_multiple_mappings(self):
        """Test multiple UUID mappings can coexist."""
        mapping = NPCCombatUUIDMapping()
        uuid1 = uuid4()
        uuid2 = uuid4()
        mapping.store_string_id_mapping(uuid1, "npc_001")
        mapping.store_string_id_mapping(uuid2, "npc_002")
        mapping.store_xp_mapping(uuid1, 50)
        mapping.store_xp_mapping(uuid2, 100)

        assert mapping.get_original_string_id(uuid1) == "npc_001"
        assert mapping.get_original_string_id(uuid2) == "npc_002"
        assert mapping.get_xp_value(uuid1) == 50
        assert mapping.get_xp_value(uuid2) == 100

    def test_zero_xp_value(self):
        """Test store_xp_mapping handles zero XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        mapping.store_xp_mapping(uuid_id, 0)
        assert mapping.get_xp_value(uuid_id) == 0

    def test_negative_xp_value(self):
        """Test store_xp_mapping handles negative XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        mapping.store_xp_mapping(uuid_id, -10)
        assert mapping.get_xp_value(uuid_id) == -10

    def test_large_xp_value(self):
        """Test store_xp_mapping handles large XP value."""
        mapping = NPCCombatUUIDMapping()
        uuid_id = uuid4()
        large_xp = 999999
        mapping.store_xp_mapping(uuid_id, large_xp)
        assert mapping.get_xp_value(uuid_id) == large_xp
