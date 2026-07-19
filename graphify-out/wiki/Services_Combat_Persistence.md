# Services Combat Persistence

> 25 nodes · cohesion 0.09

## Key Concepts

- **UUID** (10 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (9 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **Any** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Get persistence layer from application container.          Args:             pla** (2 connections) — `server/services/combat_hp_sync.py`
- **Combat persistence handling logic.  Handles player DP persistence, verification,** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: The game tick loop will also check for dead players, but this provides i** (1 connections) — `server/services/combat_persistence_handler.py`
- **Synchronously persist player DP to database.          This is the actual persist** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: DP update event is now published IMMEDIATELY in process_attack()** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget).          This met** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler.          Args:             combat_service: R** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget).          Public A** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates.          Args:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing.          Args:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a correction event when database persistence fails.          This sends** (1 connections) — `server/services/combat_persistence_handler.py`
- **Verify that player save was successful by reading back from database.          A** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded).          Args:** (1 connections) — `server/services/combat_persistence_handler.py`

## Relationships

- [[Combat Service Bundle]] (10 shared connections)
- [[Player Event Handler Tests]] (6 shared connections)
- [[Combat Domain Events]] (3 shared connections)
- [[Application DI Bundles]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 73 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
