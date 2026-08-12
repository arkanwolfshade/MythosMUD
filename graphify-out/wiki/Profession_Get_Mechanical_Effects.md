# Profession Get Mechanical Effects

> 9 nodes

## Key Concepts

- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **PlayerRespawnWrapper** (8 connections) — `server/game/player_respawn_wrapper.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.__init__()** (3 connections) — `server/game/player_search_service.py`
- **Wrapper service for player respawn operations.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (1 connections)
- **Service for player search and validation operations.** (1 connections) — `server/game/player_search_service.py`
- **Initialize with a reference to the player service for data access.** (1 connections) — `server/game/player_search_service.py`
- **Initialize the player service with a persistence layer and optional combat servi** (1 connections) — `server/game/player_service.py`

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (6 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (2 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (2 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (1 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*