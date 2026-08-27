# Respawn Death Screen Loop Limbo ID Mismatch

> 8 nodes

## Key Concepts

- **._execute_wander_movement()** (6 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (3 connections) — `server/npc/threading.py`
- **Process a message for an NPC.** (1 connections) — `server/npc/threading.py`
- **Resolve active NPC instance and definition for a WANDER action.** (1 connections) — `server/npc/threading.py`
- **Run idle movement for a resolved wander NPC.** (1 connections) — `server/npc/threading.py`
- **Process a WANDER action for idle movement. Args: npc_id: ID of the NPC to move…** (1 connections) — `server/npc/threading.py`

## Relationships

- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (5 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Mansions_of_Madness__Vol_1_-_Behind_Closed_Doors__2026-08-12.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 14 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*