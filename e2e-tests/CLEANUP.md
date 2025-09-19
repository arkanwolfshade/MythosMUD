# Post-Scenario Cleanup Procedures

## Overview

This document provides standardized cleanup procedures that should be executed after completing any multiplayer test scenario. These procedures ensure a clean state for subsequent test runs and prevent interference between different scenarios.

## Standard Cleanup Sequence

### Step 1: Close All Browser Tabs

**Purpose**: Ensure no stale browser sessions remain active

**Cursor Commands**:

```javascript
// Close all tabs except the first
const tabList = await mcp_playwright_browser_tab_list();
for (let i = tabList.length - 1; i > 0; i--) {
  await mcp_playwright_browser_tab_close({index: i});
}

// Close the last tab
await mcp_playwright_browser_tab_close({index: 0});
```

**Expected Result**: All browser tabs closed, no active browser sessions

### Step 2: Stop Development Server

**Purpose**: Ensure server is properly shut down to prevent port conflicts

**Cursor Command**:

```powershell
./scripts/stop_server.ps1
```

**Expected Result**: Server process terminated, no error messages

### Step 3: Verify Clean Shutdown

**Purpose**: Confirm all processes are properly terminated and ports are free

**Cursor Commands**:

```powershell
# Check if server port is free
netstat -an | findstr :54731

# Check if client port is free
netstat -an | findstr :5173
```

**Expected Result**: No processes found on ports 54731 and 5173

## Database State Cleanup

### Optional: Reset Player Locations

**When to Use**: If scenarios have moved players to different rooms and you want to ensure consistent starting state

**Cursor Commands**:

```powershell
# Open SQLite database
sqlite3 data/players/players.db
```

```sql
-- Reset players to starting room
UPDATE players SET current_room_id = 'earth_arkham_city_sanitarium_room_foyer_001' WHERE name IN ('ArkanWolfshade', 'Ithaqua');

-- Verify reset
SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');

-- Commit changes
.quit
```

**Expected Result**: Both players in Main Foyer, AW with admin privileges

## Log File Cleanup

### Optional: Archive Log Files

**When to Use**: For long test sessions or when log files become large

**Cursor Commands**:

```powershell
# Archive server logs (if needed)
if (Test-Path "logs/development/server.log") {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    Move-Item "logs/development/server.log" "logs/development/server.log.$timestamp"
}

# Archive client logs (if needed)
if (Test-Path "client/Logs") {
    Get-ChildItem "client/Logs" -Filter "*.log" | ForEach-Object {
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        Move-Item $_.FullName "$($_.FullName).$timestamp"
    }
}
```

## Performance Cleanup

### Clear Browser Cache (Optional)

**When to Use**: If experiencing browser-related issues or for completely clean test runs

**Cursor Commands**:

```javascript
// Clear browser cache and storage
await mcp_playwright_browser_evaluate({function: "() => { localStorage.clear(); sessionStorage.clear(); }"});
```

## Error Recovery Cleanup

### Force Kill Processes (Emergency Only)

**When to Use**: If standard cleanup fails or processes become unresponsive

**⚠️ WARNING**: Only use as last resort

**Cursor Commands**:

```powershell
# Force kill any remaining server processes
Get-Process | Where-Object {$_.ProcessName -like "*python*" -and $_.CommandLine -like "*uvicorn*"} | Stop-Process -Force

# Force kill any remaining client processes
Get-Process | Where-Object {$_.ProcessName -like "*node*" -and $_.CommandLine -like "*vite*"} | Stop-Process -Force

# Verify ports are free
netstat -an | findstr :54731
netstat -an | findstr :5173
```

## Cleanup Verification Checklist

After completing cleanup procedures, verify:

- [ ] All browser tabs closed
- [ ] Server process terminated
- [ ] Ports 54731 and 5173 are free
- [ ] No error messages in cleanup process
- [ ] Database state is consistent (if reset was performed)
- [ ] Log files archived (if cleanup was performed)

## Integration with Scenarios

### Automatic Cleanup

Most scenarios should include cleanup steps at the end:

```markdown
## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown
```

### Manual Cleanup

For scenarios that require manual intervention or when cleanup fails:

```markdown
## Manual Cleanup Required

If automatic cleanup fails:
1. Manually close all browser windows
2. Run `./scripts/stop_server.ps1`
3. Verify ports are free with `netstat -an | findstr :54731`
4. Check @TROUBLESHOOTING.md for additional recovery steps
```

## Performance Considerations

### Low-Performance Machines

- Allow extra time for browser tab closure (5-10 seconds between operations)
- Use longer timeouts for server shutdown verification
- Consider archiving log files more frequently to prevent disk space issues

### High-Performance Machines

- Standard cleanup procedures should complete quickly
- Can perform more aggressive cleanup (cache clearing, log archiving)
- May skip some optional cleanup steps for faster test cycles

## Troubleshooting

If cleanup procedures fail:

1. **Check @TROUBLESHOOTING.md** for specific error recovery steps
2. **Verify process status** with `Get-Process` commands
3. **Check port usage** with `netstat` commands
4. **Review log files** for error messages
5. **Use force kill procedures** only as last resort

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Next Review**: As needed for cleanup procedure updates
**Primary Audience**: AI Executors and Developers
**Update Frequency**: When cleanup procedures change
