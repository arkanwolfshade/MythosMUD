# Cursor Workflows Documentation

*"In the shadowed halls of Miskatonic University, we learn that proper methodology requires understanding how tools work together. This document describes end-to-end workflows combining subagents, CLI, commands, and rules."*

## Overview

This document provides end-to-end workflow examples showing how to combine Cursor subagents, CLI, commands, and rules for common development tasks.

## Workflow Components

### Rules

- **Purpose**: Persistent guidance and best practices
- **Location**: `.cursor/rules/*.mdc`
- **When Used**: Always applied automatically
- **Example**: Coding standards, framework best practices

### Commands

- **Purpose**: Single-purpose workflows
- **Location**: `.cursor/commands/*.md`
- **When Used**: Invoked explicitly via `@command-name`
- **Example**: Bug investigation, test remediation

### Subagents

- **Purpose**: Complex, multi-step tasks requiring context isolation
- **Location**: `.cursor/agents/*.md`
- **When Used**: Automatically invoked by agent or commands
- **Example**: Codebase exploration, security audits

### CLI

- **Purpose**: Automation, CI/CD, headless operations
- **When Used**: Terminal-based workflows, scripts, automation
- **Example**: Automated code review, test failure analysis

## Workflow Examples

### Workflow 1: Bug Investigation

**Scenario**: Player reports they cannot log in

**Steps**:

1. **Invoke Command**:

   ```
   @investigate-bug
   Player cannot log in. Error messages appear in console but no specific error shown to user.
   ```

2. **Command Delegates to Subagent**:
   - Command activates `bug-investigator` subagent
   - Subagent follows systematic investigation methodology
   - Subagent collects evidence in isolated context

3. **Subagent Investigation**:
   - Checks server status
   - Examines authentication logs
   - Reviews database integrity
   - Analyzes authentication code
   - Generates comprehensive report

4. **Results**:
   - Investigation report with findings
   - Root cause analysis
   - Remediation prompt for fixing

**Tools Used**:

- Command: `investigate-bug.md`
- Subagent: `bug-investigator.md`
- Rules: `MYTHOSMUD_DEBUGGING_AGENT.mdc`, `GAME_BUG_INVESTIGATION_PLAYBOOK.mdc`

### Workflow 2: Test Coverage Analysis

**Scenario**: Need to improve test coverage before release

**Steps**:

1. **Invoke Command**:

   ```
   @server-test-remediation
   ```

2. **Command Uses Subagent**:
   - Command activates `test-analyzer` subagent
   - Subagent analyzes test coverage
   - Subagent identifies gaps and quality issues

3. **Subagent Analysis**:
   - Runs coverage analysis
   - Identifies untested code paths
   - Reviews test quality
   - Generates recommendations

4. **Results**:
   - Coverage report
   - Gap analysis
   - Prioritized test recommendations

**Tools Used**:

- Command: `server-test-remediation.md`
- Subagent: `test-analyzer.md`
- Rules: `pytest.mdc`, test coverage requirements

### Workflow 3: Security Audit via CLI

**Scenario**: Automated security review in CI/CD pipeline

**Steps**:

1. **Run CLI Script**:

   ```powershell
   .\scripts\cursor-cli-review.ps1 -GitChanges -Focus security -OutputReport
   ```

2. **CLI Invokes Agent**:
   - CLI runs Cursor agent in non-interactive mode
   - Agent reviews code changes for security issues
   - Agent uses security-auditor subagent for deep analysis

3. **Subagent Security Analysis**:
   - Scans for vulnerabilities
   - Checks COPPA compliance
   - Reviews input validation
   - Analyzes authentication/authorization

4. **Results**:
   - Security review report saved to file
   - Vulnerability findings
   - Compliance status
   - Recommendations

**Tools Used**:

- CLI Script: `cursor-cli-review.ps1`
- Subagent: `security-auditor.md`
- Rules: `security.mdc`, COPPA compliance rules

### Workflow 4: Performance Optimization

**Scenario**: Game server running slowly, need to identify bottlenecks

**Steps**:

1. **Invoke Subagent Directly**:

   ```
   Use the performance profiler to analyze bottlenecks in the game loop
   ```

2. **Subagent Analysis**:
   - Analyzes performance logs
   - Reviews game loop code
   - Identifies slow operations
   - Suggests optimizations

3. **Results**:
   - Performance report
   - Bottleneck identification
   - Optimization recommendations

**Tools Used**:

- Subagent: `performance-profiler.md`
- Rules: Performance monitoring guidelines

### Workflow 5: Codebase Exploration

**Scenario**: Need to understand how authentication works across the codebase

**Steps**:

1. **Request Exploration**:

   ```
   Use the codebase explorer to find all authentication implementations
   ```

2. **Subagent Exploration**:
   - Runs parallel semantic searches
   - Finds all auth-related code
   - Maps dependencies
   - Analyzes architecture

