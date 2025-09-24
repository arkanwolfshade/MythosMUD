# Spec Requirements Document

> Spec: Profession System
> Created: 2025-09-23

## Overview

Implement a character profession selection system that allows players to choose a profession during character creation, with professions gated by stat requirements and influencing game mechanics. This feature will provide character specialization and foundation for future mechanical depth.

## User Stories

### Character Creation with Profession Selection

As a new player, I want to select a profession for my character during creation, so that I can specialize my character and understand how it will affect my gameplay experience.

**Detailed Workflow:**
1. Player completes registration
2. Player is presented with profession selection screen showing available professions
3. Player can view profession descriptions, flavor text, and stat requirements
4. Player selects a profession by clicking on the profession card
5. Player proceeds to stat rolling, which only shows combinations meeting profession requirements
6. Player can go back to change profession selection if desired
7. Player confirms stats and enters the game with their chosen profession

### Stat Rolling with Profession Requirements

As a player, I want my stat rolls to respect my chosen profession's requirements, so that I always get viable character combinations that work with my profession choice.

**Detailed Workflow:**
1. Player has selected a profession with specific stat requirements
2. System rolls stats using weighted probabilities to favor valid combinations
3. System validates rolled stats against profession requirements
4. System discards invalid rolls and re-rolls until valid combination found
5. Player sees only stat combinations that meet their profession requirements
6. Player can accept or reject the rolled stats

## Spec Scope

1. **Profession Selection Screen** - Card-based UI displaying available professions with descriptions, requirements, and flavor text
2. **Database Schema** - Professions table and player table modification to store profession choices
3. **Stat Rolling Integration** - Modified stat rolling endpoint that accepts profession_id and respects requirements
4. **Navigation Flow** - Updated character creation flow with profession selection between registration and stat rolling
5. **MVP Professions** - Two basic professions (Tramp and Gutter Rat) with no requirements for initial implementation

## Out of Scope

- Mechanical effects implementation (bonuses/penalties from professions)
- Advanced profession requirements beyond minimum stat values
- Profession-based combat or social mechanics
- Profession change functionality after character creation
- Profession-specific starting equipment or abilities

## Expected Deliverable

1. Players can successfully select a profession during character creation and proceed through the complete flow
2. Stat rolling system respects profession requirements and only shows valid combinations
3. Profession choice is properly persisted to the database and associated with the player character
