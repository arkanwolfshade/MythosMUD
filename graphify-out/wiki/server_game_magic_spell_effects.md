# server game magic spell effects

> 82 nodes

## Key Concepts

- **SpellEffects** (52 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **asyncio** (29 connections)
- **PlayerSpellRepository** (28 connections) — `server/persistence/repositories/player_spell_repository.py`
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
- **test_process_effect_stat_modify()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 57 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (45 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (13 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (13 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (6 shared connections)
- [server game skill service](server_game_skill_service.md) (6 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (2 shared connections)
- [server api players](server_api_players.md) (2 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (2 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (2 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 196 (79%)
- INFERRED: 51 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*