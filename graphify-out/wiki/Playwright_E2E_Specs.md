# Playwright E2E Specs

> 87 nodes · cohesion 0.10

## Key Concepts

- **multiplayer.ts** (79 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **executeCommand()** (56 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensurePlayerInGame()** (40 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **createMultiPlayerContexts()** (36 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **cleanupMultiPlayerContexts()** (34 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForAllPlayersInGame()** (32 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForMessage()** (31 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **local-channel-basic.spec.ts** (23 connections) — `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- **chat-messages.spec.ts** (20 connections) — `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- **local-channel-integration.spec.ts** (19 connections) — `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- **local-channel-isolation.spec.ts** (19 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **whisper-movement.spec.ts** (18 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **getPlayerMessages()** (18 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **movement-between-rooms.spec.ts** (18 connections) — `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`
- **party-commands.spec.ts** (18 connections) — `client/tests/e2e/runtime/party/party-commands.spec.ts`
- **whisper-basic.spec.ts** (17 connections) — `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- **getMessages()** (17 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensureMultiplayerCoLocated()** (16 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForCrossPlayerMessage()** (16 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **whisper-integration.spec.ts** (15 connections) — `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- **basic-connection.spec.ts** (14 connections) — `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- **local-channel-errors.spec.ts** (14 connections) — `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`
- **PlayerContext** (14 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **local-channel-movement.spec.ts** (14 connections) — `client/tests/e2e/runtime/movement/local-channel-movement.spec.ts`
- **e2e-runtime-ready.ts** (13 connections) — `client/tests/e2e/runtime/fixtures/e2e-runtime-ready.ts`
- *... and 62 more nodes in this community*

## Relationships

- [[Character Selection E2E]] (57 shared connections)
- [[E 2 E Runtime Combat]] (54 shared connections)
- [[Character Creation E2E]] (4 shared connections)
- [[E2E Global Setup Teardown]] (3 shared connections)
- [[E 2 E Runtime Multiplayer]] (2 shared connections)
- [[Multiplayer Browser Helpers]] (1 shared connections)

## Source Files

- `client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`
- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- `client/tests/e2e/runtime/admin/summon-command.spec.ts`
- `client/tests/e2e/runtime/admin/whisper-logging.spec.ts`
- `client/tests/e2e/runtime/commands/disconnect-grace-period.spec.ts`
- `client/tests/e2e/runtime/commands/rest-command.spec.ts`
- `client/tests/e2e/runtime/commands/who-command.spec.ts`
- `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- `client/tests/e2e/runtime/connection/clean-game-state.spec.ts`
- `client/tests/e2e/runtime/containers/container-corpse-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-environmental-interactions.spec.ts`
- `client/tests/e2e/runtime/containers/container-multi-user-looting.spec.ts`

## Audit Trail

- EXTRACTED: 901 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
