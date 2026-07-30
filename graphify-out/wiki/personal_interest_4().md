# personal interest 4()

> 16 nodes

## Key Concepts

- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_entered()** (5 connections) — `server/game/quest/quest_events.py`
- **Any** (4 connections)
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (3 connections) — `server/game/quest/quest_events.py`
- **_entity_id_for_quest_offer()** (2 connections) — `server/game/quest/quest_events.py`
- **UUID** (2 connections)
- **Quest event subscriptions: room entry (trigger start), room exit (complete_activ** (1 connections) — `server/game/quest/quest_events.py`
- **Return entity_id for quest_offers lookup: strip instance_<uuid>_ prefix if prese** (1 connections) — `server/game/quest/quest_events.py`
- **Subscribe to room events for quest triggers and progress.      - PlayerEnteredRo** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerEnteredRoom (entering via exit); starts room-o** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for PlayerLeftRoom that records exit_<room_id> activity.** (1 connections) — `server/game/quest/quest_events.py`
- **Return an async handler for NPCDied that records kill for kill_N goals when kill** (1 connections) — `server/game/quest/quest_events.py`
- **Parse player_id string to UUID. Returns None if invalid.** (1 connections) — `server/game/quest/quest_events.py`

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (1 shared connections)
- [test quest service](test_quest_service.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`

## Audit Trail

- EXTRACTED: 52 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*