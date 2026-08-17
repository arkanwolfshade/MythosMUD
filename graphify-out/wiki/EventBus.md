# eventbus

> 6 nodes

## Key Concepts

- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **._get_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **EventBus** (3 connections)
- **Get the event bus from connection manager.** (2 connections) — `server/realtime/connection_manager.py`
- **Set the event bus for the connection manager.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [playercombatservice](playercombatservice.md) (3 shared connections)
- [server api monitoring](server_api_monitoring.md) (1 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (1 shared connections)
- [server commands combat](server_commands_combat.md) (1 shared connections)
- [server commands go command](server_commands_go_command.md) (1 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (1 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server npc init](server_npc_init.md) (1 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 9 (50%)
- INFERRED: 9 (50%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*