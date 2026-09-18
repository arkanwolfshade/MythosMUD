# Combat Instance Turn Management

> 259 nodes

## Key Concepts

- **CombatParticipant** (219 connections) — `server/models/combat.py`
- **CombatInstance** (190 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (39 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._create_corpse_on_death()** (10 connections) — `server/services/combat_death_handler.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **asyncio** (7 connections)
- **._cap_damage_for_no_death_room()** (6 connections) — `server/services/combat_attack_handler.py`
- **_player_damage_blocked_by_grace()** (6 connections) — `server/services/combat_attack_handler.py`
- *... and 234 more nodes in this community*

## Relationships

- [Community 81](Community_81.md) (58 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (43 shared connections)
- [Community 264](Community_264.md) (29 shared connections)
- [Community 97](Community_97.md) (23 shared connections)
- [Community 150](Community_150.md) (22 shared connections)
- [Combat Events](Combat_Events.md) (20 shared connections)
- [Community 275](Community_275.md) (19 shared connections)
- [Community 152](Community_152.md) (18 shared connections)
- [Community 257](Community_257.md) (15 shared connections)
- [Community 46](Community_46.md) (15 shared connections)
- [Community 174](Community_174.md) (8 shared connections)
- [Community 519](Community_519.md) (8 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 768 (96%)
- INFERRED: 30 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*