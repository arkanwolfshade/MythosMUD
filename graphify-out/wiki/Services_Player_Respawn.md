# Services Player Respawn

> 10 nodes · cohesion 0.22

## Key Concepts

- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **LucidityService** (3 connections) — `server/services/player_respawn_service.py`
- **.choice()** (3 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (2 connections) — `server/services/player_respawn_service.py`
- **EncodeLiabilitiesFn** (2 connections) — `server/services/player_respawn_service.py`
- **PlayerLucidity** (2 connections) — `server/services/player_respawn_service.py`
- **Increase existing liability stacks or add one liability if none exist.** (1 connections) — `server/services/player_respawn_service.py`
- **Subset of random.Random / random module API used for liability picks.** (1 connections) — `server/services/player_respawn_service.py`
- **Return one element from a non-empty sequence of liability codes.** (1 connections) — `server/services/player_respawn_service.py`

## Relationships

- [[Lucidity State Models]] (5 shared connections)
- [[Player Respawn Service]] (4 shared connections)
- [[Lucidity Rescue Helpers]] (2 shared connections)
- [[Player Combat XP]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 26 (79%)
- INFERRED: 7 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
