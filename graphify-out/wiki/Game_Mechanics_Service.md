# Game Mechanics Service

> 69 nodes · cohesion 0.04

## Key Concepts

- **NPCCombatIntegrationBase** (28 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (20 connections) — `server/npc/combat_integration_base.py`
- **GameMechanicsService** (16 connections) — `server/game/mechanics.py`
- **NpcCombatServiceProtocol** (12 connections) — `server/npc/combat_integration_protocols.py`
- **ABC** (10 connections)
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (6 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (4 connections) — `server/npc/combat_integration_base.py`
- **UUID** (4 connections) — `server/npc/combat_integration_base.py`
- **.apply_corruption()** (3 connections) — `server/game/mechanics.py`
- **.apply_fear()** (3 connections) — `server/game/mechanics.py`
- **.damage_player()** (3 connections) — `server/game/mechanics.py`
- **.gain_experience()** (3 connections) — `server/game/mechanics.py`
- **.heal_player()** (3 connections) — `server/game/mechanics.py`
- **.__init__()** (3 connections) — `server/game/mechanics.py`
- *... and 44 more nodes in this community*

## Relationships

- [[NPC Admin API]] (21 shared connections)
- [[NPC Services Bundle]] (8 shared connections)
- [[Look Command Helpers]] (4 shared connections)
- [[WebSocket Message Handlers]] (3 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[Channel Broadcast Strategies]] (2 shared connections)
- [[Validation Rule Base]] (2 shared connections)
- [[NPC Combat Lifecycle]] (2 shared connections)
- [[Services Service Room]] (2 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 225 (92%)
- INFERRED: 20 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
