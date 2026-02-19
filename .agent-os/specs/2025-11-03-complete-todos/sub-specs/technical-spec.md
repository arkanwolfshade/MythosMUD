# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-03-complete-todos/spec.md

## Technical Requirements

### Phase 1: Security Hardening

#### JWT Secret Configuration

**Requirement**: Move JWT secret from hardcoded "SECRET" to environment variable

**File**: `server/auth/users.py:132`

**Implementation**:

- Add `JWT_SECRET` to `.env` file with secure random value (min 32 characters)
- Update `get_jwt_strategy()` to read `settings.jwt_secret`
- Add startup validation that raises error if JWT_SECRET not set in production
- Add `JWT_TOKEN_LIFETIME` configuration (default: 3600 seconds)
- **Testing**: Verify token generation uses env secret, test startup failure without secret

#### Admin Role Checking

**Requirement**: Enforce admin role for broadcast endpoint

**File**: `server/api/game.py:56`

**Implementation**:

- Add dependency `require_admin_role()` using existing auth system
- Check user role from `current_user` dict
- Return `HTTPException(status_code=403)` for non-admin users
- Log unauthorized access attempts with user info
- **Testing**: Unit test with admin/non-admin users, integration test with real auth

#### CSRF Validation for WebSocket

**Requirement**: Validate CSRF tokens on WebSocket messages

**File**: `server/realtime/websocket_handler.py:284`

**Implementation**:

- Generate CSRF token on WebSocket connection establishment
- Include token in connection handshake response
- Validate token on incoming messages with `csrf_token` field
- Add configuration flag `WEBSOCKET_CSRF_ENABLED` (default: true)
- Exempt read-only operations from CSRF requirement
- **Testing**: Test token validation, test rejection of invalid tokens, test token generation

### Phase 2: Core Functionality

#### Invite Tracking System

**Requirement**: Mark invites as used to prevent reuse

**File**: `server/api/players.py:601`

**Implementation**:

- Add `used_at` and `used_by_user_id` columns to invites table
- Implement `mark_invite_as_used(code, user_id)` method in invite service
- Call marking in character creation endpoint after success
- Add validation to reject already-used invites
- Include invite usage in admin audit logs
- **Testing**: Test invite reuse prevention, test usage tracking, test audit trail

#### NPC Behavior Control Methods

**Requirement**: Implement three missing methods in NPCInstanceService

**Files**: `server/commands/npc_admin_commands.py:617,648,673`

**Implementation**:

**Method 1**: `set_npc_behavior(npc_id: str, behavior_type: str) -> bool`

- Valid behaviors: patrol, guard, wander, aggressive, passive, flee

- Update NPC instance behavior state

- Publish NPCBehaviorChanged event via NATS

- Persist behavior change to NPC instance data

**Method 2**: `trigger_npc_reaction(npc_id: str, reaction_type: str) -> bool`

    - Valid reactions: greet, attack, flee, investigate, alert, calm, excited, suspicious

    - Execute immediate reaction animation/emote

    - Publish NPCReacted event via NATS

    - Log reaction for debugging

**Method 3**: `stop_npc_behavior(npc_id: str) -> bool`

    - Halt current NPC behavior loop

    - Set NPC to idle state

    - Publish NPCBehaviorStopped event

    - Clear behavior timers

- Update admin command handlers to call new methods
- Add error handling for invalid NPC IDs
- **Testing**: Unit tests for each method, integration tests with real NPCs, test event publishing

#### NPC Template Retrieval

**Requirement**: Get NPC properties from NPC database instead of using defaults

**File**: `server/npc/combat_integration.py:256`

**Implementation**:

- Query NPC database by `npc_id` to get template data
- Extract `xp_reward`, `difficulty_rating`, `npc_type` from template
- Add LRU cache for frequently accessed templates (max 100 entries)
- Fallback to default values if template not found
- Log template lookup for debugging
- **Testing**: Test with various NPC types, test caching, test fallback behavior

#### Damage Calculation System

**Requirement**: Calculate damage based on player stats and equipment

**File**: `server/commands/combat.py:263`

**Implementation**:

- Design formula: `base_damage + (strength_modifier * 0.5) + weapon_damage + critical_bonus`
- Implement `calculate_damage(attacker: Player, target: NPC, weapon: Optional[Item]) -> int`
- Factor in player strength stat (scale: 1-20, modifier: stat - 10)
- Add weapon damage property (when inventory implemented, use default for now)
- Implement critical hit chance (5% base, configurable)
- Add damage variance (+/- 20%)
- Add configuration for all damage modifiers
- **Testing**: Test with different stat values, test critical hits, test damage variance ranges

#### Player/Room Name Resolution

**Requirement**: Use actual names instead of "Player_123" placeholders

**Files**: `server/realtime/event_publisher.py:75-76,155-156`

**Implementation**:

- Call `persistence.get_player(player_id)` to get player name
- Call `persistence.get_room(room_id)` to get room name/title
- Add caching to avoid repeated lookups within same event batch
- Fallback to "Unknown Player"/"Unknown Room" if lookup fails
- Add performance logging to monitor lookup impact
- **Testing**: Test name resolution, test fallback behavior, measure performance impact

### Phase 3: Configuration & Enhancement

