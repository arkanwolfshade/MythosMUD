# Spec Requirements Document

> Spec: Combat System Implementation
> Created: 2025-01-27

## Overview

Implement a comprehensive turn-based combat system for MythosMUD that allows players to engage in tactical combat with NPCs. The system will feature dexterity-based turn order, thematic messaging, XP rewards, and full integration with existing game systems. This is a tracer-bullet implementation designed to establish the foundation for future combat enhancements.

## User Stories

### Player Combat Engagement

As a player, I want to attack NPCs in my current room using the `attack <target>` command, so that I can engage in tactical combat and earn experience points.

**Detailed Workflow:**

1. Player uses `attack <target>` command to initiate combat
2. System validates target exists and is attackable
3. Combat begins with dexterity-based turn order
4. Combat automatically progresses through rounds every 6 seconds
5. Player and NPC alternate turns until one is defeated
6. NPCs perform non-combat actions during their turns (defensive maneuvers, taunts, thematic behaviors)
7. Player receives XP rewards when defeating NPCs
8. Combat messages are broadcast to all room occupants
9. Health tracking displays real-time updates during combat

### Thematic Combat Experience

As a player, I want to receive immersive, Cthulhu Mythos-themed combat messages that vary based on my perspective (attacker/defender/observer), so that combat feels engaging and atmospheric.

**Detailed Workflow:**

1. Player attacks NPC and sees "You swing your fist at the rat and hit for 1 damage (9/10 HP remaining)"
2. Other players see "Ithaqua swings their fist at the rat and hits for 1 damage (9/10 HP remaining)"
3. NPC performs non-combat action: "The rat darts around nervously, trying to avoid your blows"
4. Combat automatically continues to next round after 6 seconds
5. NPC death messages are thematic and varied by NPC type
6. All messages maintain the game's horror atmosphere

### Combat State Management

As a player, I want combat to persist even if I disconnect temporarily, so that I can resume combat when I reconnect within the timeout period.

**Detailed Workflow:**

1. Player initiates combat with NPC
2. Player disconnects during combat
3. Combat state is maintained for timeout period
4. Player reconnects and can resume combat
5. Combat ends if timeout is exceeded

## Spec Scope

1. **Core Combat Mechanics** - Turn-based combat with dexterity-based turn order, 1 damage attacks, and mob death
2. **Auto-Progression System** - Combat automatically continues through rounds every 6 seconds until completion
3. **NPC Passive Behavior** - NPCs perform non-combat actions during their turns (defensive maneuvers, taunts, thematic behaviors)
4. **Health Tracking System** - Real-time health display during combat with on-demand status checking
5. **Command System Integration** - Attack command with target validation and multiple aliases (punch, kick, strike)
6. **Event System Integration** - Full integration with existing event system including new combat events
7. **Messaging System** - Thematic combat messages with perspective-based formatting and health updates
8. **XP Reward System** - Immediate XP awards when NPCs are defeated
9. **State Management** - In-memory combat state with automatic cleanup and turn progression
10. **Database Integration** - Combat data stored in existing NPC JSON fields
11. **Security Integration** - Extended validation with existing rate limiting and security measures

## Out of Scope

Player vs Player combat

- Weapon and equipment integration
- Status effect integration
- Room environment effects
- Advanced AI for NPCs
- Combat spells and magic
- Advanced combat mechanics (critical hits, dodging, etc.)
- Formal user acceptance testing
- Advanced performance optimization
- Complex admin commands

## Expected Deliverable

1. **Functional Combat System** - Players can attack NPCs, engage in turn-based combat, and receive XP rewards
2. **Integrated Messaging** - Thematic combat messages broadcast to all room occupants through existing event system
3. **Comprehensive Testing** - Unit tests and integration tests covering all combat functionality
4. **Full Documentation** - Complete documentation including user guides, developer guides, and troubleshooting
5. **Production Deployment** - Combat system deployed with feature flag for easy enable/disable
