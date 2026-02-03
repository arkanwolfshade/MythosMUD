---
name: mythosmud-full-stack-feature
description: Implement MythosMUD features across the full stack: client (React/TypeScript), server (FastAPI/Pydantic), and persistence (PostgreSQL). Use when the user asks to implement a feature, add an endpoint, or build a new capability.
---

# MythosMUD Full-Stack Feature

## Principle

When implementing a feature, implement the **entire stack**: client, server, and persistence (where applicable).

## Checklist

- [ ] **API / server:** Routes, request/response models (Pydantic), business logic. Location: `server/`
- [ ] **Persistence:** Schema changes, migrations, repositories if needed. PostgreSQL only; see [mythosmud-database-placement](.cursor/skills/mythosmud-database-placement). Location: `db/`, `server/`
- [ ] **Client:** UI, hooks, API calls, types. Location: `client/`
- [ ] **Terminology:** Use "coordinator" or "controller," not "master"; use "agent," not "slave"

## Stack Summary

| Layer | Tech | Notes |
|-------|------|-------|
| Client | React 18+, TypeScript | `client/` |
| API | FastAPI, Pydantic | `server/` |
| Data | PostgreSQL | No SQLite; no `*.db` without permission |

## When to Touch Each Layer

- **New endpoint:** Server route + Pydantic models; client API function + types; optionally OpenAPI regen (see mythosmud-openapi-workflow).
- **New screen or flow:** Client components + server endpoints + persistence if data is stored.
- **New persisted entity:** DB schema/migrations, server repository and models, client types and UI.

## Reference

- Full rule: [CLAUDE.md](../../CLAUDE.md) "Implement the entire stack: client, server, and persistence"
- Terminology: [CLAUDE.md](../../CLAUDE.md) and user rules: coordinator/agent, not master/slave
- Database: [mythosmud-database-placement](../mythosmud-database-placement/SKILL.md)
