# ._validate_container_access

> 12 nodes

## Key Concepts

- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **._raise_corpse_grace_denied()** (5 connections) — `server/services/container_service_access.py`
- **._validate_corpse_grace_period()** (5 connections) — `server/services/container_service_access.py`
- **._validate_ownership()** (5 connections) — `server/services/container_service_access.py`
- **._validate_proximity()** (5 connections) — `server/services/container_service_access.py`
- **._validate_role_access()** (5 connections) — `server/services/container_service_access.py`
- **Deny non-owner corpse access during (or without) a timed grace period.** (1 connections) — `server/services/container_service_access.py`
- **Validate corpse grace period access rules.** (1 connections) — `server/services/container_service_access.py`
- **Validate that player has access to the container. Checks proximity, ownership,…** (1 connections) — `server/services/container_service_access.py`
- **Validate player is in same room as container for environment/corpse containers.** (1 connections) — `server/services/container_service_access.py`
- **Validate player owns equipment container.** (1 connections) — `server/services/container_service_access.py`
- **Validate player has required role for container access.** (1 connections) — `server/services/container_service_access.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (6 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [UserManager](UserManager.md) (1 shared connections)

## Source Files

- `server/services/container_service_access.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*