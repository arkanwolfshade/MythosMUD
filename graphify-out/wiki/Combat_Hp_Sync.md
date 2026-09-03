# Combat Hp Sync

> 20 nodes

## Key Concepts

- **CombatDPSync** (10 connections) — `server/services/combat_hp_sync.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
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
- **Publish a correction event when database persistence fails.** (1 connections) — `server/services/combat_hp_sync.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_hp_sync.py`

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (1 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*