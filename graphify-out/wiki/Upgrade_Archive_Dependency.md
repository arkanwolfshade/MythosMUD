# Upgrade Archive Dependency

> 11 nodes

## Key Concepts

- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **constants.py** (2 connections) — `server/game/items/constants.py`
- **Constants supporting item prototype validation.  These enumerations anchor the s** (1 connections) — `server/game/items/constants.py`
- **Pydantic models for item prototype validation.  This module defines the ItemProt** (1 connections) — `server/game/items/models.py`
- **Prototype registry for managing item prototypes.  This module provides the Pro** (1 connections) — `server/game/items/prototype_registry.py`
- **Namespace** (1 connections)
- **CLI entrypoint for validating MythosMUD item prototype definitions.** (1 connections) — `server/scripts/validate_prototypes.py`

## Relationships

- [Npc Services Combat](Npc_Services_Combat.md) (5 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (3 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (2 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (1 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (1 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (1 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*