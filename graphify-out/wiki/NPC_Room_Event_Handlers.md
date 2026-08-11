# NPC Room Event Handlers

> 22 nodes

## Key Concepts

- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (8 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_update_event()** (6 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (6 connections) — `server/services/combat_hp_sync.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **._verify_player_save()** (4 connections) — `server/services/combat_hp_sync.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **.__init__()** (3 connections) — `server/services/combat_hp_sync.py`
- **._persist_player_dp_background()** (3 connections) — `server/services/combat_hp_sync.py`
- **Any** (2 connections)
- **Handles DP synchronization for combat operations.** (1 connections) — `server/services/combat_hp_sync.py`
- **Initialize DP sync with reference to parent combat service.** (1 connections) — `server/services/combat_hp_sync.py`
- **Persist player DP to database in background (fire-and-forget).          This met** (1 connections) — `server/services/combat_hp_sync.py`
- **Get persistence layer from application container.          Args:             pla** (1 connections) — `server/services/combat_hp_sync.py`
- **Verify that player DP was successfully saved to database.          Args:** (1 connections) — `server/services/combat_hp_sync.py`
- **Log death threshold events based on DP changes.          Args:             curre** (1 connections) — `server/services/combat_hp_sync.py`
- **Update player DP and save to database.          Args:             persistence: P** (1 connections) — `server/services/combat_hp_sync.py`
- **Synchronously persist player DP to database.          This is the actual persist** (1 connections) — `server/services/combat_hp_sync.py`
- **Publish a PlayerDPUpdated event for real-time UI updates.** (1 connections) — `server/services/combat_hp_sync.py`
- **Publish a correction event when database persistence fails.** (1 connections) — `server/services/combat_hp_sync.py`

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (2 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 73 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*