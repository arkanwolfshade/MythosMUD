# server app lifespan magic

> 66 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- **_validate_magic_prerequisites()** (6 connections) — `server/container/bundles/magic.py`
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **test_magic_bundle_create_registry_and_targeting()** (4 connections) — `server/tests/unit/container/test_container_bundles.py`
- **.connection_manager()** (3 connections) — `server/game/magic/spell_effects.py`
- *... and 41 more nodes in this community*

## Relationships

- [server game magic spell materials](server_game_magic_spell_materials.md) (17 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (15 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (14 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (12 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (12 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (9 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (4 shared connections)
- [server game magic mp regeneration](server_game_magic_mp_regeneration.md) (4 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (4 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (4 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/container/bundles/magic.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 207 (89%)
- INFERRED: 26 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*