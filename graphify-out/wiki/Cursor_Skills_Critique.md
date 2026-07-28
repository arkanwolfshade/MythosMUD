# Cursor Skills Critique

> 26 nodes · cohesion 0.15

## Key Concepts

- **sanitizeChatMessageForState()** (24 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **useRespawnHandlers.ts** (21 connections) — `client/src/components/ui-v2/hooks/useRespawnHandlers.ts`
- **messageUtils.ts** (18 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **combatHandlers.ts** (14 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **combatHandlers.test.ts** (12 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/combatHandlers.test.ts`
- **useRespawnHandlers()** (8 connections) — `client/src/components/ui-v2/hooks/useRespawnHandlers.ts`
- **getMessageMetadata()** (5 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **handleCombatDeath()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatTargetSwitch()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleNpcAttacked()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleNpcDied()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handlePlayerAttacked()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleIntentionalDisconnect()** (3 connections) — `client/src/components/ui-v2/eventHandlers/systemHandlers.ts`
- **handleRescueUpdate()** (3 connections) — `client/src/components/ui-v2/eventHandlers/systemHandlers.ts`
- **useRespawnHandlers.test.ts** (3 connections) — `client/src/components/ui-v2/hooks/__tests__/useRespawnHandlers.test.ts`
- **UseRespawnHandlersParams** (3 connections) — `client/src/components/ui-v2/hooks/useRespawnHandlers.ts`
- **isRespawnApiResponse()** (3 connections) — `client/src/utils/apiTypeGuards.ts`
- **handleCombatEnded()** (2 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatStarted()** (2 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **getMessageChannel()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getMessageType()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getMessageTypeField()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getRawTextFromMessage()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **sanitizeMessageText()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **fetchSpy** (1 connections) — `client/src/components/ui-v2/hooks/__tests__/useRespawnHandlers.test.ts`
- *... and 1 more nodes in this community*

## Relationships

- [Combat Service Bundle](Combat_Service_Bundle.md) (26 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (6 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (5 shared connections)
- [NPC Combat Events](NPC_Combat_Events.md) (4 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (3 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Combat Attack Handler](Combat_Attack_Handler.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (2 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/combatHandlers.test.ts`
- `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- `client/src/components/ui-v2/eventHandlers/systemHandlers.ts`
- `client/src/components/ui-v2/hooks/__tests__/useRespawnHandlers.test.ts`
- `client/src/components/ui-v2/hooks/useRespawnHandlers.ts`
- `client/src/components/ui-v2/utils/messageUtils.ts`
- `client/src/utils/apiTypeGuards.ts`

## Audit Trail

- EXTRACTED: 146 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*