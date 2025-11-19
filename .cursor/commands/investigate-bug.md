---
description: Unified bug investigation, debugging, and troubleshooting for server and client issues
alwaysApply: false
---

# MythosMUD Bug Investigation Command

*"In the restricted archives of Miskatonic University, we learn that proper investigation requires systematic methodology, comprehensive evidence collection, and thorough analysis. The truth lies not in hasty conclusions, but in methodical examination of all available evidence."*

## 🚨 CRITICAL AI EXECUTOR REQUIREMENTS 🚨

**CURSOR AI CONFIGURATION:**

- **MUST USE GPT-4**: This investigation command requires GPT-4 level reasoning and systematic analysis
- **DO NOT USE**: GPT-3.5, Claude, or other LLMs for investigation execution
- **REASON**: Complex bug investigation requires advanced reasoning capabilities and systematic analysis
- **VERIFICATION**: Confirm you are using GPT-4 before proceeding with any investigation

**MANDATORY RULE REFERENCES:**

This command activates and requires adherence to:

1. **`.cursor/rules/MYTHOSMUD_DEBUGGING_AGENT.mdc`** - Investigation agent configuration and methodology
2. **`.cursor/rules/GAME_BUG_INVESTIGATION_PLAYBOOK.mdc`** - Detailed investigation procedures and scenarios

**CRITICAL INSTRUCTION FOR AI INVESTIGATORS:**

**BEFORE YOU DO ANYTHING ELSE:**

- Execute EVERY investigation step EXACTLY as written
- Do NOT skip, modify, or interpret any steps
- Do NOT attempt to fix any issues found - ONLY investigate and report
- Your job is to investigate, document, and analyze - NOT to fix
- If you think a step is unnecessary, execute it anyway and document the result
- Generate a comprehensive investigation report with findings and analysis

## 🔐 MANDATORY TEST CREDENTIALS

**CRITICAL**: Always use the official test credentials:

**Test Players:**

- **ArkanWolfshade** (AW) - password: Cthulhu1
- **Ithaqua** - password: Cthulhu1

**NEVER use random or assumed credentials** - Always use these exact test accounts for all investigations involving login, authentication, or multiplayer scenarios.

## 🎯 INVESTIGATION OBJECTIVES

**PRIMARY GOAL**: Generate a comprehensive investigation report that includes:

- Detailed description of the bug behavior
- Root cause analysis
- System impact assessment
- Evidence collection and documentation
- Recommended investigation priorities (NOT fixes)
- Technical analysis of affected components
- Remediation prompt for fixing identified issues (if root cause found)

**CRITICAL RULE**: **DO NOT ATTEMPT TO FIX ANY ISSUES** - Only investigate, document, and analyze.

## 📋 PRE-INVESTIGATION CHECKLIST

Before starting ANY investigation, confirm:

- [ ] I have read the MANDATORY RULE above
- [ ] I will execute every step exactly as written
- [ ] I will NOT attempt to fix any issues found
- [ ] I will generate a comprehensive investigation report
- [ ] I will document all findings systematically
- [ ] I will focus on investigation, not resolution
- [ ] I will use ONLY the official test credentials (ArkanWolfshade/Cthulhu1, Ithaqua/Cthulhu1)
- [ ] I will NOT use random or assumed credentials
- [ ] I have activated both rule files: `MYTHOSMUD_DEBUGGING_AGENT.mdc` and `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc`

## 🔍 INVESTIGATION METHODOLOGY

### Phase 1: Initial Bug Report Analysis

1. **Parse Bug Description**: Extract key details from user report
2. **Identify Affected Systems**: Determine which components are involved
3. **Create Investigation Plan**: Outline systematic investigation approach
4. **Set Investigation Scope**: Define boundaries and priorities
5. **Generate Session ID**: Create unique investigation session identifier

### Phase 2: System State Investigation

1. **Check Server Status**: Verify current system state
2. **Examine Logs**: Analyze relevant log files for errors/patterns
3. **Database State**: Investigate database integrity and data consistency
4. **Configuration Review**: Check system configuration for anomalies

### Phase 3: Code Analysis

1. **Locate Relevant Code**: Find code responsible for bug behavior
2. **Trace Execution Path**: Follow code execution through affected systems
3. **Identify Dependencies**: Map out system dependencies and interactions
4. **Analyze Data Flow**: Understand how data moves through the system

### Phase 4: Evidence Collection

1. **Gather Error Messages**: Collect all relevant error messages
2. **Document System State**: Record current system configuration
3. **Capture Log Evidence**: Extract relevant log entries with timestamps
4. **Identify Patterns**: Look for recurring issues or anomalies

### Phase 5: Analysis and Reporting

1. **Root Cause Analysis**: Determine underlying cause of the bug
2. **Impact Assessment**: Evaluate scope and severity of the issue
3. **Generate Report**: Create comprehensive investigation report
4. **Document Findings**: Record all discoveries and analysis
5. **Generate Remediation Prompt**: If root cause found, create Cursor Chat prompt for fixing

## 🛠️ AVAILABLE INVESTIGATION TOOLS

### Codebase Analysis Tools

