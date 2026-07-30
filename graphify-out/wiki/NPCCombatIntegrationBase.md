# NPCCombatIntegrationBase

> 197 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (9 connections)
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (7 connections)
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **BoundLogger** (4 connections)
- *... and 172 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (21 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (13 shared connections)
- [.get instance()](get_instance%28%29.md) (11 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [combat initialization](combat_initialization.md) (9 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (6 shared connections)
- [world](world.md) (6 shared connections)
- [connection statistics](connection_statistics.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [circuit breaker](circuit_breaker.md) (6 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (4 shared connections)
- [test websocket handler helpers extended](test_websocket_handler_helpers_extended.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 656 (96%)
- INFERRED: 30 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*