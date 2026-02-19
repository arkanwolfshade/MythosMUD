# Scenario 41: Skills After Character Creation (Plan 10.8 E4)

## Overview

After completing the revised character creation flow (stats → profession → skills → name → create),
GET skills or the `/skills` command shows the expected skills for that character (allocated +
catalog-base + profession mods). Plan 10.8 E4.

## Prerequisites

1. **Server running** on port 54731; **client** on 5173.
2. **Test user** that can create a new character (zero or few characters).

## Execution Steps

1. Complete revised character creation (stats → profession → skills → name → create) so a new
   character exists.
2. From the character list, select that character (or the one just created) and enter the game.
3. Run `/skills` in the game (or open Skills (New Tab) and confirm content).
4. Assert the response contains "Your skills:" and either skill lines (e.g. "SkillName: 50%") or
   "No skills recorded" as appropriate; allocated and catalog-base skills should appear for a
   newly created character.

## Success Criteria

- [ ] After creation, character can be selected and game entered.
- [ ] `/skills` (or GET skills) returns that character's skills.
- [ ] Output includes "Your skills:" and at least one skill line or "No skills recorded."

## Automated Implementation

Extended test in `client/tests/e2e/runtime/character/revised-character-creation.spec.ts` (E4 test):
full creation flow, then select character and enter game, then `/skills` and assert.

## Status

**Scenario ID**: 41 | **Plan**: 10.8 E4 | **Version**: 1.0
