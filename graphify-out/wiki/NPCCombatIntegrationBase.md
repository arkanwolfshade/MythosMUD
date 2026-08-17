# NPCCombatIntegrationBase

> 25 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **ABC** (2 connections)
- **Handle an NPC attack on a target. This is a thin wrapper around…** (1 connections) — `server/npc/combat_integration_base.py`
- **Core implementation for handling an NPC attack on a target. When the app has…** (1 connections) — `server/npc/combat_integration_base.py`
- **Execute the direct NPC attack path (no full combat service available).** (1 connections) — `server/npc/combat_integration_base.py`
- **Prefer full combat codepath (same as player-initiated combat) when available.…** (1 connections) — `server/npc/combat_integration_base.py`
- **Get target stats from player or use defaults.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses provide NPC stat defaults for damage resolution.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses publish DP updates after direct NPC damage.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses publish NPCAttacked to the event bus.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses forward NPC attacks to NATS for clients.** (1 connections) — `server/npc/combat_integration_base.py`
- **Base implementation: damage, combat effects, and NPC attack orchestration.…** (1 connections) — `server/npc/combat_integration_base.py`
- **Initialize the NPC combat integration. Args: event_bus: Optional EventBus…** (1 connections) — `server/npc/combat_integration_base.py`
- **Calculate damage based on attacker and target stats. Args: attacker_stats:…** (1 connections) — `server/npc/combat_integration_base.py`

## Relationships

- [.apply_combat_effects](apply_combat_effects.md) (10 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*