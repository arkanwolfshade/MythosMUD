# zone configuration npc

> 19 nodes

## Key Concepts

- **submitAuth.ts** (18 connections) — `client/src/mythosApp/submitAuth.ts`
- **applyAuthenticatedSession.ts** (16 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **useMythosAuthForm.ts** (11 connections) — `client/src/mythosApp/useMythosAuthForm.ts`
- **mapServerCharacters.ts** (10 connections) — `client/src/mythosApp/mapServerCharacters.ts`
- **useMythosAuthForm()** (10 connections) — `client/src/mythosApp/useMythosAuthForm.ts`
- **assertLoginResponse()** (6 connections) — `client/src/utils/apiTypeGuards.ts`
- **persistTokensAndApplySession()** (5 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **submitLoginRequest()** (5 connections) — `client/src/mythosApp/submitAuth.ts`
- **submitRegisterRequest()** (5 connections) — `client/src/mythosApp/submitAuth.ts`
- **ServerCharacterResponse** (4 connections) — `client/src/utils/apiTypeGuards.ts`
- **AuthSessionSetters** (3 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **toCharacterInfoFromLogin()** (3 connections) — `client/src/mythosApp/mapServerCharacters.ts`
- **sanitizeLoginInputs()** (3 connections) — `client/src/mythosApp/submitAuth.ts`
- **sanitizeRegisterInputs()** (3 connections) — `client/src/mythosApp/submitAuth.ts`
- **AuthSuccessPayload** (2 connections) — `client/src/mythosApp/submitAuth.ts`
- **SetBool** (1 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **SetChars** (1 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **SetStep** (1 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **SanitizedCredentials** (1 connections) — `client/src/mythosApp/submitAuth.ts`

## Relationships

- [mythosApp CharacterSelectionScreen chara](mythosApp_CharacterSelectionScreen_chara.md) (16 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (8 shared connections)
- [apiTypeGuards FIELDS SHARED](apiTypeGuards_FIELDS_SHARED.md) (6 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (4 shared connections)
- [mythosApp appLazyScreens mythosAppViewMo](mythosApp_appLazyScreens_mythosAppViewMo.md) (2 shared connections)

## Source Files

- `client/src/mythosApp/applyAuthenticatedSession.ts`
- `client/src/mythosApp/mapServerCharacters.ts`
- `client/src/mythosApp/submitAuth.ts`
- `client/src/mythosApp/useMythosAuthForm.ts`
- `client/src/utils/apiTypeGuards.ts`

## Audit Trail

- EXTRACTED: 106 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*