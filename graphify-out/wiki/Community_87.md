# Community 87

> 102 nodes

## Key Concepts

- **RealTimeEventHandler** (30 connections) — `server/realtime/event_handler.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **RealtimeBundle** (21 connections) — `server/container/bundles/realtime.py`
- **bundles/realtime.py** (14 connections) — `server/container/bundles/realtime.py`
- **test_realtime_bundle_nats.py** (10 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **.__init__()** (7 connections) — `server/realtime/event_handler.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.connection_manager()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **_config()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_e2e_raises_when_connect_returns_false()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_connect_nats_local_continues_without_nats_on_timeout()** (5 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **._initialize_modules()** (4 connections) — `server/realtime/event_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **test_handle_nats_unavailable_unit_test_soft()** (4 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **asyncio** (4 connections)
- **._create_player_entered_message()** (3 connections) — `server/realtime/event_handler.py`
- *... and 77 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [Community 93](Community_93.md) (5 shared connections)
- [Community 329](Community_329.md) (4 shared connections)
- [Community 80](Community_80.md) (4 shared connections)
- [NATS Configuration](NATS_Configuration.md) (3 shared connections)
- [Community 759](Community_759.md) (3 shared connections)
- [Community 92](Community_92.md) (3 shared connections)
- [Community 200](Community_200.md) (3 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (2 shared connections)
- [Community 211](Community_211.md) (2 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (2 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_handler.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 168 (89%)
- INFERRED: 21 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*