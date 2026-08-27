# Enhanced Logging Best Practices for MythosMUD

> 12 nodes

## Key Concepts

- **FakeHallucinationService** (6 connections) — `server/services/fake_hallucination_service.py`
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (3 connections)
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **Any** (2 connections)
- **Generate a room text overlay hallucination. Args: player_id: Player UUID who…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Select which type of fake hallucination to trigger (50/50 chance). Returns:…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Service for generating fake NPC tells and room text overlays. These…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Initialize the fake hallucination service.** (1 connections) — `server/services/fake_hallucination_service.py`
- **Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will…** (1 connections) — `server/services/fake_hallucination_service.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*