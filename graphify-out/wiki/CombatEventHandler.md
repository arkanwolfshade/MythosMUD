# CombatEventHandler

> 29 nodes

## Key Concepts

- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **test_combat_event_handler.py** (17 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **asyncio** (6 connections)
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
- **Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…** (1 connections) — `server/services/combat_event_handler.py`
- **Award XP to player for defeating an NPC. Args: current_participant: Attacking…** (1 connections) — `server/services/combat_event_handler.py`
- **Publish combat ended event.** (1 connections) — `server/services/combat_event_handler.py`
- *... and 4 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (15 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_handler.py`

## Audit Trail

- EXTRACTED: 63 (81%)
- INFERRED: 15 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*