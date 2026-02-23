# Scenario 42: Quest Log Visible After Login

## Overview

Validates that after login and entering the game, the Journal (quest log) panel is visible and
shows either the quest log content or the empty state. Part of the quest subsystem E2E coverage.

## Prerequisites

1. **Server running** on port 54731; **client** on 5173.
2. **Test user** with at least one character (e.g. ArkanWolfshade) so login reaches game.
3. **E2E database** may have quest data or not; test accepts either "Quest log" (with entries)
   or "You have no active or completed quests." (empty state).

## Test Configuration

**Test player**: ArkanWolfshade (canonical E2E account).

**Approach**: Playwright; automate via `client/tests/e2e/runtime/quest/quest-log-visible.spec.ts`.

## Execution Steps

### Step 1: Login and enter game

- Log in as ArkanWolfshade and select character; dismiss MOTD until command input is visible.
- Wait for current character name to be visible (game state loaded).

### Step 2: Assert Journal panel content

- The default layout includes the Journal panel (quest log) in the middle column.
- Page must show either:
  - **With quests**: section header "Quest log" and at least one quest entry, or
  - **Empty**: "You have no active or completed quests."

## Success Criteria

- [ ] After game load, the Journal panel content is visible.
- [ ] Either "Quest log" (header) or "You have no active or completed quests." is present.

## Automated Implementation

Playwright spec: `client/tests/e2e/runtime/quest/quest-log-visible.spec.ts`.

## Status

**Scenario ID**: 42 | **Feature**: Quest subsystem | **Version**: 1.0
