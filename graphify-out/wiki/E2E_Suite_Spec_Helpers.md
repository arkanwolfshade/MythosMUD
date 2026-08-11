# E2E Suite Spec Helpers

> 16 nodes

## Key Concepts

- **.get_npc_definition()** (5 connections) — `server/services/npc_combat_data_provider.py`
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
- **Get NPC definition for an NPC instance.          Uses persistence.get_npc_life** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get player name for messaging.          Args:             player_id: ID of th** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get the current room ID for a player.          Args:             player_id: I** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get player combat participant data from persistence.          Args:** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get NPC combat participant data from NPC instance.          Args:** (1 connections) — `server/services/npc_combat_data_provider.py`

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (8 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*