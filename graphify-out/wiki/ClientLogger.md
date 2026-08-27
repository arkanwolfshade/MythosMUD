# ClientLogger

> 56 nodes

## Key Concepts

- **look_container.py** (45 connections) — `server/commands/look_container.py`
- **_format_container_display()** (21 connections) — `server/commands/look_container.py`
- **_try_lookup_container_implicit()** (14 connections) — `server/commands/look_container.py`
- **JsonMap** (13 connections)
- **_format_container_contents()** (12 connections) — `server/commands/look_container.py`
- **_as_map()** (9 connections) — `server/commands/look_container.py`
- **_get_container_data_from_component()** (9 connections) — `server/commands/look_container.py`
- **_try_match_container_component()** (9 connections) — `server/commands/look_container.py`
- **_extract_container_metadata()** (8 connections) — `server/commands/look_container.py`
- **_fetch_container()** (7 connections) — `server/commands/look_container.py`
- **_find_container_via_wearable_service()** (7 connections) — `server/commands/look_container.py`
- **_matches_item_instance_id()** (7 connections) — `server/commands/look_container.py`
- **_matches_name_or_slot()** (7 connections) — `server/commands/look_container.py`
- **Protocol** (7 connections)
- **_WearableContainer** (6 connections) — `server/commands/look_container.py`
- **_as_map_list()** (6 connections) — `server/commands/look_container.py`
- **_container_name()** (5 connections) — `server/commands/look_container.py`
- **_room_container_maps()** (5 connections) — `server/commands/look_container.py`
- **UUID** (4 connections)
- **_ContainerPersistence** (3 connections) — `server/commands/look_container.py`
- **_LookPlayer** (3 connections) — `server/commands/look_container.py`
- **_LookRoom** (3 connections) — `server/commands/look_container.py`
- **_PrototypeRegistry** (3 connections) — `server/commands/look_container.py`
- **_WearableSvc** (3 connections) — `server/commands/look_container.py`
- **_as_uuid()** (3 connections) — `server/commands/look_container.py`
- *... and 31 more nodes in this community*

## Relationships

- [errorHandler.ts](errorHandler.ts.md) (32 shared connections)
- [talk_command.py](talk_command.py.md) (26 shared connections)
- [Uvicorn ASGI Server Best Practices](Uvicorn_ASGI_Server_Best_Practices.md) (6 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (5 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (5 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (1 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`

## Audit Trail

- EXTRACTED: 174 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*