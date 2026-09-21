# TargetResolutionService

> 90 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- *... and 65 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (22 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (12 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [SpellEffectType](SpellEffectType.md) (8 shared connections)
- [SpellRegistry](SpellRegistry.md) (7 shared connections)
- [magic_service.py](magic_service.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_targeting.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 254 (87%)
- INFERRED: 38 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*