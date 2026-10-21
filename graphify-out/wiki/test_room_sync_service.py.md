# test_room_sync_service.py

> 88 nodes · cohesion 0.04

## Key Concepts

- **PrototypeRegistry** (63 connections) — `server/game/items/prototype_registry.py`
- **prototype_registry.py** (27 connections) — `server/game/items/prototype_registry.py`
- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **test_prototype_registry.py** (17 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_room_furniture_persistence.py** (13 connections) — `server/tests/integration/test_room_furniture_persistence.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_furniture_container_created_once_then_refreshed_in_place()** (10 connections) — `server/tests/integration/test_room_furniture_persistence.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **_prototype_from_equipped_stack()** (6 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (6 connections) — `server/tests/unit/game/test_weapons.py`
- **._record_validation_failure()** (5 connections) — `server/game/items/prototype_registry.py`
- **_registry()** (5 connections) — `server/tests/integration/test_room_furniture_persistence.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Path** (5 connections)
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **Any** (4 connections)
- *... and 63 more nodes in this community*

## Relationships

- [items/catalog_dml.py](items-catalog_dml.py.md) (26 shared connections)
- [test_metrics.py](test_metrics.py.md) (17 shared connections)
- [useGameClientV2ContainerNetworkPhase.ts](useGameClientV2ContainerNetworkPhase.ts.md) (15 shared connections)
- [Room](Room.md) (8 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (7 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/integration/test_room_furniture_persistence.py`
- `server/tests/unit/game/items/test_prototype_registry.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 206 (80%)
- INFERRED: 50 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*