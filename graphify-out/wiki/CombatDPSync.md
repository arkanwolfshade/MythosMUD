# CombatDPSync

> 18 nodes · cohesion 0.18

## Key Concepts

- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (8 connections) — `server/services/combat_hp_sync.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **._verify_player_save()** (4 connections) — `server/services/combat_hp_sync.py`
- **.__init__()** (3 connections) — `server/services/combat_hp_sync.py`
- **._persist_player_dp_background()** (3 connections) — `server/services/combat_hp_sync.py`
- **Any** (2 connections)
- **Get persistence layer from application container.          Args:             pla** (1 connections) — `server/services/combat_hp_sync.py`
- **Verify that player DP was successfully saved to database.          Args:** (1 connections) — `server/services/combat_hp_sync.py`
- **Log death threshold events based on DP changes.          Args:             curre** (1 connections) — `server/services/combat_hp_sync.py`
- **Update player DP and save to database.          Args:             persistence: P** (1 connections) — `server/services/combat_hp_sync.py`
- **Synchronously persist player DP to database.          This is the actual persist** (1 connections) — `server/services/combat_hp_sync.py`
- **Handles DP synchronization for combat operations.** (1 connections) — `server/services/combat_hp_sync.py`
- **Initialize DP sync with reference to parent combat service.** (1 connections) — `server/services/combat_hp_sync.py`
- **Persist player DP to database in background (fire-and-forget).          This met** (1 connections) — `server/services/combat_hp_sync.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 61 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*