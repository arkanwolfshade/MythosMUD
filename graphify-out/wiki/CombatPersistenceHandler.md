# CombatPersistenceHandler

> 23 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **Synchronously persist player DP to database. This is the actual persistence…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Handles combat-related persistence operations.** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler. Args: combat_service: Reference to the…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). Public API…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates. Args: player_id: ID…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Get persistence layer from application container. Returns: Persistence layer…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing. Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a correction event when database persistence fails. This sends a…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Verify that player save was successful by reading back from database. Args:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded). Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [persistence_handler](persistence_handler.md) (2 shared connections)
- [test_combat_persistence_handler.py](test_combat_persistence_handler.py.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [combat_service.py](combat_service.py.md) (1 shared connections)
- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (1 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 47 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*