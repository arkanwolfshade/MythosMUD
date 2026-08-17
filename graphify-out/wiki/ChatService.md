# chatservice

> 15 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.__init__()** (8 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (4 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (2 connections)
- **ChatService** (1 connections)
- **PlayerService** (1 connections)
- **SpellRegistry** (1 connections)
- **SpellRegistry** (1 connections)
- **TypedDict** (1 connections)
- **SpellEffects** (1 connections)
- **SpellLearningService** (1 connections)
- **SpellTargetingService** (1 connections)
- **Initialize the magic command handler. Args: magic_service: Magic service for…** (1 connections) — `server/commands/magic_commands.py`
- **Initialize the magic service. Args: spell_registry: Registry for spell lookups…** (1 connections) — `server/game/magic/magic_service.py`
- **Optional dependencies for MagicService. All keys optional; defaults applied in…** (1 connections) — `server/game/magic/magic_service.py`

## Relationships

- [server commands magic commands](server_commands_magic_commands.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (1 shared connections)
- [magicservicecompletionmixin](magicservicecompletionmixin.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*