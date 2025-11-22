"""
Tests for Pydantic-based configuration system.

These tests verify that the new configuration system properly validates
configuration fields, handles environment variables, and fails gracefully
with clear error messages.
"""

import os

import pytest
from pydantic import ValidationError

from server.config import AppConfig, get_config, reset_config
from server.config.models import (
    ChatConfig,
    CORSConfig,
    DatabaseConfig,
    GameConfig,
    LoggingConfig,
    NATSConfig,
    PlayerStatsConfig,
    SecurityConfig,
    ServerConfig,
)


class TestServerConfig:
    """Test ServerConfig validation."""

    def test_valid_server_config(self):
        """Test valid server configuration."""
        config = ServerConfig(port=8080)
        assert config.host == "127.0.0.1"
        assert config.port == 8080

    def test_invalid_port_too_low(self):
        """Test port validation rejects values below 1024."""
        with pytest.raises(ValidationError) as exc_info:
            ServerConfig(port=80)
        assert "Port must be between 1024 and 65535" in str(exc_info.value)

    def test_invalid_port_too_high(self):
        """Test port validation rejects values above 65535."""
        with pytest.raises(ValidationError) as exc_info:
            ServerConfig(port=70000)
        assert "Port must be between 1024 and 65535" in str(exc_info.value)

    def test_port_required(self, monkeypatch):
        """Test that port is required (no default)."""
        # Clear environment variable to test validation
        monkeypatch.delenv("SERVER_PORT", raising=False)

        # Port is required via Field(...), should fail without it
        with pytest.raises(ValidationError):
            ServerConfig()


class TestDatabaseConfig:
    """Test DatabaseConfig validation."""

    def test_sqlite_url_rejected(self):
        """Test that SQLite database URLs are rejected."""
        with pytest.raises(ValidationError) as exc_info:
            DatabaseConfig(url="sqlite+aiosqlite:///data/test.db", npc_url="sqlite+aiosqlite:///data/npcs.db")
        assert "postgresql" in str(exc_info.value).lower() or "unsupported" in str(exc_info.value).lower()

    def test_valid_postgres_url(self):
        """Test valid PostgreSQL database URL."""
        config = DatabaseConfig(
            url="postgresql://user:pass@localhost/db", npc_url="postgresql://user:pass@localhost/npcs"
        )
        assert config.url == "postgresql://user:pass@localhost/db"

    def test_invalid_database_url(self):
        """Test invalid database URL is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            DatabaseConfig(url="mysql://localhost/db", npc_url="postgresql://localhost/npcs")
        assert "postgresql" in str(exc_info.value).lower() or "unsupported" in str(exc_info.value).lower()

    def test_database_url_required(self, monkeypatch):
        """Test that database URLs are required."""
        # Clear environment variables to test validation
        monkeypatch.delenv("DATABASE_URL", raising=False)
        monkeypatch.delenv("DATABASE_NPC_URL", raising=False)

        with pytest.raises(ValidationError):
            DatabaseConfig()


class TestNATSConfig:
    """Test NATSConfig validation."""

    def test_valid_nats_config(self, monkeypatch):
        """Test valid NATS configuration."""
        # In test environment, NATS is disabled by default (see conftest.py)
        # Temporarily enable it for this test to verify the default behavior
        monkeypatch.setenv("NATS_ENABLED", "true")
        config = NATSConfig()
        assert config.enabled is True
        assert config.url == "nats://localhost:4222"
        assert config.max_payload == 1048576

    def test_invalid_max_payload_too_small(self):
        """Test max payload validation rejects values below 1KB."""
        with pytest.raises(ValidationError) as exc_info:
            NATSConfig(max_payload=512)
        assert "Max payload must be between 1KB and 10MB" in str(exc_info.value)

    def test_invalid_max_payload_too_large(self):
        """Test max payload validation rejects values above 10MB."""
        with pytest.raises(ValidationError) as exc_info:
            NATSConfig(max_payload=20000000)
        assert "Max payload must be between 1KB and 10MB" in str(exc_info.value)

    def test_invalid_timeout(self):
        """Test timeout validation rejects negative values."""
        with pytest.raises(ValidationError) as exc_info:
            NATSConfig(connect_timeout=-1)
        assert "Value must be positive" in str(exc_info.value)


class TestSecurityConfig:
    """Test SecurityConfig validation."""

    def test_valid_security_config(self):
        """Test valid security configuration."""
        config = SecurityConfig(admin_password="test_password_123")
        assert config.admin_password == "test_password_123"
        assert config.invite_codes_file == "invites.json"

    def test_weak_password_rejected(self):
        """Test weak admin password is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            SecurityConfig(admin_password="short")
        assert "Admin password must be at least 8 characters" in str(exc_info.value)

    def test_admin_password_required(self, monkeypatch):
        """Test that admin password is required."""
        # Clear environment variable to test validation
        monkeypatch.delenv("MYTHOSMUD_ADMIN_PASSWORD", raising=False)

        with pytest.raises(ValidationError):
            SecurityConfig()


