# Pydantic Testing Patterns

## FieldInfo Type Checker Issues

### Problem

When accessing nested Pydantic model attributes in tests, Pylint reports `E1101:no-member` errors because it sees nested
fields as `FieldInfo` instances rather than the actual config/model objects.

**Example Error:**

```text
Instance of 'FieldInfo' has no 'port' member
Instance of 'FieldInfo' has no 'url' member
Instance of 'FieldInfo' has no 'admin_password' member
```

### Root Cause

Pydantic uses `Field()` descriptors for nested models. Type checkers (Pylint, mypy) cannot always infer that accessing
`config.database` returns a `DatabaseConfig` instance rather than a `FieldInfo` descriptor.

### Solution Pattern

**Extract nested config objects before accessing their attributes.**

#### ❌ Incorrect Pattern (Causes Pylint Errors)

```python
def test_config_access():
    config = AppConfig()
    # Direct nested access triggers FieldInfo errors

    assert config.database.url == "postgresql://..."
    assert config.security.admin_password == "password"
    assert config.cors.allow_origins == ["http://localhost:5173"]
```

#### ✅ Correct Pattern (No Pylint Errors)

```python
def test_config_access():
    config = AppConfig()
    # Extract nested configs to avoid type checker FieldInfo issues
    # Pylint sees nested Pydantic fields as FieldInfo instances rather than the actual config objects

    database_config = config.database
    security_config = config.security
    cors_config = config.cors

    assert database_config.url == "postgresql://..."
    assert security_config.admin_password == "password"
    assert cors_config.allow_origins == ["http://localhost:5173"]
```

### When to Apply This Pattern

Apply this pattern when:

1. Accessing nested Pydantic model attributes in tests
2. Pylint reports `E1101:no-member` errors for nested field access
3. The nested field is a Pydantic model (not a primitive type)

### Alternative Approaches

#### Option 1: Pylint Suppression (Not Recommended for Tests)

In production code, you may see:

```python
# pylint: disable=no-member

database = self.database
if database.url:
    # ...
# pylint: enable=no-member

```

**Why not recommended for tests:** Suppression comments hide the issue rather than fixing it. Extracting the nested
config is clearer and more maintainable.

#### Option 2: Type Annotations (Advanced)

For complex scenarios, you can use type annotations:

```python
from server.config.models import DatabaseConfig

def test_config_access():
    config = AppConfig()
    database_config: DatabaseConfig = config.database
    assert database_config.url == "postgresql://..."
```

However, the simple extraction pattern is usually sufficient and more readable.

### Examples in Codebase

**Reference Implementation:**

- `server/tests/unit/infrastructure/test_config.py` - `test_app_config_loads_from_env()`
- `server/config/models.py` - `set_legacy_environment_variables()` (uses suppression, but in production code)

### Future Prevention

When writing new tests that access nested Pydantic models:

1. **Always extract nested configs first** before accessing their attributes
2. **Add a comment** explaining why (for future maintainers)
3. **Run Pylint** to catch these issues early
4. **Follow the established pattern** consistently across all test files

### Related Issues

Pydantic v2 Field descriptors

- Type inference limitations in static analysis tools
- Nested model access patterns

---

**Last Updated:** 2025-01-XX

**Related Files:**

- `server/tests/unit/infrastructure/test_config.py`
- `server/config/models.py`
