"""
Tests for optimized game models with lazy loading.

This module tests the performance-optimized game models that use lazy loading
for expensive computed fields and operations.

As the Pnakotic Manuscripts remind us: "Efficiency in computation ensures
the ancient calculations complete before the stars are right."
"""

from datetime import UTC, datetime

import pytest

from server.models.optimized_game import (
    AttributeType,
    OptimizedStats,
    OptimizedStatusEffect,
    StatusEffectType,
    benchmark_lazy_loading_performance,
)


class TestAttributeTypeEnum:
    """Test AttributeType enum definition."""

    def test_attribute_type_values(self):
        """Test attribute type enum has correct values."""
        assert AttributeType.STR.value == "strength"
        assert AttributeType.DEX.value == "dexterity"
        assert AttributeType.CON.value == "constitution"
        assert AttributeType.INT.value == "intelligence"
        assert AttributeType.WIS.value == "wisdom"
        assert AttributeType.CHA.value == "charisma"
        assert AttributeType.SAN.value == "sanity"
        assert AttributeType.OCC.value == "occult_knowledge"
        assert AttributeType.FEAR.value == "fear"
        assert AttributeType.CORR.value == "corruption"
        assert AttributeType.CULT.value == "cult_affiliation"

    def test_attribute_type_all_members_present(self):
        """Test all expected attribute types are present."""
        expected_types = [
            "STR",
            "DEX",
            "CON",
            "INT",
            "WIS",
            "CHA",
            "SAN",
            "OCC",
            "FEAR",
            "CORR",
            "CULT",
        ]

        for attr_name in expected_types:
            assert hasattr(AttributeType, attr_name)


class TestStatusEffectTypeEnum:
    """Test StatusEffectType enum definition."""

    def test_status_effect_type_values(self):
        """Test status effect enum has correct values."""
        assert StatusEffectType.STUNNED.value == "stunned"
        assert StatusEffectType.POISONED.value == "poisoned"
        assert StatusEffectType.HALLUCINATING.value == "hallucinating"
        assert StatusEffectType.PARANOID.value == "paranoid"
        assert StatusEffectType.TREMBLING.value == "trembling"
        assert StatusEffectType.CORRUPTED.value == "corrupted"
        assert StatusEffectType.INSANE.value == "insane"

    def test_status_effect_type_all_members_present(self):
        """Test all expected status effect types are present."""
        expected_types = ["STUNNED", "POISONED", "HALLUCINATING", "PARANOID", "TREMBLING", "CORRUPTED", "INSANE"]

        for effect_name in expected_types:
            assert hasattr(StatusEffectType, effect_name)


class TestOptimizedStatusEffectInitialization:
    """Test OptimizedStatusEffect initialization."""

    def test_status_effect_creation_defaults(self):
        """Test status effect creates with defaults."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        assert effect.effect_type == StatusEffectType.POISONED
        assert effect.duration == 10
        assert effect.intensity == 5
        assert effect.source is None
        assert isinstance(effect.applied_at, datetime)

    def test_status_effect_creation_with_all_fields(self):
        """Test status effect creates with all fields specified."""
        now = datetime.now(UTC).replace(tzinfo=None)
        effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.STUNNED, duration=5, intensity=8, source="lightning_bolt", applied_at=now
        )

        assert effect.effect_type == StatusEffectType.STUNNED
        assert effect.duration == 5
        assert effect.intensity == 8
        assert effect.source == "lightning_bolt"
        assert effect.applied_at == now

    def test_status_effect_validates_duration(self):
        """Test status effect validates duration is non-negative."""
        with pytest.raises(ValueError):
            OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=-1, intensity=5)

    def test_status_effect_validates_intensity_min(self):
        """Test status effect validates intensity minimum."""
        with pytest.raises(ValueError):
            OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=0)

    def test_status_effect_validates_intensity_max(self):
        """Test status effect validates intensity maximum."""
        with pytest.raises(ValueError):
            OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=11)

    def test_status_effect_initializes_cache(self):
        """Test status effect initializes cache on creation."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        assert hasattr(effect, "_is_active_cache")
        assert isinstance(effect._is_active_cache, dict)
        assert len(effect._is_active_cache) == 0


