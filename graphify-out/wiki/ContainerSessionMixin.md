# ContainerSessionMixin

> 23 nodes

## Key Concepts

- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **UUID** (10 connections)
- **.open_container()** (9 connections) — `server/services/container_service_session.py`
- **._raise_if_cannot_open_locks()** (8 connections) — `server/services/container_service_session.py`
- **._audit_log_container_close()** (7 connections) — `server/services/container_service_session.py`
- **._audit_container_open()** (6 connections) — `server/services/container_service_session.py`
- **.close_container()** (6 connections) — `server/services/container_service_session.py`
- **.register_open_session()** (5 connections) — `server/services/container_service_session.py`
- **._validate_container_close()** (5 connections) — `server/services/container_service_session.py`
- **.get_container_token()** (4 connections) — `server/services/container_service_session.py`
- **._remove_container_from_open_list()** (4 connections) — `server/services/container_service_session.py`
- **ContainerComponent** (2 connections)
- **Player** (2 connections)
- **Open a container for interaction. Raises: ContainerNotFoundError: If container…** (1 connections) — `server/services/container_service_session.py`
- **Validate that container is open and mutation token is valid.** (1 connections) — `server/services/container_service_session.py`
- **Remove container from open containers dictionary.** (1 connections) — `server/services/container_service_session.py`
- **Log container close event to audit log.** (1 connections) — `server/services/container_service_session.py`
- **Close a container and release mutation guard. Args: container_id: Container…** (1 connections) — `server/services/container_service_session.py`
- **Get existing mutation token if container is already open by this player. Args:…** (1 connections) — `server/services/container_service_session.py`
- **Open/close sessions for containers.** (1 connections) — `server/services/container_service_session.py`
- **Sealed/locked gates for open_container (admin/key exceptions included).** (1 connections) — `server/services/container_service_session.py`
- **Track open token; error if this player already has the container open.** (1 connections) — `server/services/container_service_session.py`
- **Best-effort audit for container_open.** (1 connections) — `server/services/container_service_session.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (1 shared connections)
- [ContainerAccessMixin](ContainerAccessMixin.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/services/container_service_session.py`

## Audit Trail

- EXTRACTED: 51 (88%)
- INFERRED: 7 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*