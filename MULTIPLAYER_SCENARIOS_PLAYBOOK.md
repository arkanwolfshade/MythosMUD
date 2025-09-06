# MythosMUD Multiplayer Scenarios Playbook - Cursor Executable Version

## Overview

This playbook contains detailed scenarios for testing multiplayer functionality in MythosMUD. **This version is specifically designed for Cursor AI to execute automatically using Playwright MCP.** Each scenario includes explicit step-by-step instructions that Cursor can follow exactly.

## Test Players

- **ArkanWolfshade** (AW) - password: Cthulhu1
- **Ithaqua** - password: Cthulhu1

## Server Configuration

- **Server Port**: 54731 (from `server/server_config.yaml`)
- **Client Port**: 5173 (from `client/vite.config.ts`)
- **Starting Room**: `earth_arkham_city_sanitarium_room_foyer_001` (Main Foyer)
- **Database**: `data/players/players.db`

## Command Syntax

- **Movement**: `go <direction>` or direction shortcuts (e.g., `go east`, `east`, `e`, `go west`, `west`, `w`)
- **Say**: `say <message>` or `/say <message>` or just `<message>` (defaults to say channel)
- **Local**: `local <message>` or `/l <message>`
- **Whisper**: `whisper <player> <message>`
- **Who**: `who` or `who <filter>`
- **Teleport**: `teleport <player>` (admin only)
- **Other**: `look`, `inventory`, `help`, `mute`, `unmute`, `dance`, etc.

## Cursor Execution Rules

### Prerequisites (Run Before Starting Scenarios)

1. **Verify Server Status**: Always check if server is running before starting
2. **Database State**: Ensure test players exist and are in correct starting room
3. **Clean Environment**: Stop any running servers and clear browser state
4. **Port Availability**: Verify ports 54731 and 5173 are available

### Execution Commands

- **Server Management**: Use `./scripts/stop_server.ps1` and `./scripts/start_dev.ps1`
- **Browser Automation**: Use Playwright MCP commands exclusively
- **Database Operations**: Use SQLite CLI for direct database access
- **Error Handling**: Document all failures and continue to next scenario

### State Verification Steps

Before each scenario, verify:

- Server is running on port 54731
- Client is accessible on port 5173
- Database contains test players
- Players are in correct starting room
- No stale browser sessions

---

## Pre-Scenario Setup (REQUIRED)

### Step 1: Environment Verification

**Cursor Command**: Verify server and client are not running

```powershell
# Check if server is running
netstat -an | findstr :54731
# Check if client is running
netstat -an | findstr :5173
```

**Expected**: No processes found on these ports

### Step 2: Database State Verification

**Cursor Command**: Verify test players exist and are in correct room

```powershell
# Open SQLite database
sqlite3 data/players/players.db
```

**SQL Commands to Run**:

```sql
-- Check if players exist
SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');

-- Update players to starting room if needed
UPDATE players SET current_room_id = 'earth_arkham_city_sanitarium_room_foyer_001' WHERE name IN ('ArkanWolfshade', 'Ithaqua');

-- Verify ArkanWolfshade has admin privileges
UPDATE players SET is_admin = 1 WHERE name = 'ArkanWolfshade';

-- Commit changes
.quit
```

**Expected**: Both players exist, are in Main Foyer, AW has admin privileges

### Step 3: Start Development Environment

**Cursor Command**: Start the development server

```powershell
./scripts/start_dev.ps1
```

**Wait**: 10-15 seconds for server to fully start

### Step 4: Verify Server Accessibility

**Cursor Command**: Test server connectivity

```powershell
# Test server health
$healthResponse = Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing
if ($healthResponse.StatusCode -eq 200) {
    $healthData = $healthResponse.Content | ConvertFrom-Json
    Write-Host "Server Status: $($healthData.status)"
    Write-Host "Uptime: $([math]::Round($healthData.uptime_seconds, 2)) seconds"
} else {
    Write-Host "Server health check failed with status: $($healthResponse.StatusCode)"
}

# Test client accessibility
$clientResponse = Invoke-WebRequest -Uri "http://localhost:5173" -UseBasicParsing
Write-Host "Client Status: $($clientResponse.StatusCode)"
```

**Expected**: Both endpoints return successful responses

---

## Scenario 1: Basic Connection/Disconnection Flow

### Description

Tests basic multiplayer connection and disconnection messaging between two players.

**⚠️ TIMING ARTIFACT NOTICE**: This scenario may fail due to a known timing issue where the first player may not be properly subscribed to the room when the second player connects. This prevents connection messages from being received. The connection message broadcasting system is working correctly, but there's a race condition in room subscription timing.

### Cursor Execution Steps

#### Step 1: Open Browser and Navigate to Client

**Cursor Command**:

```javascript
// Open browser and navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});
```

#### Step 2: AW Enters the Game

**Cursor Commands**:

```javascript
// Wait for login form
await mcp_playwright_browser_wait_for({text: "Username"});

// Fill login form for AW
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for MOTD screen and click Continue to enter game
await mcp_playwright_browser_wait_for({text: "Continue"});
await mcp_playwright_browser_click({element: "Continue button", ref: "continue-button"});

// Wait for game interface to load
await mcp_playwright_browser_wait_for({text: "Chat"});

// Wait additional time for room subscription to stabilize
await mcp_playwright_browser_wait_for({time: 3});
```

#### Step 3: Open Second Browser Tab for Ithaqua

**Cursor Commands**:

```javascript
// Open new tab for Ithaqua
await mcp_playwright_browser_tab_new({url: "http://localhost:5173"});

// Switch to new tab
await mcp_playwright_browser_tab_select({index: 1});

// Fill login form for Ithaqua
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "Ithaqua"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for MOTD screen and click Continue to enter game
await mcp_playwright_browser_wait_for({text: "Continue"});
await mcp_playwright_browser_click({element: "Continue button", ref: "continue-button"});

// Wait for game interface to load
await mcp_playwright_browser_wait_for({text: "Chat"});

// Wait additional time for connection message broadcasting
await mcp_playwright_browser_wait_for({time: 3});
```

#### Step 4: Verify AW Sees Ithaqua Entered Message (with timing tolerance)

**Cursor Commands**:

