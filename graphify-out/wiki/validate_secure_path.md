# validate_secure_path

> 26 nodes · cohesion 0.08

## Key Concepts

- **PlayerCombatService** (73 connections) — `server/services/player_combat_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.set_player_combat_service()** (3 connections) — `server/realtime/connection_manager.py`
- **.set_player_combat_service()** (3 connections) — `server/services/combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **test_is_player_in_combat_sync_false()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_service_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.get_combat_stats()** (2 connections) — `server/services/player_combat_service.py`
- **.__init__()** (2 connections) — `server/services/player_combat_service.py`
- **.set_level_service()** (2 connections) — `server/services/player_combat_service.py`
- **.set_npc_combat_integration_service()** (2 connections) — `server/services/player_combat_service.py`
- **Initialize the spell targeting service. Args: target_resolution_service:…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Set the player combat service for the connection manager.** (1 connections) — `server/realtime/connection_manager.py`
- **Attach or replace the player combat service (shared instance wiring).** (1 connections) — `server/services/combat_service.py`
- **Attach NPC combat integration for UUID/XP mapping (post-construction wiring).** (1 connections) — `server/services/player_combat_service.py`
- **Attach the LevelService (post-construction wiring, matching…** (1 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state. Args: player_id: ID of the player** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat end by clearing all players in the combat. Args: combat_id: ID of…** (1 connections) — `server/services/player_combat_service.py`
- **Clean up stale combat states. Returns: Number of stale states cleaned up** (1 connections) — `server/services/player_combat_service.py`
- **Get statistics about player combat states. Returns: Dictionary with combat…** (1 connections) — `server/services/player_combat_service.py`
- **Service for managing player combat state and XP rewards. This service tracks…** (1 connections) — `server/services/player_combat_service.py`
- **Initialize the player combat service. Args: persistence: Persistence layer for…** (1 connections) — `server/services/player_combat_service.py`
- **Test is_player_in_combat_sync returns False when not in combat.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [CharacterNameScreen.tsx](CharacterNameScreen.tsx.md) (20 shared connections)
- [The Toolkit](The_Toolkit.md) (12 shared connections)
- [UpgradeImplementationPlan](UpgradeImplementationPlan.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (3 shared connections)
- [_MigrationArgs](_MigrationArgs.md) (3 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/realtime/connection_manager.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 65 (68%)
- INFERRED: 31 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*