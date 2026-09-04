# Quick Start: Using Cursor Subagents

*"A quick reference for optimal subagent usage in Cursor IDE"*

## Automatic Discovery ✅

**Good News**: Subagents are automatically discovered! No configuration needed.

Cursor automatically finds and uses subagents in `.cursor/agents/` when appropriate.

## Quick Tips for Automatic Usage

### 1. Use Descriptive Prompts

**✅ Good** (triggers subagents automatically):
```
"Find all authentication implementations across the codebase"
"Analyze test coverage gaps in server/tests/unit"
"Perform security audit of authentication module"
"Investigate login bug systematically"
```

**❌ Less Effective**:
```
"Fix bugs"
"Review code"
```

### 2. Explicitly Request Subagents

You can always explicitly request subagent usage:

```
"Use codebase-explorer to find all Player class usages"
"Run security-auditor on server/services/auth.py"
"Use test-analyzer to check coverage"
"Invoke bug-investigator for this login issue"
```

### 3. Use Commands That Leverage Subagents

- `@investigate-bug` → Uses `bug-investigator`
- `@server-test-remediation` → Uses `test-analyzer`
- `@client-test-remediation` → Uses `test-analyzer`

## Available Subagents

| Subagent               | Use For                                  |
| ---------------------- | ---------------------------------------- |
| `codebase-explorer`    | Finding patterns, analyzing architecture |
| `test-analyzer`        | Coverage gaps, test quality              |
| `security-auditor`     | Vulnerabilities, compliance              |
| `performance-profiler` | Bottlenecks, optimization                |
| `bug-investigator`     | Systematic bug analysis                  |

## When Subagents Are Used Automatically

✅ Complex, multi-step tasks
✅ Deep research across multiple files
✅ Specialized analysis (security, performance, testing)
✅ Tasks requiring context isolation

❌ Simple, single-purpose tasks (use main agent)
❌ Quick file operations (use main agent)
❌ Tasks completing in one shot (use main agent)

## Settings Check

1. **Max Mode**: Enable if on legacy plan (usage-based plans have it by default)
2. **Agent Mode**: Set to "Auto" or "Always On"
3. **Model**: Use GPT-4, Claude Sonnet 4.5, or other subagent-capable models

## Need More Help?

- Full Setup Guide: `docs/CURSOR_SETUP_GUIDE.md`
- Subagent Details: `docs/CURSOR_SUBAGENTS.md`
- Usage Guidelines: `.cursor/rules/subagent-usage.mdc`
- Workflow Examples: `docs/CURSOR_WORKFLOWS.md`
