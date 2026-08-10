# Combat DP Persistence Tests

> 23 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Initialize empty party store. Optionally provide event_bus, connection_manager,** (1 connections) — `server/game/party_service.py`
- **Emit PartyUpdated event if event_bus is set.** (1 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader.          Returns dict with s** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband.** (1 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in a** (1 connections) — `server/game/party_service.py`
- **Safely schedule an async notification, handling cases where no event loop is run** (1 connections) — `server/game/party_service.py`
- **Notify a player they have been removed from a party. Resolves leader name.** (1 connections) — `server/game/party_service.py`
- **Remove a player from a party (leave or internal remove). If leader leaves,** (1 connections) — `server/game/party_service.py`
- **Remove a member from the party. Only the leader may kick.** (1 connections) — `server/game/party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Commands Npc Admin](Commands_Npc_Admin.md) (20 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (8 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (8 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (2 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 121 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*