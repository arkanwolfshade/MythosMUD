# MapView GameClientV2ContainerView Tabbed

> 57 nodes

## Key Concepts

- **PrototypeRegistry** (41 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (26 connections) — `server/game/items/prototype_registry.py`
- **prototype_registry.py** (22 connections) — `server/game/items/prototype_registry.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **test_prototype_registry.py** (17 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **models.py** (9 connections) — `server/game/items/models.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **registry_with_switchblade()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_get_returns_prototype()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- *... and 32 more nodes in this community*

## Relationships

- [connection cleaner realtime](connection_cleaner_realtime.md) (18 shared connections)
- [schedule service services](schedule_service_services.md) (15 shared connections)
- [tick service services](tick_service_services.md) (12 shared connections)
- [services service phantom](services_service_phantom.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (6 shared connections)
- [stats game generator](stats_game_generator.md) (5 shared connections)
- [attack combat commands](attack_combat_commands.md) (3 shared connections)
- [room cache services](room_cache_services.md) (2 shared connections)
- [player realtime event](player_realtime_event.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_prototype_registry.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 260 (88%)
- INFERRED: 37 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*