# test_combat_monitoring_service.py

> 114 nodes · cohesion 0.03

## Key Concepts

- **Room** (132 connections) — `server/models/room.py`
- **test_room_class.py** (34 connections) — `server/tests/unit/models/test_room_class.py`
- **test_tutorial_reentry_gives_stranded_player_a_fresh_instance()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_tutorial_reentry_ignores_players_outside_templates()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.player_entered()** (6 connections) — `server/models/room.py`
- **_manager_with()** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **.player_left()** (5 connections) — `server/models/room.py`
- **_foyer()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_template_bedroom()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **.add_player_silently()** (4 connections) — `server/models/room.py`
- **._container_id_of()** (4 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.remove_player_silently()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.add_container()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.remove_container()** (3 connections) — `server/models/room.py`
- **test_room_add_container_appears_in_to_dict()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 89 more nodes in this community*

## Relationships

- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (16 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (11 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (7 shared connections)
- [BaseEvent](BaseEvent.md) (5 shared connections)
- [useGameClientV2ContainerNetworkPhase.ts](useGameClientV2ContainerNetworkPhase.ts.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [TabbedInterfaceOverlay.tsx](TabbedInterfaceOverlay.tsx.md) (4 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (3 shared connections)
- [waitForMessage](waitForMessage.md) (3 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [security.ts](security.ts.md) (3 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 238 (89%)
- INFERRED: 29 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*