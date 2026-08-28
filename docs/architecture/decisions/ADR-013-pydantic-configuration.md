# ADR-013: Pydantic BaseSettings for Configuration Management

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Date**: 2025-10-11
**Status**: Accepted
**Provenance:** Recorded by the 2026-08 design/implementation audit. This document states 2025-10-11 but
first appears in this repository on 2026-02-26; its Context line notes it was **recovered from `.agent-os`**,
so the stated date is most likely the original decision date under earlier tooling and the later date is when
the record was transcribed here. Its section structure differs from ADR-001–010, consistent with that
separate origin. Unlike much of this ADR set, this one may well be a genuine contemporaneous decision record.
**Decision Makers**: Prof. Wolfshade, AI Assistant
**Context**: CRITICAL-2 Configuration Management Refactoring (recovered from .agent-os)

---

## 2. Context and Problem Statement

**[SPEC]**
The configuration system used a 395-line custom YAML loader (`config_loader.py`) with:

1. **No Validation**: Configuration errors only discovered at runtime
2. **Mixed Sources**: YAML files + environment variables with unclear precedence
3. **Security Risks**: Hardcoded defaults for sensitive values (admin passwords, secret keys)
4. **Type Ambiguity**: No type hints or validation for configuration values
5. **Environment Confusion**: Difficult to distinguish between local/test/production configs

**Question**: How should we refactor configuration management for type safety and validation?

---

## 3. Decision Drivers

**[SPEC]**
**Type Safety**: Must provide type-checked configuration access

**Validation**: Must validate configuration at startup, not runtime

**Environment Variables**: Must support environment-specific configuration

- **No Secrets in Code**: Must prevent hardcoded secrets
- **Developer Experience**: Should be easy to understand and use
- **Standard Practice**: Should follow Python best practices

---

## 4. Considered Options

**[SPEC]**

### Option 1: Pydantic BaseSettings

**Pros**:

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

**Pros**:

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

**Pros**:

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

## 5. Decision Outcome

**[SPEC]**
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

## 6. Implementation Details

**[NOTE]**

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

## 7. Consequences

**[SPEC]**

### Positive

- **Type-Safe Access**: `config.server.port` instead of `config.get("server", {}).get("port")`
- **Validation at Startup**: Invalid config fails immediately with clear error messages
- **Required Fields**: Pydantic enforces required fields (no silent defaults for secrets)
- **Environment Isolation**: Clear separation between local/test/production configs
- **IDE Support**: Autocomplete and type checking throughout codebase
- **Security**: No hardcoded secrets possible

### Negative

- **Breaking Change**: YAML config files no longer supported
- **Migration Required**: All 50+ files updated to use new config
- **Test Environment Setup**: Required `conftest.py` to load env vars before tests

### Neutral

- **Environment Variables**: Must set environment variables (standard practice anyway)
- **Backward Compatibility**: Added `to_legacy_dict()` methods for gradual migration

---

## 8. Validation

**[SPEC]**

- All configuration models validated successfully
- All environment files updated and documented
- 50+ files migrated to new configuration system
- All tests passing (3,226 tests)
- No regressions introduced
- Configuration tests added and passing

---

## 9. References

**[SPEC]**

- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App - Config](https://12factor.net/config)
- Implementation: `server/config/models.py`
- Tests: `server/tests/test_config.py`
- Environment Files: `.env.*.example`

---

## 10. Related ADRs

**[SPEC]**

- [ADR-011](ADR-011-xstate-frontend-fsm.md): XState for Frontend Connection FSM
- [ADR-012](ADR-012-python-statemachine-backend.md): python-statemachine for Backend Connection FSM
- [ADR-014](ADR-014-nats-error-boundaries.md): Circuit Breaker + Dead Letter Queue for NATS

## 11. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance (#721) |
