# Inventory Command Models

> 380 nodes

## Key Concepts

- **NATSError** (98 connections) — `server/services/nats_exceptions.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (17 connections) — `server/realtime/message_formatters.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- *... and 355 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (150 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (56 shared connections)
- [Client Event Store](Client_Event_Store.md) (32 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (21 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (15 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (12 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (12 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (12 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (10 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (9 shared connections)
- [Connection State Hooks](Connection_State_Hooks.md) (8 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (7 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/aggro_threat.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 1672 (90%)
- INFERRED: 189 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*