class TestLoggingConfig:
    """Test LoggingConfig validation."""

    def test_valid_logging_config(self):
        """Test valid logging configuration."""
        config = LoggingConfig(environment="unit_test", level="INFO")
        assert config.environment == "unit_test"
        assert config.level == "INFO"
        assert config.format == "colored"

    def test_invalid_environment(self):
        """Test invalid environment is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            LoggingConfig(environment="invalid")
        assert "Environment must be one of" in str(exc_info.value)

    def test_invalid_log_level(self):
        """Test invalid log level is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            LoggingConfig(environment="unit_test", level="TRACE")
        assert "Log level must be one of" in str(exc_info.value)

    def test_log_level_case_insensitive(self):
        """Test log level is converted to uppercase."""
        config = LoggingConfig(environment="unit_test", level="debug")
        assert config.level == "DEBUG"

    def test_invalid_log_format(self):
        """Test invalid log format is rejected.

        AI: Tests line 140 in config/models.py where invalid log formats are validated.
        Covers the ValueError raise path when format is not in valid_formats list.
        """
        with pytest.raises(ValidationError) as exc_info:
            LoggingConfig(environment="unit_test", level="INFO", format="invalid_format")
        assert "Log format must be one of" in str(exc_info.value)

    def test_to_legacy_dict(self):
        """Test conversion to legacy dict format."""
        config = LoggingConfig(environment="unit_test", level="DEBUG")
        legacy = config.to_legacy_dict()
        assert legacy["environment"] == "unit_test"
        assert legacy["level"] == "DEBUG"
        assert "rotation" in legacy
        # Unit test environment sets rotation_max_size to 10MB
        assert legacy["rotation"]["max_size"] == "10MB"


