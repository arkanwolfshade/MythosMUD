# Spec Requirements Document

> Spec: Complete Existing System TODOs
> Created: 2025-11-03

## Overview

Complete all incomplete implementations (TODOs) in existing MythosMUD systems to enhance security, functionality, and code quality. This initiative addresses 15 identified gaps across authentication, combat, NPC systems, and real-time communication, ensuring the codebase is production-ready and maintainable.

## User Stories

### Security Hardening

As a **system administrator**, I want all security vulnerabilities marked as TODO to be resolved, so that the MUD is protected against unauthorized access, CSRF attacks, and credential exposure.

The administrator needs confidence that authentication secrets are properly secured, admin-only endpoints are protected, and WebSocket communications are validated against CSRF attacks. This prevents unauthorized players from executing admin commands and protects user sessions from malicious attacks.

### Complete Combat System

As a **player**, I want the combat system to calculate damage based on my character's stats and equipment, so that my character progression feels meaningful and strategic.

Players expect combat to reflect their character development - strength, skills, weapons, and tactical choices should all factor into damage calculations rather than using a flat basic damage value. This creates engaging gameplay progression and rewards character investment.

### Functional NPC Administration

As a **game master**, I want to dynamically control NPC behaviors and reactions through admin commands, so that I can create dynamic storytelling moments and manage encounters in real-time.

Game masters need the ability to trigger NPC reactions (greet, attack, flee), modify behaviors (patrol, guard, aggressive), and stop NPC activities on demand. These controls enable responsive, narrative-driven gameplay that adapts to player actions.

## Spec Scope

1. **Security Hardening** - Implement JWT secret configuration, admin role enforcement, and CSRF validation for WebSocket communications
2. **Combat System Completion** - Implement stat-based damage calculation and immediate death handling triggers
3. **NPC Behavior Control** - Implement three missing NPC admin methods (set behavior, trigger reaction, stop behavior)
4. **Configuration Enhancement** - Make max health player-specific and add SQL logging verbosity configuration
5. **Event System Polish** - Replace placeholder names with actual player/room names in events, implement invite usage tracking
6. **Code Quality** - Remove legacy chat patterns, rewrite problematic performance test, implement confirmation dialogs for safety-critical commands
7. **Data Synchronization** - Implement fresh data request mechanism for room synchronization and JSON room saving capability

## Out of Scope

**New Feature: Inventory System** - Defer to separate feature spec

**New Feature: Status Effects System** - Defer to separate feature spec

**Architecture: Async Hooks** - Defer to persistence layer refactoring effort
- **Architecture: Alternate Database Backends** - Defer to production scaling initiative
- **NPC Movement Implementation** - Deferred (note in npc_instance_service.py:209 is documentation only)

## Expected Deliverable

1. **Security Validation** - All authentication endpoints enforce proper role-based access control, JWT secrets are environment-configured, and WebSocket CSRF validation blocks unauthorized operations
2. **Combat System Verification** - Player combat damage varies based on stats/equipment (testable with different character builds), death triggers immediate respawn flow
3. **NPC Control Demonstration** - Game master can use `npc behavior`, `npc react`, and `npc stop` commands to dynamically control NPCs, verified through browser testing
4. **Code Quality Metrics** - All linter warnings resolved, test suite passes with no skipped tests (except documented exceptions), legacy code patterns removed
5. **Real-time Accuracy** - Event messages display actual player and room names rather than "Player_123" placeholders, invite codes can only be used once