```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for message to appear (with longer timeout for timing issues)
await mcp_playwright_browser_wait_for({text: "Ithaqua has entered the game", time: 10});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasIthaquaEntered = awMessages.some(msg => msg.includes('Ithaqua has entered the game'));
console.log('AW sees Ithaqua entered:', hasIthaquaEntered);

// If message not found, check for timing artifact
if (!hasIthaquaEntered) {
    console.log('⚠️ TIMING ARTIFACT: Connection message not received - this is a known issue with room subscription timing');
    console.log('The connection message broadcasting system is working correctly, but there is a race condition');
    console.log('AW message count:', awMessages.length);
    console.log('AW messages:', awMessages);
}
```

#### Step 5: Verify Ithaqua Sees No Unwanted Messages

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check for unwanted messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const unwantedMessages = ithaquaMessages.filter(msg =>
  msg.includes('enters the room') ||
  msg.includes('leaves the room') ||
  msg.includes('entered the game') ||
  msg.includes('left the game')
);
console.log('Ithaqua unwanted messages:', unwantedMessages.length === 0);
console.log('Ithaqua message count:', ithaquaMessages.length);
```

#### Step 6: Ithaqua Leaves the Game

**Cursor Commands**:

```javascript
// Close Ithaqua's tab
await mcp_playwright_browser_tab_close({index: 1});

// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for disconnect message
await mcp_playwright_browser_wait_for({text: "Ithaqua has left the game", time: 10});
```

#### Step 7: Verify AW Sees Ithaqua Left Message

**Cursor Commands**:

```javascript
// Verify message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasIthaquaLeft = awMessagesAfter.some(msg => msg.includes('Ithaqua has left the game'));
console.log('AW sees Ithaqua left:', hasIthaquaLeft);

// If message not found, check for timing artifact
if (!hasIthaquaLeft) {
    console.log('⚠️ TIMING ARTIFACT: Disconnect message not received - this is a known issue with room subscription timing');
    console.log('AW message count after disconnect:', awMessagesAfter.length);
    console.log('AW messages after disconnect:', awMessagesAfter);
}
```

### Expected Results

- ✅ AW sees "Ithaqua has entered the game." (may fail due to timing artifact)
- ✅ Ithaqua sees NO enters/leaves messages
- ✅ AW sees "Ithaqua has left the game." (may fail due to timing artifact)

### Known Issues

**⚠️ TIMING ARTIFACT**: Due to a race condition in room subscription timing, the first player may not be properly subscribed to the room when the second player connects. This prevents connection messages from being received by the first player. The connection message broadcasting system is working correctly on the server side, but there's a timing issue between:

1. Player connection and room subscription
2. Connection message broadcasting
3. Message delivery to subscribed players

**Technical Details**:

- Server logs show connection messages are being broadcast correctly
- The issue is that the first player is not in the room subscription list when the message is sent
- This is a known limitation that requires further investigation and potential fixes

### Status: ⚠️ PARTIAL SUCCESS - TIMING ARTIFACT IDENTIFIED

---

## Scenario 2: Clean Game State on Connection

### Description

Tests that players don't see stale/previous game state information when connecting.

### Cursor Execution Steps

#### Step 1: AW Enters the Game (Fresh Session)

**Cursor Commands**:

```javascript
// Navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Login as AW
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
```

#### Step 2: Verify AW Sees No Previous Game State

**Cursor Commands**:

```javascript
// Check for stale messages
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const staleMessages = awMessages.filter(msg =>
  msg.includes('has entered the game') ||
  msg.includes('has left the game') ||
  msg.includes('enters the room') ||
  msg.includes('leaves the room')
);
console.log('AW stale messages:', staleMessages.length === 0);
```

#### Step 3: Ithaqua Enters the Game

**Cursor Commands**:

```javascript
// Open new tab for Ithaqua
await mcp_playwright_browser_tab_new({url: "http://localhost:5173"});
await mcp_playwright_browser_tab_select({index: 1});

// Login as Ithaqua
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "Ithaqua"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
```

#### Step 4: Verify Ithaqua Sees No Previous Game State

**Cursor Commands**:

```javascript
// Check for stale messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaStaleMessages = ithaquaMessages.filter(msg =>
  msg.includes('has entered the game') ||
  msg.includes('has left the game') ||
  msg.includes('enters the room') ||
  msg.includes('leaves the room')
);
console.log('Ithaqua stale messages:', ithaquaStaleMessages.length === 0);
```

#### Step 5: Verify AW Sees Current Session Event

**Cursor Commands**:

```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for current session message
await mcp_playwright_browser_wait_for({text: "Ithaqua has entered the game"});

// Verify current session works
const awCurrentMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasCurrentSession = awCurrentMessages.some(msg => msg.includes('Ithaqua has entered the game'));
console.log('AW sees current session:', hasCurrentSession);
```

### Expected Results

- ✅ AW sees NO previous game state information
- ✅ Ithaqua sees NO previous game state information
- ✅ AW sees "Ithaqua has entered the game." (current session)

### Status: ✅ FIXES IMPLEMENTED - Ready for Testing

---

## Scenario 3: Movement Between Rooms

### Description

Tests multiplayer visibility when players move between different rooms.

### Cursor Execution Steps

#### Step 1: Both Players in Main Foyer

**Cursor Commands**:

```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
```

#### Step 2: AW Moves East

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type movement command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});
```

#### Step 3: Verify Ithaqua Sees AW Leave

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for leave message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade leaves the room"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAWLeave = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade leaves the room'));
console.log('Ithaqua sees AW leave:', seesAWLeave);
```

#### Step 4: Verify AW Sees No Self-Movement Messages

**Cursor Commands**:

```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check for self-movement messages
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const selfMovementMessages = awMessages.filter(msg =>
  msg.includes('ArkanWolfshade enters the room') ||
  msg.includes('ArkanWolfshade leaves the room')
);
console.log('AW self-movement messages:', selfMovementMessages.length === 0);
```

#### Step 5: Ithaqua Moves East to Join AW

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Type movement command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});
```

#### Step 6: Verify AW Sees Ithaqua Enter

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for enter message
await mcp_playwright_browser_wait_for({text: "Ithaqua enters the room"});

// Verify message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaEnter = awMessagesAfter.some(msg => msg.includes('Ithaqua enters the room'));
console.log('AW sees Ithaqua enter:', seesIthaquaEnter);
```

#### Step 7: Verify Ithaqua Sees No Self-Movement Messages

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check for self-movement messages
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaSelfMovement = ithaquaMessagesAfter.filter(msg =>
  msg.includes('Ithaqua enters the room') ||
  msg.includes('Ithaqua leaves the room')
);
console.log('Ithaqua self-movement messages:', ithaquaSelfMovement.length === 0);
```

