# Scenario 38: Revised Character Creation (Stats → Profession → Skills → Name)

## Overview

Validates the revised character creation flow (plan 10.6): stats first, then profession, skills,
then name, then create. Ensures the full flow completes and the new character appears in the
character list and is selectable.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Server Running**: Development server is running on port 54731
2. **Client Accessible**: Client is accessible on port 5173
3. **Test User**: A test user (e.g. from TEST_PLAYERS) with zero or few characters so the
   creation flow is reachable (login → character selection → "Create New Character" → stats step)
4. **Skills API**: GET /api/skills returns a non-empty catalog so skill allocation can be completed

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

## Test Configuration

**Test Player**: ArkanWolfshade (or any user with room to create a character)

**Flow Order**: Stats → Profession → Skills → Name → Create

**Testing Approach**: Playwright (single tab); can be automated via `client/tests/e2e/runtime/character/
revised-character-creation.spec.ts` or executed manually per steps below.

**Timeout Settings**: Use project E2E timeouts (e.g. 30s per step, 180s test timeout).

## Execution Steps

### Step 1: Login and Enter Character Creation

**Purpose**: Reach the character creation flow (stats-first screen).

**Actions**:

1. Navigate to client (<<http://localhost:5173>).
2. Log in with test credentials (e.g. username/password from TEST_PLAYERS).
3. If the character selection screen appears ("Select Your Character"), click "Create New Character".
4. Wait until the stats-rolling screen is visible (data-testid="stats-rolling-screen" or "Accept Stats"
   button).

**Expected Result**: Stats rolling screen is shown (roll displayed, "Accept Stats" and "Reroll Stats"
buttons present).

### Step 2: Accept Stats

**Purpose**: Lock in rolled stats and proceed to profession selection.

**Actions**:

1. Click the "Accept Stats" button.
2. Wait for the profession selection screen.

**Expected Result**: "Choose Your Profession" heading and profession cards are visible; "Next"
button is enabled after selecting a profession.

### Step 3: Select Profession and Continue

**Purpose**: Choose a profession and move to skill allocation.

**Actions**:

1. Click one profession card to select it.
2. Click the "Next" button.
3. Wait for the skill allocation screen (data-testid="skill-assignment-screen" or "Skill Allocation"
   heading).

**Expected Result**: Skill Allocation screen with nine occupation slots and four personal interest
slots (dropdowns); "Next: Name character" button present.

### Step 4: Allocate Skills and Continue to Name

**Purpose**: Fill all occupation and personal interest slots and proceed to the name step.

**Actions**:

1. For each of the nine occupation skill dropdowns, select any valid skill (e.g. first non-placeholder
   option).
2. For each of the four personal interest dropdowns, select any valid skill.
3. Click "Next: Name character".
4. Wait for the character name screen (data-testid="character-name-screen" or "Enter name" placeholder).

**Expected Result**: Character name screen with name input and "Create Character" button.

### Step 5: Enter Name and Create Character

**Purpose**: Submit the full creation payload and create the character.

**Actions**:

1. Enter a unique character name in the name field (e.g. "E2ERevisedFlow" or a timestamped name).
2. Click "Create Character".
3. Wait for navigation to character list or game (e.g. "Select Your Character" or command input /
   game UI).

**Expected Result**: Character is created (HTTP 201); UI shows character selection list with the new
character, or the game loads with that character. New character is selectable.

### Step 6: Scenario Completion

**Purpose**: Confirm success and document completion.

**Verification**:

- New character appears in the character list or game session.
- No unhandled errors in console; creation flow completed in order: stats → profession → skills →
  name → create.

## Success Criteria

- [ ] Login and "Create New Character" (if applicable) reach stats screen
- [ ] Accept Stats advances to profession selection
- [ ] Profession selection and Next advance to skill allocation
- [ ] All 13 skill slots filled and "Next: Name character" advances to name screen
- [ ] Name entered and "Create Character" succeeds; character in list or game
- [ ] Flow order matches plan 10.6 (stats → profession → skills → name → create)

## Automated Implementation

Playwright spec: `client/tests/e2e/runtime/character/revised-character-creation.spec.ts`

Run (from project root, with server and client up): `npx playwright test revised-character-creation
--config=client/tests/e2e/playwright.runtime.config.ts` (or via project Makefile/task if defined).

## Status

**Scenario ID**: 38
**Plan Reference**: 10.8 E1 (revised character creation E2E)
**Document Version**: 1.0
**Last Updated**: 2025-02-17
