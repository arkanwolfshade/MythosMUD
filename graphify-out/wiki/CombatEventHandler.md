# CombatEventHandler

> 45 nodes

## Key Concepts

- **CombatEventHandler** (33 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (19 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **asyncio** (9 connections)
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **._publish_npc_attacked_event()** (7 connections) — `server/services/combat_event_handler.py`
- **._publish_npc_took_damage_event()** (7 connections) — `server/services/combat_event_handler.py`
- **._publish_player_attacked_event()** (7 connections) — `server/services/combat_event_handler.py`
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
- **Any** (4 connections)
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_event_handler.py`
- **test_calculate_xp_reward_default()** (3 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- *... and 20 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (14 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 116 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*