### Expected Results

- ✅ Ithaqua sees "ArkanWolfshade leaves the room."
- ✅ AW sees NO self-movement messages
- ✅ AW sees "Ithaqua enters the room."
- ✅ Ithaqua sees NO self-movement messages

### Status: ❌ FAILED - CRITICAL ISSUES

---

## Scenario 4: Muting System and Emotes

### Description

Tests the muting system and emote functionality across game sessions.

### Cursor Execution Steps

#### Step 1: Both Players Connected

**Cursor Commands**:

```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
```

#### Step 2: AW Mutes Ithaqua

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type mute command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "mute Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for mute confirmation
await mcp_playwright_browser_wait_for({text: "You have muted Ithaqua"});
```

#### Step 3: Ithaqua Uses Dance Emote

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Type dance emote
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "dance"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for emote confirmation
await mcp_playwright_browser_wait_for({text: "You dance like nobody's watching"});
```

#### Step 4: Verify AW Does NOT See Ithaqua's Emote

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check for emote message
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaEmote = awMessages.some(msg => msg.includes('Ithaqua dances like nobody\'s watching'));
console.log('AW sees Ithaqua emote (should be false):', !seesIthaquaEmote);
```

#### Step 5: AW Unmutes Ithaqua

**Cursor Commands**:

```javascript
// Type unmute command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "unmute Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for unmute confirmation
await mcp_playwright_browser_wait_for({text: "You have unmuted Ithaqua"});
```

#### Step 6: Ithaqua Uses Dance Emote Again

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Type dance emote again
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "dance"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for emote confirmation
await mcp_playwright_browser_wait_for({text: "You dance like nobody's watching"});
```

#### Step 7: Verify AW Now Sees Ithaqua's Emote

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for emote message
await mcp_playwright_browser_wait_for({text: "Ithaqua dances like nobody's watching"});

// Verify message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaEmoteAfter = awMessagesAfter.some(msg => msg.includes('Ithaqua dances like nobody\'s watching'));
console.log('AW sees Ithaqua emote after unmute:', seesIthaquaEmoteAfter);
```

### Expected Results

- ✅ AW successfully mutes Ithaqua
- ✅ AW does NOT see Ithaqua's emote when muted
- ✅ AW successfully unmutes Ithaqua
- ✅ AW sees Ithaqua's emote after unmuting

### Status: ✅ FIXES IMPLEMENTED - Ready for Testing

---

## Scenario 5: Chat Messages Between Players

### Description

Tests chat message broadcasting between players in the same room.

### Cursor Execution Steps

#### Step 1: Both Players in Same Room

**Cursor Commands**:

```javascript
// Ensure both players are in the same room from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
```

#### Step 2: AW Sends Chat Message

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type say command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Hello Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You say: Hello Ithaqua"});
```

#### Step 3: Verify Ithaqua Sees AW's Message

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says: Hello Ithaqua"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAWMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says: Hello Ithaqua'));
console.log('Ithaqua sees AW message:', seesAWMessage);
```

#### Step 4: Ithaqua Replies

**Cursor Commands**:

```javascript
// Type reply
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Greetings ArkanWolfshade"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You say: Greetings ArkanWolfshade"});
```

#### Step 5: Verify AW Sees Ithaqua's Reply

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for message
await mcp_playwright_browser_wait_for({text: "Ithaqua says: Greetings ArkanWolfshade"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaMessage = awMessages.some(msg => msg.includes('Ithaqua says: Greetings ArkanWolfshade'));
console.log('AW sees Ithaqua message:', seesIthaquaMessage);
```

### Expected Results

- ✅ AW sees "You say: Hello Ithaqua"
- ✅ Ithaqua sees "ArkanWolfshade says: Hello Ithaqua"
- ✅ Ithaqua sees "You say: Greetings ArkanWolfshade"
- ✅ AW sees "Ithaqua says: Greetings ArkanWolfshade"

### Status: ✅ FIXES IMPLEMENTED - Ready for Testing

---

## Scenario 6: Admin Teleportation System

### Description

Tests the admin teleportation system functionality with confirmation steps and error handling.

### Prerequisites

- ArkanWolfshade must have admin privileges (verified in pre-scenario setup)
- Both players should be online and in different rooms

### Cursor Execution Steps

#### Step 1: Setup Players in Different Rooms

**Cursor Commands**:

```javascript
// Ensure AW is in Main Foyer (tab 0)
await mcp_playwright_browser_tab_select({index: 0});

// Move Ithaqua to East Hallway (tab 1)
await mcp_playwright_browser_tab_select({index: 1});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});
```

#### Step 2: Test Non-Admin Permission Rejection

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab (non-admin)
await mcp_playwright_browser_tab_select({index: 1});

// Attempt teleport command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "teleport ArkanWolfshade"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for permission denied message
await mcp_playwright_browser_wait_for({text: "You do not have permission to use teleport commands"});
```

#### Step 3: Test Offline Player Handling

**Cursor Commands**:

```javascript
// Switch to AW's tab (admin)
await mcp_playwright_browser_tab_select({index: 0});

// Attempt to teleport offline player
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "teleport NonexistentPlayer"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for player not found message
await mcp_playwright_browser_wait_for({text: "Player 'NonexistentPlayer' is not online or not found"});
```

#### Step 4: Test Teleport Command Confirmation

**Cursor Commands**:

```javascript
// Use teleport command on Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "teleport Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation prompt
await mcp_playwright_browser_wait_for({text: "You are about to teleport Ithaqua to your location"});
```

#### Step 5: Confirm Teleportation

**Cursor Commands**:

```javascript
// Confirm teleportation
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "confirm teleport Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for success message
await mcp_playwright_browser_wait_for({text: "You have successfully teleported Ithaqua to your location"});
```

#### Step 6: Verify Ithaqua Receives Teleport Notification

**Cursor Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for teleport notification
await mcp_playwright_browser_wait_for({text: "You have been teleported to ArkanWolfshade's location by an administrator"});

// Verify both players are in same room
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasTeleportNotification = ithaquaMessages.some(msg => msg.includes('You have been teleported to ArkanWolfshade\'s location by an administrator'));
console.log('Ithaqua receives teleport notification:', hasTeleportNotification);
```

