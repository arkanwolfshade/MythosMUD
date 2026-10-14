# DialogueService

> 21 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
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
- **.__init__()** (2 connections) — `server/game/dialogue/dialogue_service.py`
- **Load and validate a dialogue tree, or clear cursor and return fade text.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return an error string if option_index is out of range for node.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Advance from the current cursor by 1-based option index. Returns…** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Set cursor and build prompt for node_id.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Active conversation position for one player.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Load dialogue trees and track per-player session cursors.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Drop the player's dialogue cursor if any.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return active cursor or None.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Begin (or restart) dialogue with an NPC. Returns DialoguePrompt on success, or…** (1 connections) — `server/game/dialogue/dialogue_service.py`

## Relationships

- [talk_command.py](talk_command.py.md) (12 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (2 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`

## Audit Trail

- EXTRACTED: 52 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*