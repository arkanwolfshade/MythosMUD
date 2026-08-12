# Distributed Event Bus

> 142 nodes

## Key Concepts

- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (13 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_models.py** (12 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (12 connections) — `server/npc/spawning_request_execution.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (9 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (9 connections) — `server/npc/spawning_models.py`
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **generate_npc_id()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- *... and 117 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (63 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (18 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (13 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (13 shared connections)
- [Player Position Service](Player_Position_Service.md) (9 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (7 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (7 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (4 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (3 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 612 (95%)
- INFERRED: 33 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*