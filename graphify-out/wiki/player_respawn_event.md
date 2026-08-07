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

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (18 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (14 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (8 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (7 shared connections)
- [room occupant manager](room_occupant_manager.md) (5 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [subject nats manager](subject_nats_manager.md) (2 shared connections)
- [npc combat player](npc_combat_player.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)

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