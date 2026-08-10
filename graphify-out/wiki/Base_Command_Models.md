# Base Command Models

> 48 nodes

## Key Concepts

- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **InventoryCommandFactory** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **test_create_pickup_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_zero()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_negative()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_zero()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_negative()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_with_extra_tokens()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_empty_search_term()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_zero()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_negative()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_empty_search_term()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **._parse_quantity_from_args()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_index_or_search_term()** (4 connections) — `server/utils/command_factories_inventory.py`
- **test_create_pickup_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_only()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_search_term_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_inferred_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **_normalize_equip_slot_tokens()** (3 connections) — `server/utils/command_factories_inventory.py`
- **Unit tests for inventory command factories.  Tests the InventoryCommandFactory c** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- *... and 23 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (12 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (9 shared connections)
- [Architecture Review Plan](Architecture_Review_Plan.md) (8 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (8 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (5 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 184 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*