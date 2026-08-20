# test_spell_effects.py

> 96 nodes

## Key Concepts

- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **asyncio** (29 connections)
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_process_effect_flee_not_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_effects.py`
- **spell_effects()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_to_npc_success()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_to_npc_unavailable()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_spell_effects_init_with_repository()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_apply_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_npc_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_target_match()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_corruption_adjust_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_create_object_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_corruption_adjust()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_create_object()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_damage()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_flee_services_not_configured()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_heal()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_lucidity_adjust()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 71 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (37 shared connections)
- [SpellEffectType](SpellEffectType.md) (11 shared connections)
- [magic_service.py](magic_service.py.md) (8 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 194 (86%)
- INFERRED: 31 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*