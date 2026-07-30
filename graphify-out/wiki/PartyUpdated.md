# PartyUpdated

> 10 nodes

## Key Concepts

- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **room_utils.py** (9 connections) — `server/utils/room_utils.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **Resolve the subzone ID for a destination room (from room attribute or room_id).** (1 connections) — `server/npc/movement_integration.py`
- **Validate that a destination room is within the NPC's allowed subzone.** (1 connections) — `server/npc/movement_integration.py`
- **Room utility functions for MythosMUD.  This module provides utility functions fo** (1 connections) — `server/utils/room_utils.py`
- **Extract sub-zone from room ID.      Room ID format: {plane}_{zone}_{sub_zone}_{r** (1 connections) — `server/utils/room_utils.py`
- **Generate NATS subject for sub-zone local channel messages.      This creates a s** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [. get destination subzone()](_get_destination_subzone%28%29.md) (12 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (1 shared connections)
- [AsyncSession](AsyncSession.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*