#### Configurable Max Health

**Requirement**: Support player-specific max health values

**File**: `server/persistence.py:811`

**Implementation**:

- Read max_health from Player stats dict (key: "max_health")
- Add default max_health to config (100 for most players)
- Support race/class modifiers in character creation
- Update healing logic to use `player.get_stats()["max_health"]`
- Ensure backward compatibility for existing players (default to 100)
- **Testing**: Test with various max_health values, test healing to max

#### SQL Logging Configuration

**Requirement**: Load SQL logging verbosity from configuration

**File**: `server/persistence.py:116`

**Implementation**:

- Add `SQL_ECHO` configuration option (default: false)
- Add `SQL_ECHO_POOL` configuration option (default: false)
- Read config in `_setup_logger()` method
- Apply to SQLAlchemy engine creation: `create_engine(..., echo=config.sql_echo)`
- Support environment-specific defaults (verbose in dev, quiet in prod)
- **Testing**: Test with various log levels, verify SQL queries appear in logs

#### Immediate Death Handling

**Requirement**: Trigger death handling immediately instead of waiting for tick

**File**: `server/services/combat_service.py:899`

**Implementation**:

- Add `trigger_immediate_death(player_id: str)` method
- Call PlayerDeathService.handle_player_death() immediately when HP <= 0
- Maintain tick-based processing as fallback
- Add configuration `IMMEDIATE_DEATH_HANDLING` (default: true)
- Prevent double-processing with death state flag
- **Testing**: Test immediate trigger, test no double-processing, test tick fallback

#### Teleport Confirmation Dialogs

**Requirement**: Add confirmation for safety-critical admin commands

**Files**: `server/commands/admin_commands.py:608`, `server/models/command.py:393`, `server/utils/command_parser.py:725`

**Implementation**:

- Create `ConfirmTeleportCommand` class with pending state
- Create `ConfirmGotoCommand` class with pending state
- Add `create_confirm_teleport()` and `create_confirm_goto()` methods in command_parser
- Store pending confirmations in player session (timeout: 30 seconds)
- Accept `yes`/`no` responses to execute or cancel
- Add configuration `REQUIRE_TELEPORT_CONFIRMATION` (default: false for now)
- **Testing**: Test confirmation flow, test timeout, test cancellation

#### Room JSON Saving

**Requirement**: Enable dynamic room modifications to be saved to JSON files

**Files**: `server/persistence.py:697,709`

**Implementation**:

- Implement `_save_room_to_json(room: Room)` method
- Determine JSON file path from room.id and zone structure
- Create backup of original file before modification
- Write room data in standardized JSON format
- Add `ALLOW_ROOM_MODIFICATIONS` configuration (default: false)
- Validate room data before saving
- **Testing**: Test save/load cycle, test backup creation, test validation

#### Fresh Data Request Mechanism

**Requirement**: Implement mechanism to request fresh room data when stale detected

**File**: `server/services/room_sync_service.py:399`

**Implementation**:

- Add `request_fresh_room_data(room_id: str)` method
- Publish `room.sync.request` NATS message
- Reload room from JSON file on request
- Invalidate room cache for specific room
- Return updated room data to requester
- Add staleness detection threshold (configurable)
- **Testing**: Test data refresh, test cache invalidation, test staleness detection

### Phase 4: Cleanup & Optimization

#### Remove Legacy Chat Patterns

**Requirement**: Remove backward compatibility patterns after migration verification

**File**: `server/realtime/nats_message_handler.py:139`

**Implementation**:

- Verify all active clients use standardized patterns
- Remove `legacy_patterns` list and concatenation
- Update documentation to reflect standardized patterns only
- Add migration guide if clients need updates
- Test chat functionality without legacy patterns
- **Testing**: Test all chat channels, verify no message loss

#### Rewrite Performance Test

**Requirement**: Fix skipped performance test with better approach

**File**: `server/tests/unit/commands/test_utility_commands.py:1714`

**Implementation**:

- Reduce dataset from 2000 to 200 mock players
- Use pytest-benchmark for proper performance measurement
- Set reasonable performance thresholds
- Remove skip decorator

**File**: `server/tests/unit/commands/test_utility_commands.py:1714`

**Implementation**:

- Reduce dataset from 2000 to 200 mock players
- Use pytest-benchmark for proper performance measurement
- Set reasonable performance thresholds
- Remove skip decorator
- Add memory profiling for leak detection
- **Testing**: Verify test runs in < 5 seconds, verify no hangs

## Performance Criteria

Security validation adds < 10ms latency per request

- Damage calculation completes in < 5ms
- NPC template retrieval with cache: < 1ms (99th percentile)
- Name resolution with cache: < 2ms per event
- Room data refresh completes in < 100ms
- All tests pass in < 2 minutes total

## Security Criteria

No hardcoded secrets in codebase

- All admin endpoints require admin role
- CSRF validation blocks 100% of invalid tokens
- SQL injection prevented via parameterized queries (existing)
- Rate limiting enforced on all endpoints (existing)

## Code Quality Criteria

100% of TODOs resolved or documented as future work

- Test coverage maintained at >= 88%
- No skipped tests without documented justification
- All linter errors resolved
- No legacy code patterns remaining
