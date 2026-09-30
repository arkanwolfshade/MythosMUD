# MythosApp Package Design

**Version 1.0.0** · MythosMUD · 2026-09-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`client/src/mythosApp/` is the client's **app shell**: everything that happens between page load
and the moment `GameClientV2Container` takes over. It owns the pre-game session state machine —
login / register, session restore from a stored token, character selection, the four-step
character-creation wizard, the MOTD interstitial — plus the logout path back out of the game. It
renders no game UI itself; the game screen is a lazy hand-off (§3). This document is
reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md) for the same posture applied to behavioral
subsystems).

Written to close [`#742`](https://github.com/arkanwolfshade/MythosMUD/issues/742).
[ADR-022](../architecture/decisions/ADR-022-ui-v2-client-transition.md) covers the `ui-v2/`
component migration; it does not describe this layer. `mythosApp/` is **not** part of `ui-v2/`: it
sits above it and is what mounts it.

The package follows one pattern throughout: **`useMythosApp()` composes state + actions into a
flat `MythosAppViewModel`; `AppRootViews(vm)` is a pure function of that view model that picks
which screen to render.** `client/src/App.tsx` is the whole call site:

```tsx
const vm = useMythosApp();
return AppRootViews(vm);
```

## 2. Members

**[SPEC]**

### Composition root and view model

| File                         | Exports                                         | Purpose                                                                                                                         |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `useMythosApp.tsx`           | `useMythosApp`                                  | `useMythosAppState` → `useMythosAppActions(state)` → `buildMythosAppViewModel(state, actions)`. The only hook `App.tsx` calls.  |
| `mythosAppViewModel.ts`      | `MythosAppViewModel` (interface)                | The flat contract between the hooks and every view: state fields, setters, and `handle*` callbacks.                             |
| `mythosAppViewModelFactory.ts` | `buildMythosAppViewModel`                     | Spreads `buildStateViewModel` + `buildActionViewModel`. Purely a field-copy; adds no logic.                                     |
| `creationTypes.ts`           | `CreationStep`                                  | `'stats' \| 'profession' \| 'skills' \| 'name'`.                                                                                |
| `guards.ts`                  | `isObject`                                      | `Record<string, unknown>` narrowing used by every API-response parser in the package.                                           |

### State and actions

| File                       | Exports                | Purpose                                                                                                                                                                              |
| -------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `useMythosAppState.ts`     | `useMythosAppState`    | Two `useReducer` slices (`AuthSlice`, `CreationSlice`) with merge-patch reducers, per-field `SetStateAction`-style setters, `memoryMonitor` start/stop, `useAuthSessionRestore`, `useMythosAuthForm`. |
| `useMythosAppActions.ts`   | `useMythosAppActions`  | Four handler groups: creation, character (select / delete / create), MOTD + logout, auth UI (`toggleMode`, `handleKeyDown`, disconnect registration). Owns `returnToLogin`.          |
| `useAuthSessionRestore.ts` | `useAuthSessionRestore`| Mount-only effect: validate stored token → `restoreCharactersOnMount` → route to creation / auto-select / picker.                                                                    |
| `useMythosAuthForm.ts`     | `useMythosAuthForm`    | `handleLoginClick` / `handleRegisterClick`: sanitize → request → `persistTokensAndApplySession`.                                                                                     |

### Views (pure functions of the view model)

| File                        | Exports                                                                   | Purpose                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `AppRootViews.tsx`          | `AppRootViews`, `MythosAppViewModel` (type re-export)                     | The screen router (§3 decision table).                                                                            |
| `MythosLoginForm.tsx`       | `MythosLoginForm`, `MythosLoginFormProps`                                 | Login / register form with the "demo" button.                                                                     |
| `AppCreationFlowViews.tsx`  | `AppCreationFlowViews`                                                    | One lazy screen per `CreationStep`, each wrapped in `Suspense`.                                                   |
| `AppSessionOutroViews.tsx`  | `AppSessionOutroViews`                                                    | MOTD interstitial, then `GameClientV2Container`.                                                                  |
| `AppDemoView.tsx`           | `AppDemoView`                                                             | `EldritchEffectsDemo` showcase; `onExit` clears `showDemo`.                                                       |
| `appLazyScreens.tsx`        | `EldritchEffectsDemo`, `GameClientV2Container`, `MotdInterstitialScreen`, `ProfessionSelectionScreen`, `StatsRollingScreen`, `CharacterSelectionScreen`, `SkillAssignmentScreen`, `CharacterNameScreen`, `LoadingFallback` | The single place `React.lazy` boundaries for the shell are declared. |

### Auth and character I/O (framework-free)

| File                          | Exports                                                                                              | Purpose                                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `submitAuth.ts`               | `sanitizeLoginInputs`, `sanitizeRegisterInputs`, `submitLoginRequest`, `submitRegisterRequest`, `AuthSuccessPayload` | `POST {API_V1_BASE}/auth/login` and `/auth/register`; responses go through `assertLoginResponse`.          |
| `applyAuthenticatedSession.ts`| `persistTokensAndApplySession`, `AuthSessionSetters`                                                 | Writes access/refresh tokens to `secureTokenStorage`, sets state, chooses picker vs. creation wizard.       |
| `loginFailureMessage.ts`      | `loginFailureMessage`                                                                                | Server error body → user message (login).                                                                   |
| `registerFailureMessage.ts`   | `registerFailureMessage`                                                                             | Same for register, including FastAPI 422 validation arrays and password-rule rewording.                     |
| `apiErrorMessage.ts`          | `errorMessageFromApiBody`                                                                            | Generic `{detail}` / envelope → message; used by select and delete.                                         |
| `characterSessionApi.ts`      | `parseSelectCharacterResult`, `postSelectCharacter`, `requestDeleteCharacter`, `restoreCharactersOnMount` | Raw `fetch` wrappers against `/api/players/*`.                                                              |
| `mapServerCharacters.ts`      | `toCharacterInfoFromList`, `toCharacterInfoFromLogin`                                                | `ServerCharacterResponse` → `CharacterInfo`. The two differ in `player_id` precedence (§5).                 |
| `selectCharacterFlow.ts`      | `runSelectCharacterFlow`, `selectCharacterNetworkErrorMessage`, `SelectCharacterResult`              | Tagged-union result: `ok` / `server_unavailable` / `error` / `network_error`.                               |
| `creationCompleteFlow.ts`     | `refreshCharactersAfterCreation`, `messageFromCreationRefreshHttpError`, `CreationRefreshResult`     | Re-fetch character list after creation.                                                                     |
| `creationCompleteActions.ts`  | `runAfterCharacterCreatedFlow`, `CreationCompleteActions`                                            | Applies a `CreationRefreshResult` to state via injected setters.                                            |
| `deleteCharacterFlow.ts`      | `runDeleteCharacterFlow`, `nextStepForDeleteResult`, result / step types                            | DELETE then re-fetch; distinguishes `refresh_failed` (delete succeeded) from `delete_failed`.               |
| `deleteCharacterActions.ts`   | `executeDeleteCharacterUi`, `DeleteCharacterUiDeps`                                                  | Applies a delete result to state; empties → back to creation wizard.                                        |
| `motdContinueFlow.ts`         | `tryStartLoginGracePeriod`, `isGracePeriodServerUnavailableError`                                    | Best-effort `POST /api/players/{id}/start-login-grace-period` on MOTD continue.                             |
| `startLoginGracePeriod.ts`    | `postStartLoginGracePeriod`                                                                          | The `fetch` for the above.                                                                                  |
| `serverAvailability.ts`       | `isServerUnavailable`, `stringIndicatesServerUnavailable`, `errorDetailString`                       | Classifies fetch errors / 5xx / child-screen error strings as "server down → return to login".             |

Tests: `mythosApp/__tests__/` — `deleteCharacterActions`, `deleteCharacterFlow`, `useMythosAppState`.
Most of the package's flow modules have no direct test file.

Removed in this pass: `useMythosSessionChrome.ts` (see §4).

## 3. Boundary contract

**[SPEC]**

**Entry point.** `client/src/App.tsx` is the sole production importer of this package:
`useMythosApp` and `AppRootViews`. No other file under `src/` imports from `mythosApp/`.

**Screen selection.** `AppRootViews` evaluates top to bottom; the first match wins:

| # | Condition                                                             | Rendered                                            |
| - | --------------------------------------------------------------------- | --------------------------------------------------- |
| 1 | `showDemo`                                                            | `AppDemoView` → `EldritchEffectsDemo`               |
| 2 | `!isAuthenticated`                                                    | `MythosLoginForm`                                   |
| 3 | `showCharacterSelection && characters.length > 0`                     | lazy `CharacterSelectionScreen`                     |
| 4 | `creationStep !== null`                                               | `AppCreationFlowViews` (stats → profession → skills → name) |
| 5 | otherwise                                                             | `AppSessionOutroViews`: `showMotd` → `MotdInterstitialScreen`; else `GameClientV2Container` |

**Hand-off to the game.** `AppSessionOutroViews` mounts `GameClientV2Container` with
`playerName`, `authToken`, `characterId`, `onLogout`, `isLoggingOut`, `onDisconnect`. The container
calls `onDisconnect(fn)` to register its teardown; `handleLogout` invokes it through
`disconnectCallbackRef` before clearing state. That callback is the only channel from the game
back into the shell.

**Collaborators outside the package** (this doc does not describe their internals; several are
owned by [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746)):

- `utils/security.ts` — `secureTokenStorage` (get / set / clear / validity / expiry), `inputSanitizer`
- `utils/logoutHandler.ts` — `logoutHandler` (5 s timeout, disconnect + clear)
- `utils/apiTypeGuards.ts`, `utils/errorHandler.ts`, `utils/config.ts` (`API_V1_BASE`), `utils/memoryMonitor.ts`
- `components/{CharacterSelectionScreen,StatsRollingScreen,ProfessionSelectionScreen,SkillAssignmentScreen,CharacterNameScreen,MotdInterstitialScreen}.tsx`
- `components/ui-v2/GameClientV2Container.tsx`, `components/ui-v2/demos/EldritchEffectsDemo.tsx`
- `types/auth.ts` (`CharacterInfo`), `hooks/useStatsRolling.ts` (`Stats`)

**Invariants a caller must not violate:**

- **The view model is the only surface.** Views take `vm: MythosAppViewModel`, never state or
  actions directly. A new piece of shell state needs a field on the interface **and** a line in
  `mythosAppViewModelFactory.ts` — the factory lists every field by hand, so a forgotten line is a
  type error, but only because `MythosAppViewModel` is the declared return type.
- **Flow modules take their dependencies as arguments.** `runSelectCharacterFlow`,
  `runDeleteCharacterFlow`, `refreshCharactersAfterCreation` return tagged unions and never touch
  React; `*Actions.ts` files receive setters through an injected interface. Keep it that way — it is
  what makes them testable without rendering.
- **Server-unavailable always means `returnToLogin`.** Every handler that can see a network
  failure routes it through `isServerUnavailable` / `stringIndicatesServerUnavailable` to
  `returnToLogin`, which clears tokens and state and sets a fixed error string.
- **Tokens live in `secureTokenStorage`, not in this package.** State holds `authToken` for
  prop-passing; every path that abandons a session calls `secureTokenStorage.clearAllTokens()`.

## 4. Key design decisions

**[SPEC]**

- **View model + pure view functions, not a component tree with contexts.** `AppRootViews` and its
  siblings are plain functions called as `AppRootViews(vm)` (not `<AppRootViews />`), so they hold no
  hooks of their own and every piece of shell state is visible in one interface.
- **Two reducer slices with merge-patch reducers.** `AuthSlice` and `CreationSlice` each use
  `useReducer((state, patch) => ({...state, ...patch}))`. The per-field setters imitate
  `useState`'s `SetStateAction` (value or updater) so call sites read like `useState`. The updater
  form resolves against the slice value **captured at render time**, not a queued value (§5).
- **Result-union flow modules.** `SelectCharacterResult`, `DeleteCharacterFlowResult` and
  `CreationRefreshResult` name every outcome (`ok`, `server_unavailable`, `*_failed`,
  `network_error`); `nextStepForDeleteResult` maps one to a UI step in a pure function.
- **Delete is decoupled from list refresh (#777 follow-up).** When `DELETE` succeeds but the list
  re-fetch fails, `refresh_failed` drops the character from local state rather than throwing —
  otherwise a deleted character's card stayed on screen indefinitely.
- **One `lazy` declaration site.** `appLazyScreens.tsx` holds every code-split boundary in the
  shell; views import screens from there, never from `components/` directly.
- **Session restore is a mount-only effect.** `useAuthSessionRestore` deliberately has an empty
  dependency array (with a documented `eslint-disable`): setter identities change every render
  (§5), so depending on them would re-run the restore forever.
- **`useMythosSessionChrome.ts` deleted (this change).** A 24-positional-argument hook holding
  earlier copies of `handleMotdContinue`, `handleMotdReturnToLogin`, `handleLogout`, `toggleMode`
  and `handleKeyDown`. Nothing in production imported it (only its own test), and its handlers had
  drifted from the live ones in `useMythosAppActions.ts`. Removed with its test; the live handlers
  are the only implementation. (`knip --production` did not flag it; it was found by tracing
  imports from `App.tsx`.)
- **The demo is a first-class shell state.** `showDemo` short-circuits the router ahead of
  authentication, and is how the `MythosPanel` primitive stays reachable (see
  [`PACKAGE_UI_PRIMITIVES_DESIGN.md`](PACKAGE_UI_PRIMITIVES_DESIGN.md) §4).

## 5. Constraints

**[SPEC]**

- **Setter identities are unstable.** `useAuthSliceSetters` / `useCreationSliceSetters` wrap
  `useCallback` with the whole slice in the dependency list, so every setter gets a new identity on
  every state change. Consequences: `useMemo`/`useCallback` deps that include `state` recompute
  every render; the mount-only restore effect must not depend on setters; and two updater-form
  calls in the same tick (`setX(v => …)` twice) both read the same stale slice.
- **Views mutate state during render.** `AppCreationFlowViews` (`name` step without prerequisite
  data → `vm.setCreationStep('skills')`) and `AppSessionOutroViews` (no token → resets auth state
  and sets the "Session expired" error) call setters from inside a render-phase function. React
  tolerates this only because the calls converge; a change that stops converging becomes a render
  loop.
- **`toCharacterInfoFromList` and `toCharacterInfoFromLogin` disagree on ID precedence.** List
  prefers `player_id || id`; login prefers `id || player_id`. Both fall back to `''`.
- **[BUG]** `creationCompleteActions.ts`, `http_error` branch of `runAfterCharacterCreatedFlow`:
  calls `setShowCharacterSelection(true)` immediately followed by `setShowCharacterSelection(false)`.
  Net effect is `false`. After a creation whose list refresh returns a non-5xx HTTP error,
  `creationStep` is `null` and the picker is hidden, so `AppRootViews` falls through to
  `AppSessionOutroViews` and mounts `GameClientV2Container` with whatever `selectedCharacterId`
  was already in state (empty for a first character). The `network_error` branch, by contrast,
  sets `creationStep('stats')`. Tracked in
  [`#926`](https://github.com/arkanwolfshade/MythosMUD/issues/926).
- **`useAuthSessionRestore.ts` hard-codes `const inCharacterCreation = false;`**, so the
  `&& !inCharacterCreation` guards are dead. Behavioural consequence: on page reload a
  single-character account skips the picker, sets the selected character and leaves `showMotd`
  `false`, so the MOTD interstitial and the `start-login-grace-period` call (both driven by
  `handleMotdContinue`) are skipped. They only run after an explicit `handleCharacterSelected`.
  Whether that is intended is not recorded anywhere in the code. Tracked in
  [`#927`](https://github.com/arkanwolfshade/MythosMUD/issues/927).
- **Auth request URLs are inconsistent.** Login/register use `${API_V1_BASE}/auth/...`; character
  endpoints use `${API_V1_BASE}/api/players/...`. Both are correct against the server today;
  changing `API_V1_BASE` needs both families checked.
- **`console.warn` / `console.error` are used for non-fatal failures** (grace-period start, list
  refresh). The production build strips console output ([ADR-017](../architecture/decisions/ADR-017-ast-console-pruning-client-build.md)),
  so these are diagnostics for development only, not user-visible signals.

## 6. Developer guide

**[NOTE]**

- **Adding shell state**: add the field to `AuthSlice` or `CreationSlice` and its `INITIAL_*`
  value, add a setter in the matching `use*SliceSetters`, add it to `MythosAppViewModel` **and**
  `buildStateViewModel`. Views read it from `vm`.
- **Adding a handler**: put the network / decision logic in a framework-free `*Flow.ts` returning
  a tagged union, the state application in a `*Actions.ts` taking an injected-setters interface,
  and only the `useCallback` glue in `useMythosAppActions.ts`. Add it to `buildActionViewModel`.
- **Adding a wizard step**: extend `CreationStep`, add a `render*Step` in `AppCreationFlowViews.tsx`
  and its lazy screen in `appLazyScreens.tsx`, and make the previous step's callback advance to it.
- **Adding a new full-screen state** (like MOTD): add the condition to `AppRootViews` in the right
  position — order in §3 is behavioural, not cosmetic.
- **Tests**: `client/src/mythosApp/__tests__/`, Vitest + Testing Library. Flow modules are the
  cheapest to test (`vi.spyOn(globalThis, 'fetch')`, assert the returned union).

## 7. Troubleshooting

**[NOTE]**

- **Reload sends a signed-in user to the login form**: `useAuthSessionRestore` clears everything
  unless `secureTokenStorage` has a token that is well-formed **and** unexpired; a 401 from
  `GET /api/players/characters` also clears it. A non-401 failure leaves the session intact and
  the user on a blank shell.
- **"Server is unavailable. Please try again later." on login screen**: `returnToLogin` fired.
  Check whether the trigger was a 5xx, a fetch failure, or a child screen passing an error string
  that matched `SERVER_UNAVAILABLE_ERROR_SUBSTRINGS` in `serverAvailability.ts`.
- **A deleted character reappears until refresh**: the `refresh_failed` path removes it locally
  by `player_id`; check `toCharacterInfoFromList` produced the same ID the picker is keyed on.
- **Enter key does nothing on the login form**: `handleKeyDown` requires non-blank username and
  password, and a non-blank invite code when registering.
- **Character-creation wizard jumps back a step**: `AppCreationFlowViews` returns to `skills` when
  the `name` step lacks `pendingStats`, `selectedProfession`, or `pendingSkillsPayload`.

## 8. Related docs

**[SPEC]**

- [ADR-022 — UI-v2 client transition](../architecture/decisions/ADR-022-ui-v2-client-transition.md) —
  the component layer this shell mounts.
- [ADR-020 — WebSocket authentication and CSRF](../architecture/decisions/ADR-020-websocket-authentication-and-csrf.md) —
  server side of the token this package stores.
- [`PACKAGE_UI_PRIMITIVES_DESIGN.md`](PACKAGE_UI_PRIMITIVES_DESIGN.md) — where the login screen's
  demo button leads.
- [`docs/client-message-handling.md`](../client-message-handling.md) — what the game container does
  once mounted.
- [`docs/packages/README.md`](README.md) — the package coverage index this doc is entered into.

## 9. Changelog

**[SPEC]**

| Version | Date       | Change                                                        |
| ------- | ---------- | ------------------------------------------------------------- |
| 1.0.0   | 2026-09-29 | Initial version; removes dead `useMythosSessionChrome.ts`; closes #742 |
