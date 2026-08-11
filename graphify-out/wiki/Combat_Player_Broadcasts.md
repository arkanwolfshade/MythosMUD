# Combat Player Broadcasts

> 253 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (63 connections) — `server/api/container_models.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **loot_all_items()** (35 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **container.py** (26 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (15 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestEmitTransferEventDirections** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 228 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (47 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (37 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (33 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (27 shared connections)
- [Player Effects API](Player_Effects_API.md) (18 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (10 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (9 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (3 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)

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

- EXTRACTED: 971 (88%)
- INFERRED: 131 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*