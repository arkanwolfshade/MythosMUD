# server game magic spell learning

> 45 nodes

## Key Concepts

- **SpellLearningService** (40 connections) — `server/game/magic/spell_learning_service.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_learning_service.py** (16 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (12 connections)
- **asyncio** (11 connections)
- **UUID** (10 connections)
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **._load_spell_learn_context()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **._check_required_spell_prerequisites()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._persist_spell_learning()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._apply_mythos_corruption_on_learn()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_intelligence_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_power_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._spell_learn_success_response()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **._resolve_spell()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **learning_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_increase_mastery_on_cast()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_already_known()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_no_spell_id()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_with_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- *... and 20 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (11 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [leveluphook](leveluphook.md) (2 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (2 shared connections)
- [server api players](server_api_players.md) (2 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server commands magic commands](server_commands_magic_commands.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server api character creation](server_api_character_creation.md) (1 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 118 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*