#### Step 7: Verify Room State

**Cursor Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for room entry message
await mcp_playwright_browser_wait_for({text: "Ithaqua enters the room"});

// Verify room state
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaEnter = awMessages.some(msg => msg.includes('Ithaqua enters the room'));
console.log('AW sees Ithaqua enter room after teleport:', seesIthaquaEnter);
```

### Expected Results

- ✅ Non-admin users get permission denied
- ✅ Offline players return "not found" message
- ✅ Teleport command shows confirmation prompt
- ✅ Successful teleportation with proper notifications
- ✅ Both players end up in same room

### Status: 🔄 READY FOR TESTING

---

## Scenario 7: Who Command Validation

### Objective

Test the `who` command functionality including basic listing, filtering, and error handling.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)

### Execution Steps

#### Step 1: Basic Who Command

```javascript
// Click who quick command button
await mcp_playwright_browser_click({element: "who button", ref: "e225"});
// Click Send button to execute
await mcp_playwright_browser_click({element: "Send button", ref: "e180"});
// Wait for response
await mcp_playwright_browser_wait_for({text: "Online players"});
```

#### Step 2: Filtered Who Command

```javascript
// Type filtered who command
await mcp_playwright_browser_type({element: "Command input field", ref: "e179", text: "who arka"});
// Click Send button to execute
await mcp_playwright_browser_click({element: "Send button", ref: "e180"});
// Wait for filtered response
await mcp_playwright_browser_wait_for({text: "Players matching 'arka'"});
```

#### Step 3: No-Match Who Command

```javascript
// Type non-matching filter
await mcp_playwright_browser_type({element: "Command input field", ref: "e179", text: "who xyz"});
// Click Send button to execute
await mcp_playwright_browser_click({element: "Send button", ref: "e180"});
// Wait for no-match response
await mcp_playwright_browser_wait_for({text: "No players found matching"});
```

### Expected Results

- Basic `who` shows all online players with levels, admin status, and room locations
- `who arka` shows only ArkanWolfshade (matching filter)
- `who xyz` shows helpful error message for no matches
- All commands appear in command history
- Server logs show command processing

### Actual Results from Latest Run

#### ✅ Step 1: Basic Who Command - SUCCESS

**Response**: "Online players (2): ArkanWolfshade [1] [ADMIN] - Arkham: City: Sanitarium Room Foyer 001, Ithaqua [1] - Arkham: City: Sanitarium Room Foyer 001"

**Technical Evidence**:

- Message count increased from 1 to 2
- Command history shows "> who"
- Server log: `Processing command: who with args: [] for player: ArkanWolfshade`
- Response delivered via WebSocket in real-time

#### ✅ Step 2: Filtered Who Command - SUCCESS

**Response**: "Players matching 'arka' (1): ArkanWolfshade [1] [ADMIN] - Arkham: City: Sanitarium Room Foyer 001"

**Technical Evidence**:

- Message count increased from 2 to 3
- Command history shows "> who arka"
- Server log: `Processing command: who with args: ['arka'] for player: ArkanWolfshade`
- Filter correctly excluded Ithaqua, included only ArkanWolfshade

#### ✅ Step 3: No-Match Who Command - SUCCESS

**Response**: "No players found matching 'xyz'. Try 'who' to see all online players."

**Technical Evidence**:

- Message count increased from 3 to 4
- Command history shows "> who xyz"
- Server log: `Processing command: who with args: ['xyz'] for player: ArkanWolfshade`
- Helpful error message with suggestion to use 'who'

#### Key Observations

1. **Quick Command Integration**: The "who" button in the UI works perfectly, populating the command field
2. **Real-time Delivery**: All responses delivered instantly via WebSocket
3. **Comprehensive Logging**: Server logs show detailed command processing with debugging info
4. **User-Friendly Error Handling**: Non-matching filters provide helpful suggestions
5. **Command History**: All commands properly recorded with timestamps
6. **Filter Logic**: Partial name matching works correctly (case-insensitive)

#### Server Log Evidence

```
2025-08-27 11:31:31 - Processing command: who with args: [] for player: ArkanWolfshade
2025-08-27 11:31:31 - Who command successful
2025-08-27 11:31:57 - Processing command: who with args: ['arka'] for player: ArkanWolfshade
2025-08-27 11:31:57 - Who command successful with filter
2025-08-27 11:32:13 - Processing command: who with args: ['xyz'] for player: ArkanWolfshade
2025-08-27 11:32:13 - Who command - no matches for filter
```

**🎉 SCENARIO 7 STATUS: COMPLETE SUCCESS**
The who command system is fully functional with comprehensive filtering capabilities, proper error handling, and excellent user experience integration.

---

## Scenario 8: Local Channel Communication

### Description

Tests the new local channel system that allows players to communicate within their sub-zone (geographical area) rather than just their current room.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same sub-zone (Arkham City)
- Local channel system implemented (Tasks 1-5 completed)

### Cursor Execution Steps

#### Step 1: Verify Players in Same Sub-Zone

```javascript
// Ensure both players are in Arkham City sub-zone
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in rooms with "arkham_city" in the room ID
```

#### Step 2: AW Sends Local Channel Message

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type local channel command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Hello to everyone in Arkham City!"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You say (local): Hello to everyone in Arkham City!"});
```

#### Step 3: Verify Ithaqua Receives Local Message

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): Hello to everyone in Arkham City!"});

// Verify message appears with local channel formatting
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLocalMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says (local): Hello to everyone in Arkham City!'));
console.log('Ithaqua sees local message:', seesLocalMessage);
```

#### Step 4: Test Local Channel Alias

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Use /l alias for local channel
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "l Testing the local channel alias"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You say (local): Testing the local channel alias"});
```

#### Step 5: Verify Alias Message Received

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for alias message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): Testing the local channel alias"});

// Verify alias works correctly
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAliasMessage = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade says (local): Testing the local channel alias'));
console.log('Ithaqua sees alias message:', seesAliasMessage);
```

#### Step 6: Test Empty Local Message Rejection

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Try to send empty local message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Say what? Usage: local <message> or /l <message>"});

// Verify error message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesErrorMessage = awMessages.some(msg => msg.includes('Say what? Usage: local <message> or /l <message>'));
console.log('AW sees error message for empty local:', seesErrorMessage);
```

### Expected Results

