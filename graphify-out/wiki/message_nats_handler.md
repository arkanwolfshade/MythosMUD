# message nats handler

> 53 nodes

## Key Concepts

- **test_combat_death_handler.py** (30 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **.check_connection_state()** (5 connections) — `server/services/combat_cleanup_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (3 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (3 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **handler()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **combat()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **player_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **npc_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **Check connection state before publishing combat ended event.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Return canonical room id when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`
- **Handles combat death events and state changes.** (1 connections) — `server/services/combat_death_handler.py`
- **Initialize the death handler.          Args:             combat_service: Refe** (1 connections) — `server/services/combat_death_handler.py`
- **Return connection manager from CombatService getter when exposed.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle player death events including mortally wounded, death, and corpse creatio** (1 connections) — `server/services/combat_death_handler.py`
- *... and 28 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (13 shared connections)
- [Item Instances](Item_Instances.md) (9 shared connections)
- [command factories exploration](command_factories_exploration.md) (8 shared connections)
- [game chat service](game_chat_service.md) (6 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (2 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (2 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/tests/unit/services/test_combat_death_handler.py`

## Audit Trail

- EXTRACTED: 147 (85%)
- INFERRED: 26 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*