3. **Results**:
   - Comprehensive codebase map
   - All authentication implementations
   - Dependency relationships
   - Architecture overview

**Tools Used**:

- Subagent: `codebase-explorer.md`
- Rules: Architecture guidelines

### Workflow 6: Automated Test Failure Fix

**Scenario**: CI pipeline detects test failures, need automated remediation

**Steps**:

1. **Run CLI Script**:

   ```powershell
   .\scripts\cursor-cli-test-fix.ps1 -TestPath server/tests/unit -OutputReport
   ```

2. **CLI Analysis**:
   - CLI runs agent in non-interactive mode
   - Agent analyzes test failures
   - Agent uses test-analyzer subagent

3. **Subagent Analysis**:
   - Identifies failure patterns
   - Suggests specific fixes
   - Validates test quality

4. **Results**:
   - Test fix report
   - Specific code changes needed
   - Validation steps

**Tools Used**:

- CLI Script: `cursor-cli-test-fix.ps1`
- Subagent: `test-analyzer.md`
- Rules: Test quality requirements

## Combining Components

### Pattern 1: Command → Subagent

```
User invokes command → Command delegates to subagent → Subagent performs work → Results returned
```

**Example**: `investigate-bug.md` → `bug-investigator.md`

### Pattern 2: CLI → Agent → Subagent

```
CLI script runs → Agent invoked → Agent uses subagent → Results saved
```

**Example**: `cursor-cli-review.ps1` → Agent → `security-auditor.md`

### Pattern 3: Direct Subagent Invocation

```
User requests → Agent invokes subagent → Subagent performs work → Results returned
```

**Example**: "Use codebase explorer to..." → `codebase-explorer.md`

### Pattern 4: Rules Guide All

```
Rules provide guidance → Commands/Subagents/CLI follow rules → Consistent results
```

**Example**: Security rules guide security-auditor subagent

## Decision Tree

```
Need to perform a task?
├─ Simple, single-purpose?
│  └─ Use Command (@command-name)
├─ Complex, multi-step, needs isolation?
│  └─ Use Subagent (request directly or via command)
├─ Automation, CI/CD, headless?
│  └─ Use CLI (scripts/cursor-cli-*.ps1)
└─ Need persistent guidance?
   └─ Rules (always applied automatically)
```

## Best Practices

### When to Use Each Component

**Use Rules For**:

- Coding standards and best practices
- Framework-specific guidelines
- Project conventions
- Always-applied guidance

**Use Commands For**:

- Quick, repeatable workflows
- Single-purpose tasks
- Common development tasks
- User-initiated actions

**Use Subagents For**:

- Complex, multi-step analysis
- Deep research tasks
- Parallel workstreams
- Context-heavy operations

**Use CLI For**:

- Automation and scripts
- CI/CD pipelines
- Headless operations
- Non-interactive workflows

### Workflow Optimization

1. **Start with Rules**: Rules provide foundation for all work
2. **Use Commands for Common Tasks**: Quick access to workflows
3. **Delegate Complex Work to Subagents**: Isolate context-heavy tasks
4. **Automate with CLI**: Use CLI for repetitive or scheduled tasks

## Integration Examples

### Example 1: Full Development Cycle

1. **Planning**: Use Plan mode in CLI

   ```powershell
   .\scripts\cursor-cli-agent.ps1 -Plan -Prompt "implement new feature"
   ```

2. **Implementation**: Use Agent mode with subagents

   ```
   Use codebase explorer to understand existing patterns
   ```

3. **Testing**: Use test-analyzer subagent

   ```
   Analyze test coverage for new feature
   ```

4. **Review**: Use CLI review script

   ```powershell
   .\scripts\cursor-cli-review.ps1 -GitChanges -Focus all
   ```

5. **Security**: Use security-auditor subagent

   ```
   Perform security audit of new feature
   ```

### Example 2: Bug Fix Workflow

1. **Investigation**: Use investigate-bug command

   ```
   @investigate-bug
   Bug description...
   ```

2. **Fix**: Use main agent with context from investigation

   ```
   Fix the issues identified in the investigation report
   ```

3. **Test**: Use test-analyzer subagent

   ```
   Verify test coverage for bug fix
   ```

4. **Review**: Use CLI review

   ```powershell
   .\scripts\cursor-cli-review.ps1 -GitChanges
   ```

## References

- Subagents: `docs/CURSOR_SUBAGENTS.md`
- CLI: `docs/CURSOR_CLI.md`
- Commands: `.cursor/commands/`
- Rules: `.cursor/rules/`
- Subagent usage: `.cursor/rules/subagent-usage.mdc`

## Notes

- All components work together seamlessly
- Rules provide the foundation for all work
- Commands provide quick access to common workflows
- Subagents handle complex, context-heavy tasks
- CLI enables automation and CI/CD integration
