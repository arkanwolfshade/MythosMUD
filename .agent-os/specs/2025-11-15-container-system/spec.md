# Spec Requirements Document

> Spec: Container System
> Created: 2025-11-15

## Overview

Implement a unified container system that allows environmental props, wearable gear, and corpses to act as secure storage with auditable interactions. The feature delivers consistent server persistence plus modern client UX for looting, backpack management, and compliance-safe sharing.

## User Stories

### Looting Environmental Containers

As an explorer, I want to open world objects like chests and cabinets, so that I can move items between them and my inventory under the game’s slot limits. When I interact with a container, the client should display a split-pane view, enforce locking rules, and render real-time updates if another player moves items.

### Wearable Storage Management

As a player who carries backpacks or bandoliers, I want nested storage that travels with my character, so that I can organize equipment without dropping items. Equipping or unequipping a wearable container should automatically persist its internal contents, respect capacity rules, and warn me before overflow forces items onto the ground.

### Corpse Looting with Grace Periods

As a teammate, I want to loot a fallen ally or foe once an ownership timer expires, so that loot sharing stays fair and COPPA-compliant. Corpses should appear as containers with countdown overlays, emit structured logs for every transfer, and delete themselves after decay while redistributing any unclaimed items.

## Spec Scope

1. **ContainerComponent data model** - Introduce a reusable server component storing metadata (type, owner, locks, capacity, decay) plus nested `InventoryStack` items.
2. **Persistence & schema updates** - Extend inventory schema, add `containers` storage, and migrate room JSON definitions to flag environmental containers.
3. **ContainerService + APIs** - Implement server commands/events (`ContainerOpened/Updated/Closed`) and guard concurrent mutations through the existing mutation guard pattern.
4. **React container UI** - Build split-pane environmental UI, backpack tabs, corpse countdown overlay, and keyboard-accessible controls wired to new websocket events.
5. **Corpse lifecycle automation** - Hook combat death events to spawn corpse containers, enforce owner-only windows, decay timers, and structured logging.

## Out of Scope

Crafting or enchanting new container item types beyond backpacks already in game data.

- Any monetization or cosmetic systems tied to container skins or capacity boosts.

## Expected Deliverable

1. Players can open any configured container, transfer items bi-directionally, and observe updates across multiple clients without desync.
2. Automated tests (server + client) cover container creation, mutation guards, wearable transitions, and corpse decay flows with ≥80% coverage in touched modules.
