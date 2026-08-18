# server models combat

> 143 nodes

## Key Concepts

- **models/combat.py** (58 connections) — `server/models/combat.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (38 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **asyncio** (7 connections)
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **fixture** (6 connections)
- **Test validate_and_get_combat_participants returns participants.** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_apply_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 118 more nodes in this community*

## Relationships

- [server models combat combataction](server_models_combat_combataction.md) (30 shared connections)
- [server events combat events](server_events_combat_events.md) (20 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (18 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (15 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (7 shared connections)
- [server services aggro threat clear](server_services_aggro_threat_clear.md) (7 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (7 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (7 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (6 shared connections)
- [server game mechanics](server_game_mechanics.md) (6 shared connections)
- [server events combat events combatendedevent](server_events_combat_events_combatendedevent.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 362 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*