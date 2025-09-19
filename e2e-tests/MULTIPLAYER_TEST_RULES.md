# MythosMUD Multiplayer Test Rules - Master Documentation

## 🤖 CRITICAL AI EXECUTOR REQUIREMENTS 🤖

**🚨 STOP! READ THIS FIRST! 🚨**

**MANDATORY EXECUTION ORDER - NO EXCEPTIONS:**

1. **FIRST**: Complete ALL database verification steps (Step 2)
2. **SECOND**: Start the server (Step 3)
3. **THIRD**: Execute scenarios in order

**⚠️ VIOLATING THIS ORDER = COMPLETE FAILURE**

**MANDATORY LLM REQUIREMENT:**

- **MUST USE GPT-4**: This playbook requires GPT-4 level reasoning and instruction adherence
- **DO NOT USE**: GPT-3.5, Claude, or other LLMs for playbook execution
- **REASON**: Complex multi-step scenarios with strict execution requirements need advanced reasoning capabilities
- **VERIFICATION**: Confirm you are using GPT-4 before proceeding with any scenario

## 🚨 CRITICAL INSTRUCTION FOR AI EXECUTORS 🚨

**MANDATORY EXECUTION PROTOCOL - NO EXCEPTIONS:**

**BEFORE YOU DO ANYTHING ELSE:**

1. **MANDATORY DATABASE VERIFICATION**: You MUST verify the starting room configuration BEFORE starting the server
2. **MANDATORY PREREQUISITE CHECKS**: You MUST complete ALL pre-execution steps before ANY scenario
3. **ZERO TOLERANCE FOR SKIPPING**: Execute EVERY step in EVERY scenario EXACTLY as written
4. **NO INTERPRETATION ALLOWED**: Do NOT skip, modify, or interpret any steps
5. **NO ASSUMPTIONS ALLOWED**: Do NOT make assumptions about how systems should work
6. **EXECUTION ONLY**: Your job is to execute, not to interpret or improve
7. **EXECUTE EVEN IF WRONG**: If you think a step is wrong, execute it anyway and document the result

**VIOLATION CONSEQUENCES:**

- Skipping database verification = COMPLETE FAILURE
- Starting server without prerequisites = COMPLETE FAILURE
- Modifying any command = COMPLETE FAILURE
- Making assumptions = COMPLETE FAILURE

## Test Configuration

### Test Players

- **ArkanWolfshade** (AW) - password: Cthulhu1
- **Ithaqua** - password: Cthulhu1

### Server Configuration

- **Server Port**: 54731 (from `server/server_config.yaml`)
- **Client Port**: 5173 (from `client/vite.config.ts`)
- **Starting Room**: `earth_arkham_city_sanitarium_room_foyer_001` (Main Foyer)
- **Database**: `data/players/players.db`

### Command Syntax

- **Movement**: `go <direction>` or direction shortcuts (e.g., `go east`, `east`, `e`, `go west`, `west`, `w`)
- **Say**: `say <message>` or `/say <message>` or just `<message>` (defaults to say channel)
- **Local**: `local <message>` or `/l <message>`
- **Whisper**: `whisper <player> <message>`
- **Who**: `who` or `who <filter>`
- **Teleport**: `teleport <player>` (admin only)
- **Other**: `look`, `inventory`, `help`, `mute`, `unmute`, `dance`, etc.

## Configurable Timeout Settings

### Standard Timeouts (Default)

- **Login form wait**: 15 seconds
- **MOTD screen wait**: 15 seconds
- **Game interface load**: 15 seconds
- **Message delivery wait**: 10 seconds
- **Tab switching**: 2 seconds
- **Page load**: 5 seconds

### Low-Performance Machine Timeouts

- **Login form wait**: 30 seconds
- **MOTD screen wait**: 30 seconds
- **Game interface load**: 30 seconds
- **Message delivery wait**: 30 seconds
- **Tab switching**: 5 seconds
- **Page load**: 10 seconds

### High-Performance Machine Timeouts

- **Login form wait**: 5 seconds
- **MOTD screen wait**: 5 seconds
- **Game interface load**: 5 seconds
- **Message delivery wait**: 3 seconds
- **Tab switching**: 1 second
- **Page load**: 2 seconds

## CRITICAL SERVER MANAGEMENT RULES

### ONE SERVER ONLY RULE

**THERE CAN ONLY BE ONE SERVER RUNNING AT ANY TIME**

### MANDATORY SERVER STARTUP PROCEDURE

