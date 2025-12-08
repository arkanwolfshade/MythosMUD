# Spec Requirements Document

> Spec: Extend Look Command
> Created: 2025-11-20

## Overview

Extend the `/look` command to support examining players, items, and containers with explicit syntax options and instance targeting. This enhancement improves player interaction and information discovery while maintaining backward compatibility with existing look functionality.

## User Stories

### Examining Other Players

As a player, I want to look at other players in my room to see their visible equipment, position, and apparent health/lucidity status, so that I can assess their condition and appearance. When I use `/look player Armitage` or `/look Armitage`, I should see their name, externally visible equipment (head, torso, legs, hands, feet, weapons), current position, and descriptive health/lucidity labels like "healthy" or "wounded" and "lucid" or "disturbed".

### Examining Items

As a player, I want to look at items in my room, inventory, equipped gear, or containers to see their detailed descriptions, so that I can understand item properties and make informed decisions. When I use `/look item lantern` or `/look lantern`, the system should search all accessible locations and display the item's name and long description from its prototype definition.

### Examining Container Contents

As a player, I want to look inside containers to see what items they contain, their capacity usage, and lock status, so that I can plan my looting and inventory management. When I use `/look container backpack`, `/look in backpack`, or `/look backpack`, I should see the container's name/description, a list of items inside with quantities, slot usage (e.g., "5/20 slots used"), and whether it's unlocked, locked, or sealed.

## Spec Scope

1. **Command Parser Extensions** - Add support for explicit type syntax (`/look player <name>`, `/look item <name>`, `/look container <name>`) and instance targeting (`backpack-2` or `backpack 2`) in the command parser.
2. **Player Look Functionality** - Implement player examination showing visible equipment, position, and descriptive health/lucidity labels with priority resolution.
3. **Item Look Functionality** - Implement item examination across all locations (room, inventory, equipped, containers) with prototype description lookup.
4. **Container Look Functionality** - Implement container examination with contents listing, capacity information, and lock status display.
5. **Target Resolution Priority** - Establish priority order (Players > NPCs > Items > Containers > Directions) for ambiguous target resolution.
6. **Direction Support Cleanup** - Remove diagonal direction support (northeast, northwest, southeast, southwest) to align with cardinal-only movement.

## Out of Scope

- Looking at room features or environmental objects beyond containers.
- Looking at items inside other players' inventories or equipped gear (only visible equipment shown).
- Looking at detailed item statistics beyond name and description.
- Container manipulation (opening/closing) via look command - that remains separate functionality.

## Expected Deliverable

1. Players can use `/look` with explicit syntax (`/look player <name>`, `/look item <name>`, `/look container <name>`) or implicit targeting that resolves in priority order, with instance targeting support for multiple items/containers.
2. Comprehensive test coverage (unit and integration) validates all look functionality including priority resolution, instance targeting, and edge cases with ≥80% coverage in touched modules.
