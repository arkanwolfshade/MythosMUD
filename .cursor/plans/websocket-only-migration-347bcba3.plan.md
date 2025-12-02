# WebSocket-Only Migration Plan

## Overview

This plan consolidates the dual WebSocket/SSE connection system to WebSocket-only. The current system maintains both connections simultaneously, receiving duplicate messages. This migration will:

1. Remove all SSE connection code from client and server
2. Simplify ConnectionManager to track only WebSocket connections
3. Update all tests to reflect WebSocket-only architecture
4. Update documentation to reflect new architecture

## Phase 1: Client-Side Changes ✅

### 1.1 Remove SSE Connection Hook ✅

**File**: `client/src/hooks/useSSEConnection.ts`
- **Action**: Delete entire file
- **Status**: ✅ COMPLETE

### 1.2 Update Game Connection Hook ✅

**File**: `client/src/hooks/useGameConnectionRefactored.ts`
- **Status**: ✅ COMPLETE
- All SSE connection logic removed
- Connection state machine simplified to WebSocket-only
- Session ID generation moved to WebSocket connection

### 1.3 Update Connection State Machine ✅

**File**: `client/src/hooks/useConnectionStateMachine.ts`
- **Status**: ✅ COMPLETE
- SSE-related states and transitions removed
- Simplified to WebSocket-only flow

### 1.4 Update Connection Store ✅

**File**: `client/src/stores/connectionStore.ts`
- **Status**: ✅ COMPLETE
- SSE connection tracking removed
- Connection statistics updated to WebSocket-only

### 1.5 Remove SSE Tests ✅

**Files**: All SSE-related test files
- **Status**: ✅ COMPLETE
- `useSSEConnection.test.ts` - Deleted
- `useGameConnection.sse-url.test.ts` - Deleted
- `test_dual_connection_integration.ts` - Deleted
- All remaining tests updated to WebSocket-only

### 1.6 Update Resource Cleanup ✅

**File**: `client/src/utils/resourceCleanup.ts`
- **Status**: ✅ COMPLETE
- EventSource cleanup logic removed

## Phase 2: Server-Side Changes ✅

### 2.1 Remove SSE Endpoints ✅

**File**: `server/api/real_time.py`
- **Status**: ✅ COMPLETE
- `sse_events()` endpoint removed
- `sse_events_token()` endpoint removed
- SSE-related imports removed

### 2.2 Remove SSE Handler Module ✅

**File**: `server/realtime/sse_handler.py`
- **Status**: ✅ COMPLETE
- File deleted
- Utility functions moved to `connection_manager.py`

### 2.3 Update ConnectionManager ✅

**File**: `server/realtime/connection_manager.py`
- **Status**: ✅ COMPLETE
- SSE connection tracking removed
- All SSE methods removed
- Message sending methods updated
- Statistics methods updated to WebSocket-only
- Utility functions added from sse_handler.py

### 2.4 Update Message Sending ✅

**Files**: All files that call SSE-specific functions
- **Status**: ✅ COMPLETE
- `prefer_sse` parameter removed from all calls
- All message sending updated to WebSocket-only

### 2.5 Remove SSE Tests ✅

**Files**: All SSE-related test files
- **Status**: ✅ COMPLETE
- `test_sse_handler.py` - Deleted
- `test_sse_auth.py` - Deleted
- `test_readiness_gate.py` - Deleted
- `test_dual_connection_integration.py` - Deleted
- `test_dual_connection_testing_strategy.py` - Deleted
- All remaining tests updated to WebSocket-only

### 2.6 Update Monitoring Endpoints ✅

**File**: `server/api/monitoring.py`
- **Status**: ✅ COMPLETE
- Connection statistics updated to WebSocket-only

## Phase 3: Documentation Updates ✅

### 3.1 Architecture Documentation ✅

**Files**: All architecture documentation
- **Status**: ✅ COMPLETE
- `REAL_TIME_ARCHITECTURE.md` - Updated to WebSocket-only
- `EVENT_OWNERSHIP_MATRIX.md` - Updated to WebSocket-only
- All dual connection docs archived in `docs/archive/`

### 3.2 API Documentation ✅

**File**: `docs/EVENT_OWNERSHIP_MATRIX.md`
- **Status**: ✅ COMPLETE
- SSE references removed
- WebSocket-only message flow documented

## Phase 4: Testing & Validation ✅

### 4.1 Update Test Fixtures ✅

**File**: `server/tests/fixtures/success_criteria_validator.py`
- **Status**: ✅ COMPLETE
- Dual connection validation removed
- Success criteria updated to WebSocket-only

### 4.2 Integration Tests ✅

**Files**: All integration test files
- **Status**: ✅ COMPLETE
- SSE connection establishment removed from test setup
- All tests updated to WebSocket-only connections

### 4.3 E2E Tests ✅

**Files**: E2E test scenarios
- **Status**: ✅ COMPLETE
- Dual connection scenarios removed
- All scenarios updated to WebSocket-only

### 4.4 Manual Testing Checklist ✅

- [x] Client connects successfully with WebSocket only
- [x] Commands work correctly via WebSocket
- [x] Chat messages work correctly via WebSocket
- [x] Game events (room updates, combat, etc.) delivered via WebSocket
- [x] Reconnection works correctly
- [x] Multiple players can connect simultaneously
- [x] Connection health monitoring works
- [x] Session management works correctly

## Phase 5: Cleanup ✅

### 5.1 Remove Dead Code ✅

- **Status**: ✅ COMPLETE
- All SSE references removed from active code
- Unused imports removed
- Unused type definitions removed
- SSE-related configuration cleaned up

### 5.2 Update Monitoring ✅

**File**: `monitoring/mythos_alerts.yml`
- **Status**: ✅ COMPLETE
- SSE-specific alerts removed
- Alerts updated to WebSocket-only metrics

## Implementation Summary

**All phases completed successfully!**

### Completed Tasks

- [x] Delete useSSEConnection.ts hook file
- [x] Update useGameConnectionRefactored.ts to remove all SSE connection logic and simplify state machine
- [x] Update useConnectionStateMachine.ts to remove SSE states and transitions
- [x] Update connectionStore.ts to remove SSE tracking properties
- [x] Delete SSE-related test files and update remaining tests
- [x] Remove SSE endpoints from server/api/real_time.py
- [x] Move utility functions from sse_handler.py to connection_manager.py before deleting sse_handler.py
- [x] Remove all SSE tracking from ConnectionManager class
- [x] Remove prefer_sse parameter from all message sending calls
- [x] Archive dual connection docs and update architecture documentation
- [x] Run complete test suite and fix any failures
- [x] Remove dead code, unused imports, and update monitoring configs

### Migration Complete

The WebSocket-only migration is **100% complete**. All SSE code has been removed, all tests updated, and all documentation reflects the new WebSocket-only architecture.
