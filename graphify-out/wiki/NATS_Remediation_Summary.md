# Nats Remediation Summary

> 13 nodes

## Key Concepts

- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Any** (5 connections)
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_respawn()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._build_mortally_wounded_messages()** (3 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Build personal and room messages for mortally wounded broadcast.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Send mortally wounded personal message. Logs warning on failure.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Broadcast player mortally wounded to room. Sends personal message to wounded pla** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Broadcast player death message to all players in the room.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Broadcast player respawn message to all players in the room.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Send DP decay message to a specific mortally wounded player.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)

## Source Files

- `server/services/combat_messaging/player_broadcasts.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*