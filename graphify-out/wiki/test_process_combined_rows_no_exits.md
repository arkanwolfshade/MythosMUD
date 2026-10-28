# test_process_combined_rows_no_exits

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_overflow_spills_into_a_real_players_json_backed_inventory()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Player.inventory is a JSON string column; spilling must go through…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [HolidayService](HolidayService.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 3 (60%)
- INFERRED: 2 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*