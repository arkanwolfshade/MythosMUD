# HallucinationRng

> 13 nodes

## Key Concepts

- **HallucinationRng** (9 connections) — `server/services/hallucination_rng.py`
- **test_hallucination_rng.py** (6 connections) — `server/tests/unit/services/test_hallucination_rng.py`
- **.get()** (4 connections) — `server/services/hallucination_rng.py`
- **.reset()** (2 connections) — `server/services/hallucination_rng.py`
- **test_get_returns_same_instance_across_calls()** (2 connections) — `server/tests/unit/services/test_hallucination_rng.py`
- **test_reset_forces_reread_of_config()** (2 connections) — `server/tests/unit/services/test_hallucination_rng.py`
- **test_seeded_rng_is_deterministic()** (2 connections) — `server/tests/unit/services/test_hallucination_rng.py`
- **Random** (2 connections)
- **.__init__()** (1 connections) — `server/services/hallucination_rng.py`
- **Lazily-seeded `random.Random`, shared by every hallucination call site.** (1 connections) — `server/services/hallucination_rng.py`
- **Return the shared RNG, seeding it from config on first use.** (1 connections) — `server/services/hallucination_rng.py`
- **Drop the cached RNG so the next `get()` re-reads the config seed (tests).** (1 connections) — `server/services/hallucination_rng.py`
- **Unit tests for the shared hallucination RNG (#714).** (1 connections) — `server/tests/unit/services/test_hallucination_rng.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/services/hallucination_rng.py`
- `server/tests/unit/services/test_hallucination_rng.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*