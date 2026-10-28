# fastapi_integration.py

> 49 nodes · cohesion 0.09

## Key Concepts

- **SpellLearningService** (49 connections) — `server/game/magic/spell_learning_service.py`
- **spell_learning_service.py** (25 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_learning_service.py** (16 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **Any** (12 connections)
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **asyncio** (12 connections)
- **UUID** (10 connections)
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **._load_spell_learn_context()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **._apply_mythos_corruption_on_learn()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._check_required_spell_prerequisites()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._persist_spell_learning()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **test_learn_mythos_spell_applies_corruption()** (5 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **._check_intelligence_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_power_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._spell_learn_success_response()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **._resolve_spell()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **learning_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_increase_mastery_on_cast()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_already_known()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (14 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (6 shared connections)
- [reset_database](reset_database.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (4 shared connections)
- [CORSConfig](CORSConfig.md) (4 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_item.py](test_item.py.md) (2 shared connections)
- [_str_id](_str_id.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [endpoints.py](endpoints.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 133 (86%)
- INFERRED: 22 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*