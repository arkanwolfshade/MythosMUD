# client tests e2e runtime accessibility

> 82 nodes

## Key Concepts

- **executeCommand()** (82 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **multiplayer.ts** (54 connections) — `client/tests/e2e/runtime/fixtures/multiplayer.ts`
- **waitForMessage()** (51 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensurePlayerInGame()** (48 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **cleanupMultiPlayerContexts()** (40 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- **createMultiPlayerContexts()** (40 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- **waitForAllPlayersInGame()** (35 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **ensurePlayableConnection()** (31 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **multiplayer-ready.ts** (27 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **local-channel-basic.spec.ts** (23 connections) — `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- **local-channel-movement.spec.ts** (22 connections) — `client/tests/e2e/runtime/movement/local-channel-movement.spec.ts`
- **waitForCrossPlayerMessage()** (21 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **chat-messages.spec.ts** (20 connections) — `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- **local-channel-integration.spec.ts** (20 connections) — `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- **getPlayerMessages()** (19 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **movement-between-rooms.spec.ts** (19 connections) — `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`
- **PlayerContext** (18 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- **admin-teleportation.spec.ts** (18 connections) — `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- **party-commands.spec.ts** (18 connections) — `client/tests/e2e/runtime/party/party-commands.spec.ts`
- **prepareReceiverForInboundMessages()** (16 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- **whisper-basic.spec.ts** (16 connections) — `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- **ensurePlayersInSameRoom()** (15 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **waitForLookReflectedInUi()** (15 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **whisper-integration.spec.ts** (15 connections) — `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- **basic-connection.spec.ts** (15 connections) — `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- *... and 57 more nodes in this community*

## Relationships

- [client tests e2e runtime character](client_tests_e2e_runtime_character.md) (80 shared connections)
- [client tests e2e runtime communication](client_tests_e2e_runtime_communication.md) (70 shared connections)
- [client src utils deathvoidlocation](client_src_utils_deathvoidlocation.md) (65 shared connections)
- [client tests e2e runtime fixtures](client_tests_e2e_runtime_fixtures.md) (28 shared connections)
- [client src test e2e bootstrap](client_src_test_e2e_bootstrap.md) (3 shared connections)

## Source Files

- `client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`
- `client/tests/e2e/runtime/admin/admin-teleportation.spec.ts`
- `client/tests/e2e/runtime/admin/summon-command.spec.ts`
- `client/tests/e2e/runtime/admin/whisper-logging.spec.ts`
- `client/tests/e2e/runtime/commands/disconnect-grace-period.spec.ts`
- `client/tests/e2e/runtime/commands/rest-command.spec.ts`
- `client/tests/e2e/runtime/commands/who-command.spec.ts`
- `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- `client/tests/e2e/runtime/connection/basic-connection.spec.ts`
- `client/tests/e2e/runtime/connection/clean-game-state.spec.ts`
- `client/tests/e2e/runtime/containers/container-corpse-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-environmental-interactions.spec.ts`
- `client/tests/e2e/runtime/containers/container-multi-user-looting.spec.ts`
- `client/tests/e2e/runtime/containers/container-wearable-management.spec.ts`
- `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`

## Audit Trail

- EXTRACTED: 610 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*