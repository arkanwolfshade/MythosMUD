# Scenario 39: Skills (New Tab) — URL and Content (Plan 10.8 E2)

## Overview

Validates that from the in-game main menu (ESC), "Skills (New Tab)" opens a new tab with the
active character's ID in the URL and the skills page loads and shows that character's skills
(or appropriate error). Plan 10.8 E2.

## Prerequisites

1. **Server running** on port 54731; **client** on 5173.
2. **Test user** with at least one character (so login reaches game).
3. **Character has skills** (created via revised flow or existing data) so the skills page
   can show a non-empty list (or "No skills recorded" is acceptable).

## Test Configuration

**Test player**: ArkanWolfshade (or any user with a character in game).

**Approach**: Playwright; automate via `client/tests/e2e/runtime/character/skills-visibility.spec.ts`.

## Execution Steps

### Step 1: Reach game and open main menu

- Log in and enter the game (character selected, command input visible).
- Press **Escape** to open the main menu.
- Confirm the menu shows a "Skills (New Tab)" button.

### Step 2: Open Skills in new tab

- Click "Skills (New Tab)".
- A new tab/window opens. Switch to it (or capture popup in Playwright).

### Step 3: Assert URL and skills page

- **URL**: New tab URL contains `/skills` and `playerId=` (e.g. `/skills?playerId=<uuid>`).
- **Content**: Page shows "Character Skills" heading and either a list of skills (name and %)
  or "No skills recorded" or an explicit error ("Not authenticated", "No character specified",
  etc.), depending on auth and playerId.

## Success Criteria

- [ ] Main menu opens on Escape; "Skills (New Tab)" is visible and clickable.
- [ ] Clicking it opens a new tab.
- [ ] New tab URL includes `playerId=` and path `/skills`.
- [ ] Skills page loads and shows "Character Skills" (or a defined error state).

## Automated Implementation

Playwright spec: `client/tests/e2e/runtime/character/skills-visibility.spec.ts` (E2 test).

## Status

**Scenario ID**: 39 | **Plan**: 10.8 E2 | **Version**: 1.0
