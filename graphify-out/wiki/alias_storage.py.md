# alias_storage.py

> 21 nodes · cohesion 0.15

## Key Concepts

- **connection_utils.py** (28 connections) — `server/realtime/connection_utils.py`
- **get_npc_disposition_from_instance()** (22 connections) — `server/utils/npc_disposition_lookup.py`
- **npc_disposition_lookup.py** (17 connections) — `server/utils/npc_disposition_lookup.py`
- **npc_occupant()** (13 connections) — `server/utils/npc_disposition_lookup.py`
- **npc_disposition_from_type()** (12 connections) — `server/utils/npc_disposition_lookup.py`
- **npc_disposition_from_row()** (11 connections) — `server/utils/npc_disposition_lookup.py`
- **_npc_instance_service()** (4 connections) — `server/utils/npc_disposition_lookup.py`
- **_NpcInstanceService** (4 connections) — `server/utils/npc_disposition_lookup.py`
- **NpcDisposition** (4 connections)
- **_LifecycleManager** (3 connections) — `server/utils/npc_disposition_lookup.py`
- **Protocol** (2 connections)
- **Utility functions for connection management. This module provides helper…** (1 connections) — `server/realtime/connection_utils.py`
- **NpcOccupant** (1 connections)
- **Resolve and wrap an NPC's wire disposition (#1025, #1036). A leaf module (it…** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **Map an NPC instance's ``npc_type`` (an ``NPCDefinitionType`` value) to its wire…** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **Disposition carried on an NPC occupant row (``disposition``); the NPC id is…** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **One entry of a payload's ``npcs`` list.** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **The slice of the NPC lifecycle manager this lookup reads.** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **The slice of the NPC instance service this lookup reads.** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **The NPC instance service, imported on demand. Uses importlib so this leaf…** (1 connections) — `server/utils/npc_disposition_lookup.py`
- **Disposition of the live NPC instance ``npc_id``; the default when the instance…** (1 connections) — `server/utils/npc_disposition_lookup.py`

## Relationships

- [security.ts](security.ts.md) (11 shared connections)
- [look_container.py](look_container.py.md) (8 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (6 shared connections)
- [Room](Room.md) (4 shared connections)
- [session](session.md) (4 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (4 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (3 shared connections)
- [ChatHistoryPanel.tsx](ChatHistoryPanel.tsx.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_utils.py`
- `server/utils/npc_disposition_lookup.py`

## Audit Trail

- EXTRACTED: 73 (74%)
- INFERRED: 25 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*