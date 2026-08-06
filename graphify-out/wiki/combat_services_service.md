# combat services service

> 24 nodes

## Key Concepts

- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Protocol** (1 connections)
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return messaging integration dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat from mixin combat pipeline.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **start_combat / process_attack paths and post-death broadcast.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Resolve participant combat data and apply the initial attack damage through Comb** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Structured logging / observability trail when NPC-initiated combat begins.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows error** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`

## Relationships

- [player look commands](player_look_commands.md) (6 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (3 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [game skill service](game_skill_service.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)
- [tick game processing](tick_game_processing.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 89 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*