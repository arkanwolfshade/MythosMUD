# initialize nats and combat services()

> 362 nodes

## Key Concepts

- **CombatService** (178 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 337 more nodes in this community*

## Relationships

- [combat](combat.md) (102 shared connections)
- [. init ()](_init_%28%29.md) (77 shared connections)
- [get current tick()](get_current_tick%28%29.md) (45 shared connections)
- [main()](main%28%29.md) (44 shared connections)
- [.end combat()](end_combat%28%29.md) (27 shared connections)
- [.initialize()](initialize%28%29.md) (24 shared connections)
- [Spell Targeting](Spell_Targeting.md) (24 shared connections)
- [Any](Any.md) (23 shared connections)
- [combat initialization](combat_initialization.md) (23 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (14 shared connections)
- [.store npc xp mapping for](store_npc_xp_mapping_for.md) (14 shared connections)
- [Player Position Service](Player_Position_Service.md) (10 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/events/combat_events.py`
- `server/game/player_service.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_types.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 1669 (91%)
- INFERRED: 162 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*