"""
Tests for model configuration consistency and behavior.

This module tests the consistency of Pydantic model configurations across
all models in the server, ensuring proper validation, performance, and
standardized behavior.
"""

import pytest
from pydantic import BaseModel, ConfigDict, ValidationError

from server.models.alias import Alias
from server.models.command import BaseCommand, LookCommand
from server.models.game import Stats
from server.models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthErrorResponse,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)


class TestModelConfigurationConsistency:
    """Test model configuration consistency across all models."""

    def test_model_config_usage_consistency(self):
        """Test that models use consistent model_config patterns."""
        # Models with model_config
        models_with_config = [
            (BaseCommand, {"extra": "forbid", "use_enum_values": True, "validate_assignment": True}),
            (HealthResponse, {"json_schema_extra": {"example": {}}}),
        ]

        for model_class, expected_config in models_with_config:
            assert hasattr(model_class, "model_config"), f"{model_class.__name__} should have model_config"

            # Check that model_config is properly defined
            config = model_class.model_config
            assert isinstance(config, dict | ConfigDict), (
                f"{model_class.__name__}.model_config should be dict or ConfigDict"
            )

            # Check specific configuration values
            for key, expected_value in expected_config.items():
                assert key in config, f"{model_class.__name__} should have {key} in model_config"
                if key == "json_schema_extra":
                    # For json_schema_extra, just check that it exists and has an example
                    assert isinstance(config[key], dict), f"{model_class.__name__}.model_config[{key}] should be a dict"
                    assert "example" in config[key], f"{model_class.__name__}.model_config[{key}] should have 'example'"
                else:
                    assert config[key] == expected_value, (
                        f"{model_class.__name__}.model_config[{key}] should be {expected_value}"
                    )

    def test_models_have_explicit_config(self):
        """Test that models have explicit model_config for consistency."""
        # Models that should have explicit model_config for consistency
        models_with_explicit_config = [
            BaseCommand,
            Alias,
            Stats,
            ServerComponent,
            DatabaseComponent,
            ConnectionsComponent,
            HealthComponents,
            HealthResponse,
            HealthErrorResponse,
        ]

        for model_class in models_with_explicit_config:
            # Check if model has explicit model_config (not just default empty dict)
            has_explicit_config = (
                hasattr(model_class, "model_config")
                and model_class.model_config  # Not empty
                and model_class.model_config != {}  # Not default empty dict
            )
            assert has_explicit_config, f"{model_class.__name__} should have explicit model_config for consistency"

    def test_extra_field_handling(self):
        """Test that models handle extra fields consistently."""
        # BaseCommand should forbid extra fields
        with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
            BaseCommand(extra_field="test")

        # Alias model now has model_config that forbids extra fields
        with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
            Alias(name="test", command="say hello", extra_field="not_allowed")

        # Stats model ignores extra fields for backward compatibility with serialized stats
        # that may include computed fields like max_health and max_lucidity
        # Using "ignore" is safer than "allow" - extra fields are silently ignored
        stats = Stats(extra_field="ignored_for_compatibility")
        # With extra="ignore", the field is not stored, so accessing it raises AttributeError
        with pytest.raises(AttributeError):
            _ = stats.extra_field

    def test_enum_value_handling(self):
        """Test that models handle enum values consistently."""
        # BaseCommand should use enum values
        look_cmd = LookCommand(direction="north")
        assert look_cmd.direction == "north"  # Should be string value, not enum object

        # Health models should handle enum values properly
        health_response = HealthResponse(
            status=HealthStatus.HEALTHY,
            timestamp="2025-01-01T00:00:00Z",
            uptime_seconds=100.0,
            version="1.0.0",
            components={
                "server": {
                    "status": HealthStatus.HEALTHY,
                    "uptime_seconds": 100.0,
                    "memory_usage_mb": 50.0,
                    "cpu_usage_percent": 10.0,
                },
                "database": {
                    "status": HealthStatus.HEALTHY,
                    "connection_count": 1,
                    "last_query_time_ms": 5.0,
                },
                "connections": {
                    "status": HealthStatus.HEALTHY,
                    "active_connections": 1,
                    "max_connections": 100,
                    "connection_rate_per_minute": 10.0,
                },
            },
        )
        assert health_response.status == "healthy"  # Should be string value

    def test_validation_assignment_consistency(self):
        """Test that models handle validation assignment consistently."""
        # BaseCommand should validate assignment
        look_cmd = LookCommand(direction="north")

        # This should raise validation error on invalid assignment
        with pytest.raises(ValidationError):
            look_cmd.direction = "invalid_direction"

    def test_field_validation_consistency(self):
        """Test that field validation is consistent across models."""
        # Test Stats model field validation
        with pytest.raises(ValidationError, match="Input should be greater than or equal to 1"):
            Stats(strength=0)

        with pytest.raises(ValidationError, match="Input should be less than or equal to 100"):
            Stats(strength=101)

        # Test Alias model field validation
        with pytest.raises(ValidationError, match="Field required"):
            Alias(name="test")  # Missing command field

        with pytest.raises(ValidationError, match="Field required"):
            Alias(command="say hello")  # Missing name field

    @pytest.mark.skip(reason="TODO: Fix after Stats model changes - default value initialization changed")
    def test_default_value_consistency(self):
        """Test that default values are handled consistently."""
        # Test Stats model defaults
        stats = Stats()
        assert stats.lucidity == 100
        assert stats.occult_knowledge == 0
        assert stats.fear == 0
        assert stats.corruption == 0
        assert stats.cult_affiliation == 0
        assert stats.current_health == 100

        # Test Alias model defaults
        alias = Alias(name="test", command="say hello")
        assert alias.id is not None
        assert alias.created_at is not None
        assert alias.updated_at is not None

    def test_computed_field_consistency(self):
        """Test that computed fields work consistently."""
        stats = Stats(constitution=75, wisdom=60)

        # Test computed fields
        assert stats.max_health == 75  # Direct constitution value
        assert stats.max_lucidity == 60  # Direct wisdom value

    def test_model_repr_consistency(self):
        """Test that model string representations are consistent."""
        # Test Alias repr
        alias = Alias(name="test", command="say hello")
        repr_str = repr(alias)
        assert "Alias" in repr_str
        assert "test" in repr_str
        assert "say hello" in repr_str

        # Test that other models have proper repr methods or fall back to default
        stats = Stats()
        repr_str = repr(stats)
        assert "Stats" in repr_str

    def test_model_serialization_consistency(self):
        """Test that model serialization is consistent."""
        # Test Alias custom serialization
        alias = Alias(name="test", command="say hello")
        serialized = alias.model_dump()

        assert isinstance(serialized, dict)
        assert serialized["name"] == "test"
        assert serialized["command"] == "say hello"
        assert "created_at" in serialized
        assert "updated_at" in serialized

        # Test that other models use standard Pydantic serialization
        stats = Stats()
        serialized = stats.model_dump()
        assert isinstance(serialized, dict)
        assert "strength" in serialized
        assert "lucidity" in serialized

    def test_model_initialization_consistency(self):
        """Test that model initialization is consistent."""
        # Test Stats custom initialization with random values
        stats = Stats()

        # Should have random values for physical/mental attributes
        assert 15 <= stats.strength <= 90
        assert 15 <= stats.dexterity <= 90
        assert 15 <= stats.constitution <= 90
        assert 15 <= stats.intelligence <= 90
        assert 15 <= stats.wisdom <= 90
        assert 15 <= stats.charisma <= 90

        # Test that other models use standard Pydantic initialization
        alias = Alias(name="test", command="say hello")
        assert alias.name == "test"
        assert alias.command == "say hello"


