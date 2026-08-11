# Combat Player Broadcasts

> 216 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (63 connections) — `server/api/container_models.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **loot_all_items()** (35 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_transfer_all_items_from_container_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 191 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (52 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (47 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (24 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (22 shared connections)
- [Player Effects API](Player_Effects_API.md) (14 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (8 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (6 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (4 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (3 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 810 (87%)
- INFERRED: 116 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*