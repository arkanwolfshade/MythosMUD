# Lizard Complexity Analysis Findings

**Analysis Date**: 2025-01-29
**Threshold**: CCN > 10 (functions with cyclomatic complexity > 10 need attention)
**File NLOC Threshold**: 550 lines

## 🔴 CRITICAL: Functions Exceeding Threshold (CCN > 10)

### 1. `create_app` - CCN: 22

**Location**: `server/app/factory.py:46-187`
**NLOC**: 102
**Issue**: Application factory function with high complexity due to multiple conditional branches for CORS configuration and environment variable parsing.

**Recommendations**:

- Extract CORS configuration logic into a separate function: `_configure_cors()`
- Extract environment variable parsing into: `_parse_cors_env_vars()`
- Consider using a configuration class/object for CORS settings

**Priority**: HIGH - This is a critical application setup function

---

### 2. `_load_rooms_with_coordinates` - CCN: 12

**Location**: `server/api/maps.py:294-374`
**NLOC**: 62
**Issue**: Complex room loading logic with multiple conditional branches for coordinate processing and exit loading.

**Recommendations**:

- Extract exit loading logic into: `_load_room_exits(rooms, session)`
- Extract room dictionary construction into: `_build_room_dict(row)`
- Simplify zone pattern construction

**Priority**: MEDIUM - Core functionality but can be refactored

---

### 3. `_parse_websocket_token` - CCN: 12

**Location**: `server/api/real_time.py:75-100`
**NLOC**: 18
**Issue**: Complex token parsing logic with multiple fallback strategies and nested conditionals.

**Recommendations**:

- Extract subprotocol parsing into: `_parse_subprotocol_token(subproto_header)`
- Extract bearer token extraction into: `_extract_bearer_token(parts)`
- Simplify the fallback chain

**Priority**: MEDIUM - Security-critical but can be simplified

---

### 4. `_ensure_coordinates_generated` - CCN: 11

**Location**: `server/api/maps.py:94-117`
**NLOC**: 21
**Issue**: Multiple conditional branches for coordinate generation and filtering.

**Recommendations**:

- Extract coordinate generation check into: `_needs_coordinate_generation(rooms)`
- Extract filtering logic (already partially done with `_filter_explored_rooms`)

**Priority**: LOW - Just over threshold, minor refactoring needed

---

## 🟡 WARNING: Functions Near Threshold (CCN 9-10)

These functions are close to the threshold and should be monitored:

### Functions with CCN = 10

- `respawn_player_from_delirium` - `server/api/player_respawn.py:29-114` (CCN: 10, NLOC: 63)
- `_process_player_status_effects` - `server/app/game_tick_processing.py:183-220` (CCN: 10, NLOC: 28)
- `_process_mp_regeneration` - `server/app/game_tick_processing.py:320-349` (CCN: 10, NLOC: 24)

### Functions with CCN = 9

- `loot_all_items` - `server/api/container_endpoints_loot.py:51-194` (CCN: 9, NLOC: 97)
- `respawn_player` - `server/api/player_respawn.py:118-199` (CCN: 9, NLOC: 59)
- `websocket_endpoint_route` - `server/api/real_time.py:345-406` (CCN: 9, NLOC: 42)
- `list_rooms` - `server/api/rooms.py:94-193` (CCN: 9, NLOC: 78)
- `cleanup_decayed_corpses` - `server/app/game_tick_processing.py:414-492` (CCN: 10, NLOC: 69)
- `game_tick_loop` - `server/app/game_tick_processing.py:511-549` (CCN: 6, NLOC: 30)

**Note**: The `loot_all_items` function we recently worked on has CCN: 9, which is acceptable but could benefit from extracting exception handling into a dedicated handler function (similar to the pattern used in `container_endpoints_basic.py`).

---

## 📋 Recommended Action Plan

### Phase 1: Critical Functions (CCN > 10)

1. **`create_app`** - Extract CORS configuration logic
2. **`_load_rooms_with_coordinates`** - Extract exit loading and room dict construction
3. **`_parse_websocket_token`** - Extract subprotocol parsing logic
4. **`_ensure_coordinates_generated`** - Minor refactoring to reduce complexity

### Phase 2: High-Priority Near-Threshold (CCN 9-10)

1. **`loot_all_items`** - Extract exception handling into `handle_loot_all_exceptions()` (follow pattern from `container_endpoints_basic.py`)
2. **`respawn_player_from_delirium`** - Extract validation and state management logic
3. **`_process_player_status_effects`** - Extract effect processing into smaller functions

### Phase 3: Monitoring

- Monitor functions with CCN 8-9 during future development
- Add complexity checks to pre-commit hooks if not already present

---

## 🎯 Refactoring Patterns

### Pattern 1: Extract Exception Handling

```python
# Before: Exception handling inline (increases complexity)
async def endpoint():
    try:
        # ... logic ...
    except SpecificError1:
        # ... handle ...
    except SpecificError2:
        # ... handle ...
    # ... more exceptions ...

# After: Extract to handler function
async def endpoint():
    try:
        # ... logic ...
    except Exception as e:
        handle_endpoint_exceptions(e, request, current_user, context)
        raise AssertionError("handler should always raise") from e
```

### Pattern 2: Extract Configuration Logic

```python
# Before: Configuration inline
def create_app():
    if condition1:
        if condition2:
            # ... config ...
        else:
            # ... config ...
    # ... more conditions ...

# After: Extract configuration
def create_app():
    cors_config = _configure_cors()
    # ... use config ...
```

### Pattern 3: Extract Data Processing

```python
# Before: Complex data processing inline
async def load_data():
    for item in items:
        if condition1:
            if condition2:
                # ... process ...
            else:
                # ... process ...
        # ... more conditions ...

# After: Extract processing
async def load_data():
    processed_items = [_process_item(item) for item in items]
    return processed_items
```

---

## 📊 Summary Statistics

- **Total functions analyzed**: ~200+ (truncated output)
- **Functions exceeding threshold (CCN > 10)**: 4
- **Functions near threshold (CCN 9-10)**: 9
- **Most complex function**: `create_app` (CCN: 22)
- **Average complexity**: ~4-5 (estimated from visible output)

---

## ✅ Next Steps

1. **Immediate**: Address the 4 functions with CCN > 10
2. **Short-term**: Refactor `loot_all_items` to extract exception handling
3. **Long-term**: Establish complexity monitoring in CI/CD pipeline
4. **Documentation**: Update coding standards to include complexity guidelines
