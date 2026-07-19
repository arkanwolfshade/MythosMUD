# Quest Game Events

> 16 nodes · cohesion 0.18

## Key Concepts

- **quest_events.py** (12 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (8 connections) — `server/game/quest/quest_events.py`
- **Any** (7 connections) — `server/game/quest/quest_events.py`
- **UUID** (5 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_entered()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (3 connections) — `server/game/quest/quest_events.py`
- **_entity_id_for_quest_offer()** (2 connections) — `server/game/quest/quest_events.py`
- **Quest event subscriptions: room entry (trigger start), room exit (complete_activ** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for NPCDied that records kill for kill_N goals when kill** (1 connections) — `server/game/quest/quest_events.py`
- **Parse player_id string to UUID. Returns None if invalid.** (1 connections) — `server/game/quest/quest_events.py`
- **Return entity_id for quest_offers lookup: strip instance_<uuid>_ prefix if prese** (1 connections) — `server/game/quest/quest_events.py`
- **Subscribe to room events for quest triggers and progress.      - PlayerEnteredRo** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerEnteredRoom (entering via exit); starts room-o** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerLeftRoom that records exit_<room_id> activity.** (1 connections) — `server/game/quest/quest_events.py`

## Relationships

- [[Distributed Event Bus]] (3 shared connections)
- [[NPC Services Bundle]] (3 shared connections)
- [[NPC Death Lifecycle]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Lifespan Startup Hooks]] (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`

## Audit Trail

- EXTRACTED: 50 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
