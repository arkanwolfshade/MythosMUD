# shutdown admin command

> 41 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Current FSM state as a single State.          Uses python-statemachine 3.x confi** (1 connections) — `server/realtime/connection_state_machine.py`
- **Provides initial game state for newly connected players.      This class provide** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Initialize the game state provider.          Args:             room_manager: Roo** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 16 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (10 shared connections)
- [command commands aliases](command_commands_aliases.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)
- [spell models rationale](spell_models_rationale.md) (2 shared connections)
- [game state provider](game_state_provider.md) (2 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [follow game service](follow_game_service.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 180 (79%)
- INFERRED: 47 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*