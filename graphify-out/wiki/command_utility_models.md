# command utility models

> 178 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **UUID** (15 connections)
- **npc_combat_grace.py** (14 connections) — `server/services/npc_combat_grace.py`
- **Any** (13 connections)
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **is_player_attack_blocked_by_login_grace_period()** (11 connections) — `server/services/npc_combat_grace.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (9 connections)
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- *... and 153 more nodes in this community*

## Relationships

- [look helpers commands](look_helpers_commands.md) (29 shared connections)
- [models npc rationale](models_npc_rationale.md) (22 shared connections)
- [combat commands handler](combat_commands_handler.md) (15 shared connections)
- [npc combat base](npc_combat_base.md) (13 shared connections)
- [combat services messaging](combat_services_messaging.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [Player Stats](Player_Stats.md) (7 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (7 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (5 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [character creation service](character_creation_service.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/config/__init__.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/nats_message_handler.py`
- `server/services/npc_combat_grace.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 767 (93%)
- INFERRED: 57 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*