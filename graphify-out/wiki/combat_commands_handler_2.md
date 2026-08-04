# combat commands handler

> 76 nodes

## Key Concepts

- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (6 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_attacker()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **UUID** (2 connections)
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_attack_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_attack_active()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_attack_inactive()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_kills()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_negative_cap()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_npc()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 51 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (9 shared connections)
- [command factories exploration](command_factories_exploration.md) (8 shared connections)
- [Item Instances](Item_Instances.md) (7 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (3 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 184 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*