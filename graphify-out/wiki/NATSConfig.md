# NATSConfig

> 41 nodes

## Key Concepts

- **multiplayer-colocated.ts** (41 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **multiplayer-contexts.ts** (24 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- **ensurePlayersInSameRoom()** (20 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **reopenPlayerPageIfClosed()** (15 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- **resyncE2ePlayersAfterDatabaseReset()** (11 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **executeCommandTrusted()** (10 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **pages/index.ts** (10 connections) — `client/tests/e2e/runtime/pages/index.ts`
- **logoutPlayer()** (8 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **runCoLocateTeleportAttempt()** (8 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **ensureMultiplayerReadyForCoLocate()** (7 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **resetE2ePlayerRoomsInDatabase()** (7 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **assertPlayerAlive()** (7 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **MotdPage** (6 connections) — `client/tests/e2e/runtime/pages/MotdPage.ts`
- **assertNoRestDisconnectPollution()** (6 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **multiplayer-browser-window.d.ts** (6 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-browser-window.d.ts`
- **LoginPage** (5 connections) — `client/tests/e2e/runtime/pages/LoginPage.ts`
- **throwOtherPlayersNotSeen()** (5 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **TestPlayer** (4 connections) — `client/tests/e2e/runtime/fixtures/test-data.ts`
- **retryCoLocateUntilSameRoom()** (4 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **throwOccupantsWaitTimeout()** (4 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **assertNotStuckOnLogin()** (3 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **captureOccupantsSnapshot()** (3 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **formatOccupantsSnapshotForError()** (3 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **.enterRealm()** (3 connections) — `client/tests/e2e/runtime/pages/MotdPage.ts`
- **.waitForGameReady()** (3 connections) — `client/tests/e2e/runtime/pages/MotdPage.ts`
- *... and 16 more nodes in this community*

## Relationships

- [test_command_processor.py](test_command_processor.py.md) (47 shared connections)
- [quality_fragmentation_ai_guardrails.py](quality_fragmentation_ai_guardrails.py.md) (26 shared connections)
- [CombatValidator](CombatValidator.md) (18 shared connections)
- [Test Pruning Candidates - Detailed List](Test_Pruning_Candidates_-_Detailed_List.md) (4 shared connections)
- [health_service](health_service.md) (3 shared connections)
- [Design Critique](Design_Critique.md) (2 shared connections)
- [migration_examples.py](migration_examples.py.md) (2 shared connections)
- [2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage](2._Primitive_Anti-Patterns-_Direct_`asyncio`_Primitive_Usage.md) (2 shared connections)
- [test_chat_moderation.py](test_chat_moderation.py.md) (2 shared connections)

## Source Files

- `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer-browser-window.d.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- `client/tests/e2e/runtime/fixtures/player.ts`
- `client/tests/e2e/runtime/fixtures/test-data.ts`
- `client/tests/e2e/runtime/pages/LoginPage.ts`
- `client/tests/e2e/runtime/pages/MotdPage.ts`
- `client/tests/e2e/runtime/pages/index.ts`

## Audit Trail

- EXTRACTED: 174 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*