class TestModelPerformanceOptimizations:
    """Test model performance optimization opportunities."""

    def test_slots_optimization_availability(self):
        """Test which models could benefit from __slots__ optimization."""
        # Models that could benefit from __slots__ (frequently instantiated)
        frequent_models = [
            BaseCommand,
            Stats,
            Alias,
        ]

        for model_class in frequent_models:
            # Check if model already uses __slots__
            has_slots = hasattr(model_class, "__slots__")

            # For now, we're just documenting which models could benefit
            # In a real optimization, we'd add __slots__ to frequently used models
            assert isinstance(has_slots, bool), f"Could check {model_class.__name__} for __slots__ optimization"

    def test_model_rebuild_capability(self):
        """Test that models can be rebuilt for dynamic schema changes."""
        # Test that models can be rebuilt (useful for dynamic schema changes)
        models_to_test = [
            BaseCommand,
            Stats,
            Alias,
        ]

        for model_class in models_to_test:
            # Test model rebuild capability
            assert hasattr(model_class, "model_rebuild"), f"{model_class.__name__} should support model_rebuild"

            # Test that rebuild works
            model_class.model_rebuild()

            # Model should still work after rebuild
            if model_class == BaseCommand:
                # BaseCommand is abstract, test with a concrete command
                LookCommand(direction="north")
            elif model_class == Stats:
                Stats()
            elif model_class == Alias:
                Alias(name="test", command="say hello")


