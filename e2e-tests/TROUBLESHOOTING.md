# Error Handling and Troubleshooting Guide

## Overview

This document provides comprehensive troubleshooting procedures for common issues encountered during multiplayer test scenario execution. It includes both standard troubleshooting steps and performance-specific optimizations for different machine types.

## Common Issues and Solutions

### Issue 1: Server Won't Start

**Symptoms**:
- `./scripts/start_local.ps1` fails
- Server startup errors
- Port already in use errors

**Solutions**:

1. **Check if ports are already in use**:
   ```powershell
   netstat -an | findstr :54731
   netstat -an | findstr :5173
   ```

2. **Verify database file exists and is accessible**:
   ```powershell
   Test-Path "data/players/local_players.db"
   ```

3. **Check server logs for detailed error information**:
   ```powershell
   Get-Content logs/development/server.log -Tail 50
   ```

4. **Restart with proper shutdown sequence**:
   ```powershell
   ./scripts/stop_server.ps1
   Start-Sleep -Seconds 5
   ./scripts/start_local.ps1
   ```

5. **Low-Performance Machine Specific**:
   - Allow 5-10 minutes for server startup on very slow machines
   - Monitor system resources (CPU/Memory) during startup
   - Close unnecessary applications to free up resources
   - Check available disk space (minimum 2GB free recommended)

6. **High-Performance Machine Specific**:
   - Server should start within 30-60 seconds
   - If startup takes longer than 2 minutes, investigate system issues

### Issue 2: Players Can't Connect

**Symptoms**:
- Browser shows connection errors
- WebSocket connection failures
- Login timeouts

**Solutions**:

1. **Verify server is running on correct port**:
   ```powershell
   netstat -an | findstr :54731
   ```

2. **Check client accessibility**:
   ```powershell
   netstat -an | findstr :5173
   ```

3. **Verify database contains test players**:
   ```powershell
   sqlite3 data/players/local_players.db "SELECT name FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"
   ```

4. **Check network connectivity**:
   ```powershell
   Test-NetConnection -ComputerName localhost -Port 54731
   Test-NetConnection -ComputerName localhost -Port 5173
   ```

5. **Low-Performance Machine Specific**:
   - Use retry logic with 30-second intervals
   - Close other applications to free up system resources
   - Allow 2-3 minutes for initial connection establishment
   - Check browser memory usage and restart if needed

6. **High-Performance Machine Specific**:
   - Connections should establish within 5-10 seconds
   - If connections take longer than 30 seconds, investigate network issues

### Issue 3: Messages Not Appearing

**Symptoms**:
- Expected messages don't show up in chat
- WebSocket message delivery failures
- Timing-related message issues

**Solutions**:

1. **Wait longer for message delivery**:
   - Standard machines: Wait 10-15 seconds
   - Low-performance machines: Wait 30-60 seconds
   - High-performance machines: Wait 3-5 seconds

2. **Check browser console for errors**:
   ```javascript
   // In browser console
   console.log('WebSocket status:', window.websocket?.readyState);
   ```

3. **Verify WebSocket connections are active**:
   ```javascript
   // Check connection status
   await mcp_playwright_browser_evaluate({function: "() => window.websocket?.readyState === 1"});
   ```

4. **Check server logs for message broadcasting errors**:
   ```powershell
   Get-Content logs/development/server.log -Tail 100 | Select-String "message|broadcast|websocket"
   ```

5. **Low-Performance Machine Specific**:
   - Increase all wait_for timeouts to 30+ seconds
   - Add buffer time between critical operations
   - Check for memory pressure affecting message processing

6. **High-Performance Machine Specific**:
   - Messages should appear within 1-2 seconds
   - If messages take longer than 5 seconds, investigate server performance

### Issue 4: Database State Issues

**Symptoms**:
- Players in wrong rooms
- Missing test players
- Admin privileges not working

**Solutions**:

1. **Use SQLite CLI to verify player state**:
   ```powershell
   sqlite3 data/players/local_players.db
   ```

   ```sql
   -- Check current player state
   SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');

   -- Fix player locations
   UPDATE players SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001' WHERE name IN ('ArkanWolfshade', 'Ithaqua');

   -- Fix admin privileges
   UPDATE players SET is_admin = 1 WHERE name = 'ArkanWolfshade';

   -- Verify fixes
   SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');
   ```

2. **Check database file permissions**:
   ```powershell
   Get-Acl "data/players/local_players.db" | Format-List
   ```

3. **Restore from backup if needed**:
   ```powershell
   # If database is corrupted
   Copy-Item "data/players/local_players.db.backup" "data/players/local_players.db"
   ```

### Issue 5: Browser Automation Failures

**Symptoms**:
- Playwright commands fail
- Element not found errors
- Tab switching issues

**Solutions**:

