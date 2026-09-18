# Community 519

> 33 nodes

## Key Concepts

- **CombatEventHandler** (30 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (19 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **asyncio** (9 connections)
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
- **Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…** (1 connections) — `server/services/combat_event_handler.py`
- **Award XP to player for defeating an NPC. Args: current_participant: Attacking…** (1 connections) — `server/services/combat_event_handler.py`
- *... and 8 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (10 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (8 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (3 shared connections)
- [Community 46](Community_46.md) (2 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (1 shared connections)
- [Community 275](Community_275.md) (1 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 73 (83%)
- INFERRED: 15 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*