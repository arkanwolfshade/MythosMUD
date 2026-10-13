# Community 636

> 27 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (9 connections)
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_event_to_bus()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_update_to_nats()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **Verify that player save was successful by reading back from database. Args:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded). Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Synchronously persist player DP to database. This is the actual persistence…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Handles combat-related persistence operations.** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler. Args: combat_service: Reference to the…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). Public API…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates. Args: player_id: ID…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event via NATS, for systems that don't use the event…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing. Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated(-shaped) event to the shared combat-service event…** (1 connections) — `server/services/combat_persistence_handler.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 118](Community_118.md) (2 shared connections)
- [Community 736](Community_736.md) (2 shared connections)
- [Community 1588](Community_1588.md) (2 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [Community 515](Community_515.md) (1 shared connections)
- [Community 542](Community_542.md) (1 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (1 shared connections)
- [Community 1507](Community_1507.md) (1 shared connections)
- [Community 1448](Community_1448.md) (1 shared connections)
- [Community 43](Community_43.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 50 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*