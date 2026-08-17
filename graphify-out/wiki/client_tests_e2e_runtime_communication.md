# client tests e2e runtime communication

> 23 nodes

## Key Concepts

- **multiplayer-colocated.ts** (40 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **local-channel-isolation.spec.ts** (25 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **ensureMultiplayerCoLocated()** (19 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **prepareLocalIsolationPair()** (6 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **resetE2ePlayerRoomsInDatabase()** (6 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **ensureIthaquaInFoyer()** (5 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **throwOtherPlayersNotSeen()** (5 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **leaveEasternHallwayWest()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **primeBothForCoLocate()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **returnAwToFoyerIfInHallway()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **softCommand()** (4 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **retryCoLocateUntilSameRoom()** (4 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **runCoLocateTeleportAttempt()** (4 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **throwOccupantsWaitTimeout()** (4 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **captureOccupantsSnapshot()** (3 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **formatOccupantsSnapshotForError()** (3 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **resyncE2ePlayersAfterDatabaseReset()** (3 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **EnsureMultiplayerCoLocatedOptions** (2 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **pageShowsEasternHallway()** (2 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **waitForLookReflected()** (2 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **capturePresenceEvents()** (2 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **ensureMultiplayerReadyForCoLocate()** (2 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- **resolveOtherCharacterName()** (2 connections) — `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Relationships

- [client tests e2e runtime accessibility](client_tests_e2e_runtime_accessibility.md) (46 shared connections)
- [client tests e2e runtime character](client_tests_e2e_runtime_character.md) (15 shared connections)
- [client src utils deathvoidlocation](client_src_utils_deathvoidlocation.md) (9 shared connections)
- [client src test e2e bootstrap](client_src_test_e2e_bootstrap.md) (3 shared connections)
- [client tests e2e runtime communication](client_tests_e2e_runtime_communication.md) (1 shared connections)
- [client src test multiplayer browser](client_src_test_multiplayer_browser.md) (1 shared connections)

## Source Files

- `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Audit Trail

- EXTRACTED: 115 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*