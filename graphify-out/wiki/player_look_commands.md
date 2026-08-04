# player look commands

> 101 nodes

## Key Concepts

- **NPCCombatDataProvider** (39 connections) — `server/services/npc_combat_data_provider.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **test_npc_combat_data_provider.py** (17 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
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
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_name()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (38 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [services combat sync](services_combat_sync.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [room occupant manager](room_occupant_manager.md) (2 shared connections)
- [logging setup structured](logging_setup_structured.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 351 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*