# Spec Requirements Document

> Spec: Lucidity System Expansion
> Created: 2025-11-13

## Overview

Define the gameplay, backend, and client features required to deliver the newly designed MythosMUD lucidity mechanics, ensuring structured loss/recovery flows, hallucination feedback, and sanitarium failover while meeting security and compliance constraints.

## User Stories

### Investigator Lucidity Management

As a MythosMUD player, I want my lucidity to respond to encounters, environments, and rituals so that the horror gameplay feels reactive and meaningful.

Describe backend services to track SAN values, apply passive/active adjustments, surface tier transitions, and trigger liabilities that persist across sessions.

### Comrade Intervention

As a party member, I want tools to stabilize a catatonic ally so that our group can rescue companions before they become institutionalized.

Detail commands, cooldowns, and server validation for the `ground` interaction alongside feedback presented in the client terminal.

### Narrative Feedback

As a player, I want hallucinations and command disruptions to manifest contextually so that low lucidity feels immersive without being unfair.

Outline event generation, weighting, and client delivery for hallucinated mobs, distorted chat, and involuntary actions with accessible indicators.

## Spec Scope

1. **Lucidity Tracking Service** - Implement authoritative SAN storage, tier thresholds, passive flux scheduler, and liability assignment.
2. **Recovery & Loss Hooks** - Wire encounter logging, ritual learning, and recovery actions into existing combat, exploration, and social systems.
3. **Player Interaction UX** - Extend client messaging to communicate SAN changes, hallucinations, command misfires, and rescue prompts.
4. **Telemetry & Logging** - Capture structured SAN adjustments, hallucination triggers, and sanitarium visits for balancing and compliance review.

## Out of Scope

Full balancing pass for individual SAN values beyond initial defaults

- Visual redesign of the web terminal or HUD components

## Expected Deliverable

1. Playable build where SAN tiers, liabilities, hallucinations, and sanitarium flows operate end-to-end with automated coverage.
2. Administrative telemetry dashboards or logs demonstrating traceability of SAN changes and rescue attempts.
