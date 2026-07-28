# Client E2E

> 50 nodes

## Key Concepts

- **waitForMessage** (35 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **createMultiPlayerContexts** (32 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **cleanupMultiPlayerContexts** (32 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **ensurePlayerInGame** (31 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForAllPlayersInGame** (30 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **party-commands.spec.ts** (16 connections) — `client/tests/e2e/runtime/party/party-commands.spec.ts`
- **getMessages** (16 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **getPlayerMessages** (16 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **movement-between-rooms.spec.ts** (15 connections) — `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`
- **ensureMultiplayerCoLocated** (15 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **whisper-basic.spec.ts** (14 connections) — `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- **waitForCrossPlayerMessage** (14 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **whisper-integration.spec.ts** (13 connections) — `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- **admin-teleportation.spec.ts** (12 connections) — `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- **basic-connection.spec.ts** (12 connections) — `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- **admin-set-stat-command.spec.ts** (11 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **local-channel-errors.spec.ts** (11 connections) — `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`
- **local-channel-movement.spec.ts** (11 connections) — `client/tests/e2e/runtime/movement/local-channel-movement.spec.ts`
- **muting-system-emotes.spec.ts** (11 connections) — `client/tests/e2e/runtime/muting/muting-system-emotes.spec.ts`
- **who-command.spec.ts** (10 connections) — `client/tests/e2e/runtime/commands/who-command.spec.ts`
- **whisper-logging.spec.ts** (8 connections) — `client/tests/e2e/runtime/admin/whisper-logging.spec.ts`
- **rest-command.spec.ts** (8 connections) — `client/tests/e2e/runtime/commands/rest-command.spec.ts`
- **summon-command.spec.ts** (7 connections) — `client/tests/e2e/runtime/admin/summon-command.spec.ts`
- **logout-errors.spec.ts** (7 connections) — `client/tests/e2e/runtime/error-handling/logout-errors.spec.ts`
- **whisper-errors.spec.ts** (7 connections) — `client/tests/e2e/runtime/error-handling/whisper-errors.spec.ts`
- *... and 25 more nodes in this community*

## Relationships

- [Client E2E (3)](Client_E2E_%283%29.md) (98 shared connections)
- [Client E2E (7)](Client_E2E_%287%29.md) (15 shared connections)
- [Client E2E (5)](Client_E2E_%285%29.md) (3 shared connections)
- [Client E2E (9)](Client_E2E_%289%29.md) (2 shared connections)

## Source Files

- `client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`
- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- `client/tests/e2e/runtime/admin/summon-command.spec.ts`
- `client/tests/e2e/runtime/admin/whisper-logging.spec.ts`
- `client/tests/e2e/runtime/commands/disconnect-grace-period.spec.ts`
- `client/tests/e2e/runtime/commands/rest-command.spec.ts`
- `client/tests/e2e/runtime/commands/who-command.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- `client/tests/e2e/runtime/connection/clean-game-state.spec.ts`
- `client/tests/e2e/runtime/containers/container-corpse-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-environmental-interactions.spec.ts`
- `client/tests/e2e/runtime/containers/container-multi-user-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-wearable-management.spec.ts`
- `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`
- `client/tests/e2e/runtime/error-handling/logout-errors.spec.ts`
- `client/tests/e2e/runtime/error-handling/whisper-errors.spec.ts`
- `client/tests/e2e/runtime/error-handling/whisper-rate-limiting.spec.ts`

## Audit Trail

- EXTRACTED: 466 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*