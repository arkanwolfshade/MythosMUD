# Community 65

> 116 nodes

## Key Concepts

- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **combat_events.py** (21 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **PlayerDPDecayEvent** (13 connections) — `server/events/event_types.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatStartedEvent** (9 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (9 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTargetSwitchEvent** (8 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (8 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (8 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (7 connections) — `server/events/event_types.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NPCAttackedEvent** (6 connections) — `server/events/combat_events.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **publish_npc_damage_event()** (6 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (6 connections) — `server/services/combat_service_events.py`
- **broadcast_aggro_target_switches()** (5 connections) — `server/services/combat_service_events.py`
- **_dp_decay_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_attacked_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_died_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_took_damage_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 91 more nodes in this community*

## Relationships

- [Community 98](Community_98.md) (12 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (10 shared connections)
- [Game Event Types](Game_Event_Types.md) (8 shared connections)
- [Community 96](Community_96.md) (6 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (4 shared connections)
- [Community 491](Community_491.md) (2 shared connections)
- [Community 318](Community_318.md) (2 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (2 shared connections)
- [Community 244](Community_244.md) (1 shared connections)
- [Community 343](Community_343.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/player_event_handlers.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 234 (88%)
- INFERRED: 31 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*