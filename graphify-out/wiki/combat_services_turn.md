# combat services turn

> 131 nodes

## Key Concepts

- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_warded_indicator_in_game_state_provider()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **UUID** (4 connections)
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 106 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (22 shared connections)
- [look helpers commands](look_helpers_commands.md) (19 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (15 shared connections)
- [look command commands](look_command_commands.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (9 shared connections)
- [rest grace period](rest_grace_period.md) (9 shared connections)
- [help content websocket](help_content_websocket.md) (6 shared connections)
- [command models moderation](command_models_moderation.md) (6 shared connections)
- [nats services metrics](nats_services_metrics.md) (6 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (3 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 530 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*