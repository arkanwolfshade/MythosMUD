# useConnectionStateMachine.test

> 70 nodes

## Key Concepts

- **logger.ts** (35 connections) — `client/src/utils/logger.ts`
- **logger** (32 connections) — `client/src/utils/logger.ts`
- **useGameConnectionRefactored.ts** (18 connections) — `client/src/hooks/useGameConnectionRefactored.ts`
- **useWebSocketConnection.ts** (18 connections) — `client/src/hooks/useWebSocketConnection.ts`
- **useGameConnectionManagement.ts** (15 connections) — `client/src/components/ui-v2/hooks/useGameConnectionManagement.ts`
- **useWebSocketConnectionTestFixtures.ts** (12 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **MockWebSocket** (12 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **useGameConnection()** (12 connections) — `client/src/hooks/useGameConnectionRefactored.ts`
- **useWebSocketConnection()** (12 connections) — `client/src/hooks/useWebSocketConnection.ts`
- **useWebSocketConnection.pingHeartbeat.test.ts** (11 connections) — `client/src/hooks/__tests__/useWebSocketConnection.pingHeartbeat.test.ts`
- **useWebSocketConnection.connection.test.ts** (8 connections) — `client/src/hooks/__tests__/useWebSocketConnection.connection.test.ts`
- **useWebSocketConnection.errorHandling.test.ts** (8 connections) — `client/src/hooks/__tests__/useWebSocketConnection.errorHandling.test.ts`
- **useConnectionStateMachine.ts** (8 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **logger.test.ts** (8 connections) — `client/src/utils/logger.test.ts`
- **useWebSocketConnection.callbacks.test.ts** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnection.callbacks.test.ts`
- **useWebSocketConnection.cleanup.test.ts** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnection.cleanup.test.ts`
- **useWebSocketConnection.messageHandling.test.ts** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnection.messageHandling.test.ts`
- **wsTestState** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **defaultOptions** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **wsConnectionBeforeEach()** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **wsConnectionAfterEach()** (7 connections) — `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- **useConnectionState.ts** (7 connections) — `client/src/hooks/useConnectionState.ts`
- **useSessionManagement.ts** (7 connections) — `client/src/hooks/useSessionManagement.ts`
- **useGameConnectionManagement()** (5 connections) — `client/src/components/ui-v2/hooks/useGameConnectionManagement.ts`
- **useGameConnection.ts** (5 connections) — `client/src/hooks/useGameConnection.ts`
- *... and 45 more nodes in this community*

## Relationships

- [SERVER UNAVAILABLE PATTERNS](SERVER_UNAVAILABLE_PATTERNS.md) (8 shared connections)
- [player respawn](player_respawn.md) (7 shared connections)
- [.append()](append%28%29.md) (7 shared connections)
- [monitoring models](monitoring_models.md) (6 shared connections)
- [fetchSpy](fetchSpy.md) (6 shared connections)
- [AppCreationFlowViews](AppCreationFlowViews.md) (4 shared connections)
- [handle reply command()](handle_reply_command%28%29.md) (4 shared connections)
- [roomHandlers](roomHandlers.md) (4 shared connections)
- [MythosTimeHud](MythosTimeHud.md) (4 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (3 shared connections)
- [test combat persistence handler](test_combat_persistence_handler.md) (3 shared connections)
- [useComponentLifecycleTracking.test](useComponentLifecycleTracking.test.md) (3 shared connections)

## Source Files

- `client/src/components/ui-v2/hooks/useGameConnectionManagement.ts`
- `client/src/hooks/__tests__/useConnectionState.test.ts`
- `client/src/hooks/__tests__/useConnectionStateMachine.test.ts`
- `client/src/hooks/__tests__/useGameConnection.export.test.ts`
- `client/src/hooks/__tests__/useSessionManagement.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.callbacks.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.cleanup.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.connection.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.errorHandling.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.messageHandling.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnection.pingHeartbeat.test.ts`
- `client/src/hooks/__tests__/useWebSocketConnectionTestFixtures.ts`
- `client/src/hooks/useConnectionState.ts`
- `client/src/hooks/useConnectionStateMachine.test.ts`
- `client/src/hooks/useConnectionStateMachine.ts`
- `client/src/hooks/useGameConnection.test.ts`
- `client/src/hooks/useGameConnection.ts`
- `client/src/hooks/useGameConnectionRefactored.ts`
- `client/src/hooks/useSessionManagement.ts`
- `client/src/hooks/useWebSocketConnection.ts`

## Audit Trail

- EXTRACTED: 351 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*