1. **Check element selectors and references**:
   ```javascript
   // Verify element exists
   await mcp_playwright_browser_evaluate({function: "() => document.querySelector('[data-testid=\"element-id\"]') !== null"});
   ```

2. **Add explicit waits for element loading**:
   ```javascript
   // Wait for element to be available
   await mcp_playwright_browser_wait_for({text: "Expected Text", time: 30});
   ```

3. **Verify tab state before switching**:
   ```javascript
   // Check current tab count
   const tabs = await mcp_playwright_browser_tab_list();
   console.log('Current tabs:', tabs.length);
   ```

4. **Low-Performance Machine Specific**:
   - Use longer timeouts for all browser operations
   - Add buffer time between tab operations
   - Check browser memory usage and restart if needed

5. **High-Performance Machine Specific**:
   - Standard timeouts should be sufficient
   - If browser operations fail, check for system resource issues

## Performance-Specific Troubleshooting

### Low-Performance Machine Issues

**Common Symptoms**:
- Timeouts on all operations
- Slow browser responses
- Browser freezing or crashing
- Memory pressure warnings

**Solutions**:

1. **Memory Management**:
   ```powershell
   # Check available memory
   Get-WmiObject -Class Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory

   # Close unnecessary applications
   Get-Process | Where-Object {$_.WorkingSet -gt 100MB} | Sort-Object WorkingSet -Descending
   ```

2. **Browser Optimization**:
   - Use Chrome/Edge with hardware acceleration disabled
   - Close unnecessary browser tabs
   - Restart browser between test scenarios
   - Use incognito/private browsing mode

3. **System Resource Management**:
   - Close background applications
   - Disable unnecessary Windows services
   - Ensure minimum 4GB RAM available
   - Check disk space (minimum 5GB free)

4. **Timeout Adjustments**:
   - Double all standard timeouts
   - Add 10-15 second buffer between operations
   - Use retry logic for critical operations

### High-Performance Machine Issues

**Common Symptoms**:
- Unexpected timeouts despite fast hardware
- Race conditions in test execution
- Browser automation too fast for server

**Solutions**:

1. **Add Delays for Server Processing**:
   ```javascript
   // Add small delays for server processing
   await mcp_playwright_browser_wait_for({time: 1});
   ```

2. **Check for Race Conditions**:
   - Verify server state before proceeding
   - Add explicit state checks
   - Use proper synchronization

3. **Optimize for Speed**:
   - Use shorter timeouts where appropriate
   - Parallel operations where possible
   - Skip unnecessary waits

## Debugging Commands

### Check Server Status

```powershell
# Check if server is running
netstat -an | findstr :54731

# Check server logs
Get-Content logs/development/server.log -Tail 50

# Check server health endpoint
Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing
```

### Check Database State

```powershell
# Check player state
sqlite3 data/players/local_players.db "SELECT name, current_room_id, is_admin, last_active FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# Check database integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"
```

### Check Browser State

```javascript
// Get all messages in current tab
const messages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
console.log('Current messages:', messages);

// Get current room information
const roomInfo = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.room-description')?.textContent.trim()"});
console.log('Current room:', roomInfo);

// Check WebSocket connection
const wsStatus = await mcp_playwright_browser_evaluate({function: "() => window.websocket?.readyState"});
console.log('WebSocket status:', wsStatus);
```

## Emergency Recovery Procedures

### Complete System Reset

If all else fails:

1. **Force kill all processes**:
   ```powershell
   Get-Process | Where-Object {$_.ProcessName -like "*python*" -or $_.ProcessName -like "*node*"} | Stop-Process -Force
   ```

2. **Clear all ports**:
   ```powershell
   netstat -an | findstr :54731
   netstat -an | findstr :5173
   ```

3. **Restart from clean state**:
   ```powershell
   ./scripts/stop_server.ps1
   Start-Sleep -Seconds 10
   ./scripts/start_local.ps1
   ```

4. **Verify clean startup**:
   ```powershell
   # Wait 3 minutes for startup
   Start-Sleep -Seconds 180

   # Check server health
   Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing
   ```

## Prevention Strategies

### Regular Maintenance

1. **Daily**:
   - Check available disk space
   - Monitor system memory usage
   - Review server logs for errors

2. **Weekly**:
   - Archive old log files
   - Clean up temporary files
   - Update system if needed

3. **Before Major Test Sessions**:
   - Restart system for clean state
   - Close unnecessary applications
   - Verify all dependencies are current

### Best Practices

1. **Always follow the mandatory execution order**
2. **Complete database verification before starting server**
3. **Use appropriate timeouts for your machine type**
4. **Document any deviations from expected behavior**
5. **Keep logs for troubleshooting reference**

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Next Review**: As needed for troubleshooting updates
**Primary Audience**: AI Executors and Developers
**Update Frequency**: When new issues are discovered or solutions are improved
