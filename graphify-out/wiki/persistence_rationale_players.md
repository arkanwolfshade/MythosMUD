# persistence rationale players

> 256 nodes

## Key Concepts

- **AsyncPersistenceLayer** (184 connections) — `server/async_persistence.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **ScheduleService** (30 connections) — `server/services/schedule_service.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Any** (19 connections)
- **idle_movement.py** (17 connections) — `server/npc/idle_movement.py`
- **combat_hp_sync.py** (15 connections) — `server/services/combat_hp_sync.py`
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 231 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (38 shared connections)
- [models npc rationale](models_npc_rationale.md) (37 shared connections)
- [schemas invite user](schemas_invite_user.md) (23 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (18 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (17 shared connections)
- [Item Instances](Item_Instances.md) (14 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (13 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [holiday service services](holiday_service_services.md) (9 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (7 shared connections)
- [nats services service](nats_services_service.md) (7 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/commands/combat_handler.py`
- `server/game/profession_service.py`
- `server/npc/idle_movement.py`
- `server/schemas/calendar/calendar.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/schedule_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 1069 (93%)
- INFERRED: 81 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*