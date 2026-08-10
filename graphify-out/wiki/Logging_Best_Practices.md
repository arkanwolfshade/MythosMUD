# Logging Best Practices

> 43 nodes

## Key Concepts

- **executeCommand()** (67 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **combat-messages-game-info.spec.ts** (31 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **player.ts** (31 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **local-channel-isolation.spec.ts** (21 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **ensureStanding()** (20 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **admin-teleportation.spec.ts** (16 connections) — `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- **ensurePlayableAlive()** (16 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **tryStartCombat()** (9 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **spawnCombatTargetNpc()** (8 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **despawnSanitariumCultists()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **retryUntilCombatStarted()** (7 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **listSanitariumCultistIds()** (7 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **resolveSpawnedCultistTarget()** (6 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **getPageSessionCredentials()** (6 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensureNotInCombat()** (6 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **resetE2ePlayerRoomsInDatabase()** (5 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **keepFirstCultistInstanceId()** (4 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **returnAwToFoyerIfInHallway()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **primeBothForCoLocate()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **ensureIthaquaInFoyer()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **prepareLocalIsolationPair()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **hopEastUntilHallway()** (4 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **dismissDeathInterstitial()** (4 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **hasCombatMessage()** (3 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **waitForCombatRoundMessage()** (3 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- *... and 18 more nodes in this community*

## Relationships

- [Lifespan Startup Hooks](Lifespan_Startup_Hooks.md) (103 shared connections)
- [Room Sync Service](Room_Sync_Service.md) (23 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (5 shared connections)

## Source Files

- `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- `client/tests/e2e/runtime/commands/who-command.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- `client/tests/e2e/runtime/fixtures/player.ts`
- `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`

## Audit Trail

- EXTRACTED: 333 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*