# Community 635

> 26 nodes

## Key Concepts

- **npc_base.py** (25 connections) — `server/npc/npc_base.py`
- **behavior_engine.py** (7 connections) — `server/npc/behavior_engine.py`
- **CommunicationIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **CombatIntegrationProtocol** (4 connections) — `server/npc/npc_protocols.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **register_npc_display_name()** (2 connections) — `server/npc/npc_display_names.py`
- **resolve_npc_display_name()** (2 connections) — `server/npc/npc_display_names.py`
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- **.handle_player_message()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_message_to_room()** (2 connections) — `server/npc/npc_protocols.py`
- **.send_whisper_to_player()** (2 connections) — `server/npc/npc_protocols.py`
- **ABC** (2 connections)
- **Protocol** (2 connections)
- **Behavior engine for NPCs. This module provides the deterministic behavior…** (1 connections) — `server/npc/behavior_engine.py`
- **Base NPC class with stats, inventory, communication, and behavior framework.** (1 connections) — `server/npc/npc_base.py`
- **NPC display names for chat delivery (kept free of ChatService imports).** (1 connections) — `server/npc/npc_display_names.py`
- **Resolve NPC display name for chat speaker_name.** (1 connections) — `server/npc/npc_display_names.py`
- **Remember an NPC display name for NPCSpoke chat bridging.** (1 connections) — `server/npc/npc_display_names.py`
- **Protocols for NPC combat and communication integration (used by NPCBase).** (1 connections) — `server/npc/npc_protocols.py`
- **Handle NPC death in the combat integration layer.** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for communication integration (whisper, room message, handle player…** (1 connections) — `server/npc/npc_protocols.py`
- **Send a private whisper from this NPC to a single player.** (1 connections) — `server/npc/npc_protocols.py`
- **Send a message from this NPC to all players in a room.** (1 connections) — `server/npc/npc_protocols.py`
- **Handle an incoming player message directed at this NPC.** (1 connections) — `server/npc/npc_protocols.py`
- *... and 1 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [Community 325](Community_325.md) (3 shared connections)
- [Community 85](Community_85.md) (3 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (3 shared connections)
- [Community 149](Community_149.md) (2 shared connections)
- [Community 114](Community_114.md) (2 shared connections)
- [Community 35](Community_35.md) (2 shared connections)
- [Community 190](Community_190.md) (1 shared connections)
- [Community 563](Community_563.md) (1 shared connections)
- [Community 756](Community_756.md) (1 shared connections)
- [Community 175](Community_175.md) (1 shared connections)
- [Community 91](Community_91.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/npc/npc_display_names.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*