class TestOptimizedStatusEffectActivity:
    """Test OptimizedStatusEffect activity checking."""

    def test_is_active_permanent_effect(self):
        """Test permanent effect (duration=0) is always active."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.CORRUPTED, duration=0, intensity=5)

        assert effect.is_active(0) is True
        assert effect.is_active(100) is True
        assert effect.is_active(1000) is True

    def test_is_active_temporary_effect(self):
        """Test temporary effect activity based on ticks."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=3)

        assert effect.is_active(5) is True  # Before duration expires
        assert effect.is_active(9) is True  # Just before expiry
        assert effect.is_active(10) is False  # At duration
        assert effect.is_active(15) is False  # After duration

    def test_is_active_caching(self):
        """Test is_active uses caching for performance."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        # First call should cache the result
        result1 = effect.is_active(5)
        assert len(effect._is_active_cache) == 1

        # Second call should use cached result
        result2 = effect.is_active(5)
        assert result1 == result2
        assert len(effect._is_active_cache) == 1  # Still only one cached result

        # Different tick should create new cache entry
        _ = effect.is_active(7)
        assert len(effect._is_active_cache) == 2

    def test_clear_cache(self):
        """Test cache clearing functionality."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        # Populate cache
        effect.is_active(5)
        effect.is_active(7)
        assert len(effect._is_active_cache) == 2

        # Clear cache
        effect.clear_cache()
        assert len(effect._is_active_cache) == 0


class TestOptimizedStatsInitialization:
    """Test OptimizedStats initialization."""

    def test_stats_creation_defaults(self):
        """Test stats creates with random defaults."""
        stats = OptimizedStats()

        # All core attributes should have values
        assert 3 <= stats.strength <= 18
        assert 3 <= stats.dexterity <= 18
        assert 3 <= stats.constitution <= 18
        assert 3 <= stats.intelligence <= 18
        assert 3 <= stats.wisdom <= 18
        assert 3 <= stats.charisma <= 18

        # Horror attributes should have defaults
        assert stats.sanity == 100
        assert stats.occult_knowledge == 0
        assert stats.fear == 0
        assert stats.corruption == 0
        assert stats.cult_affiliation == 0
        assert stats.current_health == 100

    def test_stats_creation_with_specified_values(self):
        """Test stats creates with specified values."""
        stats = OptimizedStats(
            strength=15,
            dexterity=14,
            constitution=16,
            intelligence=12,
            wisdom=10,
            charisma=8,
            sanity=75,
            occult_knowledge=25,
            fear=30,
            corruption=10,
            cult_affiliation=5,
            current_health=80,
        )

        assert stats.strength == 15
        assert stats.dexterity == 14
        assert stats.constitution == 16
        assert stats.intelligence == 12
        assert stats.wisdom == 10
        assert stats.charisma == 8
        assert stats.sanity == 75
        assert stats.occult_knowledge == 25
        assert stats.fear == 30
        assert stats.corruption == 10
        assert stats.cult_affiliation == 5
        assert stats.current_health == 80

    def test_stats_validates_attribute_min(self):
        """Test stats validates minimum attribute values."""
        with pytest.raises(ValueError):
            OptimizedStats(strength=0)  # Below minimum of 1

    def test_stats_validates_attribute_max(self):
        """Test stats validates maximum attribute values."""
        with pytest.raises(ValueError):
            OptimizedStats(strength=21)  # Above maximum of 20

    def test_stats_validates_sanity_min(self):
        """Test stats validates minimum sanity."""
        stats = OptimizedStats(sanity=0)  # Minimum allowed
        assert stats.sanity == 0

    def test_stats_validates_sanity_max(self):
        """Test stats validates maximum sanity."""
        with pytest.raises(ValueError):
            OptimizedStats(sanity=101)  # Above maximum of 100

    def test_stats_validates_current_health_min(self):
        """Test stats validates minimum current_health."""
        stats = OptimizedStats(current_health=0)  # Minimum allowed
        assert stats.current_health == 0

    def test_stats_initializes_caches(self):
        """Test stats initializes caches on creation."""
        stats = OptimizedStats()

        assert hasattr(stats, "_computed_cache")
        assert hasattr(stats, "_method_cache")
        assert isinstance(stats._computed_cache, dict)
        assert isinstance(stats._method_cache, dict)


