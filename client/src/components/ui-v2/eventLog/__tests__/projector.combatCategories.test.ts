/**
 * Combat / status events carry a server-assigned `data.category`; the projector passes it through to the
 * message it appends. Combat lines are not chat, so they carry no channel.
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import { getInitialGameState, projectEvent } from '../projector';

function event(event_type: string, data: Record<string, unknown>): GameEvent {
  return { event_type, timestamp: new Date().toISOString(), sequence_number: 1, data };
}

describe('projector combat and status categories', () => {
  it('npc_attacked passes combat.hit through and carries no channel', () => {
    const next = projectEvent(
      getInitialGameState(),
      event('npc_attacked', { npc_name: 'Ghoul', damage: 3, category: 'combat.hit' })
    );
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].category).toBe('combat.hit');
    expect(next.messages[0].channel).toBeUndefined();
  });

  it('npc_took_damage passes combat.hit through', () => {
    const next = projectEvent(
      getInitialGameState(),
      event('npc_took_damage', { npc_name: 'Ghoul', damage: 3, category: 'combat.hit' })
    );
    expect(next.messages[0].category).toBe('combat.hit');
  });

  it('player_attacked passes combat.hurt through, including when the payload is wrapped in event_data', () => {
    const next = projectEvent(
      getInitialGameState(),
      event('player_attacked', { event_data: { attacker_name: 'Ghoul', damage: 3, category: 'combat.hurt' } })
    );
    expect(next.messages[0].category).toBe('combat.hurt');
  });

  it('npc_died and combat_death pass combat.death through', () => {
    const data = { message: 'The Ghoul has been slain.', category: 'combat.death' };
    expect(projectEvent(getInitialGameState(), event('npc_died', data)).messages[0].category).toBe('combat.death');
    expect(projectEvent(getInitialGameState(), event('combat_death', data)).messages[0].category).toBe('combat.death');
  });

  it.each(['combat_target_switch', 'combat_participant_joined', 'combat_taunt', 'combat_protect'])(
    '%s passes combat.status through and stays a combat message',
    eventType => {
      const next = projectEvent(
        getInitialGameState(),
        event(eventType, { message: 'The Ghoul turns its gaze.', category: 'combat.status' })
      );
      expect(next.messages[0].category).toBe('combat.status');
    }
  );

  it('combat_ended passes combat.status through for its reason line', () => {
    const next = projectEvent(
      getInitialGameState(),
      event('combat_ended', { reason: 'victory', category: 'combat.status' })
    );
    expect(next.messages[0].category).toBe('combat.status');
  });

  it('rescue_update passes status.rescue through and still drives rescueStatus', () => {
    const next = projectEvent(
      getInitialGameState(),
      event('rescue_update', { status: 'channeling', message: 'Hold on.', category: 'status.rescue' })
    );
    expect(next.messages[0].category).toBe('status.rescue');
    expect(next.rescueStatus).toBeTruthy();
  });

  it('falls back to command.output when the server sent no category', () => {
    const next = projectEvent(getInitialGameState(), event('npc_attacked', { npc_name: 'Ghoul', damage: 3 }));
    expect(next.messages[0].category).toBe('command.output');
  });
});