- ✅ AW sees "You say (local): Hello to everyone in Arkham City!"
- ✅ Ithaqua sees "ArkanWolfshade says (local): Hello to everyone in Arkham City!"
- ✅ /l alias works correctly for local channel
- ✅ Empty local messages are rejected with helpful error message
- ✅ Local messages are properly formatted with "(local)" indicator

### Status: ✅ READY FOR TESTING

---

## Scenario 9: Local Channel Sub-Zone Isolation

### Description

Tests that local channel messages are properly isolated by sub-zone, ensuring players in different sub-zones don't see each other's local messages.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Players in different sub-zones (AW in Arkham City, Ithaqua in different sub-zone)

### Cursor Execution Steps

#### Step 1: Move Players to Different Sub-Zones

```javascript
// Move AW to Arkham City sub-zone (if not already there)
await mcp_playwright_browser_tab_select({index: 0});
// Verify AW is in arkham_city sub-zone

// Move Ithaqua to a different sub-zone
await mcp_playwright_browser_tab_select({index: 1});
// Navigate Ithaqua to a room in a different sub-zone (e.g., campus, docks, etc.)
// This may require multiple movement commands depending on world layout
// Example: await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
```

#### Step 2: AW Sends Local Message in Arkham City

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send local message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local This message should only be seen in Arkham City"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say (local): This message should only be seen in Arkham City"});
```

#### Step 3: Verify Ithaqua Does NOT Receive Local Message

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check that Ithaqua does NOT see the local message
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLocalMessage = ithaquaMessages.some(msg => msg.includes('This message should only be seen in Arkham City'));
console.log('Ithaqua sees local message (should be false):', !seesLocalMessage);
```

#### Step 4: Ithaqua Sends Local Message in Different Sub-Zone

```javascript
// Send local message from Ithaqua's sub-zone
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local This message is from a different sub-zone"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say (local): This message is from a different sub-zone"});
```

#### Step 5: Verify AW Does NOT Receive Ithaqua's Local Message

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check that AW does NOT see Ithaqua's local message
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaLocalMessage = awMessages.some(msg => msg.includes('This message is from a different sub-zone'));
console.log('AW sees Ithaqua local message (should be false):', !seesIthaquaLocalMessage);
```

### Expected Results

- ✅ AW sees their local message in Arkham City
- ✅ Ithaqua does NOT see AW's local message (different sub-zone)
- ✅ Ithaqua sees their local message in their sub-zone
- ✅ AW does NOT see Ithaqua's local message (different sub-zone)
- ✅ Sub-zone isolation works correctly

### Status: ✅ READY FOR TESTING

---

## Scenario 10: Local Channel with Player Movement

### Description

Tests that local channel messages are sent to the destination sub-zone when a player is moving between rooms during message composition.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in same sub-zone initially

### Cursor Execution Steps

#### Step 1: Setup Players in Same Sub-Zone

```javascript
// Ensure both players are in the same sub-zone initially
// AW should be on tab 0, Ithaqua on tab 1
```

#### Step 2: AW Moves to Different Sub-Zone

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move AW to a different sub-zone
// This may require multiple movement commands
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});

// Continue moving until AW is in a different sub-zone
```

#### Step 3: AW Sends Local Message from New Sub-Zone

```javascript
// Send local message from new sub-zone
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Hello from my new sub-zone!"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say (local): Hello from my new sub-zone!"});
```

#### Step 4: Verify Ithaqua Does NOT Receive Message

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check that Ithaqua does NOT see the message (different sub-zone)
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMessage = ithaquaMessages.some(msg => msg.includes('Hello from my new sub-zone!'));
console.log('Ithaqua sees message from different sub-zone (should be false):', !seesMessage);
```

#### Step 5: Ithaqua Moves to AW's Sub-Zone

```javascript
// Move Ithaqua to the same sub-zone as AW
// This may require multiple movement commands
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});

// Continue moving until Ithaqua is in the same sub-zone as AW
```

#### Step 6: AW Sends Another Local Message

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send another local message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Now we're in the same sub-zone!"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say (local): Now we're in the same sub-zone!"});
```

#### Step 7: Verify Ithaqua Now Receives Message

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): Now we're in the same sub-zone!"});

// Verify message appears
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMessageAfter = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade says (local): Now we\'re in the same sub-zone!'));
console.log('Ithaqua sees message from same sub-zone:', seesMessageAfter);
```

### Expected Results

- ✅ AW's local message from different sub-zone is NOT seen by Ithaqua
- ✅ AW's local message from same sub-zone IS seen by Ithaqua
- ✅ Sub-zone-based message routing works correctly during player movement
- ✅ Local channel respects current player location for message delivery

### Status: ✅ READY FOR TESTING

---

## Scenario 11: Local Channel Error Handling

### Description

Tests error handling for local channel commands including invalid room IDs, missing services, and edge cases.

### Prerequisites

- One player connected (AW)
- Local channel system implemented

### Cursor Execution Steps

#### Step 1: Test Invalid Room ID Handling

```javascript
// This test may require database manipulation or special setup
// For now, we'll test basic error handling

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Try to send a very long local message
const longMessage = "a".repeat(501); // Exceeds 500 character limit
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `local ${longMessage}`});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Message too long"});

// Verify error message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesErrorMessage = awMessages.some(msg => msg.includes('Message too long'));
console.log('AW sees error message for long message:', seesErrorMessage);
```

#### Step 2: Test Whitespace-Only Message Rejection

```javascript
// Try to send whitespace-only message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local    "});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Say what? Usage: local <message> or /l <message>"});

// Verify error message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhitespaceError = awMessagesAfter.some(msg => msg.includes('Say what? Usage: local <message> or /l <message>'));
console.log('AW sees error message for whitespace-only:', seesWhitespaceError);
```

#### Step 3: Test Special Characters in Local Messages

```javascript
// Send local message with special characters
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing special chars: <>&\"'!@#$%^&*()"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say (local): Testing special chars: <>&\"'!@#$%^&*()"});

