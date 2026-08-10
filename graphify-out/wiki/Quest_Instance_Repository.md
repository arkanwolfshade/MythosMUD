# Quest Instance Repository

> 18 nodes

## Key Concepts

- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **constants.py** (2 connections) — `server/game/items/constants.py`
- **Constants supporting item prototype validation.  These enumerations anchor the s** (1 connections) — `server/game/items/constants.py`
- **Pydantic models for item prototype validation.  This module defines the ItemProt** (1 connections) — `server/game/items/models.py`
- **Exception** (1 connections)
- **Prototype registry for managing item prototypes.  This module provides the Pro** (1 connections) — `server/game/items/prototype_registry.py`
- **Raised when prototype registry lookups fail.** (1 connections) — `server/game/items/prototype_registry.py`
- **Namespace** (1 connections)
- **CLI entrypoint for validating MythosMUD item prototype definitions.** (1 connections) — `server/scripts/validate_prototypes.py`
- **When prototype is not found, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When registry.get raises PrototypeRegistryError, returns None.** (1 connections) — `server/tests/unit/game/test_weapons.py`

## Relationships

- [Commands Inventory Display](Commands_Inventory_Display.md) (10 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (7 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (6 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (4 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (3 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (2 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (2 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 74 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*