# Quick Start: Running E2E Tests

## Prerequisites ✅

All infrastructure is in place:

- ✅ 114 automated Playwright tests created
- ✅ Test database seeding configured
- ✅ E2E test configuration file created
- ✅ UI elements have proper test IDs
- ✅ Playwright browsers installed

## Step 1: Start the E2E Test Server

Choose one of these methods:

### Method A: Use the E2E startup script (Simplest)

```powershell
.\scripts\start_e2e_test.ps1
```

This will:

- Stop any running servers
- Start server with `server/server_config.e2e_test.yaml`
- Use test database: `data/unit_test/players/unit_test_players.db`
- Open in new window

### Method B: Manual startup (More control)

```powershell
# Set the E2E test config
$env:MYTHOSMUD_CONFIG_PATH = "E:\projects\GitHub\MythosMUD\server\server_config.e2e_test.yaml"

# Start server
.\scripts\start_e2e_test.ps1 -Environment test
```

## Step 2: Wait for Server to Start

Watch the server window for:

```
Application startup complete
Uvicorn running on http://0.0.0.0:54731
```

## Step 3: Run the E2E Tests

In a **separate PowerShell window**:

```powershell
cd E:\projects\GitHub\MythosMUD\client
npm run test:e2e:runtime
```

This will:

- Auto-start Vite dev server (client)
- Run all 114 automated E2E tests
- Generate HTML report
- Show pass/fail results

## Expected Results

```
Running 114 tests using 1 worker

✓ 25 Logout Accessibility tests
✓ 5 Whisper Logging tests
✓ 8 Local Channel Error tests
✓ 9 Logout Error tests
✓ 10 Whisper Error tests
✓ 9 Whisper Rate Limiting tests
✓ 11 Local Channel Integration tests
✓ 13 Logout Button tests
✓ 13 Whisper Integration tests
✓ 10 Who Command tests

114 passed (Xm Xs)
```

## Troubleshooting

### Problem: Login failed (500)

**Cause**: Server not using test database
**Solution**: Verify `MYTHOSMUD_CONFIG_PATH` is set to `server_config.e2e_test.yaml`

### Problem: Server won't start

**Cause**: Configuration file not found
**Solution**: Verify `server/server_config.e2e_test.yaml` exists

### Problem: Tests timeout waiting for elements

**Cause**: Server not running or client not started
**Solution**: Ensure both server (port 54731) and client (port 5173) are running

### Problem: "element(s) not found" errors

**Cause**: Missing `data-testid` attributes
**Solution**: Verify recent changes didn't remove test IDs from UI components

## Test Credentials

The E2E tests use these pre-seeded test players:

| Username       | Password | Role      | Player ID               |
| -------------- | -------- | --------- | ----------------------- |
| ArkanWolfshade | Cthulhu1 | Admin     | test-player-arkan-001   |
| Ithaqua        | Cthulhu1 | Regular   | test-player-ithaqua-001 |
| TestAdmin      | Cthulhu1 | Superuser | test-player-admin-001   |

All players start in: `earth_arkhamcity_sanitarium_room_foyer_001`

## Viewing Test Results

After tests complete:

```powershell
# Open HTML report
npx playwright show-report client/playwright-report/runtime
```

Or click the link shown in terminal: `http://localhost:<port>`

## Next Actions

Once E2E tests are passing:

1. ✅ Verify all 114 tests pass
2. ✅ Review any failures
3. ✅ Run linting: `make lint`
4. ✅ Commit changes
5. ✅ Update GitHub Issues

The E2E test infrastructure is ready to run!