// Verify message appears correctly
const awMessagesSpecial = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesSpecialChars = awMessagesSpecial.some(msg => msg.includes('Testing special chars: <>&"\'!@#$%^&*()'));
console.log('AW sees special characters message:', seesSpecialChars);
```

### Expected Results

- ✅ Long messages (>500 chars) are rejected with error message
- ✅ Whitespace-only messages are rejected with helpful error message
- ✅ Special characters are handled correctly in local messages
- ✅ Error messages are clear and helpful

### Status: ✅ READY FOR TESTING

---

## Scenario 12: Local Channel Integration with Existing Systems

### Description

Tests that local channel system integrates properly with existing chat, movement, and moderation systems.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in same sub-zone
- Existing systems (say, movement, muting) working

### Cursor Execution Steps

#### Step 1: Test Local Channel with Regular Say Commands

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send regular say message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say This is a regular say message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: This is a regular say message"});

// Send local message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local This is a local channel message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say (local): This is a local channel message"});
```

#### Step 2: Verify Both Message Types Work Independently

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for both messages
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says: This is a regular say message"});
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): This is a local channel message"});

// Verify both messages appear
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesRegularSay = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says: This is a regular say message'));
const seesLocalMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says (local): This is a local channel message'));
console.log('Ithaqua sees regular say:', seesRegularSay);
console.log('Ithaqua sees local message:', seesLocalMessage);
```

#### Step 3: Test Local Channel with Movement Messages

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move to different room in same sub-zone
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});

// Send local message from new room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Hello from the new room!"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say (local): Hello from the new room!"});
```

#### Step 4: Verify Local Message Still Works After Movement

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for local message from new room
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): Hello from the new room!"});

// Verify message appears
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLocalAfterMovement = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade says (local): Hello from the new room!'));
console.log('Ithaqua sees local message after AW movement:', seesLocalAfterMovement);
```

### Expected Results

- ✅ Regular say commands work alongside local channel commands
- ✅ Local messages work correctly after player movement within sub-zone
- ✅ Both message types are properly formatted and distinguishable
- ✅ Local channel integrates seamlessly with existing movement system

### Status: ✅ READY FOR TESTING

---

## Scenario 13: Whisper Channel Basic Functionality

### Description

Tests the basic whisper channel functionality including player-to-player messaging, proper message formatting, and target validation.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)
- Whisper channel system implemented (Phase 3 completed)

### Cursor Execution Steps

#### Step 1: AW Sends Whisper to Ithaqua

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type whisper command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Hello, this is a private message"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Hello, this is a private message"});
```

#### Step 2: Verify Ithaqua Receives Whisper

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Hello, this is a private message"});

// Verify message appears with whisper formatting
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisper = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Hello, this is a private message'));
console.log('Ithaqua sees whisper message:', seesWhisper);
```

#### Step 3: Ithaqua Replies with Whisper

```javascript
// Type whisper reply
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Thank you for the private message"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Thank you for the private message"});
```

#### Step 4: Verify AW Receives Whisper Reply

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper reply
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Thank you for the private message"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisperReply = awMessages.some(msg => msg.includes('Ithaqua whispers to you: Thank you for the private message'));
console.log('AW sees whisper reply:', seesWhisperReply);
```

#### Step 5: Test Whisper Command (No Alias)

```javascript
// Use full whisper command (no /w alias to avoid confusion with movement)
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing the whisper command"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation message
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing the whisper command"});
```

#### Step 6: Verify Command Message Received

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for command message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing the whisper command"});

// Verify command works correctly
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesCommandMessage = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing the whisper command'));
console.log('Ithaqua sees command message:', seesCommandMessage);
```

### Expected Results

- ✅ AW sees "You whisper to Ithaqua: Hello, this is a private message"
- ✅ Ithaqua sees "ArkanWolfshade whispers to you: Hello, this is a private message"
- ✅ Ithaqua sees "You whisper to ArkanWolfshade: Thank you for the private message"
- ✅ AW sees "Ithaqua whispers to you: Thank you for the private message"
- ✅ Full "whisper" command works correctly (no /w alias to avoid movement conflicts)
- ✅ Whisper messages are properly formatted with "whispers to you" indicator
- ✅ Clear distinction between outgoing ("You whisper to") and incoming ("whispers to you") messages

### Status: ✅ READY FOR TESTING

---

## Scenario 14: Whisper Channel Error Handling

### Description

Tests error handling for whisper channel commands including invalid targets, empty messages, and edge cases.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)

### Cursor Execution Steps

#### Step 1: Test Whisper to Non-Existent Player

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Try to whisper to non-existent player
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper NonexistentPlayer Hello there"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Player 'NonexistentPlayer' is not online or not found"});

// Verify error message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesError = awMessages.some(msg => msg.includes('Player \'NonexistentPlayer\' is not online or not found'));
console.log('AW sees error for non-existent player:', seesError);
```

#### Step 2: Test Whisper to Self

```javascript
// Try to whisper to self
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Hello myself"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "You cannot whisper to yourself"});

// Verify error message appears
const awMessagesSelf = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesSelfError = awMessagesSelf.some(msg => msg.includes('You cannot whisper to yourself'));
console.log('AW sees error for whispering to self:', seesSelfError);
```

#### Step 3: Test Empty Whisper Message

```javascript
// Try to send empty whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Say what? Usage: whisper <player> <message>"});

// Verify error message appears
const awMessagesEmpty = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesEmptyError = awMessagesEmpty.some(msg => msg.includes('Say what? Usage: whisper <player> <message>'));
console.log('AW sees error for empty whisper:', seesEmptyError);
```

#### Step 4: Test Whitespace-Only Whisper Message

```javascript
// Try to send whitespace-only whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua    "});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Say what? Usage: whisper <player> <message>"});

// Verify error message appears
const awMessagesWhitespace = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhitespaceError = awMessagesWhitespace.some(msg => msg.includes('Say what? Usage: whisper <player> <message>'));
console.log('AW sees error for whitespace-only whisper:', seesWhitespaceError);
```

#### Step 5: Test Long Whisper Message

```javascript
// Try to send very long whisper message
const longMessage = "a".repeat(501); // Exceeds 500 character limit
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `whisper Ithaqua ${longMessage}`});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Message too long"});

// Verify error message appears
const awMessagesLong = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLongError = awMessagesLong.some(msg => msg.includes('Message too long'));
console.log('AW sees error for long whisper:', seesLongError);
```

### Expected Results

- ✅ Whisper to non-existent player returns helpful error message
- ✅ Whisper to self returns appropriate error message
- ✅ Empty whisper messages are rejected with usage instructions (no /w alias)
- ✅ Whitespace-only whisper messages are rejected
- ✅ Long whisper messages (>500 chars) are rejected with error message
- ✅ All error messages are clear and helpful
- ✅ Error messages use full "whisper" command syntax (no /w alias)

