# command communication models

> 128 nodes

## Key Concepts

- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **SayCommand** (13 connections) — `server/models/command_communication.py`
- **PoseCommand** (13 connections) — `server/models/command_communication.py`
- **LocalCommand** (12 connections) — `server/models/command_communication.py`
- **SystemCommand** (12 connections) — `server/models/command_communication.py`
- **EmoteCommand** (12 connections) — `server/models/command_communication.py`
- **MeCommand** (12 connections) — `server/models/command_communication.py`
- **ReplyCommand** (12 connections) — `server/models/command_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_pose_command()** (5 connections) — `server/utils/command_factories_communication.py`
- **test_say_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_say_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_me_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- *... and 103 more nodes in this community*

## Relationships

- [add used user](add_used_user.md) (34 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (25 shared connections)
- [command inventory factories](command_inventory_factories.md) (15 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (9 shared connections)
- [Inventory Equip](Inventory_Equip.md) (6 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 380 (92%)
- INFERRED: 35 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*