# NATS Retry Handler

> 76 nodes

## Key Concepts

- **PrototypeRegistry** (37 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **item_factory.py** (14 connections) — `server/game/items/item_factory.py`
- **weapons.py** (14 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **WeaponAttackInfo** (10 connections) — `server/game/weapons.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **_roll_weapon_attack()** (4 connections) — `server/game/weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- *... and 51 more nodes in this community*

## Relationships

- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (13 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (7 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (5 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (5 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (4 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (3 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (2 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/constants.py`
- `server/game/items/item_factory.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 300 (87%)
- INFERRED: 45 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*