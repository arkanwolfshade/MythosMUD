# room realtime occupant

> 5 nodes

## Key Concepts

- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **BaseUserManager** (1 connections)
- **UP** (1 connections)
- **ID** (1 connections)
- **Reads a JWT token, validating its signature, audience, and server epoch.** (1 connections) — `server/auth/jwt_strategy.py`

## Relationships

- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*