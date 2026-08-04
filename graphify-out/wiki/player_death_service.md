# player death service

> 6 nodes

## Key Concepts

- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Get the global NPC startup service.** (1 connections) — `server/services/npc_startup_service.py`
- **Create an NPCStartupService instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test get_npc_startup_service() returns service instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [map layout useMapLayout](map_layout_useMapLayout.md) (3 shared connections)
- [realtime player connection](realtime_player_connection.md) (3 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*