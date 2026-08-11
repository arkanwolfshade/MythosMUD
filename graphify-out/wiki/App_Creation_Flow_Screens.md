# App Creation Flow Screens

> 19 nodes

## Key Concepts

- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **.validate_item_type()** (2 connections) — `server/game/items/models.py`
- **.validate_flags()** (2 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (2 connections) — `server/game/items/models.py`
- **.validate_effect_components()** (2 connections) — `server/game/items/models.py`
- **.validate_tags()** (2 connections) — `server/game/items/models.py`
- **BaseModel** (1 connections)
- **Validated representation of an item prototype definition.      This model keeps** (1 connections) — `server/game/items/models.py`
- **Validate that item_type is in the allowed list.          Args:             value** (1 connections) — `server/game/items/models.py`
- **Validate that all flags are in the allowed list.          Args:             valu** (1 connections) — `server/game/items/models.py`
- **Validate that all wear slots are in the allowed list.          Args:** (1 connections) — `server/game/items/models.py`
- **Validate and normalize effect components.          Args:             value: The** (1 connections) — `server/game/items/models.py`
- **Validate and normalize tags.          Args:             value: The list of tags** (1 connections) — `server/game/items/models.py`
- **Find all prototypes that have a specific tag.          Args:             tag:** (1 connections) — `server/game/items/prototype_registry.py`
- **Get all prototypes in the registry.          Returns:             Iterable[It** (1 connections) — `server/game/items/prototype_registry.py`
- **Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade).** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (8 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (6 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (2 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/tests/integration/test_combat_weapon_resolution.py`

## Audit Trail

- EXTRACTED: 49 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*