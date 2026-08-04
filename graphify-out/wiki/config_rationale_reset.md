# config rationale reset

> 8 nodes

## Key Concepts

- **test_mp_regeneration_service.py** (33 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_default_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_at_max()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_restore_mp_from_rest_calculates_max_from_power()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Unit tests for MP regeneration service.  Tests the MPRegenerationService class f** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test _get_regen_multiplier() defaults to 1.0 when position not specified.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() returns message when MP already at max.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() calculates max_mp from power if not present.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [npc aggressive mob](npc_aggressive_mob.md) (4 shared connections)
- [schemas room schema](schemas_room_schema.md) (2 shared connections)
- [schemas unified room](schemas_unified_room.md) (2 shared connections)
- [schemas calendar schedule](schemas_calendar_schedule.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (1 shared connections)
- [schemas items item](schemas_items_item.md) (1 shared connections)
- [add fastapi users](add_fastapi_users.md) (1 shared connections)
- [tsconfig build DOM](tsconfig_build_DOM.md) (1 shared connections)
- [tsconfig app DOM](tsconfig_app_DOM.md) (1 shared connections)
- [admin services auth](admin_services_auth.md) (1 shared connections)
- [tick services game](tick_services_game.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*