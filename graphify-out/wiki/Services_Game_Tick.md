# Services Game Tick

> 4 nodes · cohesion 0.50

## Key Concepts

- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._start_writer_thread()** (3 connections) — `server/services/chat_logger.py`
- **Initialize chat logger.          Args:             log_dir: Directory for log fi** (1 connections) — `server/services/chat_logger.py`
- **Start the background writer thread for thread-safe file writing.** (1 connections) — `server/services/chat_logger.py`

## Relationships

- [Chat Channel Logger](Chat_Channel_Logger.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Cursor Plans Address](Cursor_Plans_Address.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*