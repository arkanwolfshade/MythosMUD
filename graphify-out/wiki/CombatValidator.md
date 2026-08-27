# CombatValidator

> 67 nodes

## Key Concepts

- **executeCommand()** (85 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **player.ts** (47 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **ensurePlayableConnection()** (36 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **whisper-movement.spec.ts** (35 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **combat-messages-game-info.spec.ts** (31 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **ensureStanding()** (26 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **admin-set-stat-command.spec.ts** (23 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **ensurePlayableAlive()** (20 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **tryStartCombat()** (9 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **clickWithoutStability()** (9 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **getPageSessionCredentials()** (9 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **despawnSanitariumCultists()** (9 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **spawnCombatTargetNpc()** (8 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **ensureNotInCombat()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **goEastFromFoyer()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **listSanitariumCultistIds()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **retryUntilCombatStarted()** (7 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **resolveSpawnedCultistTarget()** (6 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **lookAndStand()** (5 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **prepAwForAdminSet()** (5 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **attemptEastHop()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **lookAndWaitForUi()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **moveAwToEasternHallway()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **sendCrossRoomWhisper()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **whisperUntilSenderAck()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- *... and 42 more nodes in this community*

## Relationships

- [test_command_processor.py](test_command_processor.py.md) (106 shared connections)
- [quality_fragmentation_ai_guardrails.py](quality_fragmentation_ai_guardrails.py.md) (37 shared connections)
- [Design Critique](Design_Critique.md) (26 shared connections)
- [NATSConfig](NATSConfig.md) (18 shared connections)
- [health_service](health_service.md) (10 shared connections)
- [Test Pruning Candidates - Detailed List](Test_Pruning_Candidates_-_Detailed_List.md) (5 shared connections)

## Source Files

- `client/src/utils/__tests__/deathVoidLocation.test.ts`
- `client/src/utils/deathVoidLocation.ts`
- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- `client/tests/e2e/runtime/commands/who-command.spec.ts`
- `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/fixtures/player.ts`
- `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`

## Audit Trail

- EXTRACTED: 367 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*