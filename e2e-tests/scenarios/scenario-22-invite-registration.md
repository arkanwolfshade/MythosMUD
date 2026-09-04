# Scenario 22: Invite-Only Registration Enforcement

## Overview

Verifies #733's fix end-to-end through the real client UI: registration must be rejected when
the invite code is blank, invalid, or already used. Before this fix, an omitted `invite_code`
created an account anyway (the invite-only system was not actually enforced). This scenario is
single-player and does not require multi-tab coordination.

**Testing Approach**: Playwright MCP (single tab; no multiplayer coordination needed)

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Server Running**: Development server running on port 54768 (see `mythosmud-server-runbook`
   skill - stop first, verify ports free, start once)
2. **Client Accessible**: Client is accessible on port 5173
3. **Seeded Invites**: Three rows exist in `mythos_dev.invites`:
   - One active, unexpired code (`VALID`)
   - One active but expired code (`EXPIRED`)
   - One already-used (`is_active = false`) code (`USED`)

   Seed via direct SQL against `mythos_dev` (additive only - never truncate/delete existing
   rows in `mythos_dev` per `.claude/rules/database.md`):

   ```sql
   INSERT INTO invites (id, invite_code, is_active, expires_at) VALUES
     (gen_random_uuid(), 'E2E-VALID-<run-id>', true, now() + interval '1 day'),
     (gen_random_uuid(), 'E2E-EXPIRED-<run-id>', true, now() - interval '1 day'),
     (gen_random_uuid(), 'E2E-USED-<run-id>', false, now() + interval '1 day');
   ```

   Use a run-specific suffix (e.g. a short UUID) so codes don't collide across runs, and record
   it for the cleanup step.

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

## Test Configuration

**Test Player**: none created by this scenario - every step is expected to reject registration.

**Form selectors** (from `client/src/mythosApp/MythosLoginForm.tsx`): username input
`[data-testid="username-input"]`, password input `[data-testid="password-input"]`, invite code
input `input[placeholder="Invite Code"]` (only rendered once in registration mode - click the
"Need an account? Register" toggle first), submit button `[data-testid="login-button"]`, error
text rendered in `.error-message`.

## Execution Steps

### Step 1: Switch to registration mode

**Purpose**: Reveal the invite code field.

**Commands**:

```javascript
await mcp_playwright_browser_navigate({ url: "http://localhost:5173" });
await mcp_playwright_browser_click({ element: "Need an account? Register toggle", ref: "text=Need an account? Register" });
```

**Expected Result**: Invite Code input becomes visible.

### Step 2: Blank invite code is rejected client-side, no request sent

**Purpose**: Verify `sanitizeRegisterInputs` blocks submission before any network call
(`client/src/mythosApp/useMythosAuthForm.ts:37-42`).

**Commands**:

```javascript
await mcp_playwright_browser_type({ element: "Username input", ref: "[data-testid=\"username-input\"]", text: "e2e_invite_test_1" });
await mcp_playwright_browser_type({ element: "Password input", ref: "[data-testid=\"password-input\"]", text: "testpassword123" });
// Invite code left blank
await mcp_playwright_browser_click({ element: "Submit button", ref: "[data-testid=\"login-button\"]" });
const errorText = await mcp_playwright_browser_evaluate({ function: "() => document.querySelector('.error-message')?.textContent ?? null" });
console.log('Blank invite code error:', errorText);
```

**Expected Result**: `.error-message` reads "Username, password, and invite code are required".
No network request to `/auth/register` (client-side rejection only).

### Step 3: Invalid invite code is rejected by the server

**Purpose**: Verify the server rejects an unknown code with a clear message.

**Commands**:

```javascript
await mcp_playwright_browser_type({ element: "Invite code input", ref: "input[placeholder=\"Invite Code\"]", text: "NOT-A-REAL-CODE" });
await mcp_playwright_browser_click({ element: "Submit button", ref: "[data-testid=\"login-button\"]" });
await mcp_playwright_browser_wait_for({ text: "Invalid invite code" });
const errorText = await mcp_playwright_browser_evaluate({ function: "() => document.querySelector('.error-message')?.textContent ?? null" });
console.log('Invalid invite code error:', errorText);
```

