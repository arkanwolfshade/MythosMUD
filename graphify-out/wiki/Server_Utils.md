# Server Utils

> 211 nodes

## Key Concepts

- **ValidationError** (536 connections) — `server/exceptions.py`
- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **CommunicationCommandFactory** (15 connections) — `server/utils/command_factories_communication.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **Test create_say_command() raises error with no args.** (7 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **.create_local_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.gain_occult_knowledge()** (6 connections) — `server/game/mechanics.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/mechanics.py`
- **Test create_pickup_command() raises error when quantity is negative.** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- *... and 186 more nodes in this community*

## Relationships

- [Server Models](Server_Models.md) (51 shared connections)
- [Server Game](Server_Game.md) (36 shared connections)
- [Server Api](Server_Api.md) (29 shared connections)
- [Server Infrastructure (2)](Server_Infrastructure_%282%29.md) (28 shared connections)
- [Server Models (5)](Server_Models_%285%29.md) (28 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (26 shared connections)
- [Server Models (4)](Server_Models_%284%29.md) (20 shared connections)
- [Server Utils (2)](Server_Utils_%282%29.md) (20 shared connections)
- [Server Utils (4)](Server_Utils_%284%29.md) (18 shared connections)
- [Server Game (6)](Server_Game_%286%29.md) (14 shared connections)
- [Server Utils (5)](Server_Utils_%285%29.md) (14 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (13 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/profession_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 808 (63%)
- INFERRED: 469 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*