# server game magic casting state

> 82 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **test_magic_service.py** (48 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **asyncio** (19 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **test_can_cast_spell_unknown_and_materials()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_material_consume_failure()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_casting_progress_completes()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_value_error()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_can_cast_spell_paths()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_delayed()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_complete_casting_via_combat_queue()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_fail()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_pass()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [server game magic spell materials](server_game_magic_spell_materials.md) (29 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (19 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (9 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (9 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server events combat events](server_events_combat_events.md) (4 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (4 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (3 shared connections)
- [server dependencies](server_dependencies.md) (2 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 244 (83%)
- INFERRED: 51 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*