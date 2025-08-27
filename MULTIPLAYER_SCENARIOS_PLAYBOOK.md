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
SELECT display_name, current_room, is_admin FROM players WHERE display_name IN ('ArkanWolfshade', 'Ithaqua');

-- Update players to starting room if needed
UPDATE players SET current_room = 'earth_arkham_city_sanitarium_room_foyer_001' WHERE display_name IN ('ArkanWolfshade', 'Ithaqua');

-- Verify ArkanWolfshade has admin privileges
UPDATE players SET is_admin = 1 WHERE display_name = 'ArkanWolfshade';

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
curl http://localhost:54731/health
# Test client accessibility
curl http://localhost:5173
```

**Expected**: Both endpoints return successful responses

---

## Scenario 1: Basic Connection/Disconnection Flow

### Description

Tests basic multiplayer connection and disconnection messaging between two players.


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

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
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

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
```

#### Step 4: Verify AW Sees Ithaqua Entered Message

**Cursor Commands**:

```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for message to appear
await mcp_playwright_browser_wait_for({text: "Ithaqua has entered the game"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasIthaquaEntered = awMessages.some(msg => msg.includes('Ithaqua has entered the game'));
console.log('AW sees Ithaqua entered:', hasIthaquaEntered);
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
```

#### Step 6: Ithaqua Leaves the Game

**Cursor Commands**:

```javascript
// Close Ithaqua's tab
await mcp_playwright_browser_tab_close({index: 1});

// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});
```

#### Step 7: Verify AW Sees Ithaqua Left Message

**Cursor Commands**:

```javascript
// Wait for disconnect message
await mcp_playwright_browser_wait_for({text: "Ithaqua has left the game"});

// Verify message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasIthaquaLeft = awMessagesAfter.some(msg => msg.includes('Ithaqua has left the game'));
console.log('AW sees Ithaqua left:', hasIthaquaLeft);
```

### Expected Results

- ✅ AW sees "Ithaqua has entered the game."
- ✅ Ithaqua sees NO enters/leaves messages
- ✅ AW sees "Ithaqua has left the game."

### Status: ✅ PASSED

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
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
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
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
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
SELECT display_name, current_room, is_admin, last_seen FROM players WHERE display_name IN ('ArkanWolfshade', 'Ithaqua');
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