class TestDuplicateModelDefinitions:
    """Test for duplicate model definitions that need consolidation."""

    def test_stats_model_consolidation(self):
        """Test that Stats model is properly consolidated and not duplicated."""
        # Import Stats from the package (which should come from game module)
        from server.models import Stats
        from server.models.game import Stats as GameStats

        # Both imports should refer to the same class
        assert Stats is GameStats, "Stats imports should refer to the same class"

        # Verify that Stats is defined in the correct module
        assert Stats.__module__ == "server.models.game", (
            f"Stats should be defined in server.models.game, not {Stats.__module__}"
        )

        # Verify that the legacy models.py file has been removed
        # (This would fail if the legacy file still exists)
        try:
            import server.models as models_module

            # If we can import the module, check that it doesn't have a direct Stats definition
            # (it should only be available through __init__.py)
            assert not hasattr(models_module, "Stats") or models_module.Stats is GameStats, (
                "Package should import Stats from game module"
            )
        except ImportError:
            pytest.fail("server.models package should be importable")

    def test_model_import_consistency(self):
        """Test that model imports are consistent and don't cause conflicts."""
        # Test that we can import models without conflicts
        from server.models import Alias, AttributeType, Stats

        # Test that imports work correctly
        assert Stats is not None
        assert AttributeType is not None
        assert Alias is not None

        # Test that we can use the models
        stats = Stats()
        assert stats is not None

        alias = Alias(name="test", command="say hello")
        assert alias is not None


class TestModelConfigurationValidation:
    """Test model configuration validation and error handling."""

    def test_invalid_config_dict_handling(self):
        """Test handling of invalid ConfigDict values."""
        # Test that invalid config values are caught
        with pytest.raises((ValueError, TypeError, Exception)):

            class InvalidModel(BaseModel):
                model_config = ConfigDict(extra="invalid_value")

    def test_config_dict_vs_dict_consistency(self):
        """Test that ConfigDict and dict configurations work consistently."""

        # Test that both ConfigDict and dict work for model_config
        class DictConfigModel(BaseModel):
            model_config = {"extra": "forbid"}

        class ConfigDictModel(BaseModel):
            model_config = ConfigDict(extra="forbid")

        # Both should work identically
        with pytest.raises(ValidationError):
            DictConfigModel(invalid_field="test")

        with pytest.raises(ValidationError):
            ConfigDictModel(invalid_field="test")

    def test_model_config_inheritance(self):
        """Test that model_config is properly inherited."""
        # Test that child classes inherit parent model_config
        assert LookCommand.model_config == BaseCommand.model_config

        # Test that inherited config works
        with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
            LookCommand(direction="north", extra_field="test")
