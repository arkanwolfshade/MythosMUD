# Any

> 72 nodes

## Key Concepts

- **PrototypeRegistry** (35 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **.load_from_path()** (8 connections) — `server/game/items/prototype_registry.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 47 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (23 shared connections)
- [Any](Any.md) (8 shared connections)
- [combat](combat.md) (6 shared connections)
- [combat attack](combat_attack.md) (3 shared connections)
- [equipment helpers](equipment_helpers.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [init](init.md) (1 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 242 (86%)
- INFERRED: 40 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*