class TestOptimizedStatsComputedFields:
    """Test OptimizedStats computed fields."""

    def test_max_health_computation(self):
        """Test max_health computed from constitution."""
        stats = OptimizedStats(constitution=15)

        assert stats.max_health == 150  # constitution * 10

    def test_max_health_caching(self):
        """Test max_health uses caching."""
        stats = OptimizedStats(constitution=15)

        # First access
        max_health1 = stats.max_health
        assert len(stats._computed_cache) >= 1

        # Second access should use cache
        max_health2 = stats.max_health
        assert max_health1 == max_health2

    def test_max_sanity_computation(self):
        """Test max_sanity computed from wisdom."""
        stats = OptimizedStats(wisdom=16)

        assert stats.max_sanity == 80  # wisdom * 5

    def test_max_sanity_caching(self):
        """Test max_sanity uses caching."""
        stats = OptimizedStats(wisdom=16)

        # First access
        max_sanity1 = stats.max_sanity
        assert len(stats._computed_cache) >= 1

        # Second access should use cache
        max_sanity2 = stats.max_sanity
        assert max_sanity1 == max_sanity2


class TestOptimizedStatsAttributeModifiers:
    """Test attribute modifier calculations."""

    def test_get_attribute_modifier_calculation(self):
        """Test attribute modifier calculation follows D&D formula."""
        stats = OptimizedStats(strength=10, dexterity=15, constitution=8)

        assert stats.get_attribute_modifier(AttributeType.STR) == 0  # (10-10)/2 = 0
        assert stats.get_attribute_modifier(AttributeType.DEX) == 2  # (15-10)/2 = 2.5 -> 2
        assert stats.get_attribute_modifier(AttributeType.CON) == -1  # (8-10)/2 = -1

    def test_get_attribute_modifier_edge_cases(self):
        """Test attribute modifier for edge case values."""
        stats = OptimizedStats(strength=1, dexterity=20, constitution=10)

        assert stats.get_attribute_modifier(AttributeType.STR) == -5  # (1-10)//2 = -9//2 = -5
        assert stats.get_attribute_modifier(AttributeType.DEX) == 5  # (20-10)/2 = 5

    def test_get_attribute_modifier_caching(self):
        """Test attribute modifier uses caching."""
        stats = OptimizedStats(strength=15)

        # First call
        mod1 = stats.get_attribute_modifier(AttributeType.STR)
        cache_size_1 = len(stats._method_cache)

        # Second call should use cache
        mod2 = stats.get_attribute_modifier(AttributeType.STR)
        cache_size_2 = len(stats._method_cache)

        assert mod1 == mod2
        assert cache_size_1 == cache_size_2  # Cache didn't grow

    def test_get_attribute_modifier_all_attributes(self):
        """Test modifier calculation for all attribute types."""
        stats = OptimizedStats(
            strength=12,
            dexterity=14,
            constitution=16,
            intelligence=10,
            wisdom=18,
            charisma=8,
            sanity=75,
            occult_knowledge=50,
            fear=25,
            corruption=30,
            cult_affiliation=10,
        )

        # Physical attributes
        assert stats.get_attribute_modifier(AttributeType.STR) == 1
        assert stats.get_attribute_modifier(AttributeType.DEX) == 2
        assert stats.get_attribute_modifier(AttributeType.CON) == 3

        # Mental attributes
        assert stats.get_attribute_modifier(AttributeType.INT) == 0
        assert stats.get_attribute_modifier(AttributeType.WIS) == 4
        assert stats.get_attribute_modifier(AttributeType.CHA) == -1

        # Horror attributes
        assert stats.get_attribute_modifier(AttributeType.SAN) == 32
        assert stats.get_attribute_modifier(AttributeType.OCC) == 20
        assert stats.get_attribute_modifier(AttributeType.FEAR) == 7


