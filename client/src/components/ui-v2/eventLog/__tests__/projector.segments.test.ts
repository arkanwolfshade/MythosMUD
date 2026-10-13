/**
 * NPC-name segments through the projector (#1025): server `segments` and client-composed combat lines both end up
 * on the appended message, validated, and never at the cost of the plain text.
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import { getInitialGameState, projectEvent } from '../projector';

function event(event_type: string, data: Record<string, unknown>): GameEvent {
  return { event_type, timestamp: new Date().toISOString(), sequence_number: 1, data };
}

const project = (e: GameEvent) => projectEvent(getInitialGameState(), e).messages[0];

describe('server-supplied segments', () => {
  const moved = {
    message: 'Rat entered from north.',
    category: 'room.movement',
    segments: [{ text: 'Rat', category: 'npc.aggressive_mob' }, { text: ' entered from north.' }],
  };

  it('room_message carries validated segments next to its unchanged text', () => {
    const message = project(event('room_message', moved));
    expect(message.text).toBe('Rat entered from north.');
    expect(message.segments).toEqual(moved.segments);
  });

  it('npc_died and combat_death carry the segmented death line', () => {
    const data = {
      message: 'The Shoggoth has been slain.',
      category: 'combat.death',
      segments: [{ text: 'The ' }, { text: 'Shoggoth', category: 'npc.aggressive_mob' }, { text: ' has been slain.' }],
    };
    expect(project(event('npc_died', data)).segments).toEqual(data.segments);
    expect(project(event('combat_death', data)).segments).toEqual(data.segments);
  });

  it('drops segments that do not join back to the message instead of showing different words', () => {
    const message = project(event('room_message', { ...moved, message: 'Rat strolled in from the north.' }));
    expect(message.text).toBe('Rat strolled in from the north.');
    expect(message.segments).toBeUndefined();
  });

  it('never attaches segments to a line without any', () => {
    expect(project(event('room_message', { message: 'A rat scurries in.', category: 'room.movement' })).segments).toBe(
      undefined
    );
  });

  it('ignores segments on an HTML line, which is sanitized as a whole', () => {
    const message = project(event('room_message', { ...moved, is_html: true }));
    expect(message.segments).toBeUndefined();
  });
});

describe('client-composed combat lines', () => {
  it('npc_attacked styles the NPC name from npc_disposition', () => {
    const message = project(
      event('npc_attacked', {
        npc_name: 'Ghoul',
        damage: 3,
        action_type: 'auto_attack',
        category: 'combat.hit',
        npc_disposition: 'aggressive_mob',
      })
    );
    expect(message.text).toBe('You attack Ghoul for 3 damage.');
    expect(message.segments).toEqual([
      { text: 'You attack ' },
      { text: 'Ghoul', category: 'npc.aggressive_mob' },
      { text: ' for 3 damage.' },
    ]);
  });

  it('npc_took_damage styles the NPC name and keeps the DP suffix', () => {
    const message = project(
      event('npc_took_damage', {
        npc_name: 'Ghoul',
        damage: 3,
        current_dp: 7,
        max_dp: 10,
        category: 'combat.hit',
        npc_disposition: 'quest_giver',
      })
    );
    expect(message.text).toBe('Dealt 3 damage to Ghoul. (7/10 DP)');
    expect(message.segments?.[1]).toEqual({ text: 'Ghoul', category: 'npc.quest_giver' });
  });

  it('player_attacked styles an NPC attacker, and leaves a player attacker plain', () => {
    const npc = project(
      event('player_attacked', {
        attacker_name: 'Ghoul',
        damage: 3,
        category: 'combat.hurt',
        attacker_disposition: 'aggressive_mob',
      })
    );
    expect(npc.text).toBe('Ghoul attacks you for 3 damage.');
    expect(npc.segments?.[0]).toEqual({ text: 'Ghoul', category: 'npc.aggressive_mob' });

    const player = project(event('player_attacked', { attacker_name: 'Bully', damage: 3, category: 'combat.hurt' }));
    expect(player.text).toBe('Bully attacks you for 3 damage.');
    expect(player.segments).toBeUndefined();
  });

  it('leaves the line plain when the server sent no disposition or an unrecognised one', () => {
    const base = { npc_name: 'Ghoul', damage: 3, category: 'combat.hit' };
    expect(project(event('npc_attacked', base)).segments).toBeUndefined();
    expect(project(event('npc_attacked', { ...base, npc_disposition: 'friendly' })).segments).toBeUndefined();
  });
});

describe('combat status lines (#1036)', () => {
  it.each([
    ['combat_target_switch', 'Ghoul turns its gaze to Ashcroft.', [0, 'Ghoul']],
    ['combat_participant_joined', 'Blackwood joins the fight against Ghoul!', [1, 'Ghoul']],
    ['combat_taunt', 'Tank bellows a challenge at Ghoul!', [1, 'Ghoul']],
  ] as const)('%s carries the server segments next to its text', (eventType, message, [index, name]) => {
    const before = message.slice(0, message.indexOf(name));
    const after = message.slice(message.indexOf(name) + name.length);
    const spans = [
      ...(before ? [{ text: before }] : []),
      { text: name, category: 'npc.aggressive_mob' },
      ...(after ? [{ text: after }] : []),
    ];
    const line = project(event(eventType, { message, category: 'combat.status', segments: spans }));
    expect(line.text).toBe(message);
    expect(line.segments).toEqual(spans);
    expect(line.segments?.[index]).toEqual({ text: name, category: 'npc.aggressive_mob' });
  });

  it('drops combat status segments that do not join back to the text', () => {
    const line = project(
      event('combat_taunt', {
        message: 'Tank bellows a challenge at Ghoul!',
        category: 'combat.status',
        segments: [{ text: 'Ghoul', category: 'npc.aggressive_mob' }],
      })
    );
    expect(line.segments).toBeUndefined();
  });
});

describe('command_response segments (#1036)', () => {
  const result = 'A damp cellar.\n\nAlso here: Goblin, Rat\nExits: north';
  const segments = [
    { text: 'A damp cellar.\n\nAlso here: ' },
    { text: 'Goblin', category: 'npc.shopkeeper' },
    { text: ', ' },
    { text: 'Rat', category: 'npc.aggressive_mob' },
    { text: '\nExits: north' },
  ];

  it('carries the look result segments next to its text', () => {
    const line = project(event('command_response', { result, category: 'room.description', segments }));
    expect(line.text).toBe(result);
    expect(line.segments).toEqual(segments);
  });

  it('drops them when the displayed text is not the result they describe', () => {
    const line = project(
      event('command_response', {
        result,
        suppress_chat: true,
        game_log_message: 'You look around.',
        category: 'room.description',
        segments,
      })
    );
    expect(line.text).toBe('You look around.');
    expect(line.segments).toBeUndefined();
  });
});

describe('chat_message segments (#1036)', () => {
  it('carries an NPC speaker name span next to the formatted line', () => {
    const segments = [{ text: 'Elder', category: 'npc.quest_giver' }, { text: ' says: Welcome.' }];
    const line = project(
      event('chat_message', {
        message: 'Elder says: Welcome.',
        channel: 'say',
        category: 'chat.say',
        segments,
      })
    );
    expect(line.text).toBe('Elder says: Welcome.');
    expect(line.segments).toEqual(segments);
  });

  it('carries the spans inside a system narration line, framed by the channel prefix', () => {
    const segments = [
      { text: '[SYSTEM] A ' },
      { text: 'Shadow', category: 'npc.aggressive_mob' },
      { text: ' materializes before you!' },
    ];
    const line = project(
      event('chat_message', {
        message: '[SYSTEM] A Shadow materializes before you!',
        channel: 'system',
        category: 'system.info',
        segments,
      })
    );
    expect(line.segments).toEqual(segments);
  });

  it('drops spans that no longer describe the (dampened) line', () => {
    const line = project(
      event('chat_message', {
        message: 'Elder says: W☁lcome.',
        channel: 'say',
        category: 'chat.say',
        segments: [{ text: 'Elder', category: 'npc.quest_giver' }, { text: ' says: Welcome.' }],
      })
    );
    expect(line.text).toBe('Elder says: W☁lcome.');
    expect(line.segments).toBeUndefined();
  });
});
