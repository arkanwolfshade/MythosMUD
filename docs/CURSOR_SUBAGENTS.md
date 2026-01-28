# Cursor Subagents Documentation

*"In the shadowed halls of Miskatonic University, we learn that complex investigations require specialized expertise. Each subagent operates in its own isolated context, allowing deep exploration without contaminating the main conversation."*

## Overview

Subagents are specialized AI assistants that Cursor's agent can delegate complex tasks to. Each subagent operates in its own context window, handles specific types of work, and returns its result to the parent agent.

## Key Concepts

### Context Isolation
Each subagent has its own context window. Long research or exploration tasks don't consume space in your main conversation.

### Parallel Execution
Multiple subagents can launch simultaneously. Work on different parts of your codebase without waiting for sequential completion.

### Specialized Expertise
Subagents can be configured with custom prompts, tool access, and models for domain-specific tasks.

### Reusability
Custom subagents can be defined and used across projects.

## Available Subagents

### Codebase Explorer
**File**: `.cursor/agents/codebase-explorer.md`

**Purpose**: Deep codebase exploration and analysis

**Use Cases**:
- Finding all implementations of patterns or interfaces
- Analyzing architecture across multiple files
- Researching dependencies and relationships
- Parallel exploration of different codebase areas

**Example Usage**:
```
"Use the codebase explorer to find all authentication implementations"
"Explore the codebase to understand how the persistence layer works"
"Find all usages of the Player class across the codebase"
```

### Test Suite Analyzer
**File**: `.cursor/agents/test-analyzer.md`

**Purpose**: Comprehensive test analysis and coverage reporting

**Use Cases**:
- Analyzing test coverage gaps
- Finding untested code paths
- Identifying test quality issues
- Generating test improvement recommendations

**Example Usage**:
```
"Analyze test coverage and find gaps"
"Review test quality in server/tests/unit"
"Find untested code paths in the authentication module"
```

**Integration**: Used by `server-test-remediation.md` and `client-test-remediation.md` commands

### Security Auditor
**File**: `.cursor/agents/security-auditor.md`

**Purpose**: Security-focused code review and vulnerability analysis

**Use Cases**:
- Security vulnerability scanning
- COPPA compliance verification
- Input validation review
- Authentication/authorization analysis

**Example Usage**:
```
"Perform security audit of the authentication module"
"Verify COPPA compliance for user data handling"
"Review input validation in API endpoints"
```

### Performance Profiler
**File**: `.cursor/agents/performance-profiler.md`

**Purpose**: Performance analysis and optimization recommendations

**Use Cases**:
- Identifying performance bottlenecks
- Analyzing slow operations
- Database query optimization
- Memory leak detection

**Example Usage**:
```
"Analyze performance bottlenecks in the game loop"
"Review database query performance"
"Find memory leaks in the server"
```

### Bug Investigator
**File**: `.cursor/agents/bug-investigator.md`

**Purpose**: Systematic bug investigation and root cause analysis

**Use Cases**:
- Deep bug investigation
- Root cause analysis
- Evidence collection
- Regression analysis

**Example Usage**:
```
"Investigate why players cannot log in"
"Find the root cause of the movement bug"
"Systematically investigate the performance issue"
```

**Integration**: Used by `investigate-bug.md` command

## When to Use Subagents

### Use Subagents When:
- **Context Isolation Needed**: Long research or exploration tasks that would consume significant context
- **Parallel Execution**: Multiple workstreams that can run simultaneously
- **Specialized Expertise**: Tasks requiring specialized knowledge across many steps
- **Independent Verification**: Need for separate context window to verify work
- **Complex Multi-Step Tasks**: Tasks that require multiple phases and deep analysis

### Do NOT Use Subagents For:
- **Simple Single-Purpose Tasks**: Use commands instead (e.g., "format imports", "generate changelog")
- **Quick Repeatable Actions**: Use skills instead
- **Tasks Completing in One Shot**: Main agent is faster
- **Simple File Operations**: Main agent handles these efficiently

## Subagent vs Command vs Rule

