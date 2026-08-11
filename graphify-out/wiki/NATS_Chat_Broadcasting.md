# NATS Chat Broadcasting

> 135 nodes

## Key Concepts

- **NATSMessageHandler** (77 connections) — `server/realtime/nats_message_handler.py`
- **Any** (28 connections)
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._send_messages_to_players()** (8 connections) — `server/realtime/nats_message_handler.py`
- **apply_communication_dampening()** (8 connections) — `server/services/lucidity_communication_dampening.py`
- **._subscribe_to_subject()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (7 connections) — `server/realtime/nats_message_handler.py`
- **UUID** (7 connections)
- **._apply_dampening_and_send_message()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_lucidity_tier()** (7 connections) — `server/realtime/nats_message_handler.py`
- **lucidity_communication_dampening.py** (7 connections) — `server/services/lucidity_communication_dampening.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._broadcast_by_channel_type()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._echo_message_to_sender()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.unsubscribe_from_subzone()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._process_message_with_retry()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_message_fields()** (4 connections) — `server/realtime/nats_message_handler.py`
- *... and 110 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Dead Letter Queue](Dead_Letter_Queue.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Circuit Breaker Core](Circuit_Breaker_Core.md) (2 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (2 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (2 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [Vim Editor Guidelines](Vim_Editor_Guidelines.md) (1 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 427 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*