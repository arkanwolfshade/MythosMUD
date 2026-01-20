# MythosMUD Multiplayer Test Rules - Master Documentation

## 📊 E2E Testing Overview

MythosMUD uses a **hybrid E2E testing approach**:

### Automated Playwright CLI Tests (10 Scenarios)

**114 automated tests** covering error handling, accessibility, and integration

**Location**: `client/tests/e2e/runtime/`

**Execution**: `make test-client-runtime` or `npm run test:e2e:runtime`

**Runtime**: <5 minutes for all automated tests

**CI/CD**: Fully integrated with GitHub Actions

- **See**: [E2E Testing Guide](../docs/E2E_TESTING_GUIDE.md)

### Playwright MCP Scenarios (11 Scenarios)

**11 multi-player scenarios** requiring AI Agent coordination

**Location**: `e2e-tests/scenarios/`

**Execution**: Via AI Agent with Playwright MCP (this document)

**Runtime**: ~5-8 minutes per scenario (~60-90 minutes total)

**Purpose**: Real-time multi-player coordination testing

### This document covers ONLY the 11 MCP scenarios that require multi-player coordination

---

## 🤖 CRITICAL AI EXECUTOR REQUIREMENTS 🤖

### 🚨 STOP! READ THIS FIRST! 🚨

### MANDATORY EXECUTION ORDER - NO EXCEPTIONS

1. **FIRST**: Complete ALL database verification steps (Step 2)
2. **SECOND**: Start the server (Step 3)
3. **THIRD**: Execute scenarios in order

### ⚠️ VIOLATING THIS ORDER = COMPLETE FAILURE

### 🚨 INFINITE LOOP PREVENTION - CRITICAL! 🚨

### MANDATORY EXECUTION GUARDS

1. **MAXIMUM 3 ATTEMPTS** per step - then proceed with documented failure
2. **NEVER retry** `browser_evaluate` calls - empty results are often valid
3. **ALWAYS proceed** to next step after timeout or empty results
4. **ALWAYS close** browser tabs between scenarios
5. **NEVER repeat** the same step multiple times

### ⚠️ VIOLATING THESE GUARDS = INFINITE LOOPS

### EXECUTION GUARD EXAMPLES

```javascript
// ✅ CORRECT: Handle empty results gracefully
const messages = await mcp_playwright_browser_evaluate({...});
if (messages.length === 0) {
    console.log('✅ No messages found - verification complete');
    // PROCEED TO NEXT STEP - do not retry
} else {
    console.log('✅ Messages found:', messages);
    // Continue verification
}

// ❌ WRONG: This creates infinite loops
const messages = await mcp_playwright_browser_evaluate({...});
if (messages.length === 0) {
    // DON'T retry - empty is often valid!
    const messages = await mcp_playwright_browser_evaluate({...}); // INFINITE LOOP!
}
```

### MANDATORY LLM REQUIREMENT

**MUST USE GPT-4 OR NEWER MODEL**: This playbook requires GPT-4 or newer model with higher level reasoning
  and instruction adherence

**DO NOT USE**: GPT-3.5, Claude, or other LLMs for playbook execution

**REASON**: Complex multi-step scenarios with strict execution requirements
  need advanced reasoning capabilities

**VERIFICATION**: Confirm you are using GPT-4 or greater before proceeding

  with any scenario

## 🚨 CRITICAL INSTRUCTION FOR AI EXECUTORS 🚨

### MANDATORY EXECUTION PROTOCOL - NO EXCEPTIONS

### BEFORE YOU DO ANYTHING ELSE

1. **MANDATORY DATABASE VERIFICATION**: You MUST verify the starting room

   configuration BEFORE starting the server

2. **MANDATORY PREREQUISITE CHECKS**: You MUST complete ALL pre-execution

   steps before ANY scenario

3. **ZERO TOLERANCE FOR SKIPPING**: Execute EVERY step in EVERY scenario

   EXACTLY as written

4. **NO INTERPRETATION ALLOWED**: Do NOT skip, modify, or interpret any steps

5. **NO ASSUMPTIONS ALLOWED**: Do NOT make assumptions about how systems

   should work

6. **EXECUTION ONLY**: Your job is to execute, not to interpret or improve

7. **EXECUTE EVEN IF WRONG**: If you think a step is wrong, execute it anyway

   and document the result

### VIOLATION CONSEQUENCES

