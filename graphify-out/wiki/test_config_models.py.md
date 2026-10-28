# test_config_models.py

> 44 nodes · cohesion 0.06

## Key Concepts

- **FakeHallucinationService** (15 connections) — `server/services/fake_hallucination_service.py`
- **handle_hallucination_triggers()** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_room_text_overlay_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_uneasy_room_entry_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **FakeNpcTellData** (4 connections) — `server/services/fake_hallucination_service.py`
- **RoomTextOverlayData** (4 connections) — `server/services/fake_hallucination_service.py`
- **test_handle_fake_hallucination_npc_tell()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_uneasy_room_entry_hallucination_delivers_overlay_only()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **UUID** (3 connections)
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **TypedDict** (2 connections)
- *... and 19 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (10 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (5 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (2 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (1 shared connections)
- [ExitEdge.tsx](ExitEdge.tsx.md) (1 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (1 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 91 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*