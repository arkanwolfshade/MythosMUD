# Playwright E2E Specs

> 83 nodes · cohesion 0.10

## Key Concepts

- **multiplayer.ts** (80 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **ensurePlayerInGame()** (41 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **createMultiPlayerContexts()** (37 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForMessage()** (36 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **cleanupMultiPlayerContexts()** (34 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForAllPlayersInGame()** (32 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **ensurePlayableConnection()** (26 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **local-channel-basic.spec.ts** (23 connections) — `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- **whisper-movement.spec.ts** (22 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **local-channel-isolation.spec.ts** (21 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **chat-messages.spec.ts** (20 connections) — `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- **local-channel-integration.spec.ts** (20 connections) — `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- **ensureMultiplayerCoLocated()** (20 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **getMessages()** (19 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **waitForCrossPlayerMessage()** (19 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **getPlayerMessages()** (18 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **movement-between-rooms.spec.ts** (18 connections) — `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`
- **party-commands.spec.ts** (18 connections) — `client/tests/e2e/runtime/party/party-commands.spec.ts`
- **whisper-basic.spec.ts** (17 connections) — `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- **admin-set-stat-command.spec.ts** (15 connections) — `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- **whisper-integration.spec.ts** (15 connections) — `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- **local-channel-errors.spec.ts** (14 connections) — `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`
- **PlayerContext** (14 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **local-channel-movement.spec.ts** (14 connections) — `client/tests/e2e/runtime/movement/local-channel-movement.spec.ts`
- **ensurePlayersInSameRoom()** (13 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- *... and 58 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (100 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (68 shared connections)
- [Bug Investigation Guide](Bug_Investigation_Guide.md) (7 shared connections)
- [Movement Service Tests](Movement_Service_Tests.md) (2 shared connections)
- [Integer Coercion Utils](Integer_Coercion_Utils.md) (1 shared connections)

## Source Files

- `client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`
- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
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
- `client/tests/e2e/runtime/connection/clean-game-state.spec.ts`
- `client/tests/e2e/runtime/containers/container-corpse-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-environmental-interactions.spec.ts`
- `client/tests/e2e/runtime/containers/container-multi-user-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-wearable-management.spec.ts`
- `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`

## Audit Trail

- EXTRACTED: 874 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*