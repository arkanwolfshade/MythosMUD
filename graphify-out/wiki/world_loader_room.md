# world loader room

> 9 nodes

## Key Concepts

- **__init__.py** (5 connections) — `server/schemas/dialogue/__init__.py`
- **dialogue_tree.py** (5 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueOption** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueNode** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **BaseModel** (3 connections)
- **Dialogue Pydantic schemas.** (1 connections) — `server/schemas/dialogue/__init__.py`
- **Nav-only dialogue tree schema for #583.  Rejects unknown next targets, missing** (1 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **Player-facing option; next null/omitted ends the conversation.** (1 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **One NPC line plus numbered options.** (1 connections) — `server/schemas/dialogue/dialogue_tree.py`

## Relationships

- [dialogue service game](dialogue_service_game.md) (3 shared connections)

## Source Files

- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*