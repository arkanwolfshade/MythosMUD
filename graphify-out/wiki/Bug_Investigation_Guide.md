# Bug Investigation Guide

> 29 nodes · cohesion 0.17

## Key Concepts

- **e2e-bootstrap.ts** (18 connections) — `client/src/test/e2e-bootstrap.ts`
- **collect-n-daisy-quest.spec.ts** (16 connections) — `client/tests/e2e/runtime/quest/collect-n-daisy-quest.spec.ts`
- **global-setup.ts** (15 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **loadE2eEnv()** (12 connections) — `client/src/test/e2e-bootstrap.ts`
- **failBootstrap()** (11 connections) — `client/src/test/e2e-bootstrap.ts`
- **globalSetup()** (7 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **verifyServerBootstrap()** (7 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **spawnOutputDetail()** (6 connections) — `client/src/test/e2e-bootstrap.ts`
- **formatLoginFailure()** (5 connections) — `client/src/test/e2e-bootstrap.ts`
- **e2e-bootstrap.test.ts** (5 connections) — `client/src/test/e2e-bootstrap.test.ts`
- **runE2ePlayerRoomReset()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **runE2eSeed()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **verifyE2eUsersInDatabase()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **E2E_PROJECT_ROOT** (4 connections) — `client/src/test/e2e-bootstrap.ts`
- **redactDatabaseUrl()** (4 connections) — `client/src/test/e2e-bootstrap.ts`
- **runEnsureE2eDatabase()** (4 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **spawnMorgan()** (4 connections) — `client/tests/e2e/runtime/quest/collect-n-daisy-quest.spec.ts`
- **countProfessionsPayload()** (3 connections) — `client/src/test/e2e-bootstrap.ts`
- **parseE2eEnvContent()** (3 connections) — `client/src/test/e2e-bootstrap.ts`
- **verifyClientAccessible()** (3 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **appendBootstrapFailureLog()** (2 connections) — `client/src/test/e2e-bootstrap.ts`
- **E2E_ENV_DEFAULTS** (2 connections) — `client/src/test/e2e-bootstrap.ts`
- **fetchResponseBodyText()** (2 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **assertMorganVisible()** (2 connections) — `client/tests/e2e/runtime/quest/collect-n-daisy-quest.spec.ts`
- **resetDaisyQuestInstances()** (2 connections) — `client/tests/e2e/runtime/quest/collect-n-daisy-quest.spec.ts`
- *... and 4 more nodes in this community*

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (7 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)

## Source Files

- `client/src/test/e2e-bootstrap.test.ts`
- `client/src/test/e2e-bootstrap.ts`
- `client/tests/e2e/runtime/global-setup.ts`
- `client/tests/e2e/runtime/quest/collect-n-daisy-quest.spec.ts`

## Audit Trail

- EXTRACTED: 156 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*