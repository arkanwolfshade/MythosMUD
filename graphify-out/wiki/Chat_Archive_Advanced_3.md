# Chat Archive Advanced

> 4 nodes

## Key Concepts

- **quest_service()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **Return quest_service.sync_collect_progress when it is callable.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **QuestService with mocked repos.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (2 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (2 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (1 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)
- [Command Service Tests](Command_Service_Tests.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 8 (53%)
- INFERRED: 7 (47%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*