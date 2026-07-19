# User Rules

> 12 nodes · cohesion 0.17

## Key Concepts

- **MANDATORY SERVER RULES** (7 connections) — `USER_RULES.md`
- **USER RULES - CRITICAL SERVER MANAGEMENT** (5 connections) — `USER_RULES.md`
- **USER_RULES.md** (1 connections) — `USER_RULES.md`
- **After running stop_server.ps1, you MUST verify ports are free with netstat** (1 connections) — `USER_RULES.md`
- **ALWAYS use is_background: false for server startup so you can see the output** (1 connections) — `USER_RULES.md`
- **EXISTING RULES (REINFORCED)** (1 connections) — `USER_RULES.md`
- **If start_local.ps1 fails or shows errors, DO NOT run it again -** (1 connections) — `USER_RULES.md`
- **If you need to start a server, you MUST first run ./scripts/stop_server.ps1** (1 connections) — `USER_RULES.md`
- **NEVER use is_background: true for server startup commands** (1 connections) — `USER_RULES.md`
- **Only THEN can you run ./scripts/start_local.ps1 with is_background: false** (1 connections) — `USER_RULES.md`
- **PRIORITY: TOKEN EFFICIENCY OVER SPEED** (1 connections) — `USER_RULES.md`
- **VIOLATION CONSEQUENCES** (1 connections) — `USER_RULES.md`

## Relationships

- No strong cross-community connections detected

## Source Files

- `USER_RULES.md`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
