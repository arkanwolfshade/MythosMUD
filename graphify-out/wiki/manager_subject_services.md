# manager subject services

> 75 nodes

## Key Concepts

- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_controller.py** (27 connections) — `server/api/admin/subject_controller.py`
- **test_subject_controller.py** (21 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **InvalidPatternError** (19 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (12 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (10 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (8 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **BaseModel** (6 connections)
- **test_register_pattern_invalid()** (6 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 50 more nodes in this community*

## Relationships

- [commands communication support](commands_communication_support.md) (14 shared connections)
- [manager subject services](manager_subject_services.md) (14 shared connections)
- [Exception Containers](Exception_Containers.md) (10 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [zone npc config](zone_npc_config.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [admin auth service](admin_auth_service.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [subject validation services](subject_validation_services.md) (2 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [manager services nats](manager_services_nats.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/api/admin/test_subject_controller.py`

## Audit Trail

- EXTRACTED: 326 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*