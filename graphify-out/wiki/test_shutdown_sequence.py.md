# test_shutdown_sequence.py

> 27 nodes · cohesion 0.13

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (13 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (8 connections)
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueCursor** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **.validate_graph()** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **test_dialogue_tree_graph_validation_still_runs()** (3 connections) — `server/tests/unit/schemas/test_dialogue_tree.py`
- **Load and validate a dialogue tree, or clear cursor and return fade text.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return an error string if option_index is out of range for node.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Advance from the current cursor by 1-based option index. Returns…** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Set cursor and build prompt for node_id.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Active conversation position for one player.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Load dialogue trees and track per-player session cursors.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Drop the player's dialogue cursor if any.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return active cursor or None.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Begin (or restart) dialogue with an NPC. Returns DialoguePrompt on success, or…** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **model_validator** (1 connections)
- **Root tree: start node id and nodes map.** (1 connections) — `server/schemas/dialogue/dialogue_tree.py`
- *... and 2 more nodes in this community*

## Relationships

- [Persistence Layer Refactoring - COMPLETE ✅](Persistence_Layer_Refactoring_-_COMPLETE_✅.md) (14 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (6 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/schemas/test_dialogue_tree.py`

## Audit Trail

- EXTRACTED: 65 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*