# NATS Chat Broadcasting

> 20 nodes · cohesion 0.02

## Key Concepts

- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **apply_communication_dampening()** (6 connections) — `server/services/lucidity_communication_dampening.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **_not_configured_async()** (3 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **Any** (2 connections)
- **Start the NATS message handler and subscribe to subjects.          Args:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Stop the NATS message handler and unsubscribe from subjects.          Returns:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns.          This me** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject.          Args:             subject: Sub** (1 connections) — `server/realtime/nats_message_handler.py`
- **Unsubscribe from a specific NATS subject.          Returns:             True** (1 connections) — `server/realtime/nats_message_handler.py`
- **Any** (1 connections)
- **Apply communication dampening based on lucidity tiers.      Args:         messag** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Create a NATSMessageHandler instance.** (1 connections) — `server/tests/unit/realtime/conftest.py`

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (3 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [Realtime Player Event](Realtime_Player_Event.md) (2 shared connections)
- [Connection State Hooks](Connection_State_Hooks.md) (1 shared connections)
- [Contributing Guidelines](Contributing_Guidelines.md) (1 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (1 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 57 (79%)
- INFERRED: 15 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*