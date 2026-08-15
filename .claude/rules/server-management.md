---
paths:
  - "server/**"
  - "client/**"
  - "scripts/start_local.ps1"
  - "scripts/stop_server.ps1"
---

# Server Authority (Critical)

**The server is always authoritative over the client.** If there is a disparity between server state and client
state, the server is assumed to be correct.

## Implications

- **State sync:** Client state must be updated to match server data. Never treat client-held state as the source
  of truth when it conflicts with server responses or events.
- **Conflict resolution:** Prefer server payloads (e.g. `room_state`, `game_state`, command responses) over
  client-inferred or cached state.
- **Debugging:** When behavior differs between client and server, assume the server implementation is correct
  unless proven otherwise; fix client handling or display to align with server.

# CRITICAL SERVER MANAGEMENT RULES

## ONE SERVER ONLY RULE

**THERE CAN ONLY BE ONE SERVER RUNNING AT ANY TIME**

## MANDATORY SERVER STARTUP PROCEDURE

1. **STOP FIRST**: Before starting a server, ALWAYS run `./scripts/stop_server.ps1`
2. **VERIFY PORTS**: After stopping, verify ports are free — check `54768` (server) and `5173` (client)
3. **NO BACKGROUND**: NEVER start the server as a background/detached process
4. **SEE OUTPUT**: Start the server so you can see its output as it comes up
5. **ONE START ONLY**: Run `./scripts/start_local.ps1` exactly ONCE
6. **IF IT SAYS "Press any key to exit"**: The server is running — DO NOT start another

## PRE-COMMAND CHECKLIST

Before running ANY server command, ask yourself:

- Did I already start a server in this session? (YES = STOP, don't start another)
- Am I about to run it detached/backgrounded? (YES = STOP, run it in the foreground instead)
- Did I run `stop_server.ps1` first? (NO = STOP, run it first)
- Am I about to run `start_local.ps1` when I already see "Press any key to exit"? (YES = STOP, server is already running)

See the `mythosmud-server-runbook` skill for the full startup/shutdown workflow.

---

*Ported from `.cursor/rules/server-authority.mdc` and `.cursor/rules/serverstart.mdc` (both always-on in
Cursor; merged here since they're both about server lifecycle). Note this is behavioral guidance triggered by
an ACTION (starting the server), not necessarily by editing a matching file — the path scoping above is an
approximation, not a guarantee this loads before every server start. If you're about to start/stop the server
and aren't sure this rule is in context, follow the ONE-SERVER-ONLY procedure above regardless.*
