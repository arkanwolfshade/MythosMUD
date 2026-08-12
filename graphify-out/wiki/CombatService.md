# CombatService

> 188 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **run_handle_taunt_command()** (12 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (11 connections) — `server/commands/combat_taunt.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **UUID** (10 connections)
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **find_participant_uuid_by_string_id()** (9 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **get_combat_id_for_npc_via_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (7 connections) — `server/services/combat_service_npc.py`
- **_RoomWithIdOnly** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 163 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (73 shared connections)
- [combat_service.py](combat_service.py.md) (40 shared connections)
- [TargetMatch](TargetMatch.md) (19 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (19 shared connections)
- [spell_effects.py](spell_effects.py.md) (19 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (15 shared connections)
- [magic_service.py](magic_service.py.md) (7 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [Spell](Spell.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 466 (90%)
- INFERRED: 53 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*