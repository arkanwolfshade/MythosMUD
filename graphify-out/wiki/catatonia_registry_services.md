# catatonia registry services

> 14 nodes

## Key Concepts

- **CatatoniaRegistry** (43 connections) — `server/services/catatonia_registry.py`
- **UUID** (6 connections)
- **datetime** (4 connections)
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_sanitarium_failover()** (2 connections) — `server/services/catatonia_registry.py`
- **.__init__()** (1 connections) — `server/services/catatonia_registry.py`
- **Track players who have entered catatonia and coordinate failover hooks.** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if we should trigger sanitarium failover for this player (not deboun** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if the player is currently registered as catatonic.** (1 connections) — `server/services/catatonia_registry.py`
- **Return a shallow copy of the current registry for diagnostics.** (1 connections) — `server/services/catatonia_registry.py`

## Relationships

- [commands time handle](commands_time_handle.md) (6 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [game room service](game_room_service.md) (3 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (3 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (3 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`

## Audit Trail

- EXTRACTED: 72 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*