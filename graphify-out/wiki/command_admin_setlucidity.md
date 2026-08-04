# command admin setlucidity

> 27 nodes

## Key Concepts

- **_get_enum_value()** (9 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (9 connections) — `server/services/wearable_container_service.py`
- **Any** (8 connections)
- **.add_items_to_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (8 connections) — `server/services/wearable_container_service.py`
- **UUID** (7 connections)
- **.handle_equip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (6 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **test_get_enum_value_with_enum()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_enum_value_with_string()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_filter_container_data()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **ContainerComponent** (1 connections)
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/wearable_container_service.py`
- **Filter out database-only fields from container data before validation.      The** (1 connections) — `server/services/wearable_container_service.py`
- **Initialize the wearable container service.          Args:             persistenc** (1 connections) — `server/services/wearable_container_service.py`
- **Handle equipping a wearable container item.          Creates a container in Post** (1 connections) — `server/services/wearable_container_service.py`
- **Handle unequipping a wearable container item.          Preserves the container a** (1 connections) — `server/services/wearable_container_service.py`
- **Get all wearable containers for a player.          Args:             player_id:** (1 connections) — `server/services/wearable_container_service.py`
- **Add items to a wearable container.          Args:             player_id: UUID of** (1 connections) — `server/services/wearable_container_service.py`
- **Update items in a wearable container.          Args:             player_id: UUID** (1 connections) — `server/services/wearable_container_service.py`
- **Handle container overflow by spilling items to inventory or ground.          Arg** (1 connections) — `server/services/wearable_container_service.py`
- **Test _get_enum_value returns value from enum instance.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (7 shared connections)
- [wearable container service](wearable_container_service.md) (5 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (4 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 93 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*