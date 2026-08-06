# container find inventory

> 45 nodes

## Key Concepts

- **container_helpers_inventory_find.py** (32 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_wearable_container()** (17 connections) — `server/commands/container_helpers_inventory_find.py`
- **UUID** (16 connections)
- **try_wearable_container_service()** (14 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_instance_id()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **create_wearable_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **_player_for_wearable()** (12 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **try_inner_container_by_id()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_name()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_wearable_container_for_put()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **_get_container_pair()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_try_put_container_for_equipped_item()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_uuid()** (5 connections) — `server/commands/container_helpers_inventory_find.py`
- **Player** (5 connections)
- **container_id()** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_component_metadata()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_resolve_inner_uuid()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_from_equip_dict()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_fallback_create_equipment_container()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_try_wearable_container_service_finds_component()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_wearable_container_service_swallows_service_error()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_uses_equip_dict_branch()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_fallback_when_equip_returns_non_dict()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_hits_inner_container()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_creates_on_slot_only_match()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- *... and 20 more nodes in this community*

## Relationships

- [game rationale schemas](game_rationale_schemas.md) (39 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (9 shared connections)
- [player cache rationale](player_cache_rationale.md) (5 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 241 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*