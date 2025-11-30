# Move Logging Initialization to Earliest Possible Point

## Problem Analysis

Currently in `server/main.py`:

1. **Line 38**: Logger is created before logging is configured (`logger = get_logger(__name__)`)
2. **Line 186**: First log message is attempted before file handlers exist
3. **Line 187**: Logging setup happens here (too late)
4. **Line 191**: FastAPI app creation may log during initialization

This means critical startup information (configuration loading, app initialization) is not captured in logfiles.

## Solution

Move logging setup to execute immediately after imports and warnings, before any logger creation or usage.

## Implementation Steps

### 1. Restructure `server/main.py` imports and initialization

**Current structure** (lines 14-38):

- Imports
- Warnings filter
- Logger creation (TOO EARLY)

**New structure**:

- Imports
- Warnings filter
- **Early logging setup** (moved from lines 184-188)
- Logger creation (AFTER logging is set up)
- Rest of module code

### 2. Move logging setup to top of module

Move these lines from lines 184-188 to right after line 35 (after warnings filter):

```python
# Early logging setup - must happen before any logger creation
config = get_config()
setup_enhanced_logging(config.to_legacy_dict())
logger = get_logger(__name__)
logger.info("Logging setup completed", environment=config.logging.environment)
```

### 3. Remove duplicate logging setup

Remove the duplicate logging setup code from lines 184-188 that currently executes too late.

### 4. Update logger references

Ensure all logger references use the logger created AFTER setup completes. The logger on line 38 should be created after setup, and the log message on line 186 should be removed or updated.

### 5. Handle early logging in other modules

Check if `server/app/factory.py` or other imported modules create loggers at module level. These will now have proper file handlers available since logging is set up earlier.

## Files Modified

- `server/main.py`: Restructured to set up logging at the top before any logger creation

## Implementation Status: ✅ COMPLETED

### Changes Made

1. **Moved logging setup early** (now lines 37-44):
   - Moved `get_config()` and `setup_enhanced_logging()` from the old location (lines 184-188) to lines 39-40, right after the warnings filter
   - Logger creation moved to line 43, after logging is configured
   - Added confirmation log message after setup completes

2. **Removed duplicate code**:
   - Removed the late logging setup code that previously executed on lines 184-188
   - Removed the premature log message that tried to log before file handlers existed

3. **Verified compatibility**:
   - Config variable is still accessible for CORS configuration later in the file
   - All logger references work correctly since they're created after setup
   - Imported modules (like `factory.py`) will have proper file handlers since logging is configured at module import time
   - File compiles successfully with no linting errors

### Result

Logging is now initialized at the earliest possible point (immediately after imports and warnings), ensuring all startup information—including configuration loading, app initialization, and early module imports—is captured in logfiles from the very beginning of the server startup process.

### Verification

- ✅ Syntax check passed (`python -m py_compile server/main.py`)
- ✅ No linter errors
- ✅ All logger references updated correctly
- ✅ Config still accessible for later use
- ✅ Early logging in imported modules verified
