# E 2 E Testing Guide

> 16 nodes

## Key Concepts

- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **datetime** (3 connections)
- **ContainerComponent** (2 connections)
- **Container WebSocket event emission for unified container system.  As documented** (1 connections) — `server/services/container_websocket_events.py`
- **Emit container.opened event to the opening player.      Args:         connection** (1 connections) — `server/services/container_websocket_events.py`
- **Emit container.opened event to all players in the room.      This is used to not** (1 connections) — `server/services/container_websocket_events.py`
- **Emit container.updated event with diff to room occupants.      Args:         con** (1 connections) — `server/services/container_websocket_events.py`
- **Emit container.closed event to room occupants.      Args:         connection_man** (1 connections) — `server/services/container_websocket_events.py`
- **Emit container.decayed event to room occupants.      This event is emitted when** (1 connections) — `server/services/container_websocket_events.py`

## Relationships

- [Database Manager Tests](Database_Manager_Tests.md) (17 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (8 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (2 shared connections)
- [test_emit_container_opened](test_emit_container_opened.md) (1 shared connections)
- [Product Requirements Document](Product_Requirements_Document.md) (1 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (1 shared connections)

## Source Files

- `server/services/container_websocket_events.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*