| Aspect        | Subagents                 | Commands                 | Rules                     |
| ------------- | ------------------------- | ------------------------ | ------------------------- |
| **Purpose**   | Complex, multi-step tasks | Single-purpose workflows | Persistent guidance       |
| **Context**   | Isolated context window   | Shared context           | Always applied            |
| **Execution** | Parallel or sequential    | Sequential               | Applied automatically     |
| **Best For**  | Deep research, analysis   | Quick actions, workflows | Best practices, standards |

## Built-in Subagents

Cursor includes three built-in subagents that handle context-heavy operations automatically:

### Explore Subagent
- Searches and analyzes codebases
- Uses faster models for parallel searches
- Generates large intermediate output (isolated from main context)

### Bash Subagent
- Runs series of shell commands
- Isolates verbose command output
- Keeps parent focused on decisions, not logs

### Browser Subagent
- Controls browser via MCP tools
- Filters noisy DOM snapshots and screenshots
- Returns relevant results only

These are used automatically when appropriate - no configuration needed.

## Performance and Cost Considerations

### Token Usage
- **Subagents consume tokens independently**: Each subagent has its own context window
- **Parallel execution multiplies tokens**: Running 5 subagents uses ~5x tokens
- **Evaluate overhead**: For simple tasks, main agent is faster and cheaper

### Performance Trade-offs
- **Context Isolation**: Benefit is isolation, not speed
- **Startup Overhead**: Subagents gather their own context, adding latency
- **Parallel Execution**: Can be faster for complex parallel work
- **Model Flexibility**: Can use faster models for exploration tasks

### When Subagents Are Worth It
- Long-running research tasks (>10 minutes)
- Multiple parallel workstreams
- Tasks requiring specialized expertise
- Independent verification needs

### When Main Agent Is Better
- Quick, simple tasks (<5 minutes)
- Single workstream
- Tasks requiring conversation context
- Immediate feedback needed

## Integration with Commands

Subagents integrate with existing Cursor commands:

- `investigate-bug.md` → Uses `bug-investigator` subagent
- `server-test-remediation.md` → Uses `test-analyzer` subagent
- `client-test-remediation.md` → Uses `test-analyzer` subagent
- `multiplayer-playwright-testing.md` → Uses `codebase-explorer` subagent

## Creating Custom Subagents

### Subagent File Structure

Create subagent files in `.cursor/agents/` with this structure:

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

### Best Practices

- **Clear Naming**: Use descriptive names that indicate purpose
- **Focused Purpose**: Each subagent should have a clear, focused purpose
- **Reusable**: Design subagents to be reusable across projects
- **Well Documented**: Include comprehensive documentation
- **Integration**: Integrate with existing commands and rules

## References

- [Cursor Subagents Documentation](https://cursor.com/docs/context/subagents)
- Subagent definitions: `.cursor/agents/`
- Usage guidelines: `.cursor/rules/subagent-usage.mdc`
- Command definitions: `.cursor/commands/`

## Examples

### Example 1: Codebase Exploration
```
User: "Find all implementations of the PersistenceLayer interface"

Agent: [Launches codebase-explorer subagent]
Subagent: [Runs parallel searches, analyzes results]
Subagent: [Returns comprehensive report with all implementations]
Agent: [Presents findings to user]
```

### Example 2: Test Analysis
```
User: "Analyze test coverage gaps in server/tests/unit"

Agent: [Launches test-analyzer subagent]
Subagent: [Runs coverage analysis, identifies gaps]
Subagent: [Returns prioritized list of tests to add]
Agent: [Presents recommendations to user]
```

### Example 3: Security Audit
```
User: "Perform security audit of authentication module"

Agent: [Launches security-auditor subagent]
Subagent: [Scans for vulnerabilities, checks compliance]
Subagent: [Returns security assessment report]
Agent: [Presents findings to user]
```

## Notes

- Subagents are powerful but have overhead - use judiciously
- Commands provide quick workflows - use for common tasks
- Rules provide persistent guidance - always applied
- All components work together: Rules guide → Commands execute → Subagents handle complex work
