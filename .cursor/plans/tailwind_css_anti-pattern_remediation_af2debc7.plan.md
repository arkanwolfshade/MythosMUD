---
name: Tailwind CSS Anti-Pattern Remediation
overview: Remediate Tailwind CSS anti-patterns, semantic issues, and bad code across the codebase by replacing arbitrary values with design tokens, fixing accessibility issues with outline-none, improving class ordering, and identifying component abstraction opportunities.
todos:
  - id: extend-tailwind-config
    content: Extend tailwind.config.js with design tokens for arbitrary values (font sizes, spacing, heights, max-heights, letter spacing)
    status: completed
  - id: fix-outline-none-core
    content: Replace outline-none with outline-hidden in core UI components (TerminalInput.tsx, TerminalButton.tsx, designTokens.ts, LogoutButton.tsx)
    status: completed
  - id: fix-outline-none-feature
    content: Replace outline-none with outline-hidden in feature components (RescueStatusBanner, HallucinationTicker, IncapacitatedBanner, RoomEditModal, ChatPanel, FeedbackForm, BackpackTab)
    status: completed
  - id: replace-arbitrary-font-sizes
    content: Replace arbitrary font size values (text-[10px], text-[11px]) with design tokens in RescueStatusBanner, HallucinationTicker, MythosTimeHud, HeaderBar
    status: completed
  - id: replace-arbitrary-spacing
    content: Replace arbitrary spacing values (min-w-[140px], min-w-[200px], min-w-[16px]) with design tokens in ChannelSelector, ChatPanel
    status: completed
  - id: replace-arbitrary-heights
    content: Replace arbitrary height values (min-h-[150px], min-h-[300px], min-h-[44px]) with design tokens in CommandPanel, GameLogPanel, GameInfoPanel, CommandHistoryPanel, LogoutButton
    status: completed
  - id: replace-arbitrary-max-heights
    content: Replace arbitrary max-height values (max-h-[90vh], max-h-[80vh]) with design tokens in RoomEditModal, EdgeCreationModal, FeedbackForm, RoomDetailsPanel, EdgeDetailsPanel
    status: completed
  - id: replace-arbitrary-tracking
    content: Replace arbitrary letter spacing (tracking-[0.3em]) with design token in MythosTimeHud
    status: completed
  - id: reorder-classes-core
    content: Improve class ordering in high-priority core components (App.tsx, TerminalInput.tsx, TerminalButton.tsx)
    status: completed
  - id: reorder-classes-feature
    content: Improve class ordering in high-traffic feature components (FeedbackForm.tsx, ChatPanel.tsx)
    status: completed
  - id: create-dismiss-button
    content: Create reusable DismissButton component and replace instances in RescueStatusBanner, HallucinationTicker, IncapacitatedBanner
    status: completed
  - id: create-modal-container
    content: Create reusable ModalContainer component and refactor RoomEditModal, EdgeCreationModal, FeedbackForm to use it
    status: completed
  - id: audit-terminal-input-usage
    content: Audit components to ensure they use TerminalInput instead of raw input elements
    status: completed
  - id: update-test-files
    content: Update test files that check for outline-none classes (TerminalButton.test.tsx, LogoutButton.test.tsx, and others)
    status: completed
  - id: run-codacy-analysis
    content: Run Codacy analysis on all modified files to ensure code quality
    status: completed
  - id: verify-visual-regressions
    content: Verify no visual regressions and that accessibility is maintained after all changes
    status: completed
---

# Tailwind CSS Anti-Pattern Remediation Plan

## Overview

This plan addresses multiple categories of Tailwind CSS issues found in the codebase: arbitrary values, accessibility problems, class ordering inconsistencies, and opportunities for better component abstraction.

## Issues Identified

### 1. Arbitrary Values in Markup (31+ instances)

**Problem**: Using arbitrary values like `text-[11px]`, `text-[10px]`, `min-w-[140px]`, `max-h-[90vh]`, etc. instead of design tokens.

**Files Affected**:

- `client/src/components/lucidity/RescueStatusBanner.tsx` - `text-[11px]` (3 instances)
- `client/src/components/lucidity/HallucinationTicker.tsx` - `text-[11px]`
- `client/src/components/MythosTimeHud.tsx` - `text-[10px]`, `text-[11px]`, `tracking-[0.3em]`
- `client/src/components/ui-v2/HeaderBar.tsx` - `text-[10px]`
- `client/src/components/panels/CommandPanel.tsx` - `min-h-[150px]`
- `client/src/components/panels/GameLogPanel.tsx` - `min-h-[300px]`
- `client/src/components/ui-v2/panels/GameInfoPanel.tsx` - `min-h-[300px]`
- `client/src/components/ui-v2/panels/CommandHistoryPanel.tsx` - `min-h-[150px]`
- `client/src/components/ui/ChannelSelector.tsx` - `min-w-[140px]`
- `client/src/components/panels/ChatPanel.tsx` - `min-w-[16px]`, `min-w-[200px]`
- `client/src/components/map/RoomEditModal.tsx` - `max-h-[90vh]`
- `client/src/components/map/EdgeCreationModal.tsx` - `max-h-[90vh]`
- `client/src/components/ui/FeedbackForm.tsx` - `max-h-[90vh]`
- `client/src/components/map/RoomDetailsPanel.tsx` - `max-h-[80vh]`
- `client/src/components/map/EdgeDetailsPanel.tsx` - `max-h-[80vh]`
- `client/src/components/ui/LogoutButton.tsx` - `min-h-[44px]`
- And more...

**Solution**:

1. Extend `tailwind.config.js` with design tokens for:

