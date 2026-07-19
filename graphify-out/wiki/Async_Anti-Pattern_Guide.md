# Async Anti-Pattern Guide

> 29 nodes · cohesion 0.07

## Key Concepts

- **❌ NEVER DO THIS → ✅ DO THIS INSTEAD** (9 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **8. Mixing Sync and Async Code** (5 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **1. Blocking the Event Loop** (4 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **2. Using asyncio.run() Incorrectly** (4 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **5. Not Using asyncio.gather() Properly** (4 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **3. F-String Logging (Destroys Structured Logging)** (3 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **4. Missing Exception Handling in Async Code** (3 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **6. Resource Leaks (Not Closing Async Resources)** (3 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **7. Not Using Async Context Managers** (3 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Make the function async** (2 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Async all the way** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Async context managers** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Concurrent with return_exceptions=True** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Fire-and-forget with proper error handling** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Proper cleanup** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Proper exception handling** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Structured key-value pairs** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Thread pool for blocking operations** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **✅ CORRECT - Use asyncio.to_thread() if you must call sync from async** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - asyncio.run() in library code** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - Calling async from sync without care** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - Concurrent but one failure cancels all** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - F-strings destroy structured logging** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - Manual resource management** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- **❌ WRONG - Pool never closed** (1 connections) — `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`
- *... and 4 more nodes in this community*

## Relationships

- [[Async Anti Patterns]] (1 shared connections)

## Source Files

- `docs/ASYNC_ANTI_PATTERNS_QUICK_REF.md`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
