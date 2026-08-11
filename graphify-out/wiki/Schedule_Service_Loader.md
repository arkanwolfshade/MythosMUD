# Schedule Service Loader

> 32 nodes

## Key Concepts

- **WearableContainerService** (31 connections) — `server/services/wearable_container_service.py`
- **Any** (15 connections)
- **UUID** (14 connections)
- **._load_player_wearable_container()** (10 connections) — `server/services/wearable_container_service.py`
- **.handle_equip_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (9 connections) — `server/services/wearable_container_service.py`
- **._update_container_items_or_raise()** (8 connections) — `server/services/wearable_container_service.py`
- **.add_items_to_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (8 connections) — `server/services/wearable_container_service.py`
- **._validate_inner_container_capacity()** (7 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **._find_existing_equipment_container()** (5 connections) — `server/services/wearable_container_service.py`
- **._create_equipment_container_record()** (5 connections) — `server/services/wearable_container_service.py`
- **._save_overflow_inventory()** (5 connections) — `server/services/wearable_container_service.py`
- **._drop_overflow_to_ground()** (5 connections) — `server/services/wearable_container_service.py`
- **._split_overflow_items()** (4 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **Service for managing wearable container operations.      Handles container creat** (1 connections) — `server/services/wearable_container_service.py`
- **Initialize the wearable container service.          Args:             persistenc** (1 connections) — `server/services/wearable_container_service.py`
- **Validate inner container item count against capacity.** (1 connections) — `server/services/wearable_container_service.py`
- **Return existing equipment container ID for item instance if present.** (1 connections) — `server/services/wearable_container_service.py`
- **Create wearable container in persistence and return container_id payload.** (1 connections) — `server/services/wearable_container_service.py`
- **Handle equipping a wearable container item.          Creates a container in Post** (1 connections) — `server/services/wearable_container_service.py`
- **Handle unequipping a wearable container item.          Preserves the container a** (1 connections) — `server/services/wearable_container_service.py`
- **Load container and verify it belongs to the player's equipment.** (1 connections) — `server/services/wearable_container_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (7 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (6 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (6 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (5 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (3 shared connections)
- [Look Player Command](Look_Player_Command.md) (2 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (1 shared connections)
- [test_execute_idle_movement_no_current_room](test_execute_idle_movement_no_current_room.md) (1 shared connections)
- [test_calculate_distance_to_room_different_rooms](test_calculate_distance_to_room_different_rooms.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`

## Audit Trail

- EXTRACTED: 156 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*