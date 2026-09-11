# FakeSenderRegistry

> 26 nodes

## Key Concepts

- **FakeSenderRegistry** (13 connections) — `server/services/fake_sender_registry.py`
- **test_fake_sender_registry.py** (9 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **fake_sender_registry.py** (5 connections) — `server/services/fake_sender_registry.py`
- **UUID** (4 connections)
- **.clear()** (3 connections) — `server/services/fake_sender_registry.py`
- **.get_last_fake_sender()** (3 connections) — `server/services/fake_sender_registry.py`
- **.record_fake_whisper()** (3 connections) — `server/services/fake_sender_registry.py`
- **test_clear_on_unrecorded_player_does_not_raise()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **test_clear_removes_the_recorded_sender()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **test_get_last_fake_sender_is_none_for_unrecorded_player()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **test_record_fake_whisper_accepts_str_or_uuid_for_the_same_player()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **test_record_fake_whisper_overwrites_the_previous_sender()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **test_record_then_get_last_fake_sender()** (3 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **.__init__()** (1 connections) — `server/services/fake_sender_registry.py`
- **In-memory registry of each player's most recent fake NPC whisper sender (#625,…** (1 connections) — `server/services/fake_sender_registry.py`
- **Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share…** (1 connections) — `server/services/fake_sender_registry.py`
- **Record that this player's most recent whisper came from this fake NPC.** (1 connections) — `server/services/fake_sender_registry.py`
- **Return the fake NPC name this player was last whispered by, or None.** (1 connections) — `server/services/fake_sender_registry.py`
- **Drop this player's fake-sender record (e.g. leaving fractured/deranged,…** (1 connections) — `server/services/fake_sender_registry.py`
- **Unit tests for the in-memory fake whisper sender registry (#625, #714). This…** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **A player with no fake whisper history has no recorded sender.** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **The most recently recorded fake NPC name is returned.** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **Only the most recent fake sender is tracked -- no history list.** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **A UUID and its string form must key into the same registry entry.** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- **clear() drops the entry entirely -- reply falls through to the real whisper…** (1 connections) — `server/tests/unit/services/test_fake_sender_registry.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (1 shared connections)

## Source Files

- `server/services/fake_sender_registry.py`
- `server/tests/unit/services/test_fake_sender_registry.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*