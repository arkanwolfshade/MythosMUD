# Npc Event Handlers

> 13 nodes

## Key Concepts

- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **Extract spawn_message from behavior_config. Args: behavior_config: The parsed…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the spawn message for an NPC from its behavior_config. If no custom spawn…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Initialize the NPC event handler. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get NPC instance from lifecycle manager. Args: npc_id: The NPC ID Returns: NPC…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Extract behavior_config from NPC instance. Args: npc_instance: The NPC instance…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Parse behavior_config if it's a JSON string. Args: behavior_config: The…** (1 connections) — `server/realtime/npc_event_handlers.py`

## Relationships

- [Npc Event Handlers](Npc_Event_Handlers.md) (7 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Message Builders](Message_Builders.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*