1. **STOP FIRST**: Before starting a server, ALWAYS run `./scripts/stop_server.ps1`
2. **VERIFY PORTS**: After stopping, verify ports are free with `netstat -an | findstr :54731` and `netstat -an | findstr :5173`
3. **NO BACKGROUND**: NEVER use `is_background: true` for server startup commands
4. **SEE OUTPUT**: ALWAYS use `is_background: false` for server startup so you can see what's happening
5. **ONE START ONLY**: Run `./scripts/start_dev.ps1` with `is_background: false` exactly ONCE
6. **IF IT SAYS "Press any key to exit"**: The server is running - DO NOT start another

### PRE-COMMAND CHECKLIST

Before running ANY server command, ask yourself:

- Did I already start a server in this session? (YES = STOP, don't start another)
- Am I about to use `is_background: true`? (YES = STOP, use false instead)
- Did I run `stop_server.ps1` first? (NO = STOP, run it first)
- Am I about to run `start_dev.ps1` when I already see "Press any key to exit"? (YES = STOP, server is already running)

## MANDATORY PRE-EXECUTION CHECKLIST

**YOU MUST COMPLETE EVERY ITEM BEFORE STARTING ANY SCENARIO:**

**DATABASE VERIFICATION (MANDATORY):**

- [ ] I have verified both test players exist in the database
- [ ] I have confirmed both players are in room `earth_arkham_city_sanitarium_room_foyer_001`
- [ ] I have confirmed ArkanWolfshade has admin privileges (is_admin = 1)
- [ ] I have run the SQL commands to update player locations if needed

**INSTRUCTION COMPLIANCE (MANDATORY):**

- [ ] I have read the MANDATORY EXECUTION PROTOCOL above
- [ ] I understand that skipping database verification = COMPLETE FAILURE
- [ ] I will execute every step exactly as written
- [ ] I will not skip, modify, or interpret any steps
- [ ] I will not make assumptions about system behavior
- [ ] I will document actual results, not expected results

**EXECUTION AFFIRMATION (MANDATORY):**

- [ ] I affirm that I will follow the database verification steps BEFORE starting the server
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

**⚠️ CRITICAL: THIS STEP IS MANDATORY AND CANNOT BE SKIPPED**

**MANDATORY PowerShell Commands to Run (EXECUTE ALL)**:

```powershell
# MANDATORY: Check if players exist and their current state
sqlite3 "data/players/players.db" "SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# MANDATORY: Update players to starting room (ALWAYS run this)
sqlite3 "data/players/players.db" "UPDATE players SET current_room_id = 'earth_arkham_city_sanitarium_room_foyer_001' WHERE name IN ('ArkanWolfshade', 'Ithaqua');"

# MANDATORY: Verify ArkanWolfshade has admin privileges (ALWAYS run this)
sqlite3 "data/players/players.db" "UPDATE players SET is_admin = 1 WHERE name = 'ArkanWolfshade';"

# MANDATORY: Verify the updates worked
sqlite3 "data/players/players.db" "SELECT name, current_room_id, is_admin FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua');"
```

**MANDATORY VERIFICATION**: Both players must exist, be in Main Foyer (`earth_arkham_city_sanitarium_room_foyer_001`), and AW must have admin privileges (is_admin = 1)

**⚠️ FAILURE TO COMPLETE THIS STEP = COMPLETE TEST FAILURE**

### Step 3: Start Development Environment (ONLY AFTER DATABASE VERIFICATION)

**⚠️ CRITICAL: DO NOT START SERVER UNTIL DATABASE VERIFICATION IS COMPLETE**

**Cursor Command**: Start the development server

```powershell
./scripts/start_dev.ps1
```

**Wait**: 180 seconds (3 minutes) for server to fully start on low-performance machines

**⚠️ REMINDER**: If you started the server without completing database verification, STOP IMMEDIATELY and restart from Step 2

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

## NO INTERPRETATION RULE

- If a command says "say Hello" - type exactly "say Hello"
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

- **Extended Timeouts**: All `wait_for` operations use configurable timeouts based on machine performance
- **Buffer Time**: Additional 5-10 second waits between critical operations
- **Retry Logic**: Commands may be repeated if they fail due to timing
- **Resource Monitoring**: Watch for memory/CPU usage during extended operations

## Security and Environment

- **Security-First Mindset**: Before starting the server, ensure all security configurations are properly set, especially COPPA compliance settings for minor users
- **Database Placement**: Verify database files are in correct locations (/data/players/ for production, /server/tests/data/players/ for tests)
- **Environment Variables**: Ensure all secrets are properly configured via environment variables, never hardcoded

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
