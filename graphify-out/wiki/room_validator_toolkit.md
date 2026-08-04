# room validator toolkit

> 142 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **UUID** (11 connections)
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **test_aggro_healer_overpull_switches_target()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- *... and 117 more nodes in this community*

## Relationships

- [command factories exploration](command_factories_exploration.md) (25 shared connections)
- [models npc rationale](models_npc_rationale.md) (19 shared connections)
- [Item Instances](Item_Instances.md) (16 shared connections)
- [spell game magic](spell_game_magic.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (6 shared connections)
- [commands party examples](commands_party_examples.md) (5 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [services combat sync](services_combat_sync.md) (3 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)
- [retry nats handler](retry_nats_handler.md) (2 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/services/aggro_threat.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 681 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*