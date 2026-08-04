# models profession rationale

> 10 nodes

## Key Concepts

- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **test_handle_follow_response_invalid_request_id()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_no_container()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_accept_success()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_decline()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Handle follow_response message (accept/decline follow request).** (1 connections) — `server/realtime/message_handlers.py`
- **Test follow_response without request_id returns error.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test follow_response when follow service unavailable.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test follow_response accept notifies requestor.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test follow_response decline notifies requestor.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`

## Relationships

- [manager subject services](manager_subject_services.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (1 shared connections)
- [game chat moderation](game_chat_moderation.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*