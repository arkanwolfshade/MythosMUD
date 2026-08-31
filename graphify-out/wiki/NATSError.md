# NATSError

> 234 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **asyncio** (36 connections)
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **apply_target_rest_and_grace_checks()** (10 connections) — `server/services/combat_service_start.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 209 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (67 shared connections)
- [CombatInstance](CombatInstance.md) (44 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (15 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (13 shared connections)
- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [format_message_content](format_message_content.md) (12 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (10 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (8 shared connections)
- [test_nats_service_pool.py](test_nats_service_pool.py.md) (8 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [.create_combat_instance](create_combat_instance.md) (7 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 632 (87%)
- INFERRED: 92 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*