# Admin Summon Command

> 64 nodes

## Key Concepts

- **test_command_inventory.py** (63 connections) — `server/tests/unit/models/test_command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **command_inventory.py** (13 connections) — `server/models/command_inventory.py`
- **PutCommand** (12 connections) — `server/models/command_inventory.py`
- **GetCommand** (12 connections) — `server/models/command_inventory.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **test_pickup_command_validate_search_term_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_neither_provided()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_index_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_search_term_max_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_item_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_container_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_item_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_container_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_inventory_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_search_term()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_both()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_none()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_index_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 39 more nodes in this community*

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (15 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (14 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (11 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (7 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (6 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (5 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (1 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (1 shared connections)
- [Architecture Review Plan](Architecture_Review_Plan.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 230 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*