# Test Combat Event Handler

> 35 nodes

## Key Concepts

- **CombatEventHandler** (30 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (20 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
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
- **Publish attack events and calculate XP reward. Args: current_participant:…** (1 connections) — `server/services/combat_event_handler.py`
- *... and 10 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (13 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (5 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (3 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (2 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 78 (84%)
- INFERRED: 15 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*