# items/catalog_dml.py

> 62 nodes · cohesion 0.06

## Key Concepts

- **ItemPrototypeModel** (60 connections) — `server/game/items/models.py`
- **item_effects.py** (21 connections) — `server/game/items/item_effects.py`
- **test_item_effects.py** (21 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **items/models.py** (18 connections) — `server/game/items/models.py`
- **test_item_prototype_models.py** (13 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **ItemUseContext** (11 connections) — `server/game/items/item_effects.py`
- **find_effect()** (9 connections) — `server/game/items/item_effects.py`
- **_lucidity_recovery()** (9 connections) — `server/game/items/item_effects.py`
- **FakeSession** (9 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **_prototype()** (8 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **_context()** (7 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **test_lucidity_recovery_applies_the_prototypes_numbers()** (6 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **test_lucidity_recovery_with_bad_metadata_does_nothing()** (6 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **_catatonia_observer()** (5 connections) — `server/game/items/item_effects.py`
- **field_validator** (5 connections)
- **FakeService** (5 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **.apply_timed_recovery()** (5 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **test_catatonia_observer_comes_from_the_container_then_app_state()** (5 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **test_lucidity_recovery_on_cooldown_refuses_and_rolls_back()** (5 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **.validate_effect_components()** (4 connections) — `server/game/items/models.py`
- **.validate_flags()** (4 connections) — `server/game/items/models.py`
- **.validate_item_type()** (4 connections) — `server/game/items/models.py`
- **.validate_wear_slots()** (4 connections) — `server/game/items/models.py`
- **asyncio** (4 connections)
- *... and 37 more nodes in this community*

## Relationships

- [test_room_sync_service.py](test_room_sync_service.py.md) (26 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (11 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (6 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (5 shared connections)
- [UserManager](UserManager.md) (5 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [item_prototype.schema.json](item_prototype.schema.json.md) (3 shared connections)
- [useGameClientV2ContainerNetworkPhase.ts](useGameClientV2ContainerNetworkPhase.ts.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/item_effects.py`
- `server/game/items/models.py`
- `server/tests/unit/game/items/test_item_effects.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`

## Audit Trail

- EXTRACTED: 166 (81%)
- INFERRED: 39 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*