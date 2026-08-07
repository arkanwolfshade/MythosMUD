# AppRouter main AppRouter()

> 4 nodes

## Key Concepts

- **get_invite_codes.py** (4 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **get_10_active_invites()** (4 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **main()** (2 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **Get 10 active invite codes from the database.** (1 connections) — `e2e-tests/load-tests/get_invite_codes.py`

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*