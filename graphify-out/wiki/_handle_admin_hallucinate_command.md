# _handle_admin_hallucinate_command

> 78 nodes

## Key Concepts

- **_handle_admin_hallucinate_command()** (22 connections) — `server/commands/admin_hallucinate_command.py`
- **hallucinations.py** (21 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_admin_hallucinate_command.py** (19 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **FakeHallucinationService** (15 connections) — `server/services/fake_hallucination_service.py`
- **asyncio** (14 connections)
- **deliver_forced_hallucination()** (12 connections) — `server/commands/admin_hallucinate_command.py`
- **handle_hallucination_triggers()** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_phantom_hostile_hallucination()** (11 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_room_text_overlay_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (9 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_uneasy_room_entry_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **extract_args()** (5 connections) — `server/commands/admin_hallucinate_command.py`
- **FakeNpcTellData** (4 connections) — `server/services/fake_hallucination_service.py`
- **RoomTextOverlayData** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **test_get_current_lcd_or_error_raises_when_session_unavailable()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_delivers_phantom()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_admin_hallucinate_delivery_error()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_resolve_hallucinate_target_raises_when_current_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_hallucinate_command.py`
- **test_handle_fake_hallucination_npc_tell()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- *... and 53 more nodes in this community*

## Relationships

- [command_error](command_error.md) (15 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [NpcDisposition](NpcDisposition.md) (7 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (6 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (6 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/commands/admin_hallucinate_command.py`
- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/commands/test_admin_hallucinate_command.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 189 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*