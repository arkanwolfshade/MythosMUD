"""
Unit tests for the in-memory lucidity tier cache (#714).

This cache is exit hallucination's cheap eligibility check -- see server/services/
lucidity_tier_cache.py and phantom_visibility.room_has_hallucinating_viewer.
"""

import uuid

from server.services.lucidity_tier_cache import LucidityTierCache


def test_get_tier_is_none_for_unrecorded_player():
    """A player never written to the cache has no recorded tier."""
    cache = LucidityTierCache()
    assert cache.get_tier(uuid.uuid4()) is None


def test_is_deranged_false_on_cache_miss():
    """Fail safe: an unrecorded player is never treated as deranged."""
    cache = LucidityTierCache()
    assert cache.is_deranged(uuid.uuid4()) is False


def test_set_tier_then_is_deranged():
    """Only an exact 'deranged' tier makes is_deranged True."""
    cache = LucidityTierCache()
    player_id = uuid.uuid4()
    cache.set_tier(player_id, "deranged")
    assert cache.is_deranged(player_id) is True


def test_is_deranged_false_for_other_tiers():
    """Fractured (also hallucination-eligible for phantoms) is not deranged for exits."""
    cache = LucidityTierCache()
    player_id = uuid.uuid4()
    cache.set_tier(player_id, "fractured")
    assert cache.is_deranged(player_id) is False


def test_set_tier_accepts_str_or_uuid_for_the_same_player():
    """A UUID and its string form must key into the same cache entry."""
    cache = LucidityTierCache()
    player_id = uuid.uuid4()
    cache.set_tier(player_id, "deranged")
    assert cache.is_deranged(str(player_id)) is True


def test_clear_removes_the_cached_tier():
    """clear() drops the entry entirely -- back to a cache miss (non-deranged)."""
    cache = LucidityTierCache()
    player_id = uuid.uuid4()
    cache.set_tier(player_id, "deranged")
    cache.clear(player_id)
    assert cache.get_tier(player_id) is None
    assert cache.is_deranged(player_id) is False
