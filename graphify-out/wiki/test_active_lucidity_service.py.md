# test_active_lucidity_service.py

> 83 nodes · cohesion 0.05

## Key Concepts

- **server/models/__init__.py** (90 connections) — `server/models/__init__.py`
- **CorruptionTier** (42 connections) — `server/models/corruption.py`
- **corruption_service.py** (42 connections) — `server/services/corruption_service.py`
- **corruption.py** (26 connections) — `server/models/corruption.py`
- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **format_occupant_display_name()** (20 connections) — `server/realtime/occupant_display.py`
- **compute_tier()** (17 connections) — `server/models/corruption.py`
- **occupant_display.py** (16 connections) — `server/realtime/occupant_display.py`
- **test_occupant_display.py** (16 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **corruption_reactions.py** (13 connections) — `server/npc/corruption_reactions.py`
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
- **build_corruption_aware_greeting()** (10 connections) — `server/npc/corruption_reactions.py`
- **corruption_hostility_scale()** (9 connections) — `server/npc/corruption_reactions.py`
- **_reset_cache()** (9 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_pick_greeting()** (7 connections) — `server/npc/corruption_reactions.py`
- **test_corruption.py** (7 connections) — `server/tests/unit/models/test_corruption.py`
- **_reset_cache()** (7 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **_no_grace_patches()** (7 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **CorruptionTierCache** (6 connections) — `server/services/corruption_tier_cache.py`
- **test_compute_tier_boundaries()** (6 connections) — `server/tests/unit/models/test_corruption.py`
- **test_format_occupant_display_name_no_badge_when_touched()** (6 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **UUID** (5 connections)
- **test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_touched_player()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- *... and 58 more nodes in this community*

## Relationships

- [reset_database](reset_database.md) (14 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (12 shared connections)
- [BaseEvent](BaseEvent.md) (11 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (9 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (7 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (6 shared connections)
- [CorruptionTier](CorruptionTier.md) (6 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [endpoints.py](endpoints.py.md) (5 shared connections)
- [retry.py](retry.py.md) (4 shared connections)

## Source Files

- `server/models/__init__.py`
- `server/models/corruption.py`
- `server/npc/corruption_reactions.py`
- `server/realtime/occupant_display.py`
- `server/services/corruption_service.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/realtime/test_occupant_display.py`

## Audit Trail

- EXTRACTED: 340 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*