# server services phantom hostile service

> 26 nodes

## Key Concepts

- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Any** (1 connections)
- **Remove a phantom hostile from tracking. Args: player_id: Player UUID…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Get list of active phantom IDs for a player. Args: player_id: Player UUID…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Clear all phantom hostiles for a player. Args: player_id: Player UUID** (1 connections) — `server/services/phantom_hostile_service.py`
- **Service for managing phantom hostile spawns for hallucinations. NOTE: This is a…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Initialize the phantom hostile service.** (1 connections) — `server/services/phantom_hostile_service.py`
- **Check if a phantom hostile should spawn based on tier. Args: tier: Current…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Generate a random phantom hostile name. Returns: Random phantom hostile name** (1 connections) — `server/services/phantom_hostile_service.py`
- **Create phantom hostile data structure. Args: player_id: Player UUID who will…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Fractured tier uses 15% spawn chance.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Deranged tier always allows phantom spawn.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Generated name comes from phantom name pool.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 1 more nodes in this community*

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (5 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*