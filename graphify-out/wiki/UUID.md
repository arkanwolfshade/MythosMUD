# UUID

> 18 nodes

## Key Concepts

- **UUID** (13 connections)
- **.create_corpse_on_death()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **._collect_death_items()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_DeathPersistence** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._worn_container_rows()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **._strip_player_after_death()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.clear_player_inventory()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.delete_container()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_containers_by_entity_id()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Everything a dying player drops: carried and equipped stacks, worn containers…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The player's equipment-container rows (worn backpacks etc.) keyed by their…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clear what moved onto the corpse, so items are moved rather than copied (#917).…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The persistence calls moving a dead player's gear onto a corpse makes (#917).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Containers owned by an entity (a player's worn-container rows).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Delete a container row.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Empty only the player's carried and equipped items (never stats: no race with…** (1 connections) — `server/services/corpse_lifecycle_service.py`

## Relationships

- [CorpseLifecycleService](CorpseLifecycleService.md) (9 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [_DyingPlayer](_DyingPlayer.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [_get_enum_value](_get_enum_value.md) (3 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*