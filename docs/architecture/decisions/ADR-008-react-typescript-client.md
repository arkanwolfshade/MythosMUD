# ADR-008: React 18+ with TypeScript for Client

**Status:** Accepted
**Date:** 2026-02-02

## Context

MythosMUD's client must render a terminal-like game UI, manage WebSocket connection state, handle real-time game events, and provide a responsive experience. The client communicates with the FastAPI backend via REST (auth) and WebSocket (gameplay). A modern framework with strong typing, component composition, and ecosystem support is needed.

## Decision

Use **React 18+** with **TypeScript** for the client:

- **Framework**: React 18+ with functional components and hooks
- **Language**: TypeScript for type safety and IDE support
- **State**: React hooks (useState, useReducer), Zustand where appropriate
- **Real-time**: Native WebSocket API
- **Build**: Vite for development and production builds
- **Styling**: CSS modules with terminal/retro theme

Components are organized by feature; WebSocket logic centralized in connection hooks. TypeScript interfaces align with server Pydantic models where possible.

## Alternatives Considered

1. **Vue / Svelte** - Rejected: React chosen for team familiarity and ecosystem
2. **Plain JavaScript** - Rejected: TypeScript reduces bugs, improves refactoring, documents contracts
3. **Angular** - Rejected: heavier; React + TypeScript sufficient for SPA scope
4. **Elm / PureScript** - Rejected: less mainstream; hiring and onboarding harder

## Consequences

- **Positive**: Type safety catches errors at compile time; React ecosystem (testing, tooling) mature; hooks simplify stateful logic; Vite provides fast HMR
- **Negative**: TypeScript adds build step and strictness; occasional client/server type drift
- **Neutral**: State management mix (useState vs Zustand) requires conventions; documented in client architecture

## Related ADRs

- ADR-004: WebSocket-Only Real-Time Architecture
- ADR-001: Layered Architecture with Event-Driven Components

## References

- [Real-Time Architecture](../../REAL_TIME_ARCHITECTURE.md)
- [Client Layout Baseline](../../CLIENT_LAYOUT_BASELINE.md)
