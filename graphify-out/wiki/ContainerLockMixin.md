# ContainerLockMixin

> 16 nodes

## Key Concepts

- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **._require_container_for_lock_ops()** (9 connections) — `server/services/container_service_lock.py`
- **.lock_container()** (8 connections) — `server/services/container_service_lock.py`
- **._persist_lock_state()** (7 connections) — `server/services/container_service_lock.py`
- **._raise_if_cannot_lock()** (7 connections) — `server/services/container_service_lock.py`
- **._require_player_for_lock_ops()** (7 connections) — `server/services/container_service_lock.py`
- **.unlock_container()** (7 connections) — `server/services/container_service_lock.py`
- **UUID** (7 connections)
- **Player** (2 connections)
- **Lock a container (LOCKED or SEALED). Requires ownership or admin.** (1 connections) — `server/services/container_service_lock.py`
- **Unlock a container. Requires access and unlock eligibility (key/admin).** (1 connections) — `server/services/container_service_lock.py`
- **Lock/unlock container state persistence.** (1 connections) — `server/services/container_service_lock.py`
- **Load container for lock/unlock ops, or raise ContainerNotFoundError.** (1 connections) — `server/services/container_service_lock.py`
- **Load player for lock/unlock ops, or raise ValidationError.** (1 connections) — `server/services/container_service_lock.py`
- **Require admin or ownership before locking (equipment entity or owner_id).** (1 connections) — `server/services/container_service_lock.py`
- **Persist container lock_state or raise ContainerServiceError.** (1 connections) — `server/services/container_service_lock.py`

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (10 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [ContainerLockState](ContainerLockState.md) (1 shared connections)

## Source Files

- `server/services/container_service_lock.py`

## Audit Trail

- EXTRACTED: 44 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*