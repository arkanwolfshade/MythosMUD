# Test/Production Environment Separation

## Problem

The MythosMUD server was experiencing test/production cross-contamination where `main.py` was behaving differently depending on whether it was running in tests or production. The issue was caused by:

1. **Hardcoded test logging**: `main.py` was hardcoded to use `_ensure_test_logging_initialized()` which disabled logging entirely
2. **No environment detection**: The server couldn't distinguish between test and production environments
3. **Configuration contamination**: Both environments were using the same configuration approach

## Solution

We implemented a simple and clean environment separation system using configuration files:

### 1. Configuration-Based Separation

The system uses two separate configuration files:
**Production**: `server/server_config.yaml`

**Test**: `server/test_server_config.yaml`

### 2. Automatic Test Detection

The config loader automatically detects when running under pytest and uses the test configuration:

```python
def _get_config_path() -> str:
    """Determine the appropriate config file path based on environment."""
    # Check if we're running under pytest

    import sys
    if "pytest" in sys.modules:
        if os.path.exists(_TEST_CONFIG_PATH):
            return _TEST_CONFIG_PATH

    # Check for explicit test mode environment variable

    if os.environ.get("MYTHOSMUD_TEST_MODE"):
        if os.path.exists(_TEST_CONFIG_PATH):
            return _TEST_CONFIG_PATH

    # Default to production config

    return _CONFIG_PATH
```

### 3. Configuration-Driven Logging

The main.py now uses configuration to determine logging behavior:

```python
def _ensure_logging_initialized():
    """Ensure logging is initialized only once."""
    global _logging_initialized
    if not _logging_initialized:
        # Get config to determine logging settings

        config = get_config()

        # Check if we should disable logging (for tests)

        disable_logging = config.get("disable_logging", False)

        if disable_logging:
            setup_logging(disable_logging=True)
        else:
            setup_logging()

        _logging_initialized = True
```

### 4. Configuration Files

**Production**: `server/server_config.yaml`

- Port: 54731
- Host: 0.0.0.0
- Database: `../data/players/local_players.db`
- Logging: Enabled (`disable_logging: false`)

**Test**: `server/test_server_config.yaml`

- Port: 4999
- Host: 127.0.0.1
- Database: `server/tests/data/players/unit_test_players.db`
- Logging: Disabled (`disable_logging: true`)

## Usage

### Production Environment

```bash
# Normal server startup (uses production config)

python -m uvicorn server.main:app --host 0.0.0.0 --port 54731
```

### Test Environment

```bash
# Automatic detection when running under pytest

python -m pytest

# Manual test mode

MYTHOSMUD_TEST_MODE=1 python -m uvicorn server.main:app
```

## Benefits

1. **Simple and clean**: No complex environment detection logic in main.py
2. **Configuration-driven**: All separation logic is in config files
3. **Automatic**: Works seamlessly under pytest without manual configuration
4. **Flexible**: Can be overridden with environment variables when needed
5. **Maintainable**: Clear configuration files for each environment

## Files Modified

`server/main.py`: Simplified to use config-driven logging

- `server/config_loader.py`: Added automatic test config detection
- `server/server_config.yaml`: Added `disable_logging: false`
- `server/test_server_config.yaml`: Added `disable_logging: true`
- `server/tests/test_config_loader.py`: Updated tests for new functionality

## Environment Variables

`MYTHOSMUD_TEST_MODE`: Set to "1" to force test mode

## Notes

As noted in the Pnakotic Manuscripts, proper organization of dimensional boundaries is essential for maintaining the delicate balance between order and chaos in our digital realm. This simplified solution ensures that our test and production environments remain properly separated through configuration files rather than complex detection logic.
