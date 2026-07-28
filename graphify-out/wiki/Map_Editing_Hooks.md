# Map Editing Hooks

> 28 nodes · cohesion 0.14

## Key Concepts

- **FollowService** (36 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Request to follow a player (pending acceptance) or start following an NPC immedi** (1 connections) — `server/game/follow_service.py`
- **Send follow_request event to the target player only.** (1 connections) — `server/game/follow_service.py`
- **Accept a follow request. Target is the player who accepted (the followee).** (1 connections) — `server/game/follow_service.py`
- **Decline a follow request.** (1 connections) — `server/game/follow_service.py`
- **Return list of follower player IDs (for movement propagation).** (1 connections) — `server/game/follow_service.py`
- **Return (target_id, target_type) if following someone, else None.** (1 connections) — `server/game/follow_service.py`
- **Return stored display name when following an NPC, else None. For players, resolv** (1 connections) — `server/game/follow_service.py`
- **Format who you follow and who follows you for /following output.** (1 connections) — `server/game/follow_service.py`
- **Normalize ID to string for dict keys.** (1 connections) — `server/game/follow_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (20 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (1 shared connections)
- [Loot All Endpoint](Loot_All_Endpoint.md) (1 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)
- [Archive E 2 E Testing](Archive_E_2_E_Testing.md) (1 shared connections)
- [Coverage Strategy Archive](Coverage_Strategy_Archive.md) (1 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 144 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*