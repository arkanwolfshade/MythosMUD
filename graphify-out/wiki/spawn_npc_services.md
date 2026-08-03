# spawn npc services

> 23 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **Handles combat-related persistence operations.** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler.          Args:             combat_service: R** (1 connections) — `server/services/combat_persistence_handler.py`
- **Get persistence layer from application container.          Returns:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Verify that player save was successful by reading back from database.          A** (1 connections) — `server/services/combat_persistence_handler.py`
- **Log death state changes (death threshold or mortally wounded).          Args:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Synchronously persist player DP to database.          This is the actual persist** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget).          This met** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget).          Public A** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates.          Args:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing.          Args:** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a correction event when database persistence fails.          This sends** (1 connections) — `server/services/combat_persistence_handler.py`

## Relationships

- [message filtering realtime](message_filtering_realtime.md) (5 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [commands communication say](commands_communication_say.md) (2 shared connections)
- [persistence combat services](persistence_combat_services.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 81 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*