- **codebase_search**: Semantic search for code patterns and functionality
- **grep**: Exact string/regex searches across the codebase
- **read_file**: Read and analyze specific files
- **glob_file_search**: Find files by patterns
- **list_dir**: Explore directory structures

### System Analysis Tools

- **run_terminal_cmd**: Execute system commands for investigation
- **read_lints**: Check for code quality issues
- **web_search**: Research external information if needed

### Testing and Validation Tools

- **mcp_playwright_browser_***: Browser automation for client-side testing
- **todo_write**: Track investigation progress and findings

### Browser Testing Credential Requirements

When using browser automation tools for investigation:

- **ALWAYS use official test credentials**: ArkanWolfshade / Cthulhu1 or Ithaqua / Cthulhu1
- **NEVER attempt to create new accounts** during investigation
- **NEVER use random or assumed credentials**

## 🚀 INVESTIGATION SCENARIOS

### Scenario 1: Authentication/Login Issues

**Bug Report**: "Player cannot log in"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract player username/identifier, error messages, timing
2. **Check Server Status**: Verify server is running and responding
3. **Examine Authentication Logs**: Search for authentication-related errors
4. **Database Investigation**: Check database integrity and player data
5. **Code Analysis**: Review authentication flow and password validation
6. **Configuration Review**: Verify authentication settings and environment variables

**REPORT TEMPLATE**: See `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` - Scenario 1

### Scenario 2: Movement/Command Issues

**Bug Report**: "Player cannot move between rooms"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract movement commands, error messages, locations
2. **Check Game State**: Verify current game state and room data
3. **Database Investigation**: Check player location data and room integrity
4. **Room Data Analysis**: Examine room configuration and connectivity
5. **Command Processing Investigation**: Trace movement command execution
6. **System State Analysis**: Check WebSocket and game loop functionality

**REPORT TEMPLATE**: See `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` - Scenario 2

### Scenario 3: Chat/Communication Issues

**Bug Report**: "Chat messages not appearing or delayed"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract chat channel, users affected, timing
2. **Check Communication Logs**: Search for chat and WebSocket errors
3. **WebSocket Investigation**: Verify connection state and health
4. **Chat System Code Analysis**: Review message routing and delivery
5. **Database Investigation**: Check chat data storage and retrieval
6. **Network Analysis**: Analyze connectivity and performance

**REPORT TEMPLATE**: See `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` - Scenario 3

### Scenario 4: Performance/System Issues

**Bug Report**: "Game is running slowly or unresponsive"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract performance symptoms, timing, resource indicators
2. **System Resource Analysis**: Check CPU, memory, disk usage
3. **Performance Logs Analysis**: Search for slow operations and timeouts
4. **Database Performance Investigation**: Check query performance and integrity
5. **Code Performance Analysis**: Review performance-critical code paths
6. **System Monitoring**: Analyze resource usage trends

**REPORT TEMPLATE**: See `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` - Scenario 4

### Scenario 5: Client-Side Issues

**Bug Report**: "Client UI not working or displaying incorrectly"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract UI symptoms, browser, error messages
2. **Check Client Logs**: Review client-side error logs
3. **Browser Console Investigation**: Check browser console for errors
4. **Network Analysis**: Verify API calls and WebSocket connections
5. **Code Analysis**: Review React components and client-side logic
6. **Configuration Review**: Check client configuration and environment

**REPORT TEMPLATE**: Custom template for client-side issues

### Scenario 6: Server-Side Issues

**Bug Report**: "Server errors or crashes"

**INVESTIGATION STEPS:**

1. **Parse Bug Description**: Extract error messages, timing, server state
2. **Check Server Logs**: Review server error logs and stack traces
3. **Server Status Investigation**: Verify server process and resource usage
4. **Database Investigation**: Check database connectivity and integrity
5. **Code Analysis**: Review server-side error handling and logic
6. **Configuration Review**: Verify server configuration and environment

**REPORT TEMPLATE**: Custom template for server-side issues

## 📊 INVESTIGATION REPORTING STANDARDS

### Report Structure

1. **Executive Summary**: Brief overview of findings
2. **Detailed Findings**: Comprehensive analysis of each investigation area
3. **Root Cause Analysis**: Technical analysis of underlying issues
4. **System Impact Assessment**: Scope and severity evaluation
5. **Evidence Documentation**: Specific data, logs, and code references
6. **Investigation Recommendations**: Priorities for further investigation (NOT fixes)
7. **Remediation Prompt**: Cursor Chat prompt for fixing identified issues (if root cause found)

### Evidence Collection Standards

- **Timestamp All Evidence**: Include precise timestamps for all findings
- **Document Command Output**: Record exact command results
- **Include Code References**: Provide specific file and line references
- **Log Entry Documentation**: Include full log entries with context
- **System State Snapshots**: Document current system configuration
- **Screenshots**: Capture relevant UI states and error messages

### Analysis Quality Standards

- **Systematic Approach**: Follow investigation methodology consistently
- **Comprehensive Coverage**: Address all relevant system components
- **Technical Depth**: Provide detailed technical analysis
- **Evidence-Based Conclusions**: Base all conclusions on collected evidence
- **Clear Documentation**: Ensure findings are clearly documented and traceable

