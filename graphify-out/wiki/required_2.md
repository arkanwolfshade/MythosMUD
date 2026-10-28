# required

> 31 nodes · cohesion 0.10

## Key Concepts

- **CombatPersistenceHandler** (24 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (9 connections)
- **._publish_player_dp_update_event_impl()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_event_to_bus()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_update_to_nats()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **Combat persistence handling logic. Handles player DP persistence, verification,…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Verify that player save was successful by reading back from database. Args:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded). Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: The game tick loop will also check for dead players, but this provides…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Synchronously persist player DP to database. This is the actual persistence…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: DP update event is now published IMMEDIATELY in process_attack()** (1 connections) — `server/services/combat_persistence_handler.py`
- **Handles combat-related persistence operations.** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler. Args: combat_service: Reference to the…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). Public API…** (1 connections) — `server/services/combat_persistence_handler.py`
- *... and 6 more nodes in this community*

## Relationships

- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (3 shared connections)
- [world](world.md) (3 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 66 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*