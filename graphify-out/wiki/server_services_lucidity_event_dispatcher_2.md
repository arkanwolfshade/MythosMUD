# server services lucidity event dispatcher

> 16 nodes

## Key Concepts

- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_progress_only()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **LiabilityStackEntry** (1 connections)
- **Helpers for broadcasting lucidity-related SSE events.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Emit a catatonia state event to the affected player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send rescue progress/status updates to either participant.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send an event to a specific player, swallowing transport errors in headless…** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Flatten liability entries into human-readable strings for the client.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Test send_rescue_update_event with progress only.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Relationships

- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (21 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (8 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (5 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (3 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [asyncsessionfactory](asyncsessionfactory.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server utils liability types](server_utils_liability_types.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*