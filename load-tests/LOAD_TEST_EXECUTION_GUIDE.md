# Load Test Execution Guide - 10 Concurrent Players

This guide provides step-by-step instructions for executing the load test using Playwright MCP tools.

## Prerequisites

1. **Stop any running server**: Run `./scripts/stop_server.ps1`
2. **Verify ports are free**: Check ports 54731 and 5173
3. **Get invite codes**: Query database for 10 active invite codes
4. **Start server**: Run `./scripts/start_local.ps1` (wait for server to be ready)

## Step 1: Get Invite Codes from Database

Before starting, query the database for 10 active invite codes:

```python
# Use server/scripts/list_active_invites.py or similar tool
# Store the 10 invite codes for use in registration
```

## Step 2: Registration Phase (Concurrent)

For each of the 10 players, open a new browser tab and register:

### Player 1 (Tramp)
```javascript
// Open new tab
await mcp_playwright_browser_tabs({action: "new"});

// Navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Fill registration form
await mcp_playwright_browser_fill_form({
  fields: [
    {name: "Username", type: "textbox", ref: "username-input", value: "loadtest_player_1"},
    {name: "Password", type: "textbox", ref: "password-input", value: "LoadTest123!"},
    {name: "Invite Code", type: "textbox", ref: "invite-input", value: "INVITE_CODE_1"}
  ]
});

// Submit registration
await mcp_playwright_browser_click({element: "Register button", ref: "register-button"});

// Wait for profession selection screen
await mcp_playwright_browser_wait_for({text: "Choose Your Profession"});
```

Repeat for players 2-10 with their respective usernames and invite codes.

## Step 3: Profession Selection and Character Creation

For each player, select their assigned profession and complete character creation:

### Player 1 (Tramp - profession_id: 0)
```javascript
// Select Tramp profession
await mcp_playwright_browser_click({element: "Tramp profession card", ref: "profession-0"});

// Click Next
await mcp_playwright_browser_click({element: "Next button", ref: "next-button"});

// Wait for stats rolling screen
await mcp_playwright_browser_wait_for({text: "Roll Stats"});

// Accept stats (click Accept button)
await mcp_playwright_browser_click({element: "Accept button", ref: "accept-button"});

// Wait for game to load
await mcp_playwright_browser_wait_for({text: "Enter the Realm"});
```

### Player 2 (Antiquarian - profession_id: 1)
```javascript
// Select Antiquarian profession
await mcp_playwright_browser_click({element: "Antiquarian profession card", ref: "profession-1"});
// ... (same flow as Player 1)
```

Continue for all 10 players with their assigned professions:
- Player 3: Author (profession_id: 2)
- Player 4: Dilettante (profession_id: 3)
- Player 5: Doctor of Medicine (profession_id: 4)
- Player 6: Journalist (profession_id: 5)
- Player 7: Police Detective (profession_id: 6)
- Player 8: Private Investigator (profession_id: 7)
- Player 9: Professor (profession_id: 8)
- Player 10: Tramp (profession_id: 0)

## Step 4: Enter Game (All Players)

For each player, click "Enter the Realm" to enter the game:

```javascript
// Switch to player's tab
await mcp_playwright_browser_tabs({action: "select", index: PLAYER_INDEX});

// Click "Enter the Realm"
await mcp_playwright_browser_click({element: "Enter the Realm button", ref: "enter-realm-button"});

// Wait for game client to load
await mcp_playwright_browser_wait_for({text: "Command input"});
```

## Step 5: Action Execution Phase

Execute actions sequentially for each player:

### Player 1: look, say Hello everyone
```javascript
await mcp_playwright_browser_tabs({action: "select", index: 0});
await mcp_playwright_browser_type({element: "Command input", ref: "command-input", text: "look"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 2});
await mcp_playwright_browser_type({element: "Command input", ref: "command-input", text: "say Hello everyone"});
await mcp_playwright_browser_press_key({key: "Enter"});
```

### Player 2: go north, who
```javascript
await mcp_playwright_browser_tabs({action: "select", index: 1});
await mcp_playwright_browser_type({element: "Command input", ref: "command-input", text: "go north"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 2});
await mcp_playwright_browser_type({element: "Command input", ref: "command-input", text: "who"});
await mcp_playwright_browser_press_key({key: "Enter"});
```

Continue for all 10 players with their assigned actions (see plan for full list).

## Step 6: Idle Phase

After all actions complete, maintain all players connected for 5 minutes:

```javascript
// Wait for 5 minutes (300 seconds)
await mcp_playwright_browser_wait_for({time: 300});

// Monitor for disconnections during this period
// Check each tab periodically to ensure connections are still active
```

## Step 7: Server Shutdown

After idle period, shut down the server:

```powershell
# Run from terminal
./scripts/stop_server.ps1
```

## Step 8: Log Analysis

Analyze the log files:

```powershell
# Read errors.log
Get-Content logs/local/errors.log

# Read warnings.log
Get-Content logs/local/warnings.log
```

Document all errors and warnings found.

## Notes

- All registrations should happen concurrently (use Promise.all() pattern)
- All logins should happen concurrently
- Actions should be executed sequentially per player to avoid race conditions
- Monitor for connection issues during the 5-minute idle period
- Document any errors or warnings found in the log files
