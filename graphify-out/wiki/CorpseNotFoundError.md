# CorpseNotFoundError

> 17 nodes

## Key Concepts

- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_persistence_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_delete_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test cleanup_decayed_corpse() raises error when corpse not found.** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Base exception for corpse service operations.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Raised when a corpse container is not found.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Test CorpseServiceError exception.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test CorpseNotFoundError exception.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test create_corpse_on_death() raises error when player not found.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test create_corpse_on_death() handles persistence errors.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test cleanup_decayed_corpse() raises error when delete fails.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Relationships

- [test corpse lifecycle service](test_corpse_lifecycle_service.md) (9 shared connections)
- [.can access corpse()](can_access_corpse%28%29.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 36 (71%)
- INFERRED: 15 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*