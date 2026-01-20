# Complexity Refactoring Test Plan

**Date**: 2025-01-29
**Purpose**: Verify no regressions after complexity refactoring of 12 functions (Phase 1 & 2)

## 🎯 Test Categories

### 1. Application Startup & CORS (create_app)

**Test Cases:**
- [ ] **Server Startup**: Start server and verify it initializes without errors
- [ ] **CORS Configuration**:
  - [ ] Test with default CORS settings (localhost:5173)
  - [ ] Test with environment variable overrides (`CORS_ALLOW_ORIGINS`, `ALLOWED_ORIGINS`)
  - [ ] Test with JSON array format: `CORS_ALLOW_ORIGINS='["http://localhost:5173","http://127.0.0.1:5173"]'`
  - [ ] Test with comma-separated format: `CORS_ALLOW_ORIGINS='http://localhost:5173,http://127.0.0.1:5173'`
  - [ ] Verify CORS headers are correctly set in API responses
- [ ] **Error Handling**: Verify graceful fallback when config is unavailable

**Expected Results:**
- Server starts successfully
- CORS headers match configuration
- Environment variables take precedence over config file

---

### 2. WebSocket Connections

**Test Cases:**
- [ ] **Modern WebSocket Route** (`/api/ws`):
  - [ ] Connect with JWT token via subprotocol header
  - [ ] Connect with JWT token via query parameter (fallback)
  - [ ] Test with `bearer, <token>` format in subprotocol
  - [ ] Test with plain `<token>` in subprotocol
  - [ ] Verify connection manager validation
  - [ ] Test error handling when services unavailable
- [ ] **Deprecated WebSocket Route** (`/api/ws/{player_id}`):
  - [ ] Connect with valid player_id in path
  - [ ] Connect with invalid player_id (should resolve from token)
  - [ ] Connect with token in query params
  - [ ] Verify player ID resolution from token payload
  - [ ] Test error handling when player ID cannot be resolved
- [ ] **Connection Stability**:
  - [ ] Maintain connection for extended period (5+ minutes)
  - [ ] Send commands through WebSocket
  - [ ] Receive real-time updates via WebSocket

**Expected Results:**
- All connection methods work correctly
- Token parsing handles all supported formats
- Proper error messages when connection fails

---

### 3. Room Operations

**Test Cases:**
- [ ] **Room Listing** (`GET /api/rooms?plane=X&zone=Y`):
  - [ ] List rooms without filtering
  - [ ] List rooms with `filter_explored=true` as non-admin user
  - [ ] List rooms with `filter_explored=true` as admin user (should see all)
  - [ ] List rooms with sub_zone parameter
  - [ ] List rooms with `include_exits=true/false`
  - [ ] Verify room coordinates (map_x, map_y) are included
  - [ ] Verify exits are loaded correctly when requested
- [ ] **Room Coordinates**:
  - [ ] View rooms that have coordinates
  - [ ] View rooms without coordinates (should auto-generate)
  - [ ] Verify coordinate generation for new zones
  - [ ] Check ASCII map rendering with coordinates
- [ ] **Room Exits**:
  - [ ] Verify all exits are loaded correctly
  - [ ] Test navigation through exits
  - [ ] Verify exit directions match room data

**Expected Results:**
- Room listing works with all parameter combinations
- Exploration filtering works for non-admins, skipped for admins
- Coordinates generate automatically when missing
- All exits are correctly loaded and navigable

---

### 4. Container Operations

**Test Cases:**
- [ ] **Loot All Items** (`POST /api/containers/loot-all`):
  - [ ] Loot all items from a container with valid mutation token
  - [ ] Test with container that has multiple item stacks
  - [ ] Test with container that exceeds player inventory capacity
  - [ ] Test with locked container (should fail with 423)
  - [ ] Test with non-existent container (should fail with 404)
  - [ ] Test with invalid mutation token (should fail with 412)
  - [ ] Test with container you don't have access to (should fail with 403)
  - [ ] Verify items are transferred to player inventory
  - [ ] Verify container state is updated correctly
  - [ ] Verify WebSocket events are emitted for container updates
  - [ ] Test rate limiting (20 requests per 60 seconds)

**Expected Results:**
- Successful looting transfers all eligible items
- Proper error codes for all failure scenarios
- Container and inventory states update correctly
- WebSocket events notify clients of changes

---

### 5. Player Respawn

**Test Cases:**
- [ ] **Normal Respawn** (`POST /api/players/respawn`):
  - [ ] Respawn a dead player (DP <= -10)
  - [ ] Verify player moves to respawn location
  - [ ] Verify DP is restored to 100
  - [ ] Test respawn when player is not dead (should fail with 403)
  - [ ] Test respawn when player not found (should fail with 404)
  - [ ] Test rate limiting (1 request per 5 seconds)
