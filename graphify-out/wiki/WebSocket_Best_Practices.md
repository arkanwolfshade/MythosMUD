# WebSocket Best Practices

> 44 nodes

## Key Concepts

- **PartyService** (33 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (4 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader. Returns dict with success…** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband. If…** (1 connections) — `server/game/party_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [_apply_arena_seed_patch.py](_apply_arena_seed_patch.py.md) (6 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [id](id.md) (3 shared connections)
- [Chat Messages Not Displayed to Sender (Bug #2)](Chat_Messages_Not_Displayed_to_Sender_Bug__2.md) (2 shared connections)
- [SafeHtml.tsx](SafeHtml.tsx.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [passive_lucidity_flux_tick Performance Alert](passive_lucidity_flux_tick_Performance_Alert.md) (1 shared connections)
- [Python Code Coverage Status](Python_Code_Coverage_Status.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 115 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*