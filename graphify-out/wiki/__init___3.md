# .__init__

> 4 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **Path** (1 connections)
- **Load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`

## Relationships

- [DatabaseError](DatabaseError.md) (2 shared connections)
- [HolidayCollection](HolidayCollection.md) (2 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*