## 📝 INVESTIGATION SESSION MANAGEMENT

### Session Creation

- **Unique Session ID**: Generate timestamped session identifier (e.g., `2025-01-XX_session-001_auth-issue`)
- **Session Documentation**: Create investigation session file in `investigations/sessions/`
- **Pattern Tracking**: Update pattern detection files if recurring issues found

### Session Structure

```
investigations/
├── sessions/
│   ├── 2025-01-XX_session-001_auth-issue.md
│   ├── 2025-01-XX_session-002_movement-bug.md
│   └── ...
├── patterns/
│   ├── recurring-issues.md
│   ├── regression-patterns.md
│   └── system-trends.md
└── knowledge-base/
    ├── common-fixes.md
    ├── investigation-templates.md
    └── system-architecture-notes.md
```

## 🚨 CRITICAL REMINDERS

**NEVER ATTEMPT TO FIX ISSUES** - Your role is investigation and analysis only.

**ALWAYS DOCUMENT FINDINGS** - Comprehensive documentation is essential for effective investigation.

**FOLLOW METHODOLOGY** - Systematic approach ensures thorough investigation.

**EVIDENCE-BASED ANALYSIS** - Base all conclusions on collected evidence and data.

**GENERATE COMPREHENSIVE REPORTS** - Detailed reports enable effective decision-making.

**ACTIVATE BOTH RULE FILES** - Ensure both `MYTHOSMUD_DEBUGGING_AGENT.mdc` and `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` are active.

## 📋 INVESTIGATION COMPLETION CHECKLIST

Before concluding any investigation, verify:

- [ ] All investigation steps completed as written
- [ ] Comprehensive evidence collected and documented
- [ ] Root cause analysis completed (or marked inconclusive)
- [ ] System impact assessed
- [ ] Investigation report generated
- [ ] No attempt made to fix issues (investigation only)
- [ ] All findings clearly documented with evidence
- [ ] Only official test credentials were used
- [ ] Session logged in investigation history
- [ ] Pattern analysis updated if applicable
- [ ] Remediation prompt generated (if root cause found)
- [ ] Both rule files were referenced and followed

## 📖 USAGE EXAMPLES

**Investigate Authentication Issue:**

```
/investigate-bug

I'm experiencing an authentication issue where players cannot log in. Error messages appear in the console but no specific error is shown to the user.
```

**Investigate Movement Bug:**

```
/investigate-bug

Players report they cannot move between rooms. The movement command appears to execute but the player remains in the same location.
```

**Investigate Performance Issue:**

```
/investigate-bug

The game server is running slowly and becoming unresponsive after a few minutes of operation. CPU usage is high and response times are increasing.
```

**Investigate Client-Side Issue:**

```
/investigate-bug

The client UI is not displaying chat messages correctly. Messages appear in the console but not in the UI. Browser console shows no errors.
```

## 🔧 INVESTIGATION COMMANDS

### Server Status Check

```powershell
# Check server status
./scripts/stop_server.ps1
netstat -an | findstr :54731
netstat -an | findstr :5173
./scripts/start_local.ps1
```

### Log Analysis

```powershell
# Check recent logs
Get-Content logs/development/server.log -Tail 100
Get-Content logs/development/client.log -Tail 100
Get-Content logs/local/errors.log -Tail 100
```

### Database Investigation

```powershell
# Check database integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"
sqlite3 data/players/local_players.db "SELECT * FROM players;"
```

### Playwright Reproduction

```javascript
// Use Playwright MCP to reproduce issues
// Navigate to application
// Attempt to reproduce reported behavior
// Capture screenshots and logs
```

## 🎯 INVESTIGATION SUCCESS CRITERIA

**MANDATORY SUCCESS CONDITIONS:**

1. **Comprehensive Report**: Complete investigation report with all required sections
2. **Evidence Collection**: All relevant evidence documented with timestamps
3. **Root Cause Analysis**: Technical analysis of underlying issues (or marked inconclusive)
4. **System Impact**: Scope and severity assessment completed
5. **Documentation**: All findings clearly documented and traceable

**OPTIONAL SUCCESS CONDITIONS:**

1. **Remediation Prompt**: Cursor Chat prompt generated for fixing issues
2. **Pattern Detection**: Recurring issues identified and documented
3. **Knowledge Base Update**: Investigation insights added to knowledge base

**AI RULE**: Focus on mandatory success conditions first. Optional conditions are nice-to-have but not blocking.

---

**Remember**: This command activates the unified debugging and investigation system. Always follow the methodology from both rule files and generate comprehensive reports. Do not attempt to fix any issues discovered during investigation - only investigate, document, and analyze.

**AI INSTRUCTION**: When this command is invoked, activate both `MYTHOSMUD_DEBUGGING_AGENT.mdc` and `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc` rule files and follow their methodologies exactly. Generate a comprehensive investigation report with all findings, evidence, and analysis. If a root cause is identified, generate a remediation prompt for fixing the issue.

