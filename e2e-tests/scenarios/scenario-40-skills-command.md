# Scenario 40: /skills Command Returns Active Character's Skills (Plan 10.8 E3)

## Overview

Validates that the `/skills` slash command, when sent from the game as the active character,
returns that character's skills in the game log (e.g. "Your skills:", list of skill names and
values). Plan 10.8 E3.

## Prerequisites

1. **Server running** on port 54731; **client** on 5173.
2. **Test user** logged in with a character in game (command input visible).
3. **Character has skills** (created via revised flow or existing data) so the response is
   non-empty; or assert "No skills recorded" if that is the expected state.

## Test Configuration

**Test player**: ArkanWolfshade (or any user with a character that has skills).

**Approach**: Playwright; automate via `client/tests/e2e/runtime/character/skills-visibility.spec.ts`.

## Execution Steps

### Step 1: Reach game

- Log in and enter the game (command input visible).

### Step 2: Send /skills command

- In the command input, type `/skills` and submit (Enter).

### Step 3: Assert response in game log

- Game log (or command response area) shows the command result.
- **Content**: Response includes "Your skills:" and either skill lines (e.g. "SkillName: 50%")
  or "No skills recorded for this character." (exact text may vary per server).

## Success Criteria

- [ ] `/skills` can be sent from the game command input.
- [ ] Response appears in the game log.
- [ ] Response contains "Your skills:" and skill list or "No skills recorded" as appropriate.

## Automated Implementation

Playwright spec: `client/tests/e2e/runtime/character/skills-visibility.spec.ts` (E3 test).
Uses `executeCommand(page, '/skills')` and `waitForMessage(page, /Your skills:/)` (or equivalent).

## Status

**Scenario ID**: 40 | **Plan**: 10.8 E3 | **Version**: 1.0
