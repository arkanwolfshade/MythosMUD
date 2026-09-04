---
description: "Which of MythosMUD's project-specific agents to delegate to, by user intent (test analysis, bug investigation, security audit, performance, codebase exploration)."
paths:
  - "server/**"
  - "client/**"
---

# Agent Routing

MythosMUD has 5 project-specific agents in `.claude/agents/`. Route to them by intent rather than doing the
work inline when the task is complex/multi-step and benefits from an isolated context window:

| User intent | Agent | File |
|---|---|---|
| Test coverage analysis, test quality review, coverage gaps, test recommendations | Test Suite Analyzer | `test-analyzer.md` |
| Bug investigation, root cause analysis, systematic debugging, evidence collection | Bug Investigator | `bug-investigator.md` |
| Security audit, COPPA check, vulnerability scan, input validation review | Security Auditor | `security-auditor.md` |
| Performance analysis, bottlenecks, optimization, memory/query profiling | Performance Profiler | `performance-profiler.md` |
| Deep codebase exploration, pattern discovery, architecture analysis, dependency research | Codebase Explorer | `codebase-explorer.md` |

For simple, single-purpose, or quick tasks, use the main conversation or a `.claude/commands/` slash command
instead — agent overhead (separate context, startup latency) isn't worth it for anything under a few minutes
of work.

---

*Condensed from `.cursor/rules/subagent-usage.mdc`. The original also covered general subagent-vs-command
tradeoffs and Cursor's built-in Explore/Bash/Browser subagents — dropped here since Claude Code's own agent
routing (the `Agent` tool, `Explore` agent) already handles that judgment natively; the routing table above was
the part specific to this project's agents.*
