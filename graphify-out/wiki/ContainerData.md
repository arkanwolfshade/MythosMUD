# ContainerData

> 20 nodes

## Key Concepts

- **party_commands.py** (19 connections) — `server/commands/party_commands.py`
- **handle_party_command()** (12 connections) — `server/commands/party_commands.py`
- **Any** (9 connections)
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_chat()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (4 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (3 connections) — `server/commands/party_commands.py`
- **Party commands for MythosMUD.  Handlers for party, party invite <name>, party le** (1 connections) — `server/commands/party_commands.py`
- **Get application container from request.** (1 connections) — `server/commands/party_commands.py`
- **Resolve container, party service, persistence, and current player for party comm** (1 connections) — `server/commands/party_commands.py`
- **Handle party <message> (send to party chat).** (1 connections) — `server/commands/party_commands.py`
- **Handle party [invite|leave|kick|list]. No subcommand = party status/list.** (1 connections) — `server/commands/party_commands.py`
- **Handle party invite <name> logic. Uses confirmation pattern: target must accept.** (1 connections) — `server/commands/party_commands.py`
- **Handle party kick <name> logic.** (1 connections) — `server/commands/party_commands.py`
- **Handle party status/list output.** (1 connections) — `server/commands/party_commands.py`
- **Get display name for a party member ID.** (1 connections) — `server/commands/party_commands.py`

## Relationships

- [CombatService](CombatService.md) (5 shared connections)
- [Player Position Service](Player_Position_Service.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [websocket integration](websocket_integration.md) (1 shared connections)

## Source Files

- `server/commands/party_commands.py`

## Audit Trail

- EXTRACTED: 83 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*