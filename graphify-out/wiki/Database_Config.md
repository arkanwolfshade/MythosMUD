# Database Config

> 162 nodes

## Key Concepts

- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **player_combat_service()** (6 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 137 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (19 shared connections)
- [Error Conversion](Error_Conversion.md) (10 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (9 shared connections)
- [profession models rationale](profession_models_rationale.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (5 shared connections)
- [commands communication support](commands_communication_support.md) (4 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 546 (92%)
- INFERRED: 48 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*