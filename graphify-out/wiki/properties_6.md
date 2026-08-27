# properties

> 37 nodes

## Key Concepts

- **CombatEventHandler** (29 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (20 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **asyncio** (9 connections)
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **test_handle_attack_events_and_xp_phantom_target_no_xp()** (5 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_skips_phantom_attacker()** (5 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_skips_phantom_target()** (5 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **.award_xp_to_player()** (4 connections) — `server/services/combat_event_handler.py`
- **._calculate_xp_reward()** (4 connections) — `server/services/combat_event_handler.py`
- **.publish_combat_ended_event()** (4 connections) — `server/services/combat_event_handler.py`
- **._resolve_participant_display_name()** (4 connections) — `server/services/combat_event_handler.py`
- **test_award_xp_to_player()** (4 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_handle_attack_events_and_xp_npc_death()** (4 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_no_publisher()** (4 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_attack_events_player_target()** (4 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_event_handler.py`
- **test_calculate_xp_reward_default()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_combat_ended_event()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_resolve_participant_display_name_npc_fallback()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_resolve_participant_display_name_npc_from_lifecycle()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_resolve_participant_display_name_player()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **Any** (1 connections)
- *... and 12 more nodes in this community*

## Relationships

- [.get_instance](get_instance.md) (11 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (6 shared connections)
- [MythosMUDError](MythosMUDError.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 84 (86%)
- INFERRED: 14 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*