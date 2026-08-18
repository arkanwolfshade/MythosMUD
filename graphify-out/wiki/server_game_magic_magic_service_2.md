# server game magic magic service

> 37 nodes

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_costs.py`
- **UUID** (3 connections)
- **Any** (1 connections)
- **Casting completion flow for spellcasting. Mixin that handles completing a…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- *... and 12 more nodes in this community*

## Relationships

- [server game magic casting state](server_game_magic_casting_state.md) (8 shared connections)
- [server game magic spell materials](server_game_magic_spell_materials.md) (7 shared connections)
- [server api players](server_api_players.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (3 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (2 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (2 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server api character creation](server_api_character_creation.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 106 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*