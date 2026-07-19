# Combat Service Bundle

> 324 nodes · cohesion 0.01

## Key Concepts

- **CombatService** (232 connections) — `server/services/combat_service.py`
- **PlayerCombatService** (87 connections) — `server/services/player_combat_service.py`
- **combat_service.py** (60 connections) — `server/services/combat_service.py`
- **CombatEventPublisher** (50 connections) — `server/services/combat_event_publisher.py`
- **CombatParticipantData** (48 connections) — `server/services/combat_types.py`
- **UUID** (41 connections) — `server/services/combat_service.py`
- **PlayerDeathService** (40 connections) — `server/services/player_death_service.py`
- **CombatInstance** (38 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (36 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCDiedEvent** (34 connections) — `server/events/combat_events.py`
- **CombatParticipant** (34 connections) — `server/services/combat_service.py`
- **CombatPersistenceHandler** (34 connections) — `server/services/combat_persistence_handler.py`
- **NPCTookDamageEvent** (32 connections) — `server/events/combat_events.py`
- **CombatStartedEvent** (30 connections) — `server/events/combat_events.py`
- **CombatDeathHandler** (30 connections) — `server/services/combat_death_handler.py`
- **CombatAttackHandler** (29 connections) — `server/services/combat_attack_handler.py`
- **CombatEventHandler** (29 connections) — `server/services/combat_event_handler.py`
- **CombatResult** (25 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (24 connections) — `server/services/combat_cleanup_handler.py`
- **PlayerCombatService** (23 connections) — `server/services/combat_service.py`
- **CombatParticipantData** (22 connections) — `server/services/combat_service.py`
- **CombatStartedEvent** (22 connections) — `server/services/combat_service.py`
- **EventBus** (22 connections) — `server/services/combat_service.py`
- **NATSService** (22 connections) — `server/services/combat_service.py`
- **NATSSubjectManager** (22 connections) — `server/services/combat_service.py`
- *... and 299 more nodes in this community*

## Relationships

- [[NPC Combat Lifecycle]] (72 shared connections)
- [[Combat Command Handler]] (58 shared connections)
- [[Combat Domain Events]] (52 shared connections)
- [[Magic Service Bundle]] (28 shared connections)
- [[Distributed Event Bus]] (24 shared connections)
- [[Spell Effect Protocols]] (23 shared connections)
- [[Player Combat XP]] (21 shared connections)
- [[Combat Taunt Tests]] (21 shared connections)
- [[Player Respawn Service]] (20 shared connections)
- [[Combat Turn Processor]] (20 shared connections)
- [[Combat Attack Service]] (20 shared connections)
- [[NPC Admin API]] (18 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/events/combat_events.py`
- `server/game/magic/spell_targeting.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_initialization.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_types.py`
- `server/services/player_combat_service.py`
- `server/services/player_death_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_combat_initialization.py`

## Audit Trail

- EXTRACTED: 1268 (61%)
- INFERRED: 811 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
