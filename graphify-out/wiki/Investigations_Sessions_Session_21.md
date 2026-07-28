# Investigations Sessions Session

> 4 nodes · cohesion 0.50

## Key Concepts

- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_create_character_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() endpoint.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() enforces rate limiting.** (1 connections) — `server/tests/unit/api/test_character_creation.py`

## Relationships

- [Player Effects API](Player_Effects_API.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*