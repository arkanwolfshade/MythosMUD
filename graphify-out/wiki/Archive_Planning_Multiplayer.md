# Archive Planning Multiplayer

> 14 nodes

## Key Concepts

- **UUID** (5 connections)
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **Any** (4 connections)
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_combat_data()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_name()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **Initialize the data provider.          Args:             async_persistence: A** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get NPC instance from the spawning service.          Args:             npc_id** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get player name for messaging.          Args:             player_id: ID of th** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get the current room ID for a player.          Args:             player_id: I** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get player combat participant data from persistence.          Args:** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get NPC combat participant data from NPC instance.          Args:** (1 connections) — `server/services/npc_combat_data_provider.py`

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*