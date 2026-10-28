# AsciiMapRenderer

> 22 nodes · cohesion 0.19

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (5 connections)
- **Status effect spell logic (apply/remove status, force-flee, grace-period…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag.…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply a status effect, respecting login grace-period protection.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply or remove a status effect on a player, respecting grace-period rules.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Process status effect: apply/remove on player, or apply to NPC (no persistence).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **True if target is in login grace period and effect is negative (should block).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Load player, append status effect, save; return result dict or error if player…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Run flee effect when effect_data.force_flee is set; otherwise return None.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Status effects that can be applied to characters.** (1 connections) — `server/models/game.py`

## Relationships

- [RoomService](RoomService.md) (10 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (8 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (4 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [ChatLogger](ChatLogger.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [Improve Layout Systematically](Improve_Layout_Systematically.md) (2 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 79 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*