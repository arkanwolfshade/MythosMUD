# CommunicationIntegrationProtocol

> 15 nodes

## Key Concepts

- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- **.handle_player_message()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_message_to_room()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_whisper_to_player()** (2 connections) — `server/npc/npc_protocols.py`
- **Protocol** (2 connections)
- **Protocols for NPC combat and communication integration (used by NPCBase).** (1 connections) — `server/npc/npc_protocols.py`
- **Handle NPC death in the combat integration layer.** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for communication integration (whisper, room message, handle player…** (1 connections) — `server/npc/npc_protocols.py`
- **Send a private whisper from this NPC to a single player.** (1 connections) — `server/npc/npc_protocols.py`
- **Send a message from this NPC to all players in a room.** (1 connections) — `server/npc/npc_protocols.py`
- **Handle an incoming player message directed at this NPC.** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for combat integration handle_npc_death.** (1 connections) — `server/npc/npc_protocols.py`

## Relationships

- [EventBus](EventBus.md) (5 shared connections)

## Source Files

- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 18 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*