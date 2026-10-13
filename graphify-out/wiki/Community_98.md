# Community 98

> 99 nodes

## Key Concepts

- **MessageCategory** (107 connections) — `server/constants/message_category.py`
- **test_combat_status_message_categories.py** (42 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **CombatEventPublisher** (41 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (18 connections) — `server/services/combat_event_publisher.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **asyncio** (13 connections)
- **test_phantom_combat_line_matches_real_npc_category_and_never_mints_its_own()** (9 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_first_awaited_args()** (8 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_sent_personal()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_sent_room()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_attack_categories_follow_each_recipients_perspective()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_state_notices_are_combat_status()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_npc_attacked_and_took_damage_are_combat_hit()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **.publish_combat_started()** (6 connections) — `server/services/combat_event_publisher.py`
- **_dispatched()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_published_data()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_ended_is_combat_status()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_mortally_wounded_lines_are_combat_status_for_both_recipients()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_player_attacked_is_combat_hurt()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_player_death_lines_are_combat_death_for_both_recipients()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **CombatMessagingIntegration** (6 connections)
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_target_switch()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- *... and 74 more nodes in this community*

## Relationships

- [Community 41](Community_41.md) (17 shared connections)
- [Community 66](Community_66.md) (12 shared connections)
- [Community 65](Community_65.md) (12 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 206](Community_206.md) (8 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (8 shared connections)
- [Community 566](Community_566.md) (7 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (7 shared connections)
- [Community 346](Community_346.md) (6 shared connections)
- [Community 87](Community_87.md) (5 shared connections)
- [Community 144](Community_144.md) (5 shared connections)
- [Community 645](Community_645.md) (4 shared connections)

## Source Files

- `server/constants/message_category.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/constants/test_message_category.py`
- `server/tests/unit/services/test_combat_status_message_categories.py`

## Audit Trail

- EXTRACTED: 255 (76%)
- INFERRED: 81 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*