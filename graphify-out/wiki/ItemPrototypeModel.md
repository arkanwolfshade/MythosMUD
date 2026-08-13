# ItemPrototypeModel

> 18 nodes

## Key Concepts

- **ItemPrototypeModel** (22 connections) — `server/game/items/models.py`
- **field_validator** (5 connections)
- **.validate_effect_components()** (3 connections) — `server/game/items/models.py`
- **.validate_flags()** (3 connections) — `server/game/items/models.py`
- **.validate_item_type()** (3 connections) — `server/game/items/models.py`
- **.validate_tags()** (3 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (3 connections) — `server/game/items/models.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **BaseModel** (1 connections)
- **Validate and normalize effect components. Args: value: The list of effect…** (1 connections) — `server/game/items/models.py`
- **Validate and normalize tags. Args: value: The list of tags to validate Returns:…** (1 connections) — `server/game/items/models.py`
- **Validated representation of an item prototype definition. This model keeps the…** (1 connections) — `server/game/items/models.py`
- **Validate that item_type is in the allowed list. Args: value: The item type to…** (1 connections) — `server/game/items/models.py`
- **Validate that all flags are in the allowed list. Args: value: The list of flags…** (1 connections) — `server/game/items/models.py`
- **Validate that all wear slots are in the allowed list. Args: value: The list of…** (1 connections) — `server/game/items/models.py`
- **Find all prototypes that have a specific tag. Args: tag: The tag to search for…** (1 connections) — `server/game/items/prototype_registry.py`
- **Get all prototypes in the registry. Returns: Iterable[ItemPrototypeModel]: An…** (1 connections) — `server/game/items/prototype_registry.py`

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (2 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (2 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (2 shared connections)
- [registry_with_switchblade](registry_with_switchblade.md) (1 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`

## Audit Trail

- EXTRACTED: 33 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*