# server services combat persistence handler

> 27 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
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
- **Combat persistence handling logic. Handles player DP persistence, verification,…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: The game tick loop will also check for dead players, but this provides…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Synchronously persist player DP to database. This is the actual persistence…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: DP update event is now published IMMEDIATELY in process_attack()** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Handles combat-related persistence operations.** (1 connections) — `server/services/combat_persistence_handler.py`
- **Initialize the persistence handler. Args: combat_service: Reference to the…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Persist player DP to database in background (fire-and-forget). Public API…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a PlayerDPUpdated event for real-time UI updates. Args: player_id: ID…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Get persistence layer from application container. Returns: Persistence layer…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Internal implementation of player DP update event publishing. Args: player_id:…** (1 connections) — `server/services/combat_persistence_handler.py`
- **Publish a correction event when database persistence fails. This sends a…** (1 connections) — `server/services/combat_persistence_handler.py`
- *... and 2 more nodes in this community*

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (9 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (4 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 58 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*