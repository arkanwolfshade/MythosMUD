# E 2 E Runtime Multiplayer

> 4 nodes

## Key Concepts

- **get_combat_monitoring()** (5 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_monitoring()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Get the global combat monitoring service instance.      Returns:         CombatM** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test get_combat_monitoring returns global instance.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [Combat Monitoring Service](Combat_Monitoring_Service.md) (2 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*