from models import Stats


def test_stats_creation():
    """Test creating a Stats object with default values."""
    stats = Stats()
    assert stats.strength == 10
    assert stats.dexterity == 10
    assert stats.constitution == 10
    assert stats.intelligence == 10
    assert stats.wisdom == 10
    assert stats.charisma == 10
    assert stats.sanity == 100
    assert stats.occult_knowledge == 0
    assert stats.fear == 0
    assert stats.corruption == 0
    assert stats.cult_affiliation == 0


def test_stats_custom_values():
    """Test creating a Stats object with custom values."""
    stats = Stats(
        strength=15,
        dexterity=12,
        constitution=14,
        intelligence=16,
        wisdom=13,
        charisma=11,
        sanity=80,
        occult_knowledge=5,
        fear=10,
        corruption=2,
        cult_affiliation=0,
    )
    assert stats.strength == 15
    assert stats.dexterity == 12
    assert stats.constitution == 14
    assert stats.intelligence == 16
    assert stats.wisdom == 13
    assert stats.charisma == 11
    assert stats.sanity == 80
    assert stats.occult_knowledge == 5
    assert stats.fear == 10
    assert stats.corruption == 2


def test_stats_derived_values():
    """Test that derived stats are calculated correctly."""
    stats = Stats(constitution=15, wisdom=12)
    assert stats.max_health == 150  # constitution * 10
    assert stats.current_health == 100  # default value
