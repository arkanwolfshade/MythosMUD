# server game magic spell targeting

> 18 nodes

## Key Concepts

- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **Player** (1 connections)
- **Resolve the target for a spell cast. Args: player_id: ID of the player casting…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get player from persistence.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Build a TargetMatch for a combat opponent, or None if unresolved.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get the combat target for a player if they are in combat. Args: player_id:…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Service for resolving spell targets. Handles target resolution based on spell…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve self-target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve area/all target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve entity/location target spell with explicit target. Returns…** (1 connections) — `server/game/magic/spell_targeting.py`

## Relationships

- [server game magic spell materials](server_game_magic_spell_materials.md) (7 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (6 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (4 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [server dependencies](server_dependencies.md) (1 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (1 shared connections)
- [server async persistence](server_async_persistence.md) (1 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server events combat events](server_events_combat_events.md) (1 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 51 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*