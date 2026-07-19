# Memory Leak Audit

> 21 nodes · cohesion 0.10

## Key Concepts

- **Findings by Category** (8 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **1. Connection Management Leaks** (4 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **2. Event System Leaks** (3 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **3. Async Task and Background Task Leaks** (3 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **4. Cache and In-Memory Data Structure Leaks** (3 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **5. Client-Side Memory Leaks** (3 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **6. File Handle and I/O Leaks** (2 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **7. Circular Reference Leaks** (2 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **1.1 Database Connection Pools** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **1.2 WebSocket Connection Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **1.3 NATS Connection and Subscription Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **2.1 EventBus Subscriber Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **2.2 Client-Side Event Handler Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **3.1 Task Registry Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **3.2 Background Service Task Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **4.1 LRU Cache Growth** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **4.2 Dictionary and Set Growth** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **5.1 React Hook Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **5.2 Zustand Store Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **6.1 File Handle Leaks** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **7.1 Object Reference Cycles** (1 connections) — `docs/MEMORY_LEAK_AUDIT_REPORT.md`

## Relationships

- [[Memory Leak Audit]] (1 shared connections)

## Source Files

- `docs/MEMORY_LEAK_AUDIT_REPORT.md`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
