# Spec Requirements Document

> Spec: Inventory & Equipment Foundations
> Created: 2025-11-11

## Overview

Define the foundational inventory and equipment systems so players can manage items, interact with room loot, and persist their gear between sessions while respecting MythosMUD security and UX principles.

## User Stories

### Catalog My Possessions

As a player, I want to view what I am carrying and wearing, so that I can plan my next eldritch excursion without consulting arcane spreadsheets.

Players invoke an `inventory` command to see stacked item entries, remaining capacity out of 20 slots, and a separate equipped-slot readout. Responses must render through the existing terminal client without layout breakage and include structured logging of the request.

### Handle Cursed Artifacts Safely

As a player, I want to pick up, drop, equip, and unequip items with slot enforcement, so that I can manipulate relics within the rules of the Mythos without corrupting the game state.

The system enforces inventory capacity, auto-swaps items between slots and backpack, respects left/right slot variants, rejects pickups when full by leaving the item in the room, and records all actions in structured logs for moderation.

### Share Discoveries with Fellow Investigators

As a player, I want rooms to show dropped items when I enter or look, so that my party can coordinate treasure recovery without invoking forbidden DB queries.

Room descriptions append a concise list of dropped items stored in memory on the room object. Lists update on pickup/drop actions and vanish after server restart per design notes.

## Spec Scope

1. **Inventory Persistence** - Extend player persistence to store 20-slot inventories, stack counts, and equipped-slot mappings.
2. **Inventory Service Layer** - Implement services for stacking, capacity checks, equip/unequip swapping, and room drop management.
3. **Player Commands** - Add inventory, equip, unequip, drop, and pickup commands with validation and structured logging.
4. **Room Rendering** - Update room description pipeline to include current dropped item summaries.
5. **Test Coverage** - Author pytest suites covering inventory limits, stacking, equip flows, room drops, and persistence round-trips.

## Out of Scope

- Non-player inventories such as containers, NPC gear, or shared vaults.
- Item stat modifiers, combat effects, or crafting systems.
- Persistent room drops surviving server restarts or shard transfers.

## Expected Deliverable

1. Inventory/equipment interactions validated by automated tests (`make test`) with coverage for stacking, capacity, and room drops.
2. Room descriptions and command outputs render correctly in the terminal client and surface structured logs for moderation tooling.
3. Player data persistence includes inventory and equipped state, confirmed via round-trip tests without breaking existing saves.
