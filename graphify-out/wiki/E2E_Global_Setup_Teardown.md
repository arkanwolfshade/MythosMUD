# E2E Global Setup Teardown

> 30 nodes · cohesion 0.16

## Key Concepts

- **e2e-bootstrap.ts** (18 connections) — `client/src/test/e2e-bootstrap.ts`
- **global-setup.ts** (15 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **loadE2eEnv()** (12 connections) — `client/src/test/e2e-bootstrap.ts`
- **failBootstrap()** (11 connections) — `client/src/test/e2e-bootstrap.ts`
- **globalSetup()** (7 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **verifyServerBootstrap()** (7 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **global-teardown.ts** (6 connections) — `client/tests/e2e/runtime/global-teardown.ts`
- **spawnOutputDetail()** (6 connections) — `client/src/test/e2e-bootstrap.ts`
- **runE2ePlayerRoomReset()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **runE2eSeed()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **verifyE2eUsersInDatabase()** (5 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **formatLoginFailure()** (5 connections) — `client/src/test/e2e-bootstrap.ts`
- **e2e-bootstrap.test.ts** (5 connections) — `client/src/test/e2e-bootstrap.test.ts`
- **runEnsureE2eDatabase()** (4 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **redactDatabaseUrl()** (4 connections) — `client/src/test/e2e-bootstrap.ts`
- **verifyClientAccessible()** (3 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **countProfessionsPayload()** (3 connections) — `client/src/test/e2e-bootstrap.ts`
- **E2E_PROJECT_ROOT** (3 connections) — `client/src/test/e2e-bootstrap.ts`
- **parseE2eEnvContent()** (3 connections) — `client/src/test/e2e-bootstrap.ts`
- **fetchResponseBodyText()** (2 connections) — `client/tests/e2e/runtime/global-setup.ts`
- **globalTeardown()** (2 connections) — `client/tests/e2e/runtime/global-teardown.ts`
- **appendBootstrapFailureLog()** (2 connections) — `client/src/test/e2e-bootstrap.ts`
- **E2E_ENV_DEFAULTS** (2 connections) — `client/src/test/e2e-bootstrap.ts`
- **__dirname** (1 connections) — `client/tests/e2e/runtime/global-teardown.ts`
- **__filename** (1 connections) — `client/tests/e2e/runtime/global-teardown.ts`
- *... and 5 more nodes in this community*

## Relationships

- [[Playwright E2E Specs]] (3 shared connections)
- [[E 2 E Runtime Combat]] (1 shared connections)

## Source Files

- `client/src/test/e2e-bootstrap.test.ts`
- `client/src/test/e2e-bootstrap.ts`
- `client/tests/e2e/runtime/global-setup.ts`
- `client/tests/e2e/runtime/global-teardown.ts`

## Audit Trail

- EXTRACTED: 142 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
