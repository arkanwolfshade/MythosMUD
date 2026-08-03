# e2e combat spec

> 37 nodes

## Key Concepts

- **player.ts** (36 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **combat-messages-game-info.spec.ts** (31 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **ensureStanding()** (25 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **admin-set-stat-command.spec.ts** (22 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **ensurePlayableAlive()** (18 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **tryStartCombat()** (9 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **getPageSessionCredentials()** (9 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **despawnSanitariumCultists()** (9 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **spawnCombatTargetNpc()** (8 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **ensureNotInCombat()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **listSanitariumCultistIds()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **goEastFromFoyer()** (8 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **retryUntilCombatStarted()** (7 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **clickWithoutStability()** (7 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **resetE2ePlayerRoomsInDatabase()** (7 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **resolveSpawnedCultistTarget()** (6 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **lookAndStand()** (5 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **prepAwForAdminSet()** (5 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **prepNonAdminForSetAttempt()** (4 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **runAdminSetWithRecovery()** (4 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **keepFirstCultistInstanceId()** (4 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **dismissDeathInterstitial()** (4 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **prepareForDirectionalMove()** (4 connections) — `client/tests/e2e/runtime/fixtures/player.ts`
- **hasCombatMessage()** (3 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- **waitForCombatRoundMessage()** (3 connections) — `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- *... and 12 more nodes in this community*

## Relationships

- [e2e spec multiplayer](e2e_spec_multiplayer.md) (56 shared connections)
- [e2e fixtures spec](e2e_fixtures_spec.md) (26 shared connections)
- [quest e2e spec](quest_e2e_spec.md) (11 shared connections)
- [e2e fixtures multiplayer](e2e_fixtures_multiplayer.md) (8 shared connections)
- [e2e spec communication](e2e_spec_communication.md) (6 shared connections)
- [e2e bootstrap E2E](e2e_bootstrap_E2E.md) (1 shared connections)

## Source Files

- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- `client/tests/e2e/runtime/combat/combat-messages-game-info.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- `client/tests/e2e/runtime/fixtures/player.ts`

## Audit Trail

- EXTRACTED: 276 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*