- [ ] **Delirium Respawn** (`POST /api/players/respawn-delirium`):
  - [ ] Respawn a delirious player (lucidity <= -10)
  - [ ] Verify player moves to Sanitarium
  - [ ] Verify lucidity is restored to 10
  - [ ] Test respawn when player is not delirious (should fail with 403)
  - [ ] Test respawn when player not found (should fail with 404)
  - [ ] Test rate limiting (1 request per 5 seconds)

**Expected Results:**
- Successful respawns restore player state correctly
- Proper validation prevents invalid respawns
- Error messages are clear and helpful

---

### 6. Game Tick Processing

**Test Cases:**
- [ ] **Status Effects Processing**:
  - [ ] Apply damage-over-time effect to player
  - [ ] Apply heal-over-time effect to player
  - [ ] Verify effects process correctly each tick
  - [ ] Verify effects expire when duration reaches 0
  - [ ] Verify player stats update correctly
  - [ ] Test with multiple status effects simultaneously
  - [ ] Verify effects are saved to database
- [ ] **MP Regeneration**:
  - [ ] Verify MP regenerates for online players
  - [ ] Test MP regeneration rate
  - [ ] Verify MP doesn't exceed maximum
  - [ ] Test with players at different MP levels
- [ ] **Corpse Cleanup**:
  - [ ] Create a corpse container
  - [ ] Wait for decay time (60 ticks = 1 minute)
  - [ ] Verify corpse is cleaned up automatically
  - [ ] Verify WebSocket events are emitted for decayed containers
  - [ ] Test with multiple decayed corpses
  - [ ] Verify cleanup logging

**Expected Results:**
- Status effects process correctly each tick
- MP regenerates at expected rate
- Corpses are cleaned up after decay period
- All game tick processes run without errors

---

### 7. Integration Tests

**Test Cases:**
- [ ] **Full Gameplay Flow**:
  - [ ] Login → Connect WebSocket → Move between rooms → View map
  - [ ] Open container → Loot items → Check inventory
  - [ ] Take damage → Apply status effect → Wait for tick → Verify effect processes
  - [ ] Die → Respawn → Verify state restoration
  - [ ] Become delirious → Respawn from delirium → Verify state restoration
- [ ] **Multi-Player Scenarios**:
  - [ ] Multiple players in same room
  - [ ] Multiple players looting from same container
  - [ ] Multiple players with status effects
- [ ] **Error Recovery**:
  - [ ] Test behavior when services are temporarily unavailable
  - [ ] Test behavior with invalid data
  - [ ] Verify error messages are user-friendly

**Expected Results:**
- All gameplay flows work end-to-end
- Multi-player scenarios handle correctly
- Error recovery is graceful

---

## 🔍 Specific Edge Cases to Test

### CORS Configuration
- Empty environment variables
- Malformed JSON in environment variables
- Multiple CORS origin formats

### WebSocket Token Parsing
- Token with extra whitespace
- Token in different header formats
- Missing token (should fall back gracefully)

### Room Operations
- Rooms with no exits
- Rooms with missing coordinates
- Empty zone/subzone
- Non-existent plane/zone

### Container Operations
- Container with 0 items
- Container with items that exceed capacity
- Container in different room states

### Respawn Operations
- Respawn while already at respawn location
- Respawn with invalid user state
- Concurrent respawn requests

### Game Tick Processing
- Player logs out during status effect processing
- Multiple effects expiring simultaneously
- MP regeneration at maximum MP
- Corpse cleanup with no decayed corpses

---

## 📊 Performance Checks

- [ ] Server startup time (should be similar to before)
- [ ] WebSocket connection time (should be < 1 second)
- [ ] Room listing response time (should be < 500ms)
- [ ] Container loot-all operation time (should be < 1 second)
- [ ] Game tick processing time (should be < 100ms per tick)

---

## ✅ Success Criteria

All tests should pass with:
- ✅ No new errors in server logs
- ✅ No regressions in functionality
- ✅ Response times similar to or better than before
- ✅ Error messages are clear and helpful
- ✅ All edge cases handled gracefully

---

## 🚨 Red Flags to Watch For

- Server fails to start
- WebSocket connections fail
- CORS errors in browser console
- Missing room data or exits
- Items not transferring correctly
- Respawn not working
- Status effects not processing
- MP not regenerating
- Corpses not cleaning up
- Error messages are unclear or missing

---

## 📝 Notes

- Test with both admin and non-admin accounts
- Test with multiple browser sessions
- Monitor server logs during all tests
- Test with various game states (healthy, injured, dead, delirious)
- Verify database state after operations
