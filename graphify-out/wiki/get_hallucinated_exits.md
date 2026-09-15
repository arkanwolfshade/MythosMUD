# get_hallucinated_exits

> 28 nodes

## Key Concepts

- **get_hallucinated_exits()** (16 connections) — `server/services/exit_hallucination.py`
- **test_exit_hallucination.py** (12 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **exit_hallucination.py** (10 connections) — `server/services/exit_hallucination.py`
- **seed_from()** (7 connections) — `server/services/exit_hallucination.py`
- **mulberry32()** (5 connections) — `server/services/exit_hallucination.py`
- **_hash_string()** (3 connections) — `server/services/exit_hallucination.py`
- **_shuffle()** (3 connections) — `server/services/exit_hallucination.py`
- **test_get_hallucinated_exits_differs_by_player()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_is_stable_for_same_room_and_player()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_matches_js_reference()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_only_uses_the_real_direction_pool()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_mulberry32_yields_floats_in_unit_interval()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_seed_from_matches_js_reference()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_seed_from_order_matters()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **Server-side exit hallucination for the deranged lucidity tier (#626, #714).…** (1 connections) — `server/services/exit_hallucination.py`
- **32-bit string hash (djb2 variant) -- port of hashString() in…** (1 connections) — `server/services/exit_hallucination.py`
- **Combine room + player into a single seed -- order matters, port of seedFrom().** (1 connections) — `server/services/exit_hallucination.py`
- **mulberry32: small, fast, deterministic PRNG -- port of mulberry32() in…** (1 connections) — `server/services/exit_hallucination.py`
- **Deterministic shuffle driven by rng -- port of shuffle() (random-key sort, not…** (1 connections) — `server/services/exit_hallucination.py`
- **Return this viewer's seeded, deterministic fake exit set for this room (#626,…** (1 connections) — `server/services/exit_hallucination.py`
- **Unit tests for server-side exit hallucination (#626, #714). Golden values in…** (1 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **seed_from(room, player) must match the Node reference exactly (bit-for-bit…** (1 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **Room and player aren't interchangeable in the seed -- different rooms,…** (1 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **Golden values from the Node reference implementation -- see module docstring.** (1 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **Same (room, player) must yield the same lie every time -- stable across re-…** (1 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [game_state_provider.py](game_state_provider.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/services/exit_hallucination.py`
- `server/tests/unit/services/test_exit_hallucination.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*