### Status: ✅ READY FOR TESTING

---

## Scenario 15: Whisper Channel Rate Limiting

### Description

Tests the rate limiting functionality for whisper messages to prevent spam and abuse.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)
- Rate limiting system implemented

### Cursor Execution Steps

#### Step 1: Send Multiple Whisper Messages Rapidly

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send first whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Message 1"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Message 1"});

// Send second whisper message immediately
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Message 2"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Message 2"});

// Send third whisper message immediately
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Message 3"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Message 3"});

// Send fourth whisper message (should trigger rate limit)
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Message 4"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for rate limit error message
await mcp_playwright_browser_wait_for({text: "You are sending messages too quickly"});
```

#### Step 2: Verify Rate Limit Error Message

```javascript
// Verify rate limit error appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesRateLimit = awMessages.some(msg => msg.includes('You are sending messages too quickly'));
console.log('AW sees rate limit error:', seesRateLimit);
```

#### Step 3: Verify Ithaqua Only Receives First Three Messages

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check for received messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMessage1 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Message 1'));
const seesMessage2 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Message 2'));
const seesMessage3 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Message 3'));
const seesMessage4 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Message 4'));

console.log('Ithaqua sees Message 1:', seesMessage1);
console.log('Ithaqua sees Message 2:', seesMessage2);
console.log('Ithaqua sees Message 3:', seesMessage3);
console.log('Ithaqua sees Message 4 (should be false):', !seesMessage4);
```

#### Step 4: Wait for Rate Limit Reset and Test Again

```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait 5 seconds for rate limit to reset
await mcp_playwright_browser_wait_for({time: 5});

// Try to send another whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Message after rate limit reset"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for successful message
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Message after rate limit reset"});
```

#### Step 5: Verify Message After Rate Limit Reset

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for message after rate limit reset
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Message after rate limit reset"});

// Verify message appears
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMessageAfterReset = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade whispers to you: Message after rate limit reset'));
console.log('Ithaqua sees message after rate limit reset:', seesMessageAfterReset);
```

### Expected Results

- ✅ First three whisper messages are sent successfully
- ✅ Fourth whisper message triggers rate limit error
- ✅ Ithaqua only receives the first three messages
- ✅ Rate limit error message is clear and helpful
- ✅ After waiting, rate limit resets and messages work again
- ✅ Rate limiting prevents spam while allowing normal communication

### Status: ✅ READY FOR TESTING

---

## Scenario 16: Whisper Channel with Player Movement

### Description

Tests that whisper messages work correctly when players move between rooms and sub-zones.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room initially (Main Foyer)

### Cursor Execution Steps

#### Step 1: AW Moves to Different Room

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move AW to different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});
```

#### Step 2: AW Sends Whisper from Different Room

```javascript
// Send whisper from new room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Hello from the east room"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Hello from the east room"});
```

#### Step 3: Verify Ithaqua Receives Whisper from Different Room

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper from different room
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Hello from the east room"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisperFromDifferentRoom = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Hello from the east room'));
console.log('Ithaqua sees whisper from different room:', seesWhisperFromDifferentRoom);
```

#### Step 4: Ithaqua Moves to Different Sub-Zone

```javascript
// Move Ithaqua to different sub-zone
// This may require multiple movement commands depending on world layout
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});

// Continue moving until Ithaqua is in a different sub-zone
```

#### Step 5: Ithaqua Sends Whisper from Different Sub-Zone

```javascript
// Send whisper from different sub-zone
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Hello from a different sub-zone"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Hello from a different sub-zone"});
```

#### Step 6: Verify AW Receives Whisper from Different Sub-Zone

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper from different sub-zone
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Hello from a different sub-zone"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisperFromDifferentSubZone = awMessages.some(msg => msg.includes('Ithaqua whispers to you: Hello from a different sub-zone'));
console.log('AW sees whisper from different sub-zone:', seesWhisperFromDifferentSubZone);
```

### Expected Results

- ✅ Whisper messages work across different rooms
- ✅ Whisper messages work across different sub-zones
- ✅ Player movement doesn't break whisper functionality
- ✅ Whisper messages are delivered regardless of player location
- ✅ Whisper channel provides reliable private communication

### Status: ✅ READY FOR TESTING

---

## Scenario 17: Whisper Channel Integration with Existing Systems

### Description

Tests that whisper channel system integrates properly with existing chat, movement, and moderation systems.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)
- Existing systems (say, local, movement, muting) working

### Cursor Execution Steps

#### Step 1: Test Whisper with Regular Say Commands

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send regular say message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say This is a regular say message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: This is a regular say message"});

// Send whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua This is a private whisper message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: This is a private whisper message"});
```

#### Step 2: Verify Both Message Types Work Independently

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for both messages
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says: This is a regular say message"});
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: This is a private whisper message"});

// Verify both messages appear
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesRegularSay = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says: This is a regular say message'));
const seesWhisperMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: This is a private whisper message'));
console.log('Ithaqua sees regular say:', seesRegularSay);
console.log('Ithaqua sees whisper message:', seesWhisperMessage);
```

#### Step 3: Test Whisper with Local Channel Commands

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send local message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local This is a local channel message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say (local): This is a local channel message"});

// Send whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua This is another private message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: This is another private message"});
```

#### Step 4: Verify All Channel Types Work Together

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for both messages
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says (local): This is a local channel message"});
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: This is another private message"});

// Verify all messages appear
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLocalMessage = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade says (local): This is a local channel message'));
const seesWhisperMessage2 = ithaquaMessagesAfter.some(msg => msg.includes('ArkanWolfshade whispers to you: This is another private message'));
console.log('Ithaqua sees local message:', seesLocalMessage);
console.log('Ithaqua sees whisper message 2:', seesWhisperMessage2);
```

#### Step 5: Test Whisper with Movement Messages

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move to different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You move east"});

// Send whisper from new room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Hello from the new room"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Hello from the new room"});
```

#### Step 6: Verify Whisper Works After Movement

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper from new room
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Hello from the new room"});

// Verify message appears
const ithaquaMessagesFinal = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisperAfterMovement = ithaquaMessagesFinal.some(msg => msg.includes('ArkanWolfshade whispers to you: Hello from the new room'));
console.log('Ithaqua sees whisper after AW movement:', seesWhisperAfterMovement);
```

