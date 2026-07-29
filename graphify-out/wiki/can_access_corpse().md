# .can access corpse()

> 29 nodes

## Key Concepts

- **.cleanup_decayed_corpse()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (4 connections)
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Filter out database-specific fields that are not part of the ContainerComponent** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service.          Args:             persistence:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.          Args:             player_** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a player can access a corpse container.          During grace period, o** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a corpse container has decayed.          Args:             corpse: Corp** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers in a room.          Args:             room_id:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up a decayed corpse container.          Deletes the container and emits de** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up all decayed corpse containers in a room.          Args:             roo** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (9 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [test corpse lifecycle service](test_corpse_lifecycle_service.md) (3 shared connections)
- [CorpseNotFoundError](CorpseNotFoundError.md) (3 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 89 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*