**Expected Result**: `.error-message` reads "Invalid invite code" (400 from
`InviteManager.validate_invite`'s early rejection).

### Step 4: Expired invite code is rejected by the server

**Purpose**: Verify an expired-but-still-active code is rejected.

**Commands**:

```javascript
await mcp_playwright_browser_type({ element: "Invite code input", ref: "input[placeholder=\"Invite Code\"]", text: "E2E-EXPIRED-<run-id>" });
await mcp_playwright_browser_click({ element: "Submit button", ref: "[data-testid=\"login-button\"]" });
await mcp_playwright_browser_wait_for({ text: "expired or already used" });
const errorText = await mcp_playwright_browser_evaluate({ function: "() => document.querySelector('.error-message')?.textContent ?? null" });
console.log('Expired invite code error:', errorText);
```

**Expected Result**: `.error-message` reads "Invite code is expired or already used".

### Step 5: Already-used invite code is rejected by the server

**Purpose**: Verify a code already marked `is_active = false` is rejected - this is the direct
UI-level check on #733's reuse-race fix (`reserve_invite`/`capture_invite`).

**Commands**:

```javascript
await mcp_playwright_browser_type({ element: "Invite code input", ref: "input[placeholder=\"Invite Code\"]", text: "E2E-USED-<run-id>" });
await mcp_playwright_browser_click({ element: "Submit button", ref: "[data-testid=\"login-button\"]" });
await mcp_playwright_browser_wait_for({ text: "expired or already used" });
const errorText = await mcp_playwright_browser_evaluate({ function: "() => document.querySelector('.error-message')?.textContent ?? null" });
console.log('Used invite code error:', errorText);
```

**Expected Result**: `.error-message` reads "Invite code is expired or already used" - the same
message as an expired code (`InviteManager.validate_invite` does not distinguish the two, by
design, so a bypass attempt cannot tell which failure mode it hit).

### Step 6: Valid invite code succeeds (control case)

**Purpose**: Prove the rejection cases above are testing the actual invite gate, not a broken
form - a valid code must still register successfully.

**Commands**:

```javascript
await mcp_playwright_browser_type({ element: "Invite code input", ref: "input[placeholder=\"Invite Code\"]", text: "E2E-VALID-<run-id>" });
await mcp_playwright_browser_click({ element: "Submit button", ref: "[data-testid=\"login-button\"]" });
await mcp_playwright_browser_wait_for({ text: "e2e_invite_test_1" });
const url = await mcp_playwright_browser_evaluate({ function: "() => window.location.href" });
console.log('Post-registration URL:', url);
```

**Expected Result**: Registration succeeds; session is established (redirect away from the login
form).

## Expected Results

✅ Blank invite code blocked client-side with a clear message, no request sent
✅ Invalid invite code rejected server-side ("Invalid invite code")
✅ Expired invite code rejected server-side ("expired or already used")
✅ Already-used invite code rejected server-side (same message as expired - #733's reuse fix)
✅ Valid invite code still succeeds (control case - the gate isn't just failing everything)

## Success Criteria Checklist

- [x] Blank invite code shows client-side error, no network request
- [x] Invalid invite code shows server rejection
- [x] Expired invite code shows server rejection
- [x] Already-used invite code shows server rejection
- [x] Valid invite code registers successfully
- [x] Server remains stable throughout the scenario
- [x] Scenario completion is properly documented

## Cleanup

1. Delete the three seeded invite rows and the `e2e_invite_test_1` user created in Step 6 from
   `mythos_dev` (additive test data only - do not touch anything else in `mythos_dev`).
2. Execute standard cleanup procedures from @CLEANUP.md: close browser tabs, stop development
   server, verify clean shutdown.

## Execution Record

**Executed**: 2026-08-28, via Playwright MCP against local dev server (`mythos_dev`), run id
`1787951311`.

| Step | Result | Notes |
|---|---|---|
| 1. Switch to registration mode | ✅ Pass | Invite Code field appeared |
| 2. Blank invite code | ✅ Pass | `.error-message`: "Username, password, and invite code are required"; no network request |
| 3. Invalid invite code | ✅ Pass | `.error-message`: "Invalid invite code" |
| 4. Expired invite code | ✅ Pass | `.error-message`: "Invite code is expired or already used" |
| 5. Already-used invite code | ✅ Pass | Same message as expired (by design); confirmed via console event trace that a fresh click/render cycle occurred, not a stale error |
| 6. Valid invite code (control) | ⚠️ Pass, after fixing an environment gap | See below |

**Environment gap found and fixed, not part of #733's code**: Step 6 initially failed with
`asyncpg.exceptions.UndefinedFunctionError: function reserve_invite(unknown) does not exist`
against `mythos_dev` (confirmed in `logs/local/errors.log`). `db/procedures/players.sql`'s
`reserve_invite`/`capture_invite` had been applied to `mythos_unit` (the test DB, via
`make test-server`) but never to `mythos_dev`, which the local dev server actually connects to
- there is no automatic apply step for the interactive dev server the way there is for the test
suite. Ran `scripts/apply_procedures.ps1 -TargetDbs mythos_dev` and retried; registration then
succeeded and advanced to the real Character Creation screen (stat rollout), confirming the
enforcement rejects invalid/expired/used codes without breaking the valid-code path.

**Cleanup performed**: seeded invite rows (`E2E-VALID/EXPIRED/USED-1787951311`) and the
`e2e_invite_test_1` user created in Step 6 deleted from `mythos_dev`; browser tab closed; server
stopped (`stop_server.ps1` - clean shutdown confirmed via unreachable `/docs` despite a lingering
`TIME_WAIT` on port 54768 under PID 0, a normal Windows TCP artifact, not a live process).

## Status

### ✅ EXECUTED - ALL STEPS PASSED

---

**Document Version**: 1.0
**Created**: 2026-08-28
**Scenario ID**: 22
**Testing Approach**: Playwright MCP (single tab)
**Related**: #733 (server/auth/endpoints.py, server/auth/invites.py,
db/procedures/players.sql - reserve_invite/capture_invite)
**Estimated Duration**: 5-8 minutes
