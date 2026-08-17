# UUID

> 15 nodes

## Key Concepts

- **UUID** (7 connections)
- **.convert_to_uuid()** (4 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_uuid_for_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_xp_value()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.is_valid_uuid()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.store_string_id_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.store_xp_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Check if a string is a valid UUID. Args: uuid_string: String to check Returns:…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Convert string ID to UUID, creating new UUID if needed. For non-UUID string IDs…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Store UUID-to-string ID mapping. Args: uuid_id: UUID of the entity string_id:…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Store UUID-to-XP mapping. Args: uuid_id: UUID of the NPC xp_value: XP value for…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Get the UUID that was stored for a given string ID (reverse of…** (1 connections) — `server/services/npc_combat_uuid_mapping.py`

## Relationships

- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*