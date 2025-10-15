# ADR-003: Pydantic BaseSettings for Configuration Management

**Date**: 2025-10-11
**Status**: ✅ ACCEPTED
**Decision Makers**: Prof. Wolfshade, AI Assistant
**Context**: CRITICAL-2 Configuration Management Refactoring

---

## Context and Problem Statement

The configuration system used a 395-line custom YAML loader (`config_loader.py`) with:

1. **No Validation**: Configuration errors only discovered at runtime
2. **Mixed Sources**: YAML files + environment variables with unclear precedence
3. **Security Risks**: Hardcoded defaults for sensitive values (admin passwords, secret keys)
4. **Type Ambiguity**: No type hints or validation for configuration values
5. **Environment Confusion**: Difficult to distinguish between local/test/production configs

**Question**: How should we refactor configuration management for type safety and validation?

---

## Decision Drivers

- **Type Safety**: Must provide type-checked configuration access
- **Validation**: Must validate configuration at startup, not runtime
- **Environment Variables**: Must support environment-specific configuration
- **No Secrets in Code**: Must prevent hardcoded secrets
- **Developer Experience**: Should be easy to understand and use
- **Standard Practice**: Should follow Python best practices

---

## Considered Options

### Option 1: Pydantic BaseSettings
- **Pros**:
  - Automatic environment variable loading
  - Type-safe configuration access
  - Built-in validation with clear error messages
  - Nested configuration models
  - Excellent IDE support (autocomplete, type checking)
  - Industry standard (used by FastAPI, etc.)
  - Zero runtime overhead after initial load
- **Cons**:
  - Adds pydantic-settings dependency
  - Requires migration from YAML
- **Migration Effort**: Medium (2 days)

### Option 2: dataclasses + python-decouple
- **Pros**:
  - Lightweight
  - Uses stdlib dataclasses
  - Simple API
- **Cons**:
  - Less validation capabilities
  - Manual type checking required
  - No nested models
  - Less IDE support
- **Migration Effort**: Low (1 day)

### Option 3: dynaconf
- **Pros**:
  - Supports multiple formats (YAML, JSON, TOML, .env)
  - Environment-aware
  - Validation via external schemas
- **Cons**:
  - Less type safety
  - More complex API
  - Larger dependency
  - Overkill for our needs
- **Migration Effort**: High (3 days)

---

## Decision Outcome

**Chosen Option**: **Pydantic BaseSettings v2.0+**

**Rationale**:

1. **Type Safety**: Configuration access is type-checked at compile time and runtime
2. **Validation**: Invalid configuration fails fast at startup with clear messages
3. **Environment Support**: Automatic `.env` file loading with environment-specific files
4. **Security**: No hardcoded secrets - all sensitive values required via environment variables
5. **Developer Experience**: Excellent IDE support with autocomplete and type hints
6. **FastAPI Integration**: Already using Pydantic for API validation - consistency

**Trade-offs Accepted**:
- Migration effort (2 days - completed)
- Pydantic dependency (already a dependency for FastAPI)
- Breaking change (YAML no longer supported - acceptable per requirements)

---

## Implementation Details

### Configuration Models

```python
# server/config/models.py
from pydantic import Field
from pydantic_settings import BaseSettings

class ServerConfig(BaseSettings):
    host: str = Field("127.0.0.1", env="SERVER_HOST")
    port: int = Field(..., env="SERVER_PORT")  # Required!

    model_config = {
        "env_prefix": "SERVER_",
        "case_sensitive": False,
        "extra": "ignore",  # Ignore unknown env vars
    }

class AppConfig(BaseSettings):
    server: ServerConfig = Field(default_factory=ServerConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    nats: NATSConfig = Field(default_factory=NATSConfig)
    # ...
```

### Singleton Access Pattern

```python
# server/config/__init__.py
from functools import lru_cache

@lru_cache()
def get_config() -> AppConfig:
    """Get application configuration (singleton)."""
    return AppConfig()
```

### Environment Files

- `.env.local.example` - Local development template
- `.env.unit_test.example` - Unit test template
- `.env.e2e_test.example` - E2E test template
- `.env.production.example` - Production template

---

## Consequences

### Positive

✅ **Type-Safe Access**: `config.server.port` instead of `config.get("server", {}).get("port")`
✅ **Validation at Startup**: Invalid config fails immediately with clear error messages
✅ **Required Fields**: Pydantic enforces required fields (no silent defaults for secrets)
✅ **Environment Isolation**: Clear separation between local/test/production configs
✅ **IDE Support**: Autocomplete and type checking throughout codebase
✅ **Security**: No hardcoded secrets possible

### Negative

⚠️ **Breaking Change**: YAML config files no longer supported
⚠️ **Migration Required**: All 50+ files updated to use new config
⚠️ **Test Environment Setup**: Required `conftest.py` to load env vars before tests

### Neutral

ℹ️ **Environment Variables**: Must set environment variables (standard practice anyway)
ℹ️ **Backward Compatibility**: Added `to_legacy_dict()` methods for gradual migration

---

## Validation

- ✅ All configuration models validated successfully
- ✅ All environment files updated and documented
- ✅ 50+ files migrated to new configuration system
- ✅ All tests passing (3,226 tests)
- ✅ No regressions introduced
- ✅ Configuration tests added and passing

---

## References

- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App - Config](https://12factor.net/config)
- Implementation: `server/config/models.py`
- Tests: `server/tests/test_config.py`
- Environment Files: `.env.*.example`

---

## Related ADRs

- ADR-001: XState for Frontend Connection FSM
- ADR-002: python-statemachine for Backend Connection FSM
- ADR-004: Circuit Breaker + Dead Letter Queue for NATS