Skipping database verification = COMPLETE FAILURE

- Starting server without prerequisites = COMPLETE FAILURE
- Modifying any command = COMPLETE FAILURE
- Making assumptions = COMPLETE FAILURE

## Test Configuration

### Test Players

**ArkanWolfshade** (AW) - password: Cthulhu1

**Character Name**: ArkanWolfshade (must match player name)

**Ithaqua** - password: Cthulhu1

**Character Name**: Ithaqua (must match player name)

**⚠️ MULTI-CHARACTER REQUIREMENT**: After logging in, players must select a character with the same name as the player
account before proceeding to the MOTD screen. The character selection screen will appear automatically if the player has
multiple characters.

### Server Configuration

**Server Port**: 54731 (from `server/server_config.yaml`)

**Client Port**: 5173 (from `client/vite.config.ts`)

**Starting Room**: `earth_arkhamcity_sanitarium_room_foyer_001` (Main Foyer)

**Database**: PostgreSQL `mythos_e2e` database (connection:

  `postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e`)

**Log Directory**: `logs/e2e_test/`

### Command Syntax

**Movement**: `go <direction>` or direction shortcuts (e.g., `go east`,
  `east`, `e`, `go west`, `west`, `w`)

**Say**: `say <message>` or `/say <message>` or just `<message>` (defaults to say channel)

**Local**: `local <message>` or `/l <message>`

**Whisper**: `whisper <player> <message>`

**Who**: `who` or `who <filter>`

- **Teleport**: `teleport <player>` (admin only)
- **Other**: `look`, `inventory`, `help`, `mute`, `unmute`, `dance`, etc.

## Configurable Timeout Settings

### Standard Timeouts (Default)

**Login form wait**: 15 seconds

**Character selection wait**: 15 seconds (after login, if multiple characters exist)

**MOTD screen wait**: 15 seconds

**Game interface load**: 15 seconds

**Message delivery wait**: 10 seconds

- **Tab switching**: 2 seconds
- **Page load**: 5 seconds

<!-- ### Low-Performance Machine Timeouts

**Login form wait**: 30 seconds

**MOTD screen wait**: 30 seconds

**Game interface load**: 30 seconds
- **Message delivery wait**: 30 seconds
- **Tab switching**: 5 seconds
- **Page load**: 10 seconds

### High-Performance Machine Timeouts

**Login form wait**: 5 seconds

**MOTD screen wait**: 5 seconds

**Game interface load**: 5 seconds
- **Message delivery wait**: 3 seconds
- **Tab switching**: 1 second
- **Page load**: 2 seconds -->

## CRITICAL SERVER MANAGEMENT RULES

### ONE SERVER ONLY RULE

### THERE CAN ONLY BE ONE SERVER RUNNING AT ANY TIME

### MANDATORY SERVER STARTUP PROCEDURE

1. **STOP FIRST**: Before starting a server, ALWAYS run `./scripts/stop_server.ps1`

2. **VERIFY PORTS**: After stopping, verify ports are free with `netstat -an |

   findstr :54731` and `netstat -an | findstr :5173`

3. **NO BACKGROUND**: NEVER use `is_background: true` for server startup commands
4. **SEE OUTPUT**: ALWAYS use `is_background: false` for server startup so you can see what's happening
5. **ONE START ONLY**: Run `./scripts/start_local.ps1` with `is_background: false` exactly ONCE
6. **IF IT SAYS "Press any key to exit"**: The server is running - DO NOT start another

### PRE-COMMAND CHECKLIST

Before running ANY server command, ask yourself:

