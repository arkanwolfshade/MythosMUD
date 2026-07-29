# Schedule end combat if npc

> 37 nodes

## Key Concepts

- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- **.listen()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **._update_determination_points()** (3 connections) — `server/npc/npc_base.py`
- **test_schedule_end_combat_if_npc_died_no_service()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_running_loop()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Protocol** (2 connections)
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_whisper_to_player()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_message_to_room()** (2 connections) — `server/npc/npc_protocols.py`
- **.handle_player_message()** (2 connections) — `server/npc/npc_protocols.py`
- **Update determination points after taking damage; return new DP.** (1 connections) — `server/npc/npc_base.py`
- **Publish damage event to event bus.** (1 connections) — `server/npc/npc_base.py`
- **Handle NPC death after taking fatal damage.** (1 connections) — `server/npc/npc_base.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be** (1 connections) — `server/npc/npc_base.py`
- **Take damage and update determination points (DP).** (1 connections) — `server/npc/npc_base.py`
- **NPC speaks a message.** (1 connections) — `server/npc/npc_base.py`
- *... and 12 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (13 shared connections)
- [Any](Any.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_protocols.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 90 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*