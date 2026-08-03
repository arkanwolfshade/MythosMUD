# models npc rationale

> 95 nodes

## Key Concepts

- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **.get_npc_definition()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **UUID** (5 connections)
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **Any** (4 connections)
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_combat_data()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **test_get_player_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_uses_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_name()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (3 connections) — `server/services/npc_combat_data_provider.py`
- *... and 70 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (28 shared connections)
- [Item Instances](Item_Instances.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 306 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*