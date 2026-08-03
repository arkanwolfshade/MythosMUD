# player respawn event

> 72 nodes

## Key Concepts

- **MagicService** (57 connections) — `server/game/magic/magic_service.py`
- **test_magic_service.py** (47 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **CastingStateManager** (27 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (26 connections)
- **casting_state_manager.py** (10 connections) — `server/game/magic/casting_state_manager.py`
- **test_casting_state_manager.py** (10 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (8 connections)
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.start_casting()** (5 connections) — `server/game/magic/casting_state_manager.py`
- **test_can_cast_spell_unknown_and_materials()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_material_consume_failure()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_casting_progress_completes()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_in_combat()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_value_error()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.interrupt_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **_build_magic_service()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_can_cast_spell_paths()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_delayed()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_pass()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_fail()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_complete_casting_via_combat_queue()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **.is_casting()** (3 connections) — `server/game/magic/casting_state_manager.py`
- *... and 47 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (20 shared connections)
- [game models player](game_models_player.md) (14 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (9 shared connections)
- [magic completion game](magic_completion_game.md) (8 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [subject nats manager](subject_nats_manager.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [player service game](player_service_game.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 346 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*