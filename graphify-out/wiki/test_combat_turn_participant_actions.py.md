# test_combat_turn_participant_actions.py

> 20 nodes

## Key Concepts

- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (4 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **asyncio** (3 connections)
- **MonkeyPatch** (1 connections)
- **Return False if we should return early (missing participant_id or cannot act).** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve target via aggro (ADR-016), then fallback to _select_npc_target.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Process NPC turn with actual combat attack. Args: combat_service: Parent…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Select target for NPC attack. Prefers participants that are not dead (includes…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Unit tests for combat_turn_participant_actions (aggro-aware NPC targeting and…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Happy path: living NPC resolves target and combat_service.process_attack runs.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Player at 0 DP is not is_dead; NPC turn must still select them (ADR-016 / auto…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **When get_npc_current_target resolves an id, that participant is returned if…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **update_aggro may signal a switch; combat service broadcasts room narrative.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [CombatParticipant](CombatParticipant.md) (9 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (8 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (2 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*