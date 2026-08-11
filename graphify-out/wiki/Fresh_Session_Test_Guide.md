# Fresh Session Test Guide

> 30 nodes

## Key Concepts

- **SafeHtml.tsx** (14 connections) — `client/src/components/common/SafeHtml.tsx`
- **domPurifyClient.ts** (14 connections) — `client/src/utils/domPurifyClient.ts`
- **setup.ts** (13 connections) — `client/src/test/setup.ts`
- **SafeHtml()** (11 connections) — `client/src/components/common/SafeHtml.tsx`
- **domPurifyClient.test.ts** (5 connections) — `client/src/utils/__tests__/domPurifyClient.test.ts`
- **resolveSanitizeWindow()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **getDomPurify()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **verifiesDomPurifySanitize()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **resolveVitestSanitizeWindow()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **sanitizeWithDomPurify()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **domPurifyTestWindow.ts** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **installDomPurifyTestWindow()** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **collectWindowCandidates()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **resetDomPurifyClientForTests()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **localStorageShim.ts** (3 connections) — `client/src/utils/localStorageShim.ts`
- **installLocalStorageShim()** (3 connections) — `client/src/utils/localStorageShim.ts`
- **INCOMING_HTML_DOMPURIFY_CONFIG** (3 connections) — `client/src/utils/security.ts`
- **SafeHtml.test.tsx** (2 connections) — `client/src/components/common/__tests__/SafeHtml.test.tsx`
- **createDomPurifyTestWindow()** (2 connections) — `client/src/test/domPurifyTestWindow.ts`
- **localStorageShim.test.ts** (2 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **DOMPurifyInstance** (2 connections) — `client/src/utils/domPurifyClient.ts`
- **SafeHtmlProps** (1 connections) — `client/src/components/common/SafeHtml.tsx`
- **observe()** (1 connections) — `client/src/test/setup.ts`
- **unobserve()** (1 connections) — `client/src/test/setup.ts`
- **disconnect()** (1 connections) — `client/src/test/setup.ts`
- *... and 5 more nodes in this community*

## Relationships

- [Realtime Event Handlers](Realtime_Event_Handlers.md) (5 shared connections)
- [WebSocket Message Schemas](WebSocket_Message_Schemas.md) (4 shared connections)
- [Logging Rotating Handlers](Logging_Rotating_Handlers.md) (3 shared connections)
- [Holidays JSON Schema](Holidays_JSON_Schema.md) (2 shared connections)
- [Client App State Hooks](Client_App_State_Hooks.md) (2 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (2 shared connections)
- [Command Input Validator](Command_Input_Validator.md) (2 shared connections)
- [NATS Error Handling Strategy](NATS_Error_Handling_Strategy.md) (1 shared connections)

## Source Files

- `client/src/components/common/SafeHtml.tsx`
- `client/src/components/common/__tests__/SafeHtml.test.tsx`
- `client/src/test/domPurifyTestWindow.ts`
- `client/src/test/setup.ts`
- `client/src/utils/__tests__/domPurifyClient.test.ts`
- `client/src/utils/__tests__/localStorageShim.test.ts`
- `client/src/utils/domPurifyClient.ts`
- `client/src/utils/localStorageShim.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 117 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*