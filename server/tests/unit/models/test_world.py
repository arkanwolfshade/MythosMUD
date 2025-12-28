"""
Unit tests for world models.

Tests the Zone, Subzone, RoomModel, RoomLink, and ZoneConfigurationMapping SQLAlchemy models.
"""

from uuid import uuid4

from server.models.world import (
    RoomLink,
    RoomModel,
    Subzone,
    Zone,
    ZoneConfigurationMapping,
)

# --- Tests for Zone model ---


def test_zone_creation():
    """Test Zone can be instantiated with required fields."""
    zone_id = str(uuid4())
    zone = Zone(
        id=zone_id,
        stable_id="test_zone_001",
        name="Test Zone",
        zone_type="city",
        environment="outdoors",
        description="A test zone",
        weather_patterns=[],
        special_rules={},
    )

    assert zone.id == zone_id
    assert zone.stable_id == "test_zone_001"
    assert zone.name == "Test Zone"
    assert zone.zone_type == "city"
    assert zone.environment == "outdoors"
    assert zone.description == "A test zone"
    assert zone.weather_patterns == []
    assert zone.special_rules == {}


def test_zone_with_optional_fields_none():
    """Test Zone can have None for optional fields."""
    zone_id = str(uuid4())
    zone = Zone(
        id=zone_id,
        stable_id="test_zone_002",
        name="Test Zone 2",
        zone_type=None,
        environment=None,
        description=None,
        weather_patterns=None,
        special_rules=None,
    )

    assert zone.zone_type is None
    assert zone.environment is None
    assert zone.description is None
    assert zone.weather_patterns is None
    assert zone.special_rules is None


def test_zone_table_name():
    """Test Zone has correct table name."""
    assert Zone.__tablename__ == "zones"


def test_zone_repr():
    """Test Zone __repr__ method."""
    zone_id = str(uuid4())
    zone = Zone(
        id=zone_id,
        stable_id="test_zone_003",
        name="Test Zone",
        zone_type=None,
        environment=None,
        description=None,
        weather_patterns=None,
        special_rules=None,
    )

    repr_str = repr(zone)
    assert "Zone" in repr_str


# --- Tests for Subzone model ---


def test_subzone_creation():
    """Test Subzone can be instantiated with required fields."""
    zone_id = str(uuid4())
    subzone_id = str(uuid4())
    subzone = Subzone(
        id=subzone_id,
        zone_id=zone_id,
        stable_id="test_subzone_001",
        name="Test Subzone",
        environment="indoors",
        description="A test subzone",
        special_rules={},
    )

    assert subzone.id == subzone_id
    assert subzone.zone_id == zone_id
    assert subzone.stable_id == "test_subzone_001"
    assert subzone.name == "Test Subzone"
    assert subzone.environment == "indoors"
    assert subzone.description == "A test subzone"
    assert subzone.special_rules == {}


def test_subzone_with_optional_fields_none():
    """Test Subzone can have None for optional fields."""
    zone_id = str(uuid4())
    subzone_id = str(uuid4())
    subzone = Subzone(
        id=subzone_id,
        zone_id=zone_id,
        stable_id="test_subzone_002",
        name="Test Subzone 2",
        environment=None,
        description=None,
        special_rules=None,
    )

    assert subzone.environment is None
    assert subzone.description is None
    assert subzone.special_rules is None


def test_subzone_table_name():
    """Test Subzone has correct table name."""
    assert Subzone.__tablename__ == "subzones"


def test_subzone_repr():
    """Test Subzone __repr__ method."""
    zone_id = str(uuid4())
    subzone_id = str(uuid4())
    subzone = Subzone(
        id=subzone_id,
        zone_id=zone_id,
        stable_id="test_subzone_003",
        name="Test Subzone",
        environment=None,
        description=None,
        special_rules=None,
    )

    repr_str = repr(subzone)
    assert "Subzone" in repr_str


# --- Tests for RoomModel ---


def test_room_model_creation():
    """Test RoomModel can be instantiated with required fields."""
    subzone_id = str(uuid4())
    room_id = str(uuid4())
    room = RoomModel(
        id=room_id,
        subzone_id=subzone_id,
        stable_id="test_room_001",
        name="Test Room",
        description="A test room",
        attributes={},
    )

    assert room.id == room_id
    assert room.subzone_id == subzone_id
    assert room.stable_id == "test_room_001"
    assert room.name == "Test Room"
    assert room.description == "A test room"
    assert room.attributes == {}