class TestOptimizedStatsStateChecks:
    """Test state checking methods."""

    def test_is_sane_true(self):
        """Test is_sane returns True when sanity > 0."""
        stats = OptimizedStats(sanity=50)
        assert stats.is_sane() is True

    def test_is_sane_false(self):
        """Test is_sane returns False when sanity == 0."""
        stats = OptimizedStats(sanity=0)
        assert stats.is_sane() is False

    def test_is_sane_caching(self):
        """Test is_sane uses caching."""
        stats = OptimizedStats(sanity=75)

        # First call
        result1 = stats.is_sane()
        cache_size_1 = len(stats._method_cache)

        # Second call should use cache
        result2 = stats.is_sane()
        cache_size_2 = len(stats._method_cache)

        assert result1 == result2
        assert cache_size_1 == cache_size_2

    def test_is_corrupted_true(self):
        """Test is_corrupted returns True when corruption >= 50."""
        stats = OptimizedStats(corruption=50)
        assert stats.is_corrupted() is True

        stats2 = OptimizedStats(corruption=75)
        assert stats2.is_corrupted() is True

    def test_is_corrupted_false(self):
        """Test is_corrupted returns False when corruption < 50."""
        stats = OptimizedStats(corruption=49)
        assert stats.is_corrupted() is False

        stats2 = OptimizedStats(corruption=0)
        assert stats2.is_corrupted() is False

    def test_is_corrupted_caching(self):
        """Test is_corrupted uses caching."""
        stats = OptimizedStats(corruption=60)

        result1 = stats.is_corrupted()
        cache_size_1 = len(stats._method_cache)

        result2 = stats.is_corrupted()
        cache_size_2 = len(stats._method_cache)

        assert result1 == result2
        assert cache_size_1 == cache_size_2

    def test_is_insane_true(self):
        """Test is_insane returns True when sanity <= 0."""
        stats = OptimizedStats(sanity=0)
        assert stats.is_insane() is True

    def test_is_insane_false(self):
        """Test is_insane returns False when sanity > 0."""
        stats = OptimizedStats(sanity=1)
        assert stats.is_insane() is False

        stats2 = OptimizedStats(sanity=50)
        assert stats2.is_insane() is False

    def test_is_insane_caching(self):
        """Test is_insane uses caching."""
        stats = OptimizedStats(sanity=0)

        result1 = stats.is_insane()
        cache_size_1 = len(stats._method_cache)

        result2 = stats.is_insane()
        cache_size_2 = len(stats._method_cache)

        assert result1 == result2
        assert cache_size_1 == cache_size_2


class TestOptimizedStatsCacheManagement:
    """Test cache management functionality."""

    def test_clear_cache_empties_all_caches(self):
        """Test clear_cache empties all caches."""
        stats = OptimizedStats(strength=15, wisdom=16, sanity=75)

        # Populate caches
        _ = stats.max_health
        _ = stats.max_sanity
        _ = stats.get_attribute_modifier(AttributeType.STR)
        _ = stats.is_sane()
        _ = stats.is_corrupted()

        # Verify caches have entries
        assert len(stats._computed_cache) > 0
        assert len(stats._method_cache) > 0

        # Clear caches
        stats.clear_cache()

        # Verify caches are empty
        assert len(stats._computed_cache) == 0
        assert len(stats._method_cache) == 0

    def test_cache_independence(self):
        """Test computed_cache and method_cache are independent."""
        stats = OptimizedStats(constitution=15, sanity=50)

        # Access computed field
        _ = stats.max_health
        computed_cache_size = len(stats._computed_cache)
        method_cache_size = len(stats._method_cache)

        assert computed_cache_size > 0
        assert method_cache_size == 0  # Method cache not used yet

        # Access method
        _ = stats.is_sane()
        assert len(stats._method_cache) > 0  # Now method cache is populated

    def test_multiple_stats_instances_have_independent_caches(self):
        """Test different stats instances have independent caches."""
        stats1 = OptimizedStats(strength=15)
        stats2 = OptimizedStats(strength=10)

        # Populate caches
        mod1 = stats1.get_attribute_modifier(AttributeType.STR)
        mod2 = stats2.get_attribute_modifier(AttributeType.STR)

        assert mod1 == 2
        assert mod2 == 0

        # Caches should be independent
        assert len(stats1._method_cache) > 0
        assert len(stats2._method_cache) > 0
        assert stats1._method_cache != stats2._method_cache


class TestOptimizedStatsModelConfig:
    """Test Pydantic model configuration."""

    def test_extra_fields_forbidden(self):
        """Test model rejects extra fields."""
        with pytest.raises(ValueError):
            OptimizedStats(strength=15, invalid_field=999)

    def test_validate_assignment_enabled(self):
        """Test validate_assignment is enabled in config."""
        stats = OptimizedStats(strength=15)

        # Pydantic v2 doesn't allow direct assignment of validated fields
        # This test verifies the config is set correctly
        assert stats.model_config["validate_assignment"] is True

    def test_use_enum_values_enabled(self):
        """Test use_enum_values is enabled."""
        assert OptimizedStats.model_config["use_enum_values"] is True


class TestOptimizedStatsEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_stats_with_all_minimum_values(self):
        """Test stats with all minimum valid values."""
        stats = OptimizedStats(
            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,
            sanity=0,
            occult_knowledge=0,
            fear=0,
            corruption=0,
            cult_affiliation=0,
            current_health=0,
        )

        assert stats.strength == 1
        assert stats.max_health == 10  # 1 * 10
        assert stats.max_sanity == 5  # 1 * 5
        assert stats.is_insane() is True
        assert stats.is_corrupted() is False

    def test_stats_with_all_maximum_values(self):
        """Test stats with all maximum valid values."""
        stats = OptimizedStats(
            strength=20,
            dexterity=20,
            constitution=20,
            intelligence=20,
            wisdom=20,
            charisma=20,
            sanity=100,
            occult_knowledge=100,
            fear=100,
            corruption=100,
            cult_affiliation=100,
            current_health=200,  # Can be higher than max_health
        )

        assert stats.strength == 20
        assert stats.max_health == 200  # 20 * 10
        assert stats.max_sanity == 100  # 20 * 5
        assert stats.is_sane() is True
        assert stats.is_corrupted() is True


class TestOptimizedStatusEffectEdgeCases:
    """Test OptimizedStatusEffect edge cases."""

    def test_status_effect_zero_duration(self):
        """Test status effect with zero duration (permanent)."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.CORRUPTED, duration=0, intensity=5)

        # Should be active at any tick
        for tick in [0, 100, 1000, 10000]:
            assert effect.is_active(tick) is True

    def test_status_effect_minimum_intensity(self):
        """Test status effect with minimum intensity."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.TREMBLING, duration=10, intensity=1)

        assert effect.intensity == 1
        assert effect.is_active(5) is True

    def test_status_effect_maximum_intensity(self):
        """Test status effect with maximum intensity."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.INSANE, duration=10, intensity=10)

        assert effect.intensity == 10
        assert effect.is_active(5) is True

    def test_status_effect_with_long_duration(self):
        """Test status effect with very long duration."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=100000, intensity=5)

        assert effect.is_active(50000) is True
        assert effect.is_active(99999) is True
        assert effect.is_active(100000) is False

    def test_status_effect_source_tracking(self):
        """Test status effect tracks source correctly."""
        effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.STUNNED, duration=5, intensity=7, source="Elder Sign Backlash"
        )

        assert effect.source == "Elder Sign Backlash"


class TestBenchmarkPerformance:
    """Test benchmark performance functionality."""

    def test_benchmark_lazy_loading_performance_executes(self):
        """Test benchmark function executes without errors."""
        result = benchmark_lazy_loading_performance()

        # Should return timing tuples
        assert isinstance(result, tuple)
        assert len(result) == 3

        cached_time, cached_status_time, cached_modifier_time = result

        # All timings should be non-negative
        assert cached_time >= 0
        assert cached_status_time >= 0
        assert cached_modifier_time >= 0

    def test_benchmark_demonstrates_caching_benefit(self):
        """Test benchmark demonstrates caching improves performance."""
        # Run benchmark
        cached_time, cached_status_time, cached_modifier_time = benchmark_lazy_loading_performance()

        # Cached operations should be very fast (microseconds for 1000 operations)
        # This is a performance regression test
        assert cached_time < 0.1  # Should be much faster
        assert cached_status_time < 0.1
        assert cached_modifier_time < 0.1


class TestModelSerialization:
    """Test model serialization and deserialization."""

    def test_optimized_stats_serialization(self):
        """Test OptimizedStats can be serialized to dict."""
        stats = OptimizedStats(strength=15, dexterity=14, constitution=16)

        stats_dict = stats.model_dump()

        assert stats_dict["strength"] == 15
        assert stats_dict["dexterity"] == 14
        assert stats_dict["constitution"] == 16
        assert "max_health" in stats_dict
        assert "max_sanity" in stats_dict

    def test_optimized_status_effect_serialization(self):
        """Test OptimizedStatusEffect can be serialized to dict."""
        effect = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        effect_dict = effect.model_dump()

        assert effect_dict["effect_type"] == "poisoned"
        assert effect_dict["duration"] == 10
        assert effect_dict["intensity"] == 5

    def test_optimized_stats_json_serialization(self):
        """Test OptimizedStats can be serialized to JSON."""
        stats = OptimizedStats(strength=15, wisdom=16)

        json_str = stats.model_dump_json()

        assert isinstance(json_str, str)
        assert "strength" in json_str
        assert "wisdom" in json_str

    def test_optimized_stats_from_dict(self):
        """Test OptimizedStats can be created from dict."""
        data = {
            "strength": 15,
            "dexterity": 14,
            "constitution": 16,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 8,
        }

        stats = OptimizedStats(**data)

        assert stats.strength == 15
        assert stats.dexterity == 14
        assert stats.constitution == 16


