# CombatService

> God node · 232 connections · `server/services/combat_service.py`

**Community:** [[Combat Service Bundle]]

## Connections by Relation

### calls
- [[initialize_nats_and_combat_services()]] `EXTRACTED`
- [[_make_service()]] `EXTRACTED`
- [[._create_combat_service_with_nats()]] `EXTRACTED`
- [[combat_service()]] `EXTRACTED`

### contains
- [[combat_service.py]] `EXTRACTED`

### imports
- [[dependencies.py]] `EXTRACTED`
- [[lifespan_startup.py]] `EXTRACTED`
- [[npc_combat_integration_service.py]] `EXTRACTED`
- [[combat_turn_participant_actions.py]] `EXTRACTED`
- [[spell_effects_heal.py]] `EXTRACTED`
- [[spell_effects.py]] `EXTRACTED`
- [[combat_handler.py]] `EXTRACTED`
- [[combat_service_npc.py]] `EXTRACTED`
- [[combat_taunt.py]] `EXTRACTED`
- [[magic_service.py]] `EXTRACTED`
- [[combat_service_attack.py]] `EXTRACTED`
- [[combat_loader.py]] `EXTRACTED`
- [[combat_service_start.py]] `EXTRACTED`
- [[npc_combat_integration_validation_mixin.py]] `EXTRACTED`
- [[combat_flee.py]] `EXTRACTED`
- [[magic_service_completion.py]] `EXTRACTED`
- [[test_combat_service.py]] `EXTRACTED`
- [[combat_turn_processor.py]] `EXTRACTED`
- [[npc_combat_integration_combat_mixin.py]] `EXTRACTED`
- [[spell_targeting.py]] `EXTRACTED`

### method
- [[.__init__()]] `EXTRACTED`
- [[.finalize_attack_result()]] `EXTRACTED`
- [[.validate_melee_or_end_combat()]] `EXTRACTED`
- [[.apply_attack_damage()]] `EXTRACTED`
- [[.apply_damage_and_check_involuntary_flee()]] `EXTRACTED`
- [[.end_combat_if_npc_died()]] `EXTRACTED`
- [[.handle_attack_events_and_xp()]] `EXTRACTED`
- [[._handle_player_dp_update()]] `EXTRACTED`
- [[.validate_and_get_combat_participants()]] `EXTRACTED`
- [[.award_xp_to_player()]] `EXTRACTED`
- [[.check_involuntary_flee()]] `EXTRACTED`
- [[.end_combat()]] `EXTRACTED`
- [[.get_combat()]] `EXTRACTED`
- [[.get_combat_by_participant()]] `EXTRACTED`
- [[._get_combat_id_for_npc()]] `EXTRACTED`
- [[.handle_target_state_changes()]] `EXTRACTED`
- [[.process_attack()]] `EXTRACTED`
- [[.register_combat_state()]] `EXTRACTED`
- [[.start_combat()]] `EXTRACTED`
- [[.validate_melee_location()]] `EXTRACTED`

### rationale_for
- [[Service for managing combat instances and state.]] `EXTRACTED`

### uses
- [[EventBus]] `INFERRED`
- [[NPCCombatIntegrationService]] `INFERRED`
- [[NATSService]] `INFERRED`
- [[PlayerCombatService]] `INFERRED`
- [[SpellEffects]] `INFERRED`
- [[NPCCombatDataProvider]] `INFERRED`
- [[PlayerRespawnService]] `INFERRED`
- [[CombatEventPublisher]] `INFERRED`
- [[CombatCommandHandler]] `INFERRED`
- [[MagicService]] `INFERRED`
- [[CombatParticipantData]] `INFERRED`
- [[CombatTurnProcessor]] `INFERRED`
- [[_MagicServiceCore]] `INFERRED`
- [[PlayerDeathService]] `INFERRED`
- [[SpellTargetingService]] `INFERRED`
- [[NPCDiedEvent]] `INFERRED`
- [[CombatPersistenceHandler]] `INFERRED`
- [[UUID]] `INFERRED`
- [[NPCTookDamageEvent]] `INFERRED`
- [[Any]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
