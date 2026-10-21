# UtilityCommandFactory

> 41 nodes · cohesion 0.07

## Key Concepts

- **test_player_schema_converter_weapon.py** (25 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **_weapon_from_prototype_registry()** (14 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_StubRegistry** (7 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_parses_real_catalog_shape()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_still_returns_none_on_bad_modelled_keys()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **weapon_metadata.py** (3 connections) — `server/tests/fixtures/shared/weapon_metadata.py`
- **_Prototype** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_stats_from_metadata_drops_unmodelled_prototype_keys()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **WeaponStats** (1 connections)
- **Resolve metadata.weapon from prototype registry for a given prototype_id.…** (1 connections) — `server/game/player_schema_converter.py`
- **Build InventoryItem from raw item dict, enriching with weapon stats from…** (1 connections) — `server/game/player_schema_converter.py`
- **Shared weapon prototype metadata fixtures. The real shape of…** (1 connections) — `server/tests/fixtures/shared/weapon_metadata.py`
- **.__init__()** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **asyncio** (1 connections)
- *... and 16 more nodes in this community*

## Relationships

- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (6 shared connections)
- [generate_arkham_grid.py](generate_arkham_grid.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (2 shared connections)
- [test_metrics.py](test_metrics.py.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/tests/fixtures/shared/weapon_metadata.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 73 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*