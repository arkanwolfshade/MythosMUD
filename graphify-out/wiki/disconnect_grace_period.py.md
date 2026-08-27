# disconnect_grace_period.py

> 44 nodes

## Key Concepts

- **coerce_int()** (32 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **.get_stats()** (12 connections) — `server/models/player.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **test_coerce_int_string_parsing()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- *... and 19 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (7 shared connections)
- [ClientLogger](ClientLogger.md) (5 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (2 shared connections)
- [test_metrics.py](test_metrics.py.md) (1 shared connections)
- [FakeHallucinationService](FakeHallucinationService.md) (1 shared connections)
- [RoomInfoPanel.tsx](RoomInfoPanel.tsx.md) (1 shared connections)
- [Game Subsystem Design Documents Overview](Game_Subsystem_Design_Documents_Overview.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 106 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*