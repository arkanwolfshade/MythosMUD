/**
 * Category-aware presentation and routing for GameInfoPanel and ChatHistoryPanel, plus the
 * room panels that share the cat-* vocabulary. Every message carries a server category; there is no
 * messageType path any more.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import type { ReactElement } from 'react';
import { describe, expect, it, vi } from 'vitest';
import { ThemeProvider } from '../../../../contexts/ThemeContext';
import type { MessageCategory } from '../../../../types/messageCategory';
import type { ChatMessage, Room } from '../../types';
import { ChatHistoryPanel } from '../ChatHistoryPanel';
import { GameInfoPanel } from '../GameInfoPanel';
import { LocationPanel } from '../LocationPanel';
import { RoomDescriptionPanel } from '../RoomDescriptionPanel';

function msg(text: string, category: MessageCategory, extra: Partial<ChatMessage> = {}): ChatMessage {
  return { text, timestamp: new Date().toISOString(), isHtml: false, category, ...extra };
}

function renderChat(messages: ChatMessage[], corruption = 0) {
  const ui: ReactElement = (
    <ThemeProvider>
      <ChatHistoryPanel messages={messages} onSendChatMessage={vi.fn()} corruption={corruption} />
    </ThemeProvider>
  );
  return render(ui);
}

const textBox = (text: string): HTMLElement => {
  const el = document.querySelector(`[data-message-text="${text}"]`);
  if (!(el instanceof HTMLElement)) throw new Error(`no message box for ${text}`);
  return el;
};

describe('GameInfoPanel category routing', () => {
  const messages: ChatMessage[] = [
    msg('say line', 'chat.say', { channel: 'say' }),
    msg('local line', 'chat.local', { channel: 'local' }),
    msg('party line', 'chat.party', { channel: 'party' }),
    msg('whisper line', 'chat.whisper', { channel: 'whisper' }),
    msg('global line', 'chat.global', { channel: 'global' }),
    msg('shout line', 'chat.shout', { channel: 'shout' }),
    msg('emote line', 'chat.emote', { channel: 'emote' }),
    msg('admin line', 'chat.admin', { channel: 'admin' }),
    msg('combat line', 'combat.hit'),
    msg('room line', 'room.description'),
    msg('error line', 'system.error'),
    msg('lucidity line', 'status.lucidity'),
    msg('output line', 'command.output'),
  ];

  it('mirrors chat.say, chat.local and chat.party and shows every non-chat category', () => {
    render(<GameInfoPanel messages={messages} />);
    for (const shown of [
      'say line',
      'local line',
      'party line',
      'combat line',
      'room line',
      'error line',
      'lucidity line',
      'output line',
    ]) {
      expect(screen.getByText(shown)).toBeInTheDocument();
    }
  });

  it('keeps the other chat categories out of Game Info', () => {
    render(<GameInfoPanel messages={messages} />);
    for (const hidden of ['whisper line', 'global line', 'shout line', 'emote line', 'admin line']) {
      expect(screen.queryByText(hidden)).not.toBeInTheDocument();
    }
  });

  it('applies the category class', () => {
    render(<GameInfoPanel messages={[msg('Hurt!', 'combat.hurt')]} />);
    const hurt = textBox('Hurt!');
    expect(hurt.className).toContain('cat cat-combat cat-combat-hurt cat-reg-alert');
    expect(hurt.className).not.toContain('text-mythos-terminal');
  });

  it('renders a room name with the heading register', () => {
    render(<GameInfoPanel messages={[msg('Sanitarium Foyer', 'room.name')]} />);
    expect(textBox('Sanitarium Foyer').className).toContain('cat-reg-heading');
  });

  it('uses the default style for an unknown category string', () => {
    vi.spyOn(console, 'warn').mockImplementation(() => undefined);
    const unknown = { ...msg('mystery', 'command.output'), category: 'lore.tome' } as unknown as ChatMessage;
    render(<GameInfoPanel messages={[unknown]} />);
    expect(textBox('mystery').className).toBe('flex-1 text-mythos-terminal-text');
  });

  it('filters categorized messages through the domain dropdown', () => {
    render(
      <GameInfoPanel messages={[msg('boom', 'combat.hit'), msg('oops', 'system.error'), msg('hello', 'chat.say')]} />
    );
    const select = screen.getByDisplayValue('All Messages');
    fireEvent.change(select, { target: { value: 'combat' } });
    expect(screen.getByText('boom')).toBeInTheDocument();
    expect(screen.queryByText('oops')).not.toBeInTheDocument();
    fireEvent.change(select, { target: { value: 'system' } });
    expect(screen.getByText('oops')).toBeInTheDocument();
    expect(screen.queryByText('boom')).not.toBeInTheDocument();
    fireEvent.change(select, { target: { value: 'chat' } });
    expect(screen.getByText('hello')).toBeInTheDocument();
    expect(screen.queryByText('oops')).not.toBeInTheDocument();
  });
});

describe('ChatHistoryPanel category routing', () => {
  it('shows chat.* and hides every other category', () => {
    renderChat([
      msg('hello', 'chat.say', { channel: 'say' }),
      msg('psst', 'chat.whisper', { channel: 'whisper' }),
      msg('swing', 'combat.hit'),
      msg('moved', 'room.movement'),
      msg('oops', 'system.error'),
      msg('mind', 'status.lucidity'),
      msg('result', 'command.output'),
    ]);
    expect(screen.getByText('hello')).toBeInTheDocument();
    expect(screen.getByText('psst')).toBeInTheDocument();
    for (const hidden of ['swing', 'moved', 'oops', 'mind', 'result']) {
      expect(screen.queryByText(hidden)).not.toBeInTheDocument();
    }
  });

  it('still filters by message.channel', () => {
    renderChat([msg('in say', 'chat.say', { channel: 'say' }), msg('in global', 'chat.global', { channel: 'global' })]);
    fireEvent.change(screen.getByTestId('channel-selector'), { target: { value: 'global' } });
    expect(screen.getByText('in global')).toBeInTheDocument();
    expect(screen.queryByText('in say')).not.toBeInTheDocument();
  });

  it('falls back to the category suffix when a chat line carries no channel', () => {
    renderChat([msg('in whisper', 'chat.whisper'), msg('in say', 'chat.say')]);
    fireEvent.change(screen.getByTestId('channel-selector'), { target: { value: 'whisper' } });
    expect(screen.getByText('in whisper')).toBeInTheDocument();
    expect(screen.queryByText('in say')).not.toBeInTheDocument();
  });

  it('excludes system.* from the all-messages history view', () => {
    renderChat([
      msg('hello', 'chat.say', { channel: 'say' }),
      msg('sysnote', 'system.info'),
      msg('swing', 'combat.hit'),
    ]);
    fireEvent.click(screen.getByText('All Messages', { selector: 'button' }));
    expect(screen.getByText('hello')).toBeInTheDocument();
    expect(screen.getByText('swing')).toBeInTheDocument();
    expect(screen.queryByText('sysnote')).not.toBeInTheDocument();
  });

  describe('corruption tint (#804)', () => {
    it.each<[MessageCategory, boolean]>([
      ['chat.say', true],
      ['chat.local', true],
      ['chat.global', true],
      ['chat.party', true],
      ['chat.shout', true],
      ['chat.whisper', false],
      ['chat.emote', false],
      ['chat.admin', false],
    ])('%s tinted=%s', (category, tinted) => {
      renderChat([msg('line', category, { channel: category.slice(5) })], 80);
      const box = textBox('line');
      expect(box.className).toContain(`cat-${category.replace('.', '-')}`);
      expect(box.className.includes('mythos-corruption-text')).toBe(tinted);
    });

    it('is identical for any message of the same category (no per-message variation)', () => {
      renderChat(
        [msg('real', 'chat.whisper', { channel: 'whisper' }), msg('fake', 'chat.whisper', { channel: 'whisper' })],
        100
      );
      expect(textBox('real').className).toBe(textBox('fake').className);
    });
  });
});

describe('room panels share the cat vocabulary', () => {
  const room: Room = {
    id: 'r1',
    name: 'Foyer',
    description: 'A dim foyer.',
    zone: 'arkham_city',
    sub_zone: 'university_library',
    exits: {},
  };

  it('LocationPanel heading uses the room.name register (accent font)', () => {
    render(<LocationPanel room={room} />);
    const heading = screen.getByTestId('location-heading');
    expect(heading.className).toContain('cat-room-name');
    expect(heading.className).toContain('cat-reg-heading');
  });

  it('RoomDescriptionPanel uses the room.description class', () => {
    render(<RoomDescriptionPanel room={room} />);
    expect(screen.getByText('A dim foyer.').className).toContain('cat-room-description');
  });
});
