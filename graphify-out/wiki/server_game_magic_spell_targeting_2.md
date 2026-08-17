# server game magic spell targeting

> 18 nodes

## Key Concepts

- **SpellTargetingService** (24 connections) — `server/game/magic/spell_targeting.py`
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

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (9 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (3 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (2 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (1 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 48 (84%)
- INFERRED: 9 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*