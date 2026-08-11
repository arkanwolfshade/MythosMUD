# Rest Command Flow

> 208 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **Any** (5 connections)
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- *... and 183 more nodes in this community*

## Relationships

- [Combat Death Handling](Combat_Death_Handling.md) (53 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (22 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (18 shared connections)
- [Health Check Models](Health_Check_Models.md) (13 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (12 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (11 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (10 shared connections)
- [Game Client Container](Game_Client_Container.md) (7 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (5 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 826 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*