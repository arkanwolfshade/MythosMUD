# container sql injection

> 17 nodes

## Key Concepts

- **submitAuth.ts** (18 connections) — `client/src/mythosApp/submitAuth.ts`
- **applyAuthenticatedSession.ts** (16 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **useMythosAuthForm.ts** (11 connections) — `client/src/mythosApp/useMythosAuthForm.ts`
- **useMythosAuthForm()** (10 connections) — `client/src/mythosApp/useMythosAuthForm.ts`
- **assertLoginResponse()** (6 connections) — `client/src/utils/apiTypeGuards.ts`
- **persistTokensAndApplySession()** (5 connections) — `client/src/mythosApp/applyAuthenticatedSession.ts`
- **submitLoginRequest()** (5 connections) — `client/src/mythosApp/submitAuth.ts`
- **submitRegisterRequest()** (5 connections) — `client/src/mythosApp/submitAuth.ts`
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

- [mythosApp CharacterSelectionScreen chara](mythosApp_CharacterSelectionScreen_chara.md) (11 shared connections)
- [SkillAssignmentScreen helpers CharacterN](SkillAssignmentScreen_helpers_CharacterN.md) (8 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (4 shared connections)
- [apiTypeGuards FIELDS SHARED](apiTypeGuards_FIELDS_SHARED.md) (4 shared connections)
- [map maps useAsciiMap](map_maps_useAsciiMap.md) (1 shared connections)

## Source Files

- `client/src/mythosApp/applyAuthenticatedSession.ts`
- `client/src/mythosApp/mapServerCharacters.ts`
- `client/src/mythosApp/submitAuth.ts`
- `client/src/mythosApp/useMythosAuthForm.ts`
- `client/src/utils/apiTypeGuards.ts`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*