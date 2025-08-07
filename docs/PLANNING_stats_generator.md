# Technical Planning: Random Stats Generator for Character Creation (Issue #86)

## Overview
Implement a feature in the character creation process that allows new players to randomly generate their character's starting stats. This will provide a quick and engaging way to create unique characters, in addition to any existing manual stat allocation methods.

## Acceptance Criteria (from Issue #86)
- The character creator presents a "Roll for Stats" option alongside existing stat allocation methods.
- The "Roll for Stats" option generates random values for each core stat (e.g., Strength, Dexterity, Intelligence, Constitution, Wisdom, Charisma) within defined min/max ranges.
- Generated stats are displayed to the player, with options to accept or re-roll.
- Re-rolling generates a new set of random stats.
- Generated stats must allow the player to select a valid starting class (if classes have stat prerequisites).
- Once accepted, stats are permanently assigned and cannot be re-rolled again during that session.

## Technical Implementation Guidance

### 1. Identify Core Stats and Ranges
- Confirm the list of core stats (likely: Strength, Dexterity, Intelligence, Constitution, Wisdom, Charisma).
- Define min/max values for each stat (e.g., 3-18 for D&D style, or as per MythosMUD design).
- If classes have prerequisites, document these requirements.

### 2. Update Character Creation Flow
- Locate the character creation logic (likely in `server/` or related modules).
- Add a new option: "Roll for Stats".
- Ensure the UI/CLI presents this option clearly.

### 3. Implement Random Stat Generation
- Create a function to generate random values for each stat within the allowed range.
- Ensure the generated set meets any class prerequisites (if applicable). If not, re-roll or prompt the user.
- Store the generated stats temporarily until accepted.

### 4. Display and Accept/Re-roll Logic
- Present the generated stats to the player.
- Provide options: Accept or Re-roll.
- If Re-roll: generate a new set and repeat.
- If Accept: assign stats to the character and lock them in for the session.
- Prevent further re-rolls after acceptance.

### 5. Data Persistence
- Ensure accepted stats are saved to the character's profile in the database or persistent storage.
- If using sessions, ensure temporary stats are not saved until accepted.

### 6. Testing
- Unit tests for stat generation (range, class prerequisites, repeatability).
- Integration tests for the character creation flow (UI/CLI interaction, persistence).

### 7. Documentation
- Update any relevant documentation to describe the new feature and its usage.

## Potential Files/Modules to Update
- Character creation handler/module (likely in `server/` or similar)
- Player/character model definitions
- UI/CLI code for character creation
- Tests (unit and integration)
- Documentation (README, in-code comments)

## Open Questions
- What are the exact stat names and ranges?
- What are the class prerequisites, if any?
- Is the character creation flow UI, CLI, or both?
- Where is the best place to store temporary stats before acceptance?

---

This plan should be refined as you review the current codebase and answer the open questions above.
