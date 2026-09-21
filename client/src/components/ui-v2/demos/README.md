# ui-v2 demos

Design-only showcases for Mythos UI primitives and eldritch visual effects.

## Purpose

- Exercise and visually inspect `ui-v2/primitives` (icons, panels, buttons, inputs).
- Not part of `GameClientV2` gameplay UI.
- Not exported from the primitives barrel (`ui-v2/primitives/index.ts`).
- Root uses `eldritch-demo-force-motion` so OS reduced-motion does not blank the showcase.

## Entry

Reachable from the public login screen via **View Eldritch Effects Demo**
(`showDemo` → `AppDemoView` → lazy import in `appLazyScreens.tsx`).

## Contents

| File                           | Role                           |
| ------------------------------ | ------------------------------ |
| `EldritchEffectsDemo.tsx`      | Interactive effects playground |
| `eldritchEffectsDemoData.ts`   | Effect option / class data     |
| `EldritchEffectsDemo.test.tsx` | Unit tests (sibling co-locate) |