class TestGameConfig:
    """Test GameConfig validation."""

    def test_valid_game_config(self):
        """Test valid game configuration."""
        config = GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR"))
        assert config.default_player_room == "earth_arkhamcity_northside_intersection_derby_high"
        assert config.max_connections_per_player == 3

    def test_invalid_max_connections_too_low(self):
        """Test max connections validation rejects values below 1."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR"), max_connections_per_player=0)
        assert "Max connections per player must be between 1 and 10" in str(exc_info.value)

    def test_invalid_max_connections_too_high(self):
        """Test max connections validation rejects values above 10."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir=os.getenv("GAME_ALIASES_DIR"), max_connections_per_player=20)
        assert "Max connections per player must be between 1 and 10" in str(exc_info.value)

    def test_aliases_dir_required(self, monkeypatch):
        """Test that aliases_dir is required."""
        # Clear environment variable to test validation
        monkeypatch.delenv("GAME_ALIASES_DIR", raising=False)

        with pytest.raises(ValidationError):
            GameConfig()

    def test_empty_aliases_dir_rejected(self):
        """Test that empty aliases_dir is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            GameConfig(aliases_dir="")
        assert "Aliases directory must be specified" in str(exc_info.value)


class TestChatConfig:
    """Test ChatConfig validation."""

    def test_valid_chat_config(self, monkeypatch):
        """Test valid chat configuration."""
        # Clear environment variables to use defaults
        monkeypatch.delenv("CHAT_RATE_LIMIT_GLOBAL", raising=False)
        monkeypatch.delenv("CHAT_RATE_LIMIT_WHISPER", raising=False)
        monkeypatch.delenv("CHAT_PROFANITY_FILTER", raising=False)

        config = ChatConfig()
        assert config.rate_limit_global == 10
        assert config.rate_limit_whisper == 5
        assert config.profanity_filter is True

    def test_invalid_rate_limit_too_low(self):
        """Test rate limit validation rejects values below 1."""
        with pytest.raises(ValidationError) as exc_info:
            ChatConfig(rate_limit_global=0)
        assert "Rate limit must be between 1 and 1000" in str(exc_info.value)

    def test_invalid_rate_limit_too_high(self):
        """Test rate limit validation rejects values above 1000."""
        with pytest.raises(ValidationError) as exc_info:
            ChatConfig(rate_limit_global=2000)
        assert "Rate limit must be between 1 and 1000" in str(exc_info.value)


class TestCORSConfig:
    """Test CORSConfig validation and parsing."""

    def test_default_cors_config(self):
        """Test default CORS configuration values."""
        config = CORSConfig()

        assert config.allow_origins == ["http://localhost:5173", "http://127.0.0.1:5173"]
        assert config.allow_credentials is True
        assert all(method in config.allow_methods for method in ["GET", "POST", "PUT", "DELETE", "OPTIONS"])
        assert "Content-Type" in config.allow_headers
        assert config.max_age == 600

    def test_cors_env_overrides(self, monkeypatch):
        """Test that environment variables override defaults."""
        monkeypatch.setenv("CORS_ORIGINS", "https://example.com, https://alt.example.com")
        monkeypatch.setenv("CORS_ALLOW_METHODS", "GET,POST")
        monkeypatch.setenv("CORS_ALLOW_HEADERS", "Content-Type,Authorization")
        monkeypatch.setenv("CORS_MAX_AGE", "1200")

        config = CORSConfig()

        assert config.allow_origins == ["https://example.com", "https://alt.example.com"]
        assert config.allow_methods == ["GET", "POST"]
        assert config.allow_headers == ["Content-Type", "Authorization"]
        assert config.max_age == 1200

    def test_cors_backwards_compatible_aliases(self, monkeypatch):
        """Test legacy environment variable aliases such as ALLOWED_ORIGINS."""
        monkeypatch.delenv("CORS_ORIGINS", raising=False)
        monkeypatch.setenv("ALLOWED_ORIGINS", "https://legacy.example.com")

        config = CORSConfig()

        assert config.allow_origins == ["https://legacy.example.com"]

    def test_empty_origins_rejected(self):
        """Test that empty origin lists are rejected for security."""
        with pytest.raises(ValidationError):
            CORSConfig(allow_origins=[])


class TestPlayerStatsConfig:
    """Test PlayerStatsConfig validation."""

    def test_valid_player_stats_config(self, monkeypatch):
        """Test valid player stats configuration."""
        # Clear any environment variables that might override defaults
        monkeypatch.delenv("DEFAULT_STATS_STRENGTH", raising=False)
        monkeypatch.delenv("DEFAULT_STATS_DEXTERITY", raising=False)
        monkeypatch.delenv("DEFAULT_STATS_CONSTITUTION", raising=False)
        monkeypatch.delenv("DEFAULT_STATS_INTELLIGENCE", raising=False)
        monkeypatch.delenv("DEFAULT_STATS_WISDOM", raising=False)
        monkeypatch.delenv("DEFAULT_STATS_CHARISMA", raising=False)

        config = PlayerStatsConfig()
        assert config.strength == 50
        assert config.dexterity == 50
        assert config.constitution == 50
        assert config.intelligence == 50
        assert config.wisdom == 50
        assert config.charisma == 50
        assert config.max_health == 100

    def test_invalid_stat_too_low(self):
        """Test stat validation rejects values below 1."""
        with pytest.raises(ValidationError) as exc_info:
            PlayerStatsConfig(strength=0)
        assert "Stats must be between 1 and 100" in str(exc_info.value)

    def test_invalid_stat_too_high(self):
        """Test stat validation rejects values above 100."""
        with pytest.raises(ValidationError) as exc_info:
            PlayerStatsConfig(dexterity=101)
        assert "Stats must be between 1 and 100" in str(exc_info.value)

    def test_invalid_health_too_low(self):
        """Test health validation rejects values below 1."""
        with pytest.raises(ValidationError) as exc_info:
            PlayerStatsConfig(max_health=0)
        assert "Health/sanity must be between 1 and 1000" in str(exc_info.value)

    def test_to_dict_format(self):
        """Test conversion to dict format."""
        config = PlayerStatsConfig(strength=75, max_health=150)
        stats_dict = config.to_dict()
        assert stats_dict["strength"] == 75
        assert stats_dict["max_health"] == 150
        assert "dexterity" in stats_dict


class TestAppConfig:
    """Test AppConfig integration."""

    @pytest.fixture(autouse=True)
    def setup_test_env(self, monkeypatch):
        """Set up test environment variables."""
        # Set required environment variables - PostgreSQL only
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_admin_pass")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

        # Reset config cache before each test
        reset_config()

        yield

        # Clean up after test
        reset_config()

    def test_app_config_loads_from_env(self):
        """Test that AppConfig loads from environment variables."""
        config = AppConfig()
        assert config.server.port == 54731
        assert config.database.url == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
        assert config.security.admin_password == "test_admin_pass"
        assert config.logging.environment == "unit_test"
        assert config.cors.allow_origins == ["http://localhost:5173", "http://127.0.0.1:5173"]
        assert config.cors.allow_credentials is True

    def test_app_config_sets_environment_variables(self):
        """Test that AppConfig sets environment variables for legacy compatibility."""
        # Instantiate config to trigger environment variable setup
        AppConfig()
        # Check that DATABASE_URL environment variable is set
        assert os.environ.get("DATABASE_URL") == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
        assert os.environ.get("NPC_DATABASE_URL") == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
        assert os.environ.get("ALIASES_DIR") == os.environ.get("GAME_ALIASES_DIR")

    def test_to_legacy_dict_format(self, monkeypatch):
        """Test conversion to legacy dict format."""
        # Enable NATS for this test (it's disabled by default in test environment)
        monkeypatch.setenv("NATS_ENABLED", "true")

        config = AppConfig()
        legacy = config.to_legacy_dict()

        # Test top-level fields
        assert legacy["host"] == "127.0.0.1"
        assert legacy["port"] == 54731
        assert legacy["database_url"] == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
        assert legacy["admin_password"] == "test_admin_pass"

        # Test nested dicts
        assert isinstance(legacy["logging"], dict)
        assert legacy["logging"]["environment"] == "unit_test"
        assert isinstance(legacy["nats"], dict)
        assert legacy["nats"]["enabled"] is True
        assert isinstance(legacy["chat"], dict)
        assert isinstance(legacy["default_player_stats"], dict)
        assert "cors" in legacy
        assert legacy["cors"]["allow_origins"] == ["http://localhost:5173", "http://127.0.0.1:5173"]

    def test_get_config_singleton(self):
        """Test that get_config returns singleton instance."""
        config1 = get_config()
        config2 = get_config()
        assert config1 is config2

    def test_reset_config_clears_cache(self):
        """Test that reset_config clears the singleton cache."""
        config1 = get_config()
        reset_config()
        config2 = get_config()
        # After reset, we get a new instance
        assert config1 is not config2


class TestConfigurationValidation:
    """Test configuration validation scenarios."""

    def test_missing_required_port(self, monkeypatch):
        """Test that missing required port raises ValidationError."""
        # Clear environment variable
        monkeypatch.delenv("SERVER_PORT", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            ServerConfig()
        error_str = str(exc_info.value)
        assert "port" in error_str.lower()

    def test_missing_required_database_url(self, monkeypatch):
        """Test that missing required database_url raises ValidationError."""
        # Clear environment variables
        monkeypatch.delenv("DATABASE_URL", raising=False)
        monkeypatch.delenv("DATABASE_NPC_URL", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            DatabaseConfig()
        error_str = str(exc_info.value)
        assert "url" in error_str.lower()

    def test_missing_required_admin_password(self, monkeypatch):
        """Test that missing required admin_password raises ValidationError."""
        # Clear environment variable
        monkeypatch.delenv("MYTHOSMUD_ADMIN_PASSWORD", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            SecurityConfig()
        error_str = str(exc_info.value)
        assert "admin_password" in error_str.lower()

    def test_missing_required_logging_environment(self, monkeypatch):
        """Test that missing required logging environment raises ValidationError."""
        # Clear environment variable
        monkeypatch.delenv("LOGGING_ENVIRONMENT", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            LoggingConfig()
        error_str = str(exc_info.value)
        assert "environment" in error_str.lower()


class TestEnvironmentVariableLoading:
    """Test loading configuration from environment variables."""

    def test_server_config_from_env(self, monkeypatch):
        """Test ServerConfig loads from environment variables with prefix."""
        monkeypatch.setenv("SERVER_HOST", "0.0.0.0")
        monkeypatch.setenv("SERVER_PORT", "9000")

        config = ServerConfig(port=9000)  # Still need to provide port as it's required
        assert config.host == "0.0.0.0"  # But this comes from env
        assert config.port == 9000

    def test_database_config_from_env(self, monkeypatch):
        """Test DatabaseConfig loads from environment variables with prefix."""
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")

        config = DatabaseConfig()
        assert config.url == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
        assert config.npc_url == "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"

    def test_logging_config_from_env(self, monkeypatch):
        """Test LoggingConfig loads from environment variables with prefix."""
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("LOGGING_LEVEL", "warning")
        monkeypatch.setenv("LOGGING_FORMAT", "json")

        config = LoggingConfig()
        assert config.environment == "unit_test"
        assert config.level == "WARNING"  # Should be uppercased
        assert config.format == "json"

    def test_nats_config_from_env(self, monkeypatch):
        """Test NATSConfig loads from environment variables with prefix."""
        monkeypatch.setenv("NATS_URL", "nats://prod-nats:4222")
        monkeypatch.setenv("NATS_ENABLED", "false")
        monkeypatch.setenv("NATS_MAX_PAYLOAD", "2097152")

        config = NATSConfig()
        assert config.url == "nats://prod-nats:4222"
        assert config.enabled is False
        assert config.max_payload == 2097152


class TestLegacyDictConversion:
    """Test conversion to legacy dictionary format."""

    def test_app_config_to_legacy_dict_structure(self, monkeypatch):
        """Test that AppConfig.to_legacy_dict() produces correct structure."""
        # Set up environment
        monkeypatch.setenv("SERVER_PORT", "54731")
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
        monkeypatch.setenv("MYTHOSMUD_ADMIN_PASSWORD", "test_password")
        monkeypatch.setenv("LOGGING_ENVIRONMENT", "unit_test")
        monkeypatch.setenv("GAME_ALIASES_DIR", "data/aliases")

        config = AppConfig()
        legacy = config.to_legacy_dict()

        # Verify structure matches legacy format
        assert "host" in legacy
        assert "port" in legacy
        assert "database_url" in legacy
        assert "logging" in legacy
        assert isinstance(legacy["logging"], dict)
        assert "nats" in legacy
        assert isinstance(legacy["nats"], dict)
        assert "chat" in legacy
        assert isinstance(legacy["chat"], dict)
        assert "default_player_stats" in legacy
        assert isinstance(legacy["default_player_stats"], dict)

    def test_logging_config_to_legacy_dict(self):
        """Test LoggingConfig.to_legacy_dict() produces correct structure."""
        # Explicitly set rotation parameters to test conversion
        config = LoggingConfig(
            environment="unit_test", level="DEBUG", rotation_max_size="100MB", rotation_backup_count=5
        )
        legacy = config.to_legacy_dict()

        assert legacy["environment"] == "unit_test"
        assert legacy["level"] == "DEBUG"
        assert legacy["format"] == "colored"
        assert "rotation" in legacy
        assert isinstance(legacy["rotation"], dict)
        assert legacy["rotation"]["max_size"] == "100MB"
        assert legacy["rotation"]["backup_count"] == 5

    def test_player_stats_to_dict(self, monkeypatch):
        """Test PlayerStatsConfig.to_dict() produces correct structure."""
        # Clear any environment variables that might override defaults
        monkeypatch.delenv("DEFAULT_STATS_DEXTERITY", raising=False)
        config = PlayerStatsConfig(strength=75, health=80)
        stats_dict = config.to_dict()

        assert stats_dict["strength"] == 75
        assert stats_dict["health"] == 80
        assert stats_dict["dexterity"] == 50  # Default value
        assert len(stats_dict) == 13  # All 13 stats present


class TestConfigValidationEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_string_database_url(self):
        """Test that empty string database URL is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            DatabaseConfig(url="", npc_url="postgresql://localhost/test")
        assert "Database URL cannot be empty" in str(exc_info.value)

    def test_boundary_port_values(self):
        """Test boundary port values."""
        # Minimum valid port
        config = ServerConfig(port=1024)
        assert config.port == 1024

        # Maximum valid port
        config = ServerConfig(port=65535)
        assert config.port == 65535

        # Below minimum
        with pytest.raises(ValidationError):
            ServerConfig(port=1023)

        # Above maximum
        with pytest.raises(ValidationError):
            ServerConfig(port=65536)

    def test_boundary_stat_values(self):
        """Test boundary stat values."""
        # Minimum valid stat
        config = PlayerStatsConfig(strength=1)
        assert config.strength == 1

        # Maximum valid stat
        config = PlayerStatsConfig(strength=20)
        assert config.strength == 20

        # Below minimum
        with pytest.raises(ValidationError):
            PlayerStatsConfig(strength=0)

        # Above maximum
        with pytest.raises(ValidationError):
            PlayerStatsConfig(strength=21)


class TestConfigErrorMessages:
    """Test that configuration errors provide clear, actionable messages."""

    def test_port_error_message_clarity(self):
        """Test that port validation error is clear."""
        with pytest.raises(ValidationError) as exc_info:
            ServerConfig(port=80)
        error = str(exc_info.value)
        assert "1024" in error
        assert "65535" in error

    def test_environment_error_message_clarity(self):
        """Test that environment validation error is clear."""
        with pytest.raises(ValidationError) as exc_info:
            LoggingConfig(environment="staging")
        error = str(exc_info.value)
        # Verify error message mentions environment validation
        assert "environment" in error.lower()

    def test_database_url_error_message_clarity(self):
        """Test that database URL validation error is clear."""
        with pytest.raises(ValidationError) as exc_info:
            DatabaseConfig(url="mongodb://localhost/db", npc_url="postgresql://localhost/test")
        error = str(exc_info.value)
        assert "postgresql" in error.lower() or "unsupported" in error.lower()
