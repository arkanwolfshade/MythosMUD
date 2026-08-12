# Rest Command Flow

> 742 nodes

## Key Concepts

- **CombatService** (182 connections) — `server/services/combat_service.py`
- **CombatInstance** (169 connections) — `server/models/combat.py`
- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (50 connections) — `server/models/combat.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 717 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (150 shared connections)
- [Client Event Store](Client_Event_Store.md) (54 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (50 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (46 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (44 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (43 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (29 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (28 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (14 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (14 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (7 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (7 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/lifespan_startup.py`
- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/realtime/connection_helpers.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`

## Audit Trail

- EXTRACTED: 3245 (96%)
- INFERRED: 122 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*