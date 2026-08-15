# NPCCombatIntegrationReadApi

> 29 nodes

## Key Concepts

- **NPCCombatIntegrationReadApi** (7 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (6 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (6 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (5 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (4 connections) — `server/services/player_combat_service_support.py`
- **UUID** (4 connections)
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **.publish()** (2 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **Minimal event bus surface used by player combat service.** (1 connections) — `server/services/player_combat_service_support.py`
- **Publish a domain event.** (1 connections) — `server/services/player_combat_service_support.py`
- **NPC combat rewards helper.** (1 connections) — `server/services/player_combat_service_support.py`
- **Award XP to the killer for an NPC defeat.** (1 connections) — `server/services/player_combat_service_support.py`
- **UUID mapping helper with XP lookup (NPCCombatUUIDMapping).** (1 connections) — `server/services/player_combat_service_support.py`
- **Return stored XP for npc_id when present.** (1 connections) — `server/services/player_combat_service_support.py`
- **Public read API from NPC combat integration.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return rewards helper service.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return UUID mapping helper.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 4 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*