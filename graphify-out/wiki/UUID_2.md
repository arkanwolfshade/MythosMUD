# UUID

> 21 nodes

## Key Concepts

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
- **Initialize the persistence handler. Args: combat_service: Reference to the…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). Public API…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates. Args: player_id: ID…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Get persistence layer from application container. Returns: Persistence layer…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing. Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a correction event when database persistence fails. This sends a…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Verify that player save was successful by reading back from database. Args:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded). Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`

## Relationships

- [CombatInstance](CombatInstance.md) (10 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*