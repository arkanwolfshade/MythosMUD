/**
 * Tests for lucidity type definitions and utilities
 *
 * These tests verify that the type definitions are correctly structured
 * and can be used in TypeScript code.
 */

import { describe, expect, it } from 'vitest';
import type {
  HallucinationMessage,
  HallucinationSeverity,
  LucidityChangeMeta,
  LucidityStatus,
  LucidityTier,
  RescuePhase,
  RescueState,
} from '../lucidity';

describe('Lucidity Types', () => {
  describe('LucidityTier', () => {
    it('should accept valid lucidity tier values', () => {
      const tiers: LucidityTier[] = ['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic'];

      tiers.forEach(tier => {
        expect(typeof tier).toBe('string');
        expect(['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic']).toContain(tier);
      });
    });
  });

  describe('LucidityStatus', () => {
    it('should create valid LucidityStatus object', () => {
      const status: LucidityStatus = {
        current: 50,
        max: 100,
        tier: 'uneasy',
        liabilities: ['anxiety', 'paranoia'],
      };

      expect(status.current).toBe(50);
      expect(status.max).toBe(100);
      expect(status.tier).toBe('uneasy');
      expect(status.liabilities).toEqual(['anxiety', 'paranoia']);
    });

    it('should accept optional lastChange property', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: -10,
        reason: 'Witnessed eldritch horror',
        source: 'combat',
        timestamp: new Date().toISOString(),
      };

      const status: LucidityStatus = {
        current: 40,
        max: 100,
        tier: 'fractured',
        liabilities: [],
        lastChange: changeMeta,
      };

      expect(status.lastChange).toBeDefined();
      expect(status.lastChange?.delta).toBe(-10);
      expect(status.lastChange?.reason).toBe('Witnessed eldritch horror');
    });
  });

  describe('LucidityChangeMeta', () => {
    it('should create valid LucidityChangeMeta object', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: -15,
        reason: 'Read forbidden tome',
        source: 'item',
        timestamp: new Date().toISOString(),
      };

      expect(changeMeta.delta).toBe(-15);
      expect(changeMeta.reason).toBe('Read forbidden tome');
      expect(changeMeta.source).toBe('item');
      expect(typeof changeMeta.timestamp).toBe('string');
    });

    it('should accept optional reason and source', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: 5,
        timestamp: new Date().toISOString(),
      };

      expect(changeMeta.delta).toBe(5);
      expect(changeMeta.reason).toBeUndefined();
      expect(changeMeta.source).toBeUndefined();
    });
  });

  describe('HallucinationSeverity', () => {
    it('should accept valid hallucination severity values', () => {
      const severities: HallucinationSeverity[] = ['minor', 'moderate', 'severe'];

      severities.forEach(severity => {
        expect(typeof severity).toBe('string');
        expect(['minor', 'moderate', 'severe']).toContain(severity);
      });
    });
  });

  describe('HallucinationMessage', () => {
    it('should create valid HallucinationMessage object', () => {
      const message: HallucinationMessage = {
        id: 'hallucination-1',
        title: 'Whispers in the Dark',
        description: 'You hear voices calling your name',
        severity: 'moderate',
        category: 'auditory',
        timestamp: new Date().toISOString(),
      };

      expect(message.id).toBe('hallucination-1');
      expect(message.title).toBe('Whispers in the Dark');
      expect(message.description).toBe('You hear voices calling your name');
      expect(message.severity).toBe('moderate');
      expect(message.category).toBe('auditory');
      expect(typeof message.timestamp).toBe('string');
    });

    it('should accept optional description and category', () => {
      const message: HallucinationMessage = {
        id: 'hallucination-2',
        title: 'Shadow Movement',
        severity: 'minor',
        timestamp: new Date().toISOString(),
      };

      expect(message.description).toBeUndefined();
      expect(message.category).toBeUndefined();
    });
  });

  describe('RescuePhase', () => {
    it('should accept valid rescue phase values', () => {
      const phases: RescuePhase[] = ['idle', 'catatonic', 'channeling', 'success', 'failed', 'sanitarium'];

      phases.forEach(phase => {
        expect(typeof phase).toBe('string');
        expect(['idle', 'catatonic', 'channeling', 'success', 'failed', 'sanitarium']).toContain(phase);
      });
    });
  });

  describe('RescueState', () => {
    it('should create valid RescueState object', () => {
      const state: RescueState = {
        status: 'channeling',
        targetName: 'Player1',
        rescuerName: 'Player2',
        progress: 50,
        etaSeconds: 30,
        message: 'Rescue in progress',
        timestamp: new Date().toISOString(),
      };

      expect(state.status).toBe('channeling');
      expect(state.targetName).toBe('Player1');
      expect(state.rescuerName).toBe('Player2');
      expect(state.progress).toBe(50);
      expect(state.etaSeconds).toBe(30);
      expect(state.message).toBe('Rescue in progress');
      expect(typeof state.timestamp).toBe('string');
    });

    it('should accept minimal RescueState with only required fields', () => {
      const state: RescueState = {
        status: 'idle',
        timestamp: new Date().toISOString(),
      };

      expect(state.status).toBe('idle');
      expect(state.targetName).toBeUndefined();
      expect(state.rescuerName).toBeUndefined();
      expect(state.progress).toBeUndefined();
      expect(state.etaSeconds).toBeUndefined();
      expect(state.message).toBeUndefined();
    });

    it('should accept all optional fields', () => {
      const state: RescueState = {
        status: 'success',
        targetName: 'Player1',
        rescuerName: 'Player2',
        progress: 100,
        etaSeconds: 0,
        message: 'Rescue successful',
        timestamp: new Date().toISOString(),
      };

      expect(state.targetName).toBe('Player1');
      expect(state.rescuerName).toBe('Player2');
      expect(state.progress).toBe(100);
      expect(state.etaSeconds).toBe(0);
      expect(state.message).toBe('Rescue successful');
    });
  });

  describe('Type Compatibility', () => {
    it('should allow LucidityStatus to be used in arrays', () => {
      const statuses: LucidityStatus[] = [
        {
          current: 100,
          max: 100,
          tier: 'lucid',
          liabilities: [],
        },
        {
          current: 50,
          max: 100,
          tier: 'uneasy',
          liabilities: ['anxiety'],
        },
      ];

      expect(statuses.length).toBe(2);
      expect(statuses[0].tier).toBe('lucid');
      expect(statuses[1].tier).toBe('uneasy');
    });

    it('should allow HallucinationMessage to be used in arrays', () => {
      const messages: HallucinationMessage[] = [
        {
          id: 'msg1',
          title: 'Message 1',
          severity: 'minor',
          timestamp: new Date().toISOString(),
        },
        {
          id: 'msg2',
          title: 'Message 2',
          severity: 'severe',
          timestamp: new Date().toISOString(),
        },
      ];

      expect(messages.length).toBe(2);
      expect(messages[0].severity).toBe('minor');
      expect(messages[1].severity).toBe('severe');
    });

    it('should allow RescueState to transition between phases', () => {
      const states: RescueState[] = [
        { status: 'idle', timestamp: new Date().toISOString() },
        { status: 'catatonic', timestamp: new Date().toISOString() },
        { status: 'channeling', timestamp: new Date().toISOString() },
        { status: 'success', timestamp: new Date().toISOString() },
      ];

      expect(states.length).toBe(4);
      expect(states[0].status).toBe('idle');
      expect(states[3].status).toBe('success');
    });
  });
});
