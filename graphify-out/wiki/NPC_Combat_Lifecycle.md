# NPC Combat Lifecycle

> 151 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **UUID** (11 connections)
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- *... and 126 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (38 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (28 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (13 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (10 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (7 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Health Check Models](Health_Check_Models.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (3 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/services/aggro_threat.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 710 (99%)
- INFERRED: 10 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*