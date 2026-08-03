# magic completion game

> 58 nodes

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **SpellMaterialsService** (17 connections) — `server/game/magic/spell_materials.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **UUID** (12 connections)
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- *... and 33 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (15 shared connections)
- [player service game](player_service_game.md) (14 shared connections)
- [game models player](game_models_player.md) (13 shared connections)
- [player respawn event](player_respawn_event.md) (8 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [subject nats manager](subject_nats_manager.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`

## Audit Trail

- EXTRACTED: 237 (87%)
- INFERRED: 34 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*