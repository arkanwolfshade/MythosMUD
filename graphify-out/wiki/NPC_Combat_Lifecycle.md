# NPC Combat Lifecycle

> 26 nodes · cohesion 0.00

## Key Concepts

- **UUID** (41 connections) — `server/services/combat_service.py`
- **Any** (22 connections) — `server/services/nats_service.py`
- **UUID** (12 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (10 connections) — `server/commands/combat_taunt.py`
- **NATS** (9 connections) — `server/services/nats_service.py`
- **UUID** (9 connections) — `server/services/combat_event_handler.py`
- **UUID** (8 connections) — `server/services/combat_service_attack.py`
- **UUID** (8 connections) — `server/services/combat_service_events.py`
- **UUID** (8 connections) — `server/services/npc_combat_data_provider.py`
- **UUID** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (8 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Any** (7 connections) — `server/services/npc_combat_handlers.py`
- **UUID** (6 connections) — `server/services/combat_death_handler.py`
- **Any** (6 connections) — `server/services/combat_event_handler.py`
- **Any** (6 connections) — `server/services/combat_service_start.py`
- **BaseException** (6 connections) — `server/services/nats_service.py`
- **Task** (6 connections) — `server/services/nats_service.py`
- **Any** (5 connections) — `server/services/npc_combat_data_provider.py`
- **Any** (3 connections) — `server/services/combat_event_publisher.py`
- **UUID** (3 connections) — `server/services/combat_initialization.py`
- **Any** (2 connections) — `server/game/mechanics.py`
- **Any** (2 connections) — `server/services/combat_cleanup_handler.py`
- **Any** (2 connections) — `server/services/npc_combat_rewards.py`
- **Any** (1 connections) — `server/services/combat_attack_handler.py`
- *... and 1 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/mechanics.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/nats_service.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 121 (58%)
- INFERRED: 89 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*