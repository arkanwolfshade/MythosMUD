# Mythos Calendar Time Service

> 18 nodes

## Key Concepts

- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (8 connections) — `server/services/combat_hp_sync.py`
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

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 61 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*