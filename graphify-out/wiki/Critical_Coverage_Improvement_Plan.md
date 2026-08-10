# Critical Coverage Improvement Plan

> 12 nodes

## Key Concepts

- **MapPerformanceMonitor** (8 connections) — `client/src/components/map/utils/performance.ts`
- **performance.ts** (6 connections) — `client/src/components/map/utils/performance.ts`
- **performance.test.ts** (4 connections) — `client/src/components/map/__tests__/performance.test.ts`
- **debounce()** (4 connections) — `client/src/components/map/utils/performance.ts`
- **throttle()** (2 connections) — `client/src/components/map/utils/performance.ts`
- **.getAverageRenderTime()** (2 connections) — `client/src/components/map/utils/performance.ts`
- **.getStats()** (2 connections) — `client/src/components/map/utils/performance.ts`
- **isInViewport()** (1 connections) — `client/src/components/map/utils/performance.ts`
- **.startRender()** (1 connections) — `client/src/components/map/utils/performance.ts`
- **.endRender()** (1 connections) — `client/src/components/map/utils/performance.ts`
- **.getFps()** (1 connections) — `client/src/components/map/utils/performance.ts`
- **.reset()** (1 connections) — `client/src/components/map/utils/performance.ts`

## Relationships

- [Command Input Utilities](Command_Input_Utilities.md) (3 shared connections)

## Source Files

- `client/src/components/map/__tests__/performance.test.ts`
- `client/src/components/map/utils/performance.ts`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*