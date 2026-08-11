# Services Exploration Service

> 4 nodes

## Key Concepts

- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_validate_stats_invalid_input()** (4 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test validate_character_stats() endpoint.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test validate_character_stats() handles invalid stats.** (1 connections) — `server/tests/unit/api/test_character_creation.py`

## Relationships

- [Game Mechanics Service](Game_Mechanics_Service.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 10 (67%)
- INFERRED: 5 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*