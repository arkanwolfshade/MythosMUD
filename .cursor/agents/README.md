# Cursor Subagents for MythosMUD

*"In the shadowed halls of Miskatonic University, we learn that complex investigations require specialized expertise. Each subagent operates in its own isolated context, allowing deep exploration without contaminating the main conversation."*

## Overview

Subagents are specialized AI assistants that Cursor's agent can delegate complex tasks to. Each subagent operates in its own context window, handles specific types of work, and returns its result to the parent agent.

## Available Subagents

### Codebase Explorer

**File**: `codebase-explorer.md`
**Purpose**: Deep codebase exploration and analysis

- Finding all implementations of patterns
- Analyzing architecture across multiple files
- Researching dependencies and relationships
- Parallel exploration of different codebase areas

### Test Suite Analyzer

**File**: `test-analyzer.md`
**Purpose**: Comprehensive test analysis and coverage reporting

- Analyzing test coverage gaps
- Finding untested code paths
- Identifying test quality issues
- Generating test improvement recommendations

### Security Auditor

**File**: `security-auditor.md`
**Purpose**: Security-focused code review and vulnerability analysis

- Security vulnerability scanning
- COPPA compliance verification
- Input validation review
- Authentication/authorization analysis

### Performance Profiler

**File**: `performance-profiler.md`
**Purpose**: Performance analysis and optimization recommendations

- Identifying performance bottlenecks
- Analyzing slow operations
- Database query optimization
- Memory leak detection

### Bug Investigator

**File**: `bug-investigator.md`
**Purpose**: Systematic bug investigation and root cause analysis

- Deep bug investigation
- Root cause analysis
- Evidence collection
- Regression analysis

## When to Use Subagents

Use subagents when:

- You need context isolation for long research tasks
- Running multiple workstreams in parallel
- The task requires specialized expertise across many steps
- You want an independent verification of work

**Do NOT use subagents for**:

- Simple, single-purpose tasks (use commands instead)
- Quick, repeatable actions (use skills instead)
- Tasks that complete in one shot

## Subagent Structure

Each subagent file follows this structure:

```markdown
---
name: "Subagent Name"
description: "Clear description of what this subagent does"
---

# Subagent Name

## Purpose
[Clear explanation of when to use this subagent]

## Capabilities
[List of what this subagent can do]

## Usage
[How to invoke this subagent]

## Output Format
[What kind of report/result to expect]

## Integration
[How this integrates with existing commands/rules]
```

## Integration with Commands

Subagents integrate with existing Cursor commands:

- `investigate-bug.md` → Uses `bug-investigator` subagent
- `server-test-remediation.md` → Uses `test-analyzer` subagent
- `client-test-remediation.md` → Uses `test-analyzer` subagent
- `multiplayer-playwright-testing.md` → Uses `codebase-explorer` subagent

## Performance Considerations

- **Context Isolation**: Each subagent has its own context window
- **Parallel Execution**: Multiple subagents can run simultaneously
- **Token Usage**: Each subagent consumes tokens independently
- **Startup Overhead**: Subagents gather their own context, which adds latency

## References

- [Cursor Subagents Documentation](https://cursor.com/docs/context/subagents)
- Project rules: `.cursor/rules/subagent-usage.mdc`
- Project commands: `.cursor/commands/`
