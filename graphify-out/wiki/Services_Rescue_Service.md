# Services Rescue Service

> 20 nodes · cohesion 0.13

## Key Concepts

- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **rescue_service.py** (10 connections) — `server/services/rescue_service.py`
- **Any** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **.rescue()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **UUID** (4 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **AsyncSessionFactory** (3 connections) — `server/services/rescue_service.py`
- **EventDispatcher** (3 connections) — `server/services/rescue_service.py`
- **LucidityServiceFactory** (3 connections) — `server/services/rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Rescue service encapsulating rescue flows with injectable dependencies.  This is** (1 connections) — `server/services/rescue_service.py`
- **Convert value to UUID, raising ValueError if invalid.** (1 connections) — `server/services/rescue_service.py`
- **Await the value if it is awaitable.** (1 connections) — `server/services/rescue_service.py`
- **Service for performing rescue operations.** (1 connections) — `server/services/rescue_service.py`
- **Perform a rescue for the given target.          Returns:             dict contai** (1 connections) — `server/services/rescue_service.py`
- **Test rescue() returns error when persistence is not available.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a RescueService instance.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`

## Relationships

- [[Lucidity State Models]] (8 shared connections)
- [[Lucidity Database Models]] (7 shared connections)
- [[Rescue Service Tests]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[Lucidity Rescue Helpers]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Ground and Rescue Commands]] (1 shared connections)
- [[Command Helper Utilities]] (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 61 (82%)
- INFERRED: 13 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
