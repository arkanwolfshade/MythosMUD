# Services Combat Messaging

> 22 nodes · cohesion 0.12

## Key Concepts

- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **CombatMessagingIntegration** (6 connections) — `server/services/combat_messaging/integration.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_integration.py** (6 connections) — `server/services/combat_messaging_integration.py`
- **Any** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_respawn()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._build_mortally_wounded_messages()** (3 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **__init__.py** (2 connections) — `server/services/combat_messaging/__init__.py`
- **Combat messaging integration with real-time messaging system.  This package inte** (1 connections) — `server/services/combat_messaging/__init__.py`
- **Combat messaging integration - composes base and broadcast mixins.  As noted in** (1 connections) — `server/services/combat_messaging/integration.py`
- **Integrates combat messaging with the real-time messaging system.      This servi** (1 connections) — `server/services/combat_messaging/integration.py`
- **Broadcast player respawn message to all players in the room.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Mixin for player lifecycle broadcast methods. Requires connection_manager on sel** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Send DP decay message to a specific mortally wounded player.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Build personal and room messages for mortally wounded broadcast.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Send mortally wounded personal message. Logs warning on failure.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Broadcast player mortally wounded to room. Sends personal message to wounded pla** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Broadcast player death message to all players in the room.** (1 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Combat messaging integration with real-time messaging system.  Re-exports from c** (1 connections) — `server/services/combat_messaging_integration.py`

## Relationships

- [[Combat Player Broadcasts]] (5 shared connections)
- [[Combat Messaging Base]] (3 shared connections)
- [[Combat Services Messaging]] (2 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
