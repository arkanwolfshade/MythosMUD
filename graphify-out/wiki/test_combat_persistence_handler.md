# test combat persistence handler

> 13 nodes

## Key Concepts

- **.error()** (17 connections) — `client/src/utils/logger.ts`
- **ClientLogger** (13 connections) — `client/src/utils/logger.ts`
- **.info()** (6 connections) — `client/src/utils/logger.ts`
- **.initializeLogging()** (5 connections) — `client/src/utils/logger.ts`
- **.createLogEntry()** (5 connections) — `client/src/utils/logger.ts`
- **.addToBuffer()** (5 connections) — `client/src/utils/logger.ts`
- **.warn()** (4 connections) — `client/src/utils/logger.ts`
- **.flushLogs()** (4 connections) — `client/src/utils/logger.ts`
- **.debug()** (3 connections) — `client/src/utils/logger.ts`
- **.constructor()** (2 connections) — `client/src/utils/logger.ts`
- **.downloadLogs()** (2 connections) — `client/src/utils/logger.ts`
- **.clearLogs()** (2 connections) — `client/src/utils/logger.ts`
- **.getLogBuffer()** (1 connections) — `client/src/utils/logger.ts`

## Relationships

- [useConnectionStateMachine.test](useConnectionStateMachine.test.md) (3 shared connections)
- [fetchSpy](fetchSpy.md) (3 shared connections)
- [MythosTimeHud](MythosTimeHud.md) (2 shared connections)
- [CharacterSelectionScreen](CharacterSelectionScreen.md) (1 shared connections)
- [monitoring models](monitoring_models.md) (1 shared connections)
- [messageHandlers](messageHandlers.md) (1 shared connections)
- [.append()](append%28%29.md) (1 shared connections)
- [player respawn](player_respawn.md) (1 shared connections)

## Source Files

- `client/src/utils/logger.ts`

## Audit Trail

- EXTRACTED: 57 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*