class TestIntegrationScenarios:
    """Test integration scenarios combining multiple features."""

    def test_character_with_multiple_status_effects(self):
        """Test character can have multiple status effects."""
        # Stats not directly used in test but demonstrates context
        _ = OptimizedStats(sanity=50, corruption=60)

        effect1 = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=3)
        effect2 = OptimizedStatusEffect(effect_type=StatusEffectType.CORRUPTED, duration=0, intensity=7)
        effect3 = OptimizedStatusEffect(effect_type=StatusEffectType.HALLUCINATING, duration=20, intensity=5)

        # Collect active effects at tick 5
        current_tick = 5
        active_effects = [effect for effect in [effect1, effect2, effect3] if effect.is_active(current_tick)]

        assert len(active_effects) == 3  # All active at tick 5

        # Check at tick 15
        current_tick = 15
        active_effects = [effect for effect in [effect1, effect2, effect3] if effect.is_active(current_tick)]

        assert len(active_effects) == 2  # effect1 expired, effect2 (permanent) and effect3 still active

    def test_character_state_progression(self):
        """Test character state progresses correctly."""
        stats = OptimizedStats(sanity=100, corruption=0)

        # Initial state
        assert stats.is_sane() is True
        assert stats.is_corrupted() is False
        assert stats.is_insane() is False

        # After some corruption
        stats = OptimizedStats(sanity=50, corruption=50)
        assert stats.is_sane() is True
        assert stats.is_corrupted() is True
        assert stats.is_insane() is False

        # Complete madness
        stats = OptimizedStats(sanity=0, corruption=100)
        assert stats.is_sane() is False
        assert stats.is_corrupted() is True
        assert stats.is_insane() is True

    def test_cache_performance_with_multiple_accesses(self):
        """Test cache improves performance with multiple accesses."""
        stats = OptimizedStats(strength=15, constitution=16, wisdom=14)

        # Multiple accesses to computed properties
        for _ in range(100):
            _ = stats.max_health
            _ = stats.max_sanity
            _ = stats.get_attribute_modifier(AttributeType.STR)
            _ = stats.is_sane()

        # Cache should have entries
        assert len(stats._computed_cache) > 0
        assert len(stats._method_cache) > 0

        # All results should be consistent
        assert stats.max_health == 160
        assert stats.max_sanity == 70


class TestPydanticValidation:
    """Test Pydantic validation features."""

    def test_field_constraints_enforced(self):
        """Test Field constraints are properly enforced."""
        # Test minimum constraint
        with pytest.raises(ValueError):
            OptimizedStats(strength=-1)

        # Test maximum constraint
        with pytest.raises(ValueError):
            OptimizedStats(charisma=25)

    def test_default_factory_functions(self):
        """Test default factory functions work correctly."""
        effect1 = OptimizedStatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)
        effect2 = OptimizedStatusEffect(effect_type=StatusEffectType.STUNNED, duration=5, intensity=3)

        # applied_at should be set automatically
        assert effect1.applied_at is not None
        assert effect2.applied_at is not None

        # They should be close in time but potentially different
        assert isinstance(effect1.applied_at, datetime)
        assert isinstance(effect2.applied_at, datetime)

    def test_model_validation_on_creation(self):
        """Test models validate data on creation."""
        # Valid data should work
        stats = OptimizedStats(strength=15)
        assert stats.strength == 15

        # Invalid data should raise ValueError
        with pytest.raises(ValueError):
            OptimizedStats(strength="not a number")

    def test_forbid_extra_fields(self):
        """Test extra fields are forbidden by model config."""
        with pytest.raises(ValueError):
            OptimizedStatusEffect(
                effect_type=StatusEffectType.POISONED, duration=10, intensity=5, unknown_field="invalid"
            )
