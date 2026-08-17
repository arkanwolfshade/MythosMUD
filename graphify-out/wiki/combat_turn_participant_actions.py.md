# combat_turn_participant_actions.py

> 39 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_player_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_skip_for_casting()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (4 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **asyncio** (3 connections)
- **UUID** (2 connections)
- **MonkeyPatch** (1 connections)
- **Return current target participant_id for this NPC, or None.** (1 connections) — `server/services/aggro_threat.py`
- **NPC and player turn execution for combat auto-progression. Extracted from…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve damage and damage_type for a player auto-attack from equipped main_hand…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Return False if we should return early (missing participant_id or cannot act).** (1 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 14 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (18 shared connections)
- [CombatInstance](CombatInstance.md) (9 shared connections)
- [CombatService](CombatService.md) (9 shared connections)
- [models/combat.py](models-combat.py.md) (9 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (7 shared connections)
- [_weapon_damage_from_equipped_player](_weapon_damage_from_equipped_player.md) (6 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 122 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*