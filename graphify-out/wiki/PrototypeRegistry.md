# PrototypeRegistry

> 76 nodes · cohesion 0.04

## Key Concepts

- **CommunicationCommandFactory** (42 connections) — `server/utils/command_factories_communication.py`
- **test_command_factories_communication.py** (31 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_global_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **test_create_channel_command_default_no_channel()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_channel_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_emote_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_global_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_too_long()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_me_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_empty_message()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_say_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_system_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_message()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_too_long()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- *... and 51 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (16 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (10 shared connections)
- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [HeaderBar.tsx](HeaderBar.tsx.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [test_nats_service_pool.py](test_nats_service_pool.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 126 (75%)
- INFERRED: 42 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*