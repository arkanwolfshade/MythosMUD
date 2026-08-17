# TargetResolutionResult

> 73 nodes

## Key Concepts

- **TargetResolutionResult** (34 connections) — `server/schemas/shared/target_resolution.py`
- **test_spell_targeting.py** (29 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **asyncio** (7 connections)
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **test_resolve_entity_target_rejects_location()** (4 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_entity_target_success()** (4 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_get_disambiguation_list()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_disambiguation_list_empty()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match_none()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_target_match()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- *... and 48 more nodes in this community*

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (24 shared connections)
- [TargetMatch](TargetMatch.md) (18 shared connections)
- [SpellEffectType](SpellEffectType.md) (11 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (5 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (4 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 165 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*