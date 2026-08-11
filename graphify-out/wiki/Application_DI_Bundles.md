# Application DI Bundles

> 101 nodes

## Key Concepts

- **PlayerService** (141 connections) — `server/game/player_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (18 connections) — `server/game/magic/magic_service.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **UUID** (12 connections)
- **spell_costs.py** (12 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **Any** (11 connections)
- **Any** (11 connections)
- **casting_state_manager.py** (9 connections) — `server/game/magic/casting_state_manager.py`
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (8 connections)
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **CastingState** (6 connections) — `server/game/magic/casting_state_manager.py`
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- *... and 76 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (37 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (36 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (25 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (22 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (14 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (11 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (10 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (9 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (9 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (9 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (7 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (5 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/player_service.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 468 (83%)
- INFERRED: 93 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*