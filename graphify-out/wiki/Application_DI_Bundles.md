# Application DI Bundles

> 23 nodes

## Key Concepts

- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **Mixin for MagicService: complete casting (player/room, target, costs/effects, co** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Get player and room_id for casting completion.          Returns:             Tup** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Recreate target from stored casting state.          Args:             casting_st** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects.          Args:             player_id: Pla** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply costs and queue spell for next combat round. Returns True if queued, False** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs/effects, send completion message and healing event.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **If in combat, try to queue spell for next round. Return True if queued, False ot** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Complete a casting and apply spell effects.          In combat, spells are queue** (1 connections) — `server/game/magic/magic_service_completion.py`

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (12 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (1 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`

## Audit Trail

- EXTRACTED: 106 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*