def test_room_model_with_attributes():
    """Test RoomModel can have attributes dictionary."""
    subzone_id = str(uuid4())
    room_id = str(uuid4())
    room = RoomModel(
        id=room_id,
        subzone_id=subzone_id,
        stable_id="test_room_002",
        name="Test Room 2",
        description="A test room with attributes",
        attributes={"light": "bright", "temperature": "warm"},
    )

    assert room.attributes == {"light": "bright", "temperature": "warm"}


def test_room_model_table_name():
    """Test RoomModel has correct table name."""
    assert RoomModel.__tablename__ == "rooms"


def test_room_model_repr():
    """Test RoomModel __repr__ method."""
    subzone_id = str(uuid4())
    room_id = str(uuid4())
    room = RoomModel(
        id=room_id,
        subzone_id=subzone_id,
        stable_id="test_room_003",
        name="Test Room",
        description="A test room",
        attributes={},
    )

    repr_str = repr(room)
    assert "RoomModel" in repr_str


# --- Tests for RoomLink ---


def test_room_link_creation():
    """Test RoomLink can be instantiated with required fields."""
    link_id = str(uuid4())
    from_room_id = str(uuid4())
    to_room_id = str(uuid4())
    link = RoomLink(
        id=link_id,
        from_room_id=from_room_id,
        to_room_id=to_room_id,
        direction="north",
        attributes={},
    )

    assert link.id == link_id
    assert link.from_room_id == from_room_id
    assert link.to_room_id == to_room_id
    assert link.direction == "north"
    assert link.attributes == {}


def test_room_link_different_directions():
    """Test RoomLink can have different directions."""
    link_id = str(uuid4())
    from_room_id = str(uuid4())
    to_room_id = str(uuid4())
    link = RoomLink(
        id=link_id,
        from_room_id=from_room_id,
        to_room_id=to_room_id,
        direction="east",
        attributes={},
    )

    assert link.direction == "east"


def test_room_link_with_attributes():
    """Test RoomLink can have attributes dictionary."""
    link_id = str(uuid4())
    from_room_id = str(uuid4())
    to_room_id = str(uuid4())
    link = RoomLink(
        id=link_id,
        from_room_id=from_room_id,
        to_room_id=to_room_id,
        direction="south",
        attributes={"locked": True, "key_required": "master_key"},
    )

    assert link.attributes == {"locked": True, "key_required": "master_key"}


def test_room_link_table_name():
    """Test RoomLink has correct table name."""
    assert RoomLink.__tablename__ == "room_links"


def test_room_link_repr():
    """Test RoomLink __repr__ method."""
    link_id = str(uuid4())
    from_room_id = str(uuid4())
    to_room_id = str(uuid4())
    link = RoomLink(
        id=link_id,
        from_room_id=from_room_id,
        to_room_id=to_room_id,
        direction="south",
        attributes={},
    )

    repr_str = repr(link)
    assert "RoomLink" in repr_str


# --- Tests for ZoneConfigurationMapping ---


def test_zone_configuration_mapping_creation():
    """Test ZoneConfigurationMapping can be instantiated with required fields."""
    zone_id = str(uuid4())
    subzone_id = str(uuid4())
    mapping_id = str(uuid4())
    mapping = ZoneConfigurationMapping(
        id=mapping_id,
        zone_id=zone_id,
        subzone_id=subzone_id,
    )

    assert mapping.id == mapping_id
    assert mapping.zone_id == zone_id
    assert mapping.subzone_id == subzone_id


def test_zone_configuration_mapping_table_name():
    """Test ZoneConfigurationMapping has correct table name."""
    assert ZoneConfigurationMapping.__tablename__ == "zone_configurations"


def test_zone_configuration_mapping_repr():
    """Test ZoneConfigurationMapping __repr__ method."""
    zone_id = str(uuid4())
    subzone_id = str(uuid4())
    mapping_id = str(uuid4())
    mapping = ZoneConfigurationMapping(
        id=mapping_id,
        zone_id=zone_id,
        subzone_id=subzone_id,
    )

    repr_str = repr(mapping)
    assert "ZoneConfigurationMapping" in repr_str
