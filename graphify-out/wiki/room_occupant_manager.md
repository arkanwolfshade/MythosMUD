# room occupant manager

> 34 nodes

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
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
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **UUID** (3 connections)
- **costs_service()** (2 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **Casting completion flow for spellcasting.  Mixin that handles completing a casti** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Mixin for MagicService: complete casting (player/room, target, costs/effects, co** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Get player and room_id for casting completion.          Returns:             Tup** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Recreate target from stored casting state.          Args:             casting_st** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects.          Args:             player_id: Pla** (1 connections) — `server/game/magic/magic_service_completion.py`
- *... and 9 more nodes in this community*

## Relationships

- [persistence core infrastructure](persistence_core_infrastructure.md) (10 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (7 shared connections)
- [player respawn event](player_respawn_event.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (4 shared connections)
- [npc combat player](npc_combat_player.md) (2 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [subject nats manager](subject_nats_manager.md) (2 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (1 shared connections)
- [lucidity active service](lucidity_active_service.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/tests/unit/game/magic/test_spell_costs.py`

## Audit Trail

- EXTRACTED: 160 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*