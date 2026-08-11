# Logging System Planning

> 19 nodes

## Key Concepts

- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- **.listen()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **Protocol** (2 connections)
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_whisper_to_player()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_message_to_room()** (2 connections) — `server/npc/npc_protocols.py`
- **.handle_player_message()** (2 connections) — `server/npc/npc_protocols.py`
- **NPC speaks a message.** (1 connections) — `server/npc/npc_base.py`
- **NPC receives/listens to a message.** (1 connections) — `server/npc/npc_base.py`
- **Protocols for NPC combat and communication integration (used by NPCBase).** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for combat integration handle_npc_death.** (1 connections) — `server/npc/npc_protocols.py`
- **Handle NPC death in the combat integration layer.** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for communication integration (whisper, room message, handle player mes** (1 connections) — `server/npc/npc_protocols.py`
- **Send a private whisper from this NPC to a single player.** (1 connections) — `server/npc/npc_protocols.py`
- **Send a message from this NPC to all players in a room.** (1 connections) — `server/npc/npc_protocols.py`
- **Handle an incoming player message directed at this NPC.** (1 connections) — `server/npc/npc_protocols.py`

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (3 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 41 (85%)
- INFERRED: 7 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*