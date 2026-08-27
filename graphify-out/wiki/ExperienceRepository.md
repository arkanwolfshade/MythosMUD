# ExperienceRepository

> 34 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (11 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (8 connections)
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueNode** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_tree.py** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **schemas/dialogue/__init__.py** (6 connections) — `server/schemas/dialogue/__init__.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueCursor** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueOption** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **.validate_graph()** (3 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **BaseModel** (3 connections)
- **model_validator** (1 connections)
- **Load and validate a dialogue tree, or clear cursor and return fade text.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return an error string if option_index is out of range for node.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Advance from the current cursor by 1-based option index. Returns…** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Set cursor and build prompt for node_id.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Active conversation position for one player.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Load dialogue trees and track per-player session cursors.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (3 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (3 shared connections)
- [useGameTerminal.ts](useGameTerminal.ts.md) (2 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`

## Audit Trail

- EXTRACTED: 76 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*