# server services combat hp sync

> 22 nodes

## Key Concepts

- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_update_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **._verify_player_save()** (4 connections) — `server/services/combat_hp_sync.py`
- **.__init__()** (3 connections) — `server/services/combat_hp_sync.py`
- **._persist_player_dp_background()** (3 connections) — `server/services/combat_hp_sync.py`
- **Any** (2 connections)
- **Get persistence layer from application container. Args: player_id: Player ID…** (1 connections) — `server/services/combat_hp_sync.py`
- **Verify that player DP was successfully saved to database. Args: persistence:…** (1 connections) — `server/services/combat_hp_sync.py`
- **Log death threshold events based on DP changes. Args: current_dp: New current…** (1 connections) — `server/services/combat_hp_sync.py`
- **Update player DP and save to database. Args: persistence: Persistence layer…** (1 connections) — `server/services/combat_hp_sync.py`
- **Synchronously persist player DP to database. This is the actual persistence…** (1 connections) — `server/services/combat_hp_sync.py`
- **Handles DP synchronization for combat operations.** (1 connections) — `server/services/combat_hp_sync.py`
- **Initialize DP sync with reference to parent combat service.** (1 connections) — `server/services/combat_hp_sync.py`
- **Publish a PlayerDPUpdated event for real-time UI updates.** (1 connections) — `server/services/combat_hp_sync.py`
- **Publish a correction event when database persistence fails.** (1 connections) — `server/services/combat_hp_sync.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_hp_sync.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (2 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (2 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*