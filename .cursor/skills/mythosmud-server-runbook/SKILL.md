---
name: mythosmud-server-runbook
description: Follow MythosMUD server lifecycle: stop before start, verify ports 54731 and 5173, run stop script then start_local.ps1 once. Use when starting/stopping the server, debugging port conflicts, or when the user mentions server startup or 'Press any key to exit'.
---

# MythosMUD Server Runbook

## ONE SERVER ONLY RULE

**THERE CAN ONLY BE ONE SERVER RUNNING AT ANY TIME.**

Before starting a server, always stop first and verify ports are free. Never start a second instance.

## Pre-Start Checklist

Copy and follow before any server start:

```
- [ ] Run stop script: ./scripts/stop_server.ps1
- [ ] Verify port 54731 free: netstat -an | findstr :54731
- [ ] Verify port 5173 free: netstat -an | findstr :5173
- [ ] Do NOT use is_background: true for server startup
- [ ] Run start once: ./scripts/start_local.ps1 (is_background: false)
- [ ] If output shows "Press any key to exit", server is running — do NOT start again
```

## Commands

| Action | Command |
|--------|---------|
| Stop first | `./scripts/stop_server.ps1` |
| Check API port | `netstat -an | findstr :54731` |
| Check dev server port | `netstat -an | findstr :5173` |
| Start (once only) | `./scripts/start_local.ps1` |

## Critical Rules

- **Never** use `is_background: true` for server startup. Use `is_background: false` so output is visible.
- **Never** run `start_local.ps1` again if the terminal already shows "Press any key to exit."
- If startup fails, do not run start again — investigate the error first.

## Reference

- Full rules: project root [CLAUDE.md](../../CLAUDE.md) "ONE SERVER ONLY RULE" and "MANDATORY SERVER STARTUP PROCEDURE"
- Rule file: [.cursor/rules/serverstart.mdc](../../rules/serverstart.mdc)
- Scripts: [scripts/stop_server.ps1](../../scripts/stop_server.ps1), [scripts/start_local.ps1](../../scripts/start_local.ps1)
