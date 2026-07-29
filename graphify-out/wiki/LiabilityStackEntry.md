# LiabilityStackEntry

> 91 nodes

## Key Concepts

- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **LucidityUpdateResult** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections)
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- **.clear_liability()** (5 connections) — `server/services/lucidity_service.py`
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **clamp_lucidity()** (4 connections) — `server/services/lucidity_helpers.py`
- **normalize_metadata()** (4 connections) — `server/services/lucidity_helpers.py`
- **coerce_metadata_dict()** (4 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_source()** (4 connections) — `server/services/lucidity_helpers.py`
- *... and 66 more nodes in this community*

## Relationships

- [UUID](UUID.md) (28 shared connections)
- [datetime](datetime.md) (22 shared connections)
- [. init ()](_init_%28%29.md) (17 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (5 shared connections)
- [. call ()](_call_%28%29.md) (5 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (4 shared connections)
- [rescue commands](rescue_commands.md) (2 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [config](config.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 401 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*