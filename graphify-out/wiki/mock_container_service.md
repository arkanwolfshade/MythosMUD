# mock_container_service

> 8 nodes

## Key Concepts

- **mock_container_service()** (4 connections) — `server/tests/unit/api/test_containers.py`
- **fixture** (4 connections)
- **mock_persistence()** (3 connections) — `server/tests/unit/api/test_containers.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_containers.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_containers.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_containers.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/api/test_containers.py`
- **Create a mock container service.** (1 connections) — `server/tests/unit/api/test_containers.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 11 (85%)
- INFERRED: 2 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*