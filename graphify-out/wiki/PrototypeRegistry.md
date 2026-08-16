# PrototypeRegistry

> 116 nodes

## Key Concepts

- **PrototypeRegistry** (47 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **prototype_registry.py** (23 connections) — `server/game/items/prototype_registry.py`
- **test_prototype_registry.py** (18 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **test_item_prototype_models.py** (15 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_combat_weapon_resolution.py** (13 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **items/__init__.py** (11 connections) — `server/game/items/__init__.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **_prototype_from_equipped_stack()** (6 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (6 connections) — `server/tests/unit/game/test_weapons.py`
- **.get()** (5 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (5 connections) — `server/game/items/prototype_registry.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- *... and 91 more nodes in this community*

## Relationships

- [PrototypeRegistryError](PrototypeRegistryError.md) (23 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`
- `server/tests/unit/game/items/test_prototype_registry.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 242 (81%)
- INFERRED: 56 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*