# E 2 E Scenarios Scenario

> 6 nodes · cohesion 0.33

## Key Concepts

- **.refresh_configuration()** (5 connections) — `server/services/combat_configuration_service.py`
- **.clear_cache()** (3 connections) — `server/services/combat_configuration_service.py`
- **refresh_combat_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **Refresh configuration from source.** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear configuration cache.** (1 connections) — `server/services/combat_configuration_service.py`
- **Refresh combat configuration by clearing cache and reloading.** (1 connections) — `server/services/combat_configuration_service.py`

## Relationships

- [Combat Configuration Service](Combat_Configuration_Service.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*