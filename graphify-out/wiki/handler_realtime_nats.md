# handler realtime nats

> 16 nodes

## Key Concepts

- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_room()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_active_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_event_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.is_event_subscription_active()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Mixin: room, subzone, and event NATS subscription lifecycle.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to chat messages for a specific room.          Args:             room_** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active subscriptions.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get list of active subscription subjects.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to all event-related NATS subjects using standardized patterns.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Unsubscribe from all event-related NATS subjects using standardized patterns.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active event subscriptions.          Returns:             Numb** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Check if a specific event subscription is active.          Args:             sub** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [persistence services combat](persistence_services_combat.md) (6 shared connections)
- [schemas players profession](schemas_players_profession.md) (3 shared connections)
- [quests players rationale](quests_players_rationale.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)
- [invite models generate](invite_models_generate.md) (1 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [invite models create](invite_models_create.md) (1 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*