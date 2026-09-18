# Community 275

> 57 nodes

## Key Concepts

- **models/combat.py** (60 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **_get_default_damage()** (5 connections) — `server/models/combat.py`
- **Enum** (5 connections)
- **cleanup_handler()** (4 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **UUID** (4 connections)
- **.clear_queued_actions()** (3 connections) — `server/models/combat.py`
- **.get_queued_actions()** (3 connections) — `server/models/combat.py`
- **.queue_action()** (3 connections) — `server/models/combat.py`
- **test_get_default_damage_fallback_on_error()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_get_default_damage_from_config()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_end_combat_method()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **asyncio** (3 connections)
- **fixture** (3 connections)
- **test_check_connection_state()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- *... and 32 more nodes in this community*

## Relationships

- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (19 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (13 shared connections)
- [Community 46](Community_46.md) (11 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (11 shared connections)
- [Community 81](Community_81.md) (7 shared connections)
- [Community 97](Community_97.md) (6 shared connections)
- [Community 370](Community_370.md) (3 shared connections)
- [Community 264](Community_264.md) (3 shared connections)
- [Community 261](Community_261.md) (3 shared connections)
- [Community 542](Community_542.md) (2 shared connections)
- [Community 277](Community_277.md) (2 shared connections)
- [Community 174](Community_174.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 172 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*