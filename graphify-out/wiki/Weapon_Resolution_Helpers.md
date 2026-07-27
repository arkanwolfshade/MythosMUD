# Weapon Resolution Helpers

> 19 nodes · cohesion 0.01

## Key Concepts

- **Any** (30 connections) — `server/container/bundles/game.py`
- **datetime** (29 connections) — `server/container/bundles/game.py`
- **Exception** (28 connections) — `server/container/bundles/game.py`
- **Any** (14 connections) — `server/game/skill_service.py`
- **UUID** (12 connections) — `server/game/skill_service.py`
- **datetime** (7 connections) — `server/time/tick_scheduler.py`
- **HolidayResolver** (5 connections) — `server/time/tick_scheduler.py`
- **ItemInstance** (4 connections) — `server/game/items/item_factory.py`
- **get_skill_repository()** (4 connections) — `server/dependencies.py`
- **Any** (4 connections) — `server/game/items/item_factory.py`
- **Any** (4 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Any** (3 connections) — `server/game/items/prototype_registry.py`
- **Any** (3 connections) — `server/game/weapons.py`
- **Any** (3 connections) — `server/persistence/repositories/skill_repository.py`
- **Namespace** (3 connections) — `server/scripts/validate_prototypes.py`
- **Path** (2 connections) — `server/game/items/prototype_registry.py`
- **Get a SkillRepository instance for skills catalog queries.      Used by GET /v1/** (1 connections) — `server/dependencies.py`
- **Any** (1 connections) — `server/game/items/component_hooks.py`
- **Any** (1 connections) — `server/game/items/item_instance.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/dependencies.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`
- `server/game/skill_service.py`
- `server/game/weapons.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/scripts/validate_prototypes.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 42 (27%)
- INFERRED: 116 (73%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*