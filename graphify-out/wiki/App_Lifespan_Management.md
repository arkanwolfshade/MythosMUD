# App Lifespan Management

> 12 nodes · cohesion 0.01

## Key Concepts

- **UUID** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **Any** (6 connections) — `server/services/combat_turn_processor.py`
- **UUID** (5 connections) — `server/services/combat_flee_handler.py`
- **UUID** (4 connections) — `server/models/combat.py`
- **UUID** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **Any** (3 connections) — `server/services/combat_flee_handler.py`
- **UUID** (3 connections) — `server/services/combat_service_end.py`
- **UUID** (3 connections) — `server/services/combat_turn_processor.py`
- **MonkeyPatch** (3 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **UUID** (2 connections) — `server/services/combat_attack_handler.py`
- **UUID** (2 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **MonkeyPatch** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 31 (70%)
- INFERRED: 13 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*