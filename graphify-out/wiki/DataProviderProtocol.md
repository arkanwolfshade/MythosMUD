# DataProviderProtocol

> 8 nodes

## Key Concepts

- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **.get_npc_instance()** (3 connections) — `server/services/combat_service_npc.py`
- **.get_player_room_id()** (3 connections) — `server/services/combat_service_npc.py`
- **Protocol for room and NPC lookups used by combat helpers.** (1 connections) — `server/services/combat_service_npc.py`
- **Return current room id for a player id.** (1 connections) — `server/services/combat_service_npc.py`
- **Return NPC instance for a string NPC id.** (1 connections) — `server/services/combat_service_npc.py`
- **Safely fetch data provider from integration service.** (1 connections) — `server/services/combat_service_npc.py`

## Relationships

- [CombatInstance](CombatInstance.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/services/combat_service_npc.py`

## Audit Trail

- EXTRACTED: 12 (86%)
- INFERRED: 2 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*