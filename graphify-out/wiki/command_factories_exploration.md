# command factories exploration

> 58 nodes

## Key Concepts

- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatTurnAdvancedEvent** (7 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (7 connections) — `server/events/combat_events.py`
- **.publish_combat_turn_advanced()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (4 connections) — `server/services/combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **combat_event_publisher()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_not_connected()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_nats_service()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_subject_manager()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_not_connected()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_attacked_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_took_damage_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_npc_died_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_turn_advanced_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_timeout_success()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **mock_nats_service()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **mock_subject_manager()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_init()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_create_event_message()** (2 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 33 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (22 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 153 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*