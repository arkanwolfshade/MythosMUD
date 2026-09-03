# Combat Loader

> 38 nodes

## Key Concepts

- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **asyncio** (6 connections)
- **test_handle_attack_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_combat_command_handler_creates_singleton()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **reset_combat_handler()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_returns_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_combat_command_handler_requires_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- *... and 13 more nodes in this community*

## Relationships

- [Combat Handler](Combat_Handler.md) (7 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (7 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (4 shared connections)
- [Test Flee Command](Test_Flee_Command.md) (3 shared connections)
- [Test Combat Helpers](Test_Combat_Helpers.md) (3 shared connections)
- [Test Player Combat Service](Test_Player_Combat_Service.md) (2 shared connections)
- [Combat Flee](Combat_Flee.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Combat Validator](Combat_Validator.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 117 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*