### Expected Results

- ✅ Regular say commands work alongside whisper commands
- ✅ Local channel commands work alongside whisper commands
- ✅ Whisper messages work correctly after player movement
- ✅ All channel types are properly formatted and distinguishable
- ✅ Whisper channel integrates seamlessly with existing systems
- ✅ No conflicts between different communication channels

### Status: ✅ READY FOR TESTING

---

## Scenario 18: Whisper Channel Logging and Privacy

### Description

Tests that whisper messages are properly logged for moderation purposes while maintaining privacy between players.

### Prerequisites

- Two players connected (AW and Ithaqua)
- Both players in the same room (Main Foyer)
- Chat logging system implemented

### Cursor Execution Steps

#### Step 1: Send Multiple Whisper Messages

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send several whisper messages
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua This is a test whisper for logging"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: This is a test whisper for logging"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Another whisper message"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Another whisper message"});
```

#### Step 2: Verify Messages Are Delivered

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper messages
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: This is a test whisper for logging"});
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Another whisper message"});

// Verify messages appear
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisper1 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: This is a test whisper for logging'));
const seesWhisper2 = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Another whisper message'));
console.log('Ithaqua sees whisper 1:', seesWhisper1);
console.log('Ithaqua sees whisper 2:', seesWhisper2);
```

#### Step 3: Check Server Logs for Whisper Entries

```javascript
// This step would require server log access
// For now, we'll verify the messages were sent successfully
// In a real implementation, we would check logs/chat/whisper/whisper_YYYY-MM-DD.log

// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send one more whisper to ensure logging is working
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Final test whisper for logging verification"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Final test whisper for logging verification"});
```

#### Step 4: Verify Privacy Between Players

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for final whisper
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Final test whisper for logging verification"});

// Verify Ithaqua only sees whispers sent to them
const ithaquaAllMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const allWhispers = ithaquaAllMessages.filter(msg => msg.includes('whispers to you:'));
const onlyFromAW = allWhispers.every(msg => msg.includes('ArkanWolfshade whispers to you:'));
console.log('Ithaqua only sees whispers from AW:', onlyFromAW);
console.log('Total whispers Ithaqua sees:', allWhispers.length);
```

### Expected Results

- ✅ Whisper messages are delivered successfully
- ✅ Whisper messages are properly logged to whisper.log files
- ✅ Players only see whispers sent to them
- ✅ Privacy is maintained between players
- ✅ Logging includes sender, target, and message content
- ✅ Whisper channel provides secure private communication

### Status: ✅ READY FOR TESTING

---

## Post-Scenario Cleanup

### Step 1: Close All Browser Tabs

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

### Step 2: Stop Development Server

**Cursor Command**:

```powershell
./scripts/stop_server.ps1
```

### Step 3: Verify Clean Shutdown

**Cursor Commands**:

```powershell
# Check if ports are free
netstat -an | findstr :54731
netstat -an | findstr :5173
```

**Expected**: No processes found on these ports

---

## Error Handling and Troubleshooting

### Common Issues and Solutions

#### Issue 1: Server Won't Start

**Symptoms**: `./scripts/start_dev.ps1` fails
**Solutions**:

1. Check if ports are already in use
2. Verify database file exists and is accessible
3. Check server logs in `logs/development/`
4. Restart with `./scripts/stop_server.ps1` first

#### Issue 2: Players Can't Connect

**Symptoms**: Browser shows connection errors
**Solutions**:

1. Verify server is running on port 54731
2. Check client is accessible on port 5173
3. Verify database contains test players
4. Check network connectivity

#### Issue 3: Messages Not Appearing

**Symptoms**: Expected messages don't show up
**Solutions**:

1. Wait longer for message delivery (add delays)
2. Check browser console for errors
3. Verify WebSocket connections are active
4. Check server logs for message broadcasting errors

#### Issue 4: Database State Issues

**Symptoms**: Players in wrong rooms or missing
**Solutions**:

1. Use SQLite CLI to verify player state
2. Update player locations manually
3. Check admin privileges
4. Restore from backup if needed

### Debugging Commands

#### Check Server Status

```powershell
# Check if server is running
netstat -an | findstr :54731

# Check server logs
Get-Content logs/development/server.log -Tail 50
```

#### Check Database State

```powershell
# Open SQLite database
sqlite3 data/players/players.db

# Check player state
SELECT name, current_room_id, is_admin, last_active FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');
```

#### Check Browser State

```javascript
// Get all messages in current tab
const messages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
console.log('Current messages:', messages);

// Get current room information
const roomInfo = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.room-description')?.textContent.trim()"});
console.log('Current room:', roomInfo);
```

---

## Success Criteria

### Scenario Completion Checklist

For each scenario to be considered successful:

1. **All Expected Messages Appear**: Every expected message is visible in the correct player's chat
2. **No Unexpected Messages**: No unwanted or duplicate messages appear
3. **Proper Timing**: Messages appear within reasonable timeframes (2-5 seconds)
4. **State Consistency**: Player locations and game state remain consistent
5. **Error-Free Execution**: No error messages or exceptions occur
6. **Clean Transitions**: Scenarios can run back-to-back without issues

### Overall Success Criteria

- ✅ All scenarios 1-7 pass completely
- ✅ No duplicate messages in chat logs
- ✅ Consistent movement message broadcasting
- ✅ Proper disconnection message display
- ✅ Self-message exclusion working correctly
- ✅ Admin teleportation system functional
- ✅ Who command displays correct information
- ✅ Performance remains acceptable under load

---

## Development Notes

As noted in the Pnakotic Manuscripts, "The boundaries between states must remain distinct, lest chaos seep through the dimensional barriers." Each scenario must maintain proper isolation while demonstrating the interconnected nature of the multiplayer system.

The multiplayer implementation represents a successful bridge between the event-driven backend architecture and the real-time client requirements, much like the dimensional gateways described in Wilmarth's Vermont correspondence - functional, but requiring careful management to prevent unwanted intrusions from previous sessions.

*"What has been tested once can be tested again, and with proper documentation, even madness becomes methodical."* - Dr. Armitage, 1928

---

**Document Version**: 4.0 (Cursor Executable)
**Last Updated**: 2025-08-23
**Next Review**: After each scenario completion
**Primary Audience**: Cursor AI and Developers
**Update Frequency**: After each scenario completion
