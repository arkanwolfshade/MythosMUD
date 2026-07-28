# Chat Service Whispers

> 73 nodes · cohesion 0.05

## Key Concepts

- **security.ts** (35 connections) — `client/src/utils/security.ts`
- **logoutHandler.ts** (26 connections) — `client/src/utils/logoutHandler.ts`
- **.error()** (17 connections) — `client/src/utils/logger.ts`
- **ClientLogger** (13 connections) — `client/src/utils/logger.ts`
- **secureTokenStorage** (13 connections) — `client/src/utils/security.ts`
- **logoutHandler()** (12 connections) — `client/src/utils/logoutHandler.ts`
- **SessionManager** (12 connections) — `client/src/utils/security.ts`
- **SkillsPage.tsx** (9 connections) — `client/src/pages/SkillsPage.tsx`
- **App.logout.test.tsx** (8 connections) — `client/src/__tests__/App.logout.test.tsx`
- **LogoutFlow.integration.test.tsx** (8 connections) — `client/src/__tests__/LogoutFlow.integration.test.tsx`
- **inputSanitizer** (8 connections) — `client/src/utils/security.ts`
- **CSRFProtection** (7 connections) — `client/src/utils/security.ts`
- **.info()** (6 connections) — `client/src/utils/logger.ts`
- **sendLogoutCommandToServer()** (6 connections) — `client/src/utils/logoutHandler.ts`
- **.addToBuffer()** (5 connections) — `client/src/utils/logger.ts`
- **.createLogEntry()** (5 connections) — `client/src/utils/logger.ts`
- **.initializeLogging()** (5 connections) — `client/src/utils/logger.ts`
- **readLogoutErrorMessage()** (5 connections) — `client/src/utils/logoutHandler.ts`
- **secureTokenStorage.test.ts** (5 connections) — `client/src/utils/__tests__/secureTokenStorage.test.ts`
- **.flushLogs()** (4 connections) — `client/src/utils/logger.ts`
- **.warn()** (4 connections) — `client/src/utils/logger.ts`
- **processLogoutHttpResponse()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **runLogoutServerPipeline()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **.generateToken()** (4 connections) — `client/src/utils/security.ts`
- **csrfProtection.test.ts** (4 connections) — `client/src/utils/__tests__/csrfProtection.test.ts`
- *... and 48 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (27 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (6 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (5 shared connections)
- [Subzone Schema Definition](Subzone_Schema_Definition.md) (5 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (4 shared connections)
- [NPC Combat Events](NPC_Combat_Events.md) (3 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (3 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (2 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (2 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)

## Source Files

- `client/src/__tests__/App.logout.test.tsx`
- `client/src/__tests__/LogoutFlow.integration.test.tsx`
- `client/src/pages/SkillsPage.tsx`
- `client/src/pages/__tests__/SkillsPage.test.tsx`
- `client/src/utils/__tests__/csrfProtection.test.ts`
- `client/src/utils/__tests__/inputSanitizer.test.ts`
- `client/src/utils/__tests__/logoutHandler.test.ts`
- `client/src/utils/__tests__/secureTokenStorage.test.ts`
- `client/src/utils/__tests__/security.test-utils.ts`
- `client/src/utils/__tests__/sessionManager.test.ts`
- `client/src/utils/logger.ts`
- `client/src/utils/logoutHandler.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 306 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*