- Font sizes: `text-xs-2` (10px), `text-xs-3` (11px)
- Spacing: `min-w-button` (140px), `min-w-input` (200px)
- Heights: `min-h-panel-sm` (150px), `min-h-panel-md` (300px), `min-h-touch` (44px)
- Max heights: `max-h-modal` (90vh), `max-h-panel` (80vh)
- Letter spacing: `tracking-eldritch` (0.3em)

2. Replace all arbitrary values with these tokens

### 2. Accessibility: outline-none Usage (20 instances)

**Problem**: Using `focus:outline-none` and `focus-visible:outline-none` removes focus indicators completely, breaking accessibility. Should use `outline-hidden` which maintains accessibility in forced colors mode.

**Files Affected**:

- `client/src/components/ui/TerminalInput.tsx` - Line 43
- `client/src/components/ui/designTokens.ts` - Lines 185, 251, 263
- `client/src/components/ui/TerminalButton.tsx` - Line 30
- `client/src/components/ui/LogoutButton.tsx` - Line 41
- `client/src/components/lucidity/RescueStatusBanner.tsx` - Line 78
- `client/src/components/lucidity/HallucinationTicker.tsx` - Line 61
- `client/src/components/health/IncapacitatedBanner.tsx` - Line 38
- `client/src/components/map/RoomEditModal.tsx` - Lines 242, 517
- `client/src/components/panels/ChatPanel.tsx` - Line 582
- `client/src/components/ui/FeedbackForm.tsx` - Lines 83, 102, 119, 152
- `client/src/components/containers/BackpackTab.tsx` - Line 117
- Test files (update expected classes)

**Solution**: Replace all `focus:outline-none` and `focus-visible:outline-none` with `focus:outline-hidden` and `focus-visible:outline-hidden`. Update `designTokens.ts` to use `outline-hidden` in the focus utilities.

### 3. Class Ordering Inconsistencies

**Problem**: Classes are not consistently ordered according to the recommended pattern: Layout > Flexbox > Grid > Box Model > Typography > Backgrounds > Borders > Effects > Interactivity > States.

**Example Issues**:

- `client/src/components/ui/FeedbackForm.tsx` Line 63: `bg-black bg-opacity-50 flex items-center justify-center z-50` - should be `flex items-center justify-center z-50 bg-black bg-opacity-50`
- Many components have mixed ordering

**Solution**:

1. Create a linting rule or documentation for class ordering
2. Systematically review and reorder classes in affected components
3. Focus on high-traffic components first: `App.tsx`, `FeedbackForm.tsx`, `ChatPanel.tsx`, `TerminalInput.tsx`, `TerminalButton.tsx`

### 4. Component Abstraction Opportunities

**Problem**: Some repeated patterns could be abstracted into reusable components, though the codebase already has good abstractions like `TerminalButton` and `TerminalInput`.

**Opportunities**:

- Dismiss buttons with similar styling (found in `RescueStatusBanner`, `HallucinationTicker`, `IncapacitatedBanner`)
- Modal containers with similar structure (`RoomEditModal`, `EdgeCreationModal`, `FeedbackForm`)
- Input fields that aren't using `TerminalInput` component

**Solution**:

1. Create a `DismissButton` component for the repeated dismiss button pattern
2. Create a `ModalContainer` component for consistent modal styling
3. Audit components to ensure they use `TerminalInput` instead of raw `<input>` elements

### 5. Design Token Configuration

**Problem**: While `designTokens.ts` exists, arbitrary values are still used instead of extending `tailwind.config.js` properly.

**Solution**:

1. Move reusable design tokens from `designTokens.ts` into `tailwind.config.js` where appropriate
2. Keep `designTokens.ts` for component-specific class builders
3. Ensure all arbitrary values are replaced with config-based tokens

## Implementation Steps

1. **Extend tailwind.config.js** with design tokens for arbitrary values
2. **Fix accessibility issues** by replacing `outline-none` with `outline-hidden`
3. **Replace arbitrary values** with design tokens across all affected files
4. **Improve class ordering** in high-priority components
5. **Create reusable components** for repeated patterns (DismissButton, ModalContainer)
6. **Update tests** to reflect class name changes
7. **Run Codacy analysis** on all modified files
8. **Verify** no visual regressions and accessibility is maintained

## Files to Modify

### Configuration

- `client/tailwind.config.js` - Add design tokens

### Core Components (High Priority)

- `client/src/components/ui/TerminalInput.tsx`
- `client/src/components/ui/TerminalButton.tsx`
- `client/src/components/ui/designTokens.ts`
- `client/src/components/ui/LogoutButton.tsx`

### Feature Components

- `client/src/components/lucidity/RescueStatusBanner.tsx`
- `client/src/components/lucidity/HallucinationTicker.tsx`
- `client/src/components/health/IncapacitatedBanner.tsx`
- `client/src/components/MythosTimeHud.tsx`
- `client/src/components/ui-v2/HeaderBar.tsx`
- `client/src/components/panels/CommandPanel.tsx`
- `client/src/components/panels/GameLogPanel.tsx`
- `client/src/components/panels/ChatPanel.tsx`
- `client/src/components/ui/FeedbackForm.tsx`
- `client/src/components/map/RoomEditModal.tsx`
- `client/src/components/map/EdgeCreationModal.tsx`
- `client/src/components/map/RoomDetailsPanel.tsx`
- `client/src/components/map/EdgeDetailsPanel.tsx`
- `client/src/components/ui/ChannelSelector.tsx`
- `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- `client/src/components/ui-v2/panels/CommandHistoryPanel.tsx`
- `client/src/components/containers/BackpackTab.tsx`

### New Components to Create

- `client/src/components/ui/DismissButton.tsx`
- `client/src/components/ui/ModalContainer.tsx`

### Test Files

- Update test files that check for `outline-none` classes
