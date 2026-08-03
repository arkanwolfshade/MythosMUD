# CombatService

> God node · 181 connections · `server/services/combat_service.py`

**Community:** [NPC Combat](NPC_Combat.md)

## Connections by Relation

### calls
- initialize_nats_and_combat_services() `EXTRACTED`
- ._create_combat_service_with_nats() `EXTRACTED`
- combat_service() `EXTRACTED`

### contains
- combat_service.py `EXTRACTED`

### imports
- dependencies.py `EXTRACTED`
- lifespan_startup.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- spell_effects.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- spell_effects_heal.py `EXTRACTED`
- magic_service.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- combat_service_npc.py `EXTRACTED`
- combat_service_start.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- combat_loader.py `EXTRACTED`
- magic_service_completion.py `EXTRACTED`
- spell_targeting.py `EXTRACTED`
- combat_flee.py `EXTRACTED`
- combat_turn_processor.py `EXTRACTED`
- npc_combat_integration_validation_mixin.py `EXTRACTED`
- test_combat_service.py `EXTRACTED`
- npc_combat_integration_combat_mixin.py `EXTRACTED`

### indirect_call
- get_combat_service() `INFERRED`

### method
- .__init__() `EXTRACTED`
- .finalize_attack_result() `EXTRACTED`
- .validate_melee_or_end_combat() `EXTRACTED`
- .apply_attack_damage() `EXTRACTED`
- .apply_damage_and_check_involuntary_flee() `EXTRACTED`
- .end_combat_if_npc_died() `EXTRACTED`
- .handle_attack_events_and_xp() `EXTRACTED`
- ._handle_player_dp_update() `EXTRACTED`
- .start_combat() `EXTRACTED`
- .validate_and_get_combat_participants() `EXTRACTED`
- .award_xp_to_player() `EXTRACTED`
- .check_involuntary_flee() `EXTRACTED`
- .end_combat() `EXTRACTED`
- .get_combat() `EXTRACTED`
- .get_combat_by_participant() `EXTRACTED`
- ._get_combat_id_for_npc() `EXTRACTED`
- .handle_target_state_changes() `EXTRACTED`
- .process_attack() `EXTRACTED`
- .register_combat_state() `EXTRACTED`
- .validate_melee_location() `EXTRACTED`

### rationale_for
- Service for managing combat instances and state. `EXTRACTED`

### references
- run_heal_effect() `EXTRACTED`
- get_combat_id_for_npc() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _steal_life_resolve_target_dp() `EXTRACTED`
- _steal_life_apply_target_damage() `EXTRACTED`
- _run_steal_life() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- get_npc_participant_current_room() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- _run_standard_heal_after_validation() `EXTRACTED`
- validate_melee_or_end_combat() `EXTRACTED`
- find_participant_uuid_by_string_id() `EXTRACTED`
- process_npc_turn() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- get_npc_instance_for_steal_life() `EXTRACTED`
- process_attack() `EXTRACTED`
- validate_melee_location() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`
- apply_target_rest_and_grace_checks() `EXTRACTED`

### uses
- EventBus `INFERRED`
- NPCCombatIntegrationService `INFERRED`
- PlayerCombatService `INFERRED`
- NATSService `INFERRED`
- SpellEffects `INFERRED`
- CombatCommandHandler `INFERRED`
- CombatTurnProcessor `INFERRED`
- _MagicServiceCore `INFERRED`
- PlayerRespawnService `INFERRED`
- CombatParticipantData `INFERRED`
- SpellTargetingService `INFERRED`
- TauntCommandHandler `INFERRED`
- MagicService `INFERRED`
- NPCCombatDataProvider `INFERRED`
- PlayerDeathService `INFERRED`
- CombatEventPublisher `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- CombatPersistenceHandler `INFERRED`
- MagicServiceCompletionMixin `INFERRED`
- CombatBundle `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*