# Cursor IDE Setup Guide for Optimal Subagent Usage

_"In the restricted archives, we learn that proper configuration is essential for efficient research. This guide ensures Cursor IDE is optimally configured to leverage our specialized subagents."_

## Overview

This guide helps you configure Cursor IDE and chat to automatically and effectively use the custom subagents we've created for MythosMUD.

## Automatic Subagent Discovery

**Good News**: Cursor automatically discovers subagents in `.cursor/agents/` - no additional configuration needed!

The subagents are already available to Cursor's agent. However, you can optimize their usage with the following settings and practices.

## Cross-Machine Portability (DRY Source of Truth)

Use this section as the canonical checklist for making your Cursor + MythosMUD setup portable across machines.
Do not duplicate this guidance in other docs; reference this section instead.

### 1. Keep project behavior in repo-tracked files

Treat these files as the primary portable source of truth:

- `.cursor/rules/` for project rules
- `.cursor/skills/` for project skills
- `.cursor/agents/` and `.cursor/commands/` for agent workflows
- `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` for shared instructions
- Project scripts and configs (`scripts/`, `Makefile`, tool config files)

### 2. Separate user preferences from project policy

Keep machine/user ergonomics outside the repo:

- Cursor user settings and keybindings
- PowerShell profile, aliases, and local helper scripts
- Personal snippets and editor UX preferences

Recommendation: store these in a private dotfiles repository and sync them to each machine.

### 3. Recreate local state, do not copy it

Avoid copying transient state across machines:

- Terminal state/history files
- Caches, indexes, virtual environments, and `node_modules`
- Local auth sessions and tokens

Recreate these using project bootstrap steps instead.

### 4. Keep secrets portable but never versioned

- Use `.env.*.example` files as templates
- Create local `.env.*` files per machine
- Store real secrets in a password manager or OS credential store
- Never commit secret values

See `docs/CONFIGURATION_FILES_REFERENCE.md` for configuration tuple details.

### 5. Standard machine bootstrap flow

For each new machine:

1. Clone repo and open in Cursor
2. Restore user-level Cursor/PowerShell preferences from dotfiles
3. Create local `.env.*` files from example templates
4. Install dependencies and run validation (`make test`, lint/type-check flows)
5. Verify MCP servers are enabled/authenticated as needed

### 6. Documentation DRY conventions

- Put machine portability guidance in this file only
- In other docs, reference this section instead of repeating setup instructions
- When rules/skills change, update the repo-tracked sources first

## Cursor IDE Settings

### 1. Enable Max Mode (If on Legacy Plan)

If you're on a legacy request-based plan, you must enable Max Mode to use subagents:

1. Open Cursor Settings (Ctrl+, or Cmd+,)
2. Search for "Max Mode"
3. Enable "Max Mode" or "Agent Mode"
4. This enables subagent functionality

**Note**: Usage-based plans have subagents enabled by default.

### 2. Configure Agent Behavior

To optimize automatic subagent usage:

1. **Open Cursor Settings**
2. **Search for "Agent" or "AI"**
3. **Configure these settings**:
   - **Agent Mode**: Set to "Auto" or "Always On"
   - **Context Window**: Larger context windows allow subagents to work more effectively
   - **Model Selection**: Use models that support subagents (GPT-4, Claude Sonnet 4.5, etc.)

### 3. Chat Settings

Optimize chat for subagent usage:

1. **Open Chat Settings** (click gear icon in chat)
2. **Enable**:
   - "Use subagents for complex tasks"
   - "Parallel execution" (if available)
   - "Context isolation" (if available)

## Best Practices for Automatic Subagent Usage

### 1. Use Descriptive Prompts

The more specific your prompt, the better Cursor can decide when to use subagents:

**Good Prompts** (triggers subagents automatically):

```
"Find all implementations of the authentication system across the codebase"
"Analyze test coverage and identify gaps in server/tests/unit"
"Perform a security audit of the authentication module"
"Investigate why players cannot log in - need systematic analysis"
"Profile performance bottlenecks in the game loop"
```

**Less Effective Prompts** (may not trigger subagents):

```
"Fix bugs"
"Review code"
"Check tests"
```

### 2. Explicitly Request Subagents When Needed

You can explicitly request subagent usage:

```
"Use the codebase explorer to find all Player class usages"
"Run the security auditor on server/services/auth.py"
"Use the test analyzer to review coverage in server/tests/"
"Invoke the bug investigator to analyze the login issue"
"Use the performance profiler to find bottlenecks"
```

### 3. Use Commands That Leverage Subagents

Several commands automatically use subagents:

- `@investigate-bug` → Uses `bug-investigator` subagent
- `@server-test-remediation` → Uses `test-analyzer` subagent
- `@client-test-remediation` → Uses `test-analyzer` subagent
- `@multiplayer-playwright-testing` → Uses `codebase-explorer` subagent

### 4. Understand When Subagents Are Automatically Used

Cursor automatically uses subagents when:

- **Complex Multi-Step Tasks**: Tasks requiring multiple phases
- **Context-Heavy Operations**: Tasks that would consume significant context
- **Parallel Workstreams**: Multiple tasks that can run simultaneously
- **Specialized Analysis**: Security, performance, or testing analysis

