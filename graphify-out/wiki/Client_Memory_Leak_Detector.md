# Client Memory Leak Detector

> 53 nodes · cohesion 0.06

## Key Concepts

- **MemoryMonitor** (26 connections) — `client/src/utils/memoryMonitor.ts`
- **MemoryLeakDetector** (16 connections) — `client/src/utils/memoryLeakDetector.ts`
- **memoryMonitor.ts** (11 connections) — `client/src/utils/memoryMonitor.ts`
- **memoryLeakDetector.ts** (8 connections) — `client/src/utils/memoryLeakDetector.ts`
- **memoryLeakDetector.test.ts** (7 connections) — `client/src/utils/__tests__/memoryLeakDetector.test.ts`
- **memoryMonitor.test.ts** (7 connections) — `client/src/utils/__tests__/memoryMonitor.test.ts`
- **MemorySnapshot** (7 connections) — `client/src/utils/memoryLeakDetector.ts`
- **useMemoryMonitor()** (6 connections) — `client/src/utils/memoryMonitor.ts`
- **.generateReport()** (5 connections) — `client/src/utils/memoryMonitor.ts`
- **.calculateGrowthRate()** (3 connections) — `client/src/utils/memoryLeakDetector.ts`
- **.detectMemoryLeak()** (3 connections) — `client/src/utils/memoryLeakDetector.ts`
- **.getOverallStats()** (3 connections) — `client/src/utils/memoryMonitor.ts`
- **.registerComponent()** (3 connections) — `client/src/utils/memoryMonitor.ts`
- **.checkMemory()** (2 connections) — `client/src/utils/memoryLeakDetector.ts`
- **.getMemoryStats()** (2 connections) — `client/src/utils/memoryLeakDetector.ts`
- **useMemoryLeakDetector()** (2 connections) — `client/src/utils/memoryLeakDetector.ts`
- **.addReport()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.constructor()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.getComponentStats()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.getInstance()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.getMemorySummary()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.getResourceStats()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.handleComponentMemoryCritical()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.handleComponentMemoryWarning()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- **.handleMemoryCritical()** (2 connections) — `client/src/utils/memoryMonitor.ts`
- *... and 28 more nodes in this community*

## Relationships

- [[Client App State Hooks]] (4 shared connections)
- [[Game Client Container]] (3 shared connections)

## Source Files

- `client/src/utils/__tests__/memoryLeakDetector.test.ts`
- `client/src/utils/__tests__/memoryMonitor.test.ts`
- `client/src/utils/memoryLeakDetector.ts`
- `client/src/utils/memoryMonitor.ts`

## Audit Trail

- EXTRACTED: 161 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
