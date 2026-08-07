# admin auth service

> 41 nodes

## Key Concepts

- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **CombatSchemaValidationError** (17 connections) — `server/schemas/combat/combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **get_combat_stats_summary()** (6 connections) — `server/schemas/combat/combat_schema.py`
- **Any** (5 connections)
- **validate_message_template_variables()** (4 connections) — `server/schemas/combat/combat_schema.py`
- **Draft7Validator** (4 connections)
- **test_validate_base_stats_combat_data_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_invalid_type()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_missing_required()** (4 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_base_stats_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_behavior_config_combat_data_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_combat_messages_valid()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_config()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_validate_npc_combat_data()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_get_combat_stats_summary()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Combat domain schemas: combat JSON schema validation and defaults.** (1 connections) — `server/schemas/combat/__init__.py`
- **Exception** (1 connections)
- **Raised when combat data fails schema validation.** (1 connections) — `server/schemas/combat/combat_schema.py`
- **Validate base_stats combat data against schema.      Args:         data: Base st** (1 connections) — `server/schemas/combat/combat_schema.py`
- *... and 16 more nodes in this community*

## Relationships

- [room look commands](room_look_commands.md) (9 shared connections)
- [skill game service](skill_game_service.md) (6 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [useDraggablePanelInteractions draggableP](useDraggablePanelInteractions_draggableP.md) (1 shared connections)

## Source Files

- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 153 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*