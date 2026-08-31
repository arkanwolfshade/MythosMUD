# TargetResolutionResult

> 41 nodes

## Key Concepts

- **TargetResolutionResult** (36 connections) — `server/schemas/shared/target_resolution.py`
- **test_spell_targeting.py** (29 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **asyncio** (7 connections)
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **spell_targeting_service()** (5 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_entity_target_rejects_location()** (4 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_entity_target_success()** (4 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_get_disambiguation_list()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_disambiguation_list_empty()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match_none()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_target_resolution_result_disambiguation()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_target_resolution_result_success()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **.get_single_match()** (3 connections) — `server/schemas/shared/target_resolution.py`
- **mock_target_resolution_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_spell_target_self_spell_no_target_resolves_self()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_spell_target_self_spell_with_target_returns_error()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_target_resolution_result_failure()** (3 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **.get_disambiguation_list()** (2 connections) — `server/schemas/shared/target_resolution.py`
- **test_resolve_area_target()** (2 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_spell_target_requires_target()** (2 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **BaseModel** (2 connections)
- **Resolve combat target using target resolution service. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Validate target_result and resolve to a live NPC target_match.** (1 connections) — `server/commands/combat_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (14 shared connections)
- [Spell](Spell.md) (14 shared connections)
- [TargetMatch](TargetMatch.md) (13 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 105 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*