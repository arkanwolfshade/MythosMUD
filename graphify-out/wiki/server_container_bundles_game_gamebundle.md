# server container bundles game gamebundle

> 32 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **Wire exploration, movement, follow, and party services.** (1 connections) — `server/container/bundles/game.py`
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- **Clone template rooms into instance-scoped rooms with remapped exits.** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from room - use room.id if it looks like a full path.** (1 connections) — `server/game/instance_manager.py`
- **Remap exit targets: same-instance rooms use instance IDs, outside exits use…** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from a room ID (may be full path or short form).** (1 connections) — `server/game/instance_manager.py`
- **Return the instance if it exists.** (1 connections) — `server/game/instance_manager.py`
- **Remove the instance from the store.** (1 connections) — `server/game/instance_manager.py`
- *... and 7 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (2 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (1 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (1 shared connections)
- [server commands rest command](server_commands_rest_command.md) (1 shared connections)
- [followtargetvalue](followtargetvalue.md) (1 shared connections)
- [server game party service](server_game_party_service.md) (1 shared connections)
- [server tests unit test alias](server_tests_unit_test_alias.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`

## Audit Trail

- EXTRACTED: 57 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*