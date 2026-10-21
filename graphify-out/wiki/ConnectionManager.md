# ConnectionManager

> 168 nodes · cohesion 0.02

## Key Concepts

- **PlayerEventHandlerUtils** (48 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDPUpdated** (41 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (37 connections) — `server/realtime/player_event_handlers_state.py`
- **player_event_handlers_state.py** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerDPDecayEvent** (33 connections) — `server/events/event_types.py`
- **PlayerXPAwardEvent** (28 connections) — `server/events/event_types.py`
- **player_event_handlers_utils.py** (21 connections) — `server/realtime/player_event_handlers_utils.py`
- **asyncio** (21 connections)
- **test_player_event_handler_base.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handler_base.py`
- **PlayerEventHandlerBase** (13 connections) — `server/realtime/player_event_handler_base.py`
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **player_event_handler_base.py** (9 connections) — `server/realtime/player_event_handler_base.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_collaborators()** (9 connections) — `server/tests/unit/realtime/test_player_event_handler_base.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **_attach_dp_updated_posture_fields()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_state_handler()** (8 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **.process_dict_occupant()** (7 connections) — `server/realtime/player_event_handlers_utils.py`
- **Any** (7 connections)
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.add_valid_name_to_lists()** (6 connections) — `server/realtime/player_event_handlers_utils.py`
- **UUID** (6 connections)
- *... and 143 more nodes in this community*

## Relationships

- [ZoneConfiguration](ZoneConfiguration.md) (22 shared connections)
- [look_container.py](look_container.py.md) (15 shared connections)
- [ChatService](ChatService.md) (11 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (10 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (8 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [._bind_event_type](_bind_event_type.md) (6 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (6 shared connections)
- [.publish_with_pool](publish_with_pool.md) (6 shared connections)
- [BaseEvent](BaseEvent.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handler_base.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/combat_service.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_player_event_handler_base.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 394 (83%)
- INFERRED: 78 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*