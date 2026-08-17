# server app lifespan magic

> 54 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (26 connections) — `server/game/magic/spell_registry.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **.connection_manager()** (3 connections) — `server/game/magic/spell_effects.py`
- **.get_spell()** (3 connections) — `server/game/magic/spell_registry.py`
- **.get_spell_by_name()** (3 connections) — `server/game/magic/spell_registry.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_registry.py`
- **.search_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/spell_repository.py`
- *... and 29 more nodes in this community*

## Relationships

- [server container bundles chat](server_container_bundles_chat.md) (13 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (13 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (7 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (7 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (3 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (3 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (3 shared connections)
- [server game magic mp regeneration](server_game_magic_mp_regeneration.md) (3 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/spell_repository.py`

## Audit Trail

- EXTRACTED: 152 (88%)
- INFERRED: 20 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*