- Did I already start a server in this session? (YES = STOP, don't start another)

- Am I about to use `is_background: true`? (YES = STOP, use false instead)

- Did I run `stop_server.ps1` first? (NO = STOP, run it first)

- Am I about to run `start_local.ps1` when I already see "Press any key to

  exit"? (YES = STOP, server is already running)

## MANDATORY PRE-EXECUTION CHECKLIST

### YOU MUST COMPLETE EVERY ITEM BEFORE STARTING ANY SCENARIO

### DATABASE VERIFICATION (MANDATORY)

[ ] I have verified both test players exist in the database

- [ ] I have confirmed both players are in room `earth_arkhamcity_sanitarium_room_foyer_001`
- [ ] I have confirmed ArkanWolfshade has admin privileges (is_admin = 1)
- [ ] I have verified both players have active characters with names matching their player accounts
- [ ] I have run the SQL commands to update player locations if needed

### INSTRUCTION COMPLIANCE (MANDATORY)

[ ] I have read the MANDATORY EXECUTION PROTOCOL above

- [ ] I understand that skipping database verification = COMPLETE FAILURE
- [ ] I will execute every step exactly as written
- [ ] I will not skip, modify, or interpret any steps
- [ ] I will not make assumptions about system behavior
- [ ] I will document actual results, not expected results

### EXECUTION AFFIRMATION (MANDATORY)

[ ] I affirm that I will follow the database verification steps BEFORE starting the server

- [ ] I affirm that I will NOT start any scenario without completing ALL prerequisites
- [ ] I understand that any deviation from these instructions constitutes complete failure

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

### Step 2: MANDATORY Database State Verification

### ⚠️ CRITICAL: THIS STEP IS MANDATORY AND CANNOT BE SKIPPED

**MANDATORY PowerShell Commands to Run (EXECUTE ALL)**:

```powershell
# MANDATORY: Check if players exist and their current state

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# MANDATORY: Update players to starting room (ALWAYS run this)

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "UPDATE players SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001' WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# MANDATORY: Verify ArkanWolfshade has admin privileges (ALWAYS run this)

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "UPDATE players SET is_admin = 1 WHERE name = 'ArkanWolfshade';"

# MANDATORY: Verify the updates worked

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# MANDATORY: Verify characters exist with matching names

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "SELECT u.username, p.name as character_name, p.is_deleted FROM users u JOIN players p ON u.id = p.user_id WHERE u.username IN ('ArkanWolfshade', 'Ithaqua') AND p.name = u.username AND p.is_deleted = false;"
```

**MANDATORY VERIFICATION**: Both players must exist, be in Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`),
and AW must have admin privileges (is_admin = 1)

**MANDATORY CHARACTER VERIFICATION**: Both users must have active characters with names matching their usernames:

```powershell
# MANDATORY: Verify characters exist with matching names

$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "SELECT u.username, p.name as character_name, p.is_deleted FROM users u JOIN players p ON u.id = p.user_id WHERE u.username IN ('ArkanWolfshade', 'Ithaqua') AND p.name = u.username AND p.is_deleted = false;"
```

**MANDATORY VERIFICATION**: Both users must have active characters with names matching their usernames (ArkanWolfshade
character for ArkanWolfshade user, Ithaqua character for Ithaqua user)

### ⚠️ FAILURE TO COMPLETE THIS STEP = COMPLETE TEST FAILURE

### Step 3: Start Development Environment (ONLY AFTER DATABASE VERIFICATION)

### ⚠️ CRITICAL: DO NOT START SERVER UNTIL DATABASE VERIFICATION IS COMPLETE

**Cursor Command**: Start the development server

```powershell
./scripts/start_local.ps1
```

**Wait**: 180 seconds (3 minutes) for server to fully start on low-performance machines

**⚠️ REMINDER**: If you started the server without completing database verification, STOP IMMEDIATELY and restart from
Step 2

### Step 4: Verify Server Accessibility

**Cursor Command**: Test server connectivity with retries for low-performance machines

```powershell
# Test server health with retries

$maxRetries = 5
$retryCount = 0
do {
    try {
        $healthResponse = Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing -TimeoutSec 30
        if ($healthResponse.StatusCode -eq 200) {
            $healthData = $healthResponse.Content | ConvertFrom-Json
            Write-Host "Server Status: $($healthData.status)"
            Write-Host "Uptime: $([math]::Round($healthData.uptime_seconds, 2)) seconds"
            break
        }
    } catch {
        Write-Host "Server health check attempt $($retryCount + 1) failed. Retrying in 10 seconds..."
        Start-Sleep -Seconds 10
    }
    $retryCount++
} while ($retryCount -lt $maxRetries)

if ($retryCount -eq $maxRetries) {
    Write-Host "Server health check failed after $maxRetries attempts"
}

# Test client accessibility with retries

$retryCount = 0
do {
    try {
        $clientResponse = Invoke-WebRequest -Uri "http://localhost:5173" -UseBasicParsing -TimeoutSec 30
        Write-Host "Client Status: $($clientResponse.StatusCode)"
        break
    } catch {
        Write-Host "Client accessibility check attempt $($retryCount + 1) failed. Retrying in 10 seconds..."
        Start-Sleep -Seconds 10
    }
    $retryCount++
} while ($retryCount -lt $maxRetries)
```

**Expected**: Both endpoints return successful responses after retries

## Login Flow with Character Selection

### ⚠️ CRITICAL: ALL SCENARIOS MUST FOLLOW THIS LOGIN FLOW

### Standard Login Flow

1. **Navigate to Client**: Open browser and navigate to `http://localhost:5173`

2. **Wait for Login Form**: Wait for username/password fields to appear

3. **Enter Credentials**: Type username and password, click login button

4. **Wait for Login Processing**: Allow time for authentication (15 seconds)

5. **Character Selection (if applicable)**:

   - If character selection screen appears (text: "Select Your Character"), select the character with the same name as

     the player account

   - Click the "Select Character" button for the matching character

   - Wait for character selection processing (5 seconds)

6. **Wait for MOTD Screen**: Wait for "Continue" button to appear (15 seconds)
7. **Click Continue**: Click the Continue button to enter the game
8. **Wait for Game Interface**: Wait for "Chat" text to appear (15 seconds)

### Character Selection Details

**When it appears**: Character selection screen appears automatically if the player has multiple active characters

**What to select**: Always select the character with the same name as the player account (ArkanWolfshade player →
  ArkanWolfshade character, Ithaqua player → Ithaqua character)

**How to identify**: Use `browser_snapshot()` to find the correct "Select Character" button reference

**Timeout**: Wait up to 15 seconds for character selection screen to appear after login

### Example Character Selection Code

```javascript
// After login, check for character selection screen
await mcp_playwright_browser_wait_for({time: 15});

// Check if character selection screen appears
const snapshot = await mcp_playwright_browser_snapshot();
if (snapshot.includes("Select Your Character") || snapshot.includes("character-selection")) {
  // Wait for character selection screen to fully load
  await mcp_playwright_browser_wait_for({text: "Select Your Character", time: 15});

  // Find and click the "Select Character" button for the character matching the player name
  // Use browser_snapshot() to get the correct element reference
  // Example: await mcp_playwright_browser_click({element: "Select Character button for ArkanWolfshade", ref: "eXX"});

  // Wait for character selection processing
  await mcp_playwright_browser_wait_for({time: 5});
}

// Proceed to MOTD screen
await mcp_playwright_browser_wait_for({text: "Continue", time: 15});
await mcp_playwright_browser_click({element: "Continue button", ref: "e59"});
```

## NO INTERPRETATION RULE

If a command says "say Hello" - type exactly "say Hello"

- If a command says "mute Ithaqua" - type exactly "mute Ithaqua"
- If a step seems to test something obvious - execute it anyway
- If you think a step is wrong - execute it anyway and document the result
- Your job is to execute, not to interpret or improve

## STOP AND ASK RULE

If you find yourself:

- Thinking "this step seems unnecessary"
- Wanting to "help" by changing a command
- Making assumptions about what should happen
- Skipping steps because they seem obvious

STOP. Ask the user: "Should I continue with the exact steps as written, or do you want me to modify this approach?"

## RESULT DOCUMENTATION REQUIREMENTS

After each step, document:

- What command was executed (exactly)
- What response was received (exactly)
- Whether it matched the expected result (yes/no)
- If no match, what the actual result was

## Performance Optimization Notes

**Extended Timeouts**: All `wait_for` operations use configurable timeouts based on machine performance

**Buffer Time**: Additional 5-10 second waits between critical operations

**Retry Logic**: Commands may be repeated if they fail due to timing

**Resource Monitoring**: Watch for memory/CPU usage during extended operations

## Security and Environment

**Security-First Mindset**: Before starting the server, ensure all security configurations are properly set, especially
COPPA compliance settings for minor users

**Database Configuration**: Verify PostgreSQL database connection is properly configured via DATABASE_URL environment
  variable

**Environment Variables**: Ensure all secrets are properly configured via environment variables, never hardcoded

## VIOLATION CONSEQUENCES

Violating these rules will cause:

- Multiple server instances running simultaneously
- Port conflicts and connection failures
- Unpredictable behavior in multiplayer scenarios
- Complete failure of the testing process

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Next Review**: After each scenario completion
**Primary Audience**: AI Executors and Developers
**Update Frequency**: As needed for rule changes
