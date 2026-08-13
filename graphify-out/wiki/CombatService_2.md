# CombatService

> God node · 181 connections · `server/services/combat_service.py`

**Community:** [CombatService](CombatService.md)

## Connections by Relation

### calls
- initialize_nats_and_combat_services() `EXTRACTED`
- ._create_combat_service_with_nats() `EXTRACTED`
- combat_service() `EXTRACTED`

### contains
- combat_service.py `EXTRACTED`

### imports
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- [game_tick_processing.py](game_tick_processing.py.md) `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- spell_effects.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- magic_service.py `EXTRACTED`
- spell_effects_heal.py `EXTRACTED`
- [combat_taunt.py](combat_taunt.py.md) `EXTRACTED`
- combat_service_npc.py `EXTRACTED`
- combat_service_start.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- combat_loader.py `EXTRACTED`
- magic_service_completion.py `EXTRACTED`
- combat_flee.py `EXTRACTED`
- spell_targeting.py `EXTRACTED`
- combat_turn_processor.py `EXTRACTED`
- npc_combat_integration_validation_mixin.py `EXTRACTED`
- test_combat_service.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- .validate_melee_or_end_combat() `EXTRACTED`
- .finalize_attack_result() `EXTRACTED`
- .start_combat() `EXTRACTED`
- .end_combat_if_npc_died() `EXTRACTED`
- ._handle_player_dp_update() `EXTRACTED`
- .validate_and_get_combat_participants() `EXTRACTED`
- .apply_attack_damage() `EXTRACTED`
- .handle_attack_events_and_xp() `EXTRACTED`
- .apply_damage_and_check_involuntary_flee() `EXTRACTED`
- .auto_progression_enabled() `EXTRACTED`
- .turn_interval_seconds() `EXTRACTED`
- ._get_combat_id_for_npc() `EXTRACTED`
- .get_combat() `EXTRACTED`
- .get_combat_by_participant() `EXTRACTED`
- .validate_melee_location() `EXTRACTED`
- .check_involuntary_flee() `EXTRACTED`
- .handle_target_state_changes() `EXTRACTED`
- .award_xp_to_player() `EXTRACTED`
- .process_attack() `EXTRACTED`

### rationale_for
- Service for managing combat instances and state. `EXTRACTED`

### references
- run_heal_effect() `EXTRACTED`
- get_combat_id_for_npc() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _run_steal_life() `EXTRACTED`
- _steal_life_apply_target_damage() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- _run_standard_heal_after_validation() `EXTRACTED`
- get_npc_instance_for_steal_life() `EXTRACTED`
- _steal_life_resolve_target_dp() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- find_participant_uuid_by_string_id() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`
- apply_target_rest_and_grace_checks() `EXTRACTED`
- process_npc_turn() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- _make_service() `EXTRACTED`
- _steal_life_publish_npc_events() `EXTRACTED`
- validate_melee_location() `EXTRACTED`
- validate_melee_or_end_combat() `EXTRACTED`

### uses
- [EventBus](EventBus.md) `INFERRED`
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) `INFERRED`
- [PlayerCombatService](PlayerCombatService.md) `INFERRED`
- [NATSService](NATSService.md) `INFERRED`
- CombatCommandHandler `INFERRED`
- SpellEffects `INFERRED`
- CombatTurnProcessor `INFERRED`
- _MagicServiceCore `INFERRED`
- [PlayerRespawnService](PlayerRespawnService.md) `INFERRED`
- [CombatParticipantData](CombatParticipantData.md) `INFERRED`
- [CombatEventPublisher](CombatEventPublisher.md) `INFERRED`
- NPCCombatDataProvider `INFERRED`
- TauntCommandHandler `INFERRED`
- MagicService `INFERRED`
- PlayerDeathService `INFERRED`
- SpellTargetingService `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- SpellEffectsDeps `INFERRED`
- CombatBundle `INFERRED`
- CombatPersistenceHandler `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*