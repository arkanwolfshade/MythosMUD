# ._create_combat_service_with_nats

> 4 nodes

## Key Concepts

- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **set_combat_service()** (6 connections) — `server/services/combat_service_state.py`
- **Create CombatService with NATS and register it. Assumes NATS is connected.** (1 connections) — `server/container/bundles/combat.py`
- **Set the global combat service instance.** (1 connections) — `server/services/combat_service_state.py`

## Relationships

- [CombatService](CombatService.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/combat_service_state.py`

## Audit Trail

- EXTRACTED: 8 (67%)
- INFERRED: 4 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*