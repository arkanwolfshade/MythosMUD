# commands communication say

> 204 nodes

## Key Concepts

- **NATSError** (105 connections) — `server/services/nats_exceptions.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **UUID** (8 connections)
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **Any** (7 connections)
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **UserManager** (5 connections)
- *... and 179 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (24 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (21 shared connections)
- [models npc rationale](models_npc_rationale.md) (20 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (8 shared connections)
- [nats message handler](nats_message_handler.md) (6 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [services combat sync](services_combat_sync.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (3 shared connections)
- [follow game service](follow_game_service.md) (3 shared connections)
- [room validator path](room_validator_path.md) (3 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 632 (88%)
- INFERRED: 85 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*