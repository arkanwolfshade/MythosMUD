# NATSService

> 154 nodes

## Key Concepts

- **models/combat.py** (59 connections) — `server/models/combat.py`
- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_death_handler.py** (20 connections) — `server/services/combat_death_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatCleanupHandler** (9 connections) — `server/services/combat_cleanup_handler.py`
- **apply_target_rest_and_grace_checks()** (9 connections) — `server/services/combat_service_start.py`
- **test_combat_initialization.py** (9 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **check_target_rest_and_grace_period()** (6 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (6 connections) — `server/services/combat_service_start.py`
- *... and 129 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (29 shared connections)
- [MythosMUDError](MythosMUDError.md) (27 shared connections)
- [User](User.md) (25 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (24 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (12 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (11 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (10 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (10 shared connections)
- [.get_instance](get_instance.md) (9 shared connections)
- [ChatMessage](ChatMessage.md) (8 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (5 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 448 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*