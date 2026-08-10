# Cursor Plans Follow

> 6 nodes

## Key Concepts

- **TestGetChatService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_chat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_chat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_chat_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_chat_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_chat_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*