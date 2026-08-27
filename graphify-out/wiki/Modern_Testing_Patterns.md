# Modern Testing Patterns

> 8 nodes

## Key Concepts

- **Top Time Consumers (>10 seconds)** (8 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **Argon2 Password Tests (1.4+ seconds)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **Auth & Security Tests (21+ seconds setup each)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **Infrastructure Tests (3.5+ seconds)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **NATS Message Handler Tests (2-3 seconds)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **Performance Tests (still running despite slow marker)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **Rate Limiter Timing Tests (still running)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`
- **SSE Handler Tests (60 seconds total)** (1 connections) — `docs/archive/TEST_TIMING_ANALYSIS.md`

## Relationships

- [CRITICAL · WebSocket authentication bypass on `/ws`](CRITICAL_·_WebSocket_authentication_bypass_on_`-ws`.md) (1 shared connections)

## Source Files

- `docs/archive/TEST_TIMING_ANALYSIS.md`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*