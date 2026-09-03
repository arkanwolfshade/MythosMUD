# Test Npc Combat Integration Class

> 126 nodes

## Key Concepts

- **NPCCombatIntegration** (98 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_combat_integration_base.py** (25 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **UUID** (5 connections)
- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- *... and 101 more nodes in this community*

## Relationships

- [Combat Integration Base](Combat_Integration_Base.md) (10 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (5 shared connections)
- [Npc Base](Npc_Base.md) (5 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (4 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (2 shared connections)
- [Test Combat Attack](Test_Combat_Attack.md) (2 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (2 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 205 (75%)
- INFERRED: 68 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*