## Chat Conversation Patterns

### Pattern 1: Exploration Tasks

**User**: "I need to understand how authentication works across the codebase"

**Expected Behavior**:

- Agent recognizes this as a complex exploration task
- Automatically invokes `codebase-explorer` subagent
- Subagent runs parallel searches
- Returns comprehensive findings

### Pattern 2: Analysis Tasks

**User**: "Analyze test coverage in server/tests/unit and find gaps"

**Expected Behavior**:

- Agent recognizes this as test analysis task
- Automatically invokes `test-analyzer` subagent
- Subagent analyzes coverage and identifies gaps
- Returns prioritized recommendations

### Pattern 3: Investigation Tasks

**User**: "Players report they cannot log in. Investigate systematically"

**Expected Behavior**:

- Agent recognizes this as bug investigation
- Can use `@investigate-bug` command (which uses `bug-investigator` subagent)
- Or automatically invokes `bug-investigator` subagent directly
- Returns comprehensive investigation report

## Optimizing Subagent Performance

### 1. Provide Context

Give subagents enough context to work effectively:

```
"Use the codebase explorer to find all authentication implementations.
Focus on server/services/auth/ and server/api/auth/ directories.
I'm particularly interested in JWT token handling."
```

### 2. Be Specific About Goals

Clear goals help subagents focus:

```
"Use the security auditor to review server/services/auth.py for:
- COPPA compliance issues
- Input validation problems
- Authentication vulnerabilities"
```

### 3. Request Parallel Work When Appropriate

You can request parallel subagent execution:

```
"Use the codebase explorer to find all Player class usages,
and simultaneously use the test analyzer to check test coverage for Player-related code"
```

## Monitoring Subagent Usage

### How to Know When Subagents Are Used

Cursor will indicate when subagents are active:

1. **Chat Interface**: Look for indicators like "Using subagent..." or similar messages
2. **Activity Panel**: Subagent activity may appear in the activity panel
3. **Results**: Subagent results are typically comprehensive and well-structured

### Understanding Subagent Output

Subagent output typically includes:

- **Structured Reports**: Well-organized findings
- **Comprehensive Analysis**: Deep dive into the topic
- **Actionable Recommendations**: Specific next steps
- **Evidence**: Code references, file paths, line numbers

## Troubleshooting

### Subagents Not Being Used Automatically

**Check**:

1. Are you on Max Mode? (Required for legacy plans)
2. Are your prompts specific enough?
3. Is the task complex enough to warrant a subagent?

**Solution**: Explicitly request subagent usage:

```
"Use the [subagent-name] to [task]"
```

### Subagents Taking Too Long

**Reason**: Subagents gather their own context, which adds latency

**Solution**:

- For quick tasks, use main agent directly
- Subagents are optimized for complex, long-running tasks

### Too Many Subagents Running

**Reason**: Parallel execution multiplies token usage

**Solution**:

- Be selective about when to use subagents
- Use main agent for simple tasks
- See `.cursor/rules/subagent-usage.mdc` for guidance

## Advanced Configuration

### Custom Subagent Prompts

You can customize subagent behavior by editing files in `.cursor/agents/`:

1. Open the subagent file (e.g., `.cursor/agents/codebase-explorer.md`)
2. Modify the prompt or capabilities
3. Save the file
4. Cursor will use the updated subagent automatically

### Integration with Commands

Commands can be configured to always use specific subagents. See:

- `.cursor/commands/investigate-bug.md` - Example of subagent integration
- `.cursor/commands/server-test-remediation.md` - Example of subagent integration

## Quick Reference

### Available Subagents

| Subagent               | Purpose                    | When to Use                                 |
| ---------------------- | -------------------------- | ------------------------------------------- |
| `codebase-explorer`    | Deep codebase exploration  | Finding patterns, analyzing architecture    |
| `test-analyzer`        | Test analysis and coverage | Coverage gaps, test quality issues          |
| `security-auditor`     | Security review            | Vulnerability scanning, compliance checks   |
| `performance-profiler` | Performance analysis       | Bottlenecks, optimization opportunities     |
| `bug-investigator`     | Bug investigation          | Systematic bug analysis, root cause finding |

### Quick Commands

```
# Explicit subagent invocation
"Use codebase-explorer to find all Player implementations"
"Run security-auditor on auth module"
"Use test-analyzer to check coverage"

# Commands that use subagents
@investigate-bug
@server-test-remediation
@client-test-remediation
```

## References

- Subagent Documentation: `docs/CURSOR_SUBAGENTS.md`
- Usage Guidelines: `.cursor/rules/subagent-usage.mdc`
- Workflow Examples: `docs/CURSOR_WORKFLOWS.md`
- CLI Usage: `docs/CURSOR_CLI.md`

## Notes

- Subagents are automatically discovered - no manual configuration needed
- Cursor decides when to use subagents based on task complexity
- You can always explicitly request subagent usage
- Commands provide convenient wrappers for common subagent workflows
- Rules provide guidance on optimal subagent usage
