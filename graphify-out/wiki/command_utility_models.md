# command utility models

> 142 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_warded_indicator_removed_after_expiration()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 117 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (13 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (10 shared connections)
- [logging processors structured](logging_processors_structured.md) (9 shared connections)
- [npc combat base](npc_combat_base.md) (7 shared connections)
- [Player Stats](Player_Stats.md) (7 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (7 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (7 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (7 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (6 shared connections)
- [look helpers commands](look_helpers_commands.md) (6 shared connections)
- [command models moderation](command_models_moderation.md) (6 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 603 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*