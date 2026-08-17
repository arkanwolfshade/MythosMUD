# server services aggro threat

> 125 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_damage_threat()** (18 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (11 connections)
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_on_player_entered_stealth_wipes_from_all_npcs()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 100 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (42 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (26 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (19 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (8 shared connections)
- [iteminstance](iteminstance.md) (7 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (5 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (4 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (4 shared connections)
- [server config init create config](server_config_init_create_config.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 348 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*