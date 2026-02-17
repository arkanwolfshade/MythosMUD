---
name: Vite Best-Practices Remediation
overview: "Remediate client code and config to align with .cursor/rules/vite.mdc: fix process.env usage in client code, optionally merge Vitest into Vite config and add server warmup, and document barrel-file and extension policies."
todos: []
isProject: false
---

# Vite Best-Practices Remediation Plan

## Scope

Analysis against [.cursor/rules/vite.mdc](.cursor/rules/vite.mdc). Scope: **client** (Vite config, client source under `client/src`). Test files that run in Node (e.g. Vitest) may use `process.env` for test setup; application code must use `import.meta.env`.

**Already compliant**

- Native ES Modules throughout; no `require()` in client source (Rule: Embrace Native ES Modules).
- Environment variables in application code use `import.meta.env` in [config.ts](client/src/utils/config.ts), [security.ts](client/src/utils/security.ts), [logger.ts](client/src/utils/logger.ts), [useWebSocketConnection.ts](client/src/hooks/useWebSocketConnection.ts), and others.
- Large screens and routes use `React.lazy()` in [App.tsx](client/src/App.tsx) and [AppRouter.tsx](client/src/AppRouter.tsx) (Rule: Dynamic imports).
- [vite.config.ts](client/vite.config.ts) is relatively lean: one alias (`@`), no `resolve.extensions`, manualChunks for vendor splitting only.

---

## 1. process.env in client application code (Rule: Use import.meta.env)

**Rule:** "Vite injects environment variables via `import.meta.env`. `process.env` is for Node.js environments."

**Finding:** One application file uses `process.env.NODE_ENV` in client code:

- [client/src/components/map/hooks/useMapLayout.ts](client/src/components/map/hooks/useMapLayout.ts) (L240): `if (process.env.NODE_ENV === 'development')` for debug logging.

**Action:** Replace with `import.meta.env.DEV` (or `import.meta.env.MODE === 'development'`). After the change, re-check; if no other client application code uses `process.env`, consider removing the `define: { 'process.env.NODE_ENV': '"production"' }` block from [vite.config.ts](client/vite.config.ts) to avoid misleading future use of `process.env` in client code. (Test files under `client/src` that run in Vitest/Node and set `process.env` for test setup are acceptable and unchanged.)

---

## 2. Vitest config location (Rule: Standardize on Vitest)

**Rule:** "Integrate Vitest directly into vite.config.ts" so test config shares Vite's plugins and resolve.

**Finding:** Vitest is configured in a separate [client/vitest.config.ts](client/vitest.config.ts) (react plugin, test env, coverage, excludes). [client/vite.config.ts](client/vite.config.ts) has no `test` block.

**Action:** Optional. Merge the Vitest `test` block (and any Vitest-specific overrides) into [vite.config.ts](client/vite.config.ts), and add a triple-slash reference for Vitest types (e.g. `/// <reference types="vitest/config" />`). Use a single config export (e.g. `defineConfig` with both dev/build and test). Remove or slim [vitest.config.ts](client/vitest.config.ts) so the test runner uses the merged config. Ensures one config, shared `resolve.alias` and plugins, and avoids drift. Lower priority than item 1.

---

## 3. Barrel files (Rule: Avoid barrel files)

**Finding:**

- [client/src/components/ui-v2/eventHandlers/index.ts](client/src/components/ui-v2/eventHandlers/index.ts): Imports all handler modules and builds the registry; this is the main entry for event processing, not a thin re-export barrel. Acceptable as-is.
- [client/src/components/ui-v2/eventLog/index.ts](client/src/components/ui-v2/eventLog/index.ts): Re-exports types, `EventStore`, `projector` APIs. Only consumer [useEventProcessing.ts](client/src/components/ui-v2/hooks/useEventProcessing.ts) imports `EventStore` and `projectState` from `'../eventLog'`, so the barrel pulls in a small set of modules. Impact is limited.

**Action:** No mandatory change. Document: "Prefer direct imports from submodules (e.g. eventLog/eventStore, eventLog/projector) when only one or two exports are needed; use barrel only when multiple exports from the same area are used together." Optional: switch useEventProcessing to import directly from `../eventLog/eventStore` and `../eventLog/projector` if desired.

---

## 4. Explicit file extensions (Rule: Use explicit file extensions)

**Finding:** Most imports in `client/src` omit file extensions (e.g. `from '../types'`, `from '../../utils/config'`). The rule recommends explicit extensions to reduce Vite's resolution work.

**Action:** Low priority. TypeScript + Vite resolve extensionless imports by default. Optionally add a short note in team docs or a client README: "Prefer explicit extensions in imports (e.g. .ts, .tsx) where tooling allows, for faster resolution." Do not enforce project-wide refactors unless tooling (e.g. lint rule) is added.

---

## 5. Server warmup (Rule: Warm up critical files)

**Finding:** [vite.config.ts](client/vite.config.ts) has no `server.warmup`. The rule recommends warming frequently used files to avoid request waterfalls.

**Action:** Optional. Add `server.warmup` with critical entry files, e.g. `clientFiles: ['./src/main.tsx', './src/App.tsx']` (or equivalent paths). Reduces first-load latency; lower priority than items 1–2.

---

## 6. Vite config review

**Finding:** Config uses `define` for `process.env.NODE_ENV` in production, one `resolve.alias` (`@`), and `manualChunks` for vendor splitting. No `resolve.extensions`. Aligns with "keep config minimal" and "avoid resolve.extensions unless necessary."

**Action:** No change. After fixing item 1, re-evaluate whether `define` for `process.env.NODE_ENV` is still needed.

---

## Implementation order

| Priority | Item                                                                                    | Risk   |
| -------- | --------------------------------------------------------------------------------------- | ------ |
| 1        | useMapLayout.ts: replace process.env.NODE_ENV with import.meta.env.DEV                  | Low    |
| 2        | If no other client app code uses process.env: remove or narrow define in vite.config.ts | Low    |
| 3        | Merge Vitest into vite.config.ts; retire or slim vitest.config.ts                       | Medium |
| 4        | server.warmup for main.tsx, App.tsx                                                     | Low    |
| 5        | Document barrel-file and extension policies (README or docs)                            | Low    |

---

## Verification

- Run `npm run build` and `npm run dev` in client; confirm app and map layout behave as before.
- Run client unit tests (e.g. `make test-client-coverage` or `npm run test:coverage` in client); confirm all pass.
- If Vitest config was merged: run same test commands and confirm they use the single config and coverage still meets thresholds.
