# ._validate_container_access

> 15 nodes

## Key Concepts

- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **ContainerComponent** (7 connections)
- **._can_unlock_container()** (5 connections) — `server/services/container_service_access.py`
- **._raise_corpse_grace_denied()** (5 connections) — `server/services/container_service_access.py`
- **._validate_corpse_grace_period()** (5 connections) — `server/services/container_service_access.py`
- **._validate_ownership()** (5 connections) — `server/services/container_service_access.py`
- **._validate_proximity()** (5 connections) — `server/services/container_service_access.py`
- **._player_has_key_item()** (3 connections) — `server/services/container_service_access.py`
- **Deny non-owner corpse access during (or without) a timed grace period.** (1 connections) — `server/services/container_service_access.py`
- **Validate corpse grace period access rules.** (1 connections) — `server/services/container_service_access.py`
- **Validate that player has access to the container. Checks proximity, ownership,…** (1 connections) — `server/services/container_service_access.py`
- **Return True if player inventory contains the required key item_id.** (1 connections) — `server/services/container_service_access.py`
- **Check if player can unlock the container. Args: container: Container to check…** (1 connections) — `server/services/container_service_access.py`
- **Validate player is in same room as container for environment/corpse containers.** (1 connections) — `server/services/container_service_access.py`
- **Validate player owns equipment container.** (1 connections) — `server/services/container_service_access.py`

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [UserManager](UserManager.md) (2 shared connections)

## Source Files

- `server/services/container_service_access.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*