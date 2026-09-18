# Community 200

> 70 nodes

## Key Concepts

- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **room_update_event_builder.py** (19 connections) — `server/realtime/room_update_event_builder.py`
- **room_viewer_fanout.py** (18 connections) — `server/realtime/room_viewer_fanout.py`
- **get_hallucinated_exits()** (16 connections) — `server/services/exit_hallucination.py`
- **get_viewer_phantom_names()** (13 connections) — `server/services/phantom_visibility.py`
- **test_exit_hallucination.py** (12 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **send_personalized_room_events()** (10 connections) — `server/realtime/room_viewer_fanout.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **exit_hallucination.py** (10 connections) — `server/services/exit_hallucination.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **lucidity_tier_cache.py** (8 connections) — `server/services/lucidity_tier_cache.py`
- **RoomOccupancyPayload** (7 connections) — `server/realtime/room_update_event_builder.py`
- **seed_from()** (7 connections) — `server/services/exit_hallucination.py`
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **mulberry32()** (5 connections) — `server/services/exit_hallucination.py`
- **test_get_viewer_phantom_names_matches_own_room()** (4 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_false_when_no_phantoms_or_deranged()** (4 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_has_phantoms()** (4 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_is_deranged()** (4 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **_hash_string()** (3 connections) — `server/services/exit_hallucination.py`
- **_shuffle()** (3 connections) — `server/services/exit_hallucination.py`
- *... and 45 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Community 222](Community_222.md) (11 shared connections)
- [Community 90](Community_90.md) (7 shared connections)
- [Community 896](Community_896.md) (6 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (5 shared connections)
- [Community 92](Community_92.md) (5 shared connections)
- [Community 42](Community_42.md) (5 shared connections)
- [Community 467](Community_467.md) (4 shared connections)
- [Community 38](Community_38.md) (4 shared connections)
- [Community 62](Community_62.md) (4 shared connections)
- [Community 87](Community_87.md) (3 shared connections)
- [Community 95](Community_95.md) (3 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/exit_hallucination.py`
- `server/services/lucidity_tier_cache.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/services/test_exit_hallucination.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 191 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*