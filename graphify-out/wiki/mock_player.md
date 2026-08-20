# mock_player

> 5 nodes

## Key Concepts

- **mock_player()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **player_repository()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **fixture** (2 connections)
- **Create a PlayerRepository instance.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **Create a mock player for save operations.** (1 connections) — `server/tests/unit/persistence/test_player_repository.py`

## Relationships

- [test_player_repository.py](test_player_repository.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 6 (75%)
- INFERRED: 2 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*