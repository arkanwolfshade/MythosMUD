# server game magic casting state

> 76 nodes

## Key Concepts

- **test_magic_service.py** (48 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **CastingStateManager** (21 connections) — `server/game/magic/casting_state_manager.py`
- **asyncio** (19 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service()** (9 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **test_can_cast_spell_unknown_and_materials()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_material_consume_failure()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_casting_progress_completes()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_value_error()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **StartCastingTarget** (5 connections) — `server/game/magic/casting_state_manager.py`
- **test_can_cast_spell_paths()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_delayed()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_complete_casting_via_combat_queue()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_fail()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_pass()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **fixture** (5 connections)
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- *... and 51 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (18 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (11 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (4 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (3 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (2 shared connections)
- [server commands magic commands](server_commands_magic_commands.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [chatservice](chatservice.md) (1 shared connections)
- [magicservicecompletionmixin](magicservicecompletionmixin.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 177 (76%)
- INFERRED: 55 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*