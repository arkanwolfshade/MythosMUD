# Event Bus Serialization

> 61 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (20 connections) — `server/npc/combat_integration_base.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (4 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (4 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **UUID** (3 connections)
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- *... and 36 more nodes in this community*

## Relationships

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (5 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Command Parser](Command_Parser.md) (4 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [Health Check Models](Health_Check_Models.md) (2 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 209 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*