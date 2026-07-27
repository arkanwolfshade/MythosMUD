# Connection Disconnection Cleanup

> 8 nodes · cohesion 0.01

## Key Concepts

- **AttributeError** (39 connections) — `server/npc/combat_integration_base.py`
- **Any** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Any** (4 connections) — `server/services/combat_messaging/base.py`
- **UUID** (3 connections) — `server/realtime/envelope.py`
- **Any** (3 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (3 connections) — `server/realtime/websocket_room_updates.py`
- **UUID** (2 connections) — `server/realtime/integration/room_event_handler.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/envelope.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`

## Audit Trail

- EXTRACTED: 26 (39%)
- INFERRED: 40 (61%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*