# test_event_bus_lifecycle.py

> 68 nodes · cohesion 0.05

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **UUID** (8 connections)
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **spell_targeting_service()** (5 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- *... and 43 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (19 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (16 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (14 shared connections)
- [RoomService](RoomService.md) (7 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (6 shared connections)
- [test_item.py](test_item.py.md) (6 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [endpoints.py](endpoints.py.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 190 (87%)
- INFERRED: 29 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*