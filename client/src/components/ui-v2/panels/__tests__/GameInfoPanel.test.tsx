/**
 * Tests for GameInfoPanel component.
 */

import { fireEvent, render, screen, within } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MessageCategory } from '../../../../types/messageCategory';
import type { ChatMessage } from '../../types';
import { GameInfoPanel } from '../GameInfoPanel';

const msg = (text: string, category: MessageCategory, extra: Partial<ChatMessage> = {}): ChatMessage => ({
  text,
  timestamp: new Date().toISOString(),
  isHtml: false,
  category,
  ...extra,
});

describe('GameInfoPanel', () => {
  const mockOnClearMessages = vi.fn();
  const mockOnDownloadLogs = vi.fn();

  const mockMessages: ChatMessage[] = [msg('System message', 'system.info'), msg('Combat message', 'combat.hit')];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render game info panel', () => {
    render(<GameInfoPanel messages={mockMessages} />);
    expect(screen.getByText('System message')).toBeInTheDocument();
  });

  it('should display all messages by default', () => {
    render(<GameInfoPanel messages={mockMessages} />);
    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.getByText('Combat message')).toBeInTheDocument();
  });

  it('renders an isHtml message as real markup, not escaped text (help output)', () => {
    const help = [
      msg('<div class="help-entry"><p><strong>LOOK</strong></p></div>', 'command.output', { isHtml: true }),
    ];

    const { container } = render(<GameInfoPanel messages={help} />);

    expect(container.querySelector('.help-entry strong')?.textContent).toBe('LOOK');
    expect(screen.queryByText(/<strong>/)).not.toBeInTheDocument();
  });

  it('renders a non-HTML message as a plain text node with pre-wrap whitespace, never as markup', () => {
    const plain = [msg('<strong>LOOK</strong>\n  Exits: north', 'command.output')];

    const { container } = render(<GameInfoPanel messages={plain} />);

    expect(container.querySelector('strong')).toBeNull();
    const text = container.querySelector('[data-message-text] > span') as HTMLElement;
    expect(text.textContent).toBe('<strong>LOOK</strong>\n  Exits: north');
    expect(text.style.whiteSpace).toBe('pre-wrap');
  });

  it('styles each line by its category, with the category-driven class on the text container', () => {
    const { container } = render(<GameInfoPanel messages={mockMessages} />);
    expect(container.querySelector('[data-message-text="Combat message"]')).toHaveClass('cat-combat-hit');
    expect(container.querySelector('[data-message-text="System message"]')).toHaveClass('cat-system-info');
  });

  it('should call onClearMessages when clear button is clicked', () => {
    render(<GameInfoPanel messages={mockMessages} onClearMessages={mockOnClearMessages} />);

    const clearLogButton = screen.getByRole('button', { name: /clear log/i });
    fireEvent.click(clearLogButton);

    expect(mockOnClearMessages).toHaveBeenCalled();
  });

  it('should call onDownloadLogs when download button is clicked', () => {
    render(<GameInfoPanel messages={mockMessages} onDownloadLogs={mockOnDownloadLogs} />);

    const downloadButton = screen.getByRole('button', { name: /download/i });
    fireEvent.click(downloadButton);

    expect(mockOnDownloadLogs).toHaveBeenCalled();
  });

  it('should handle empty messages array', () => {
    render(<GameInfoPanel messages={[]} />);
    // Should render without errors
    expect(screen.queryByText('System message')).not.toBeInTheDocument();
  });

  describe('category-domain filter dropdown', () => {
    const everyDomain: ChatMessage[] = [
      msg('combat line', 'combat.hurt'),
      msg('status line', 'status.lucidity'),
      msg('system line', 'system.warning'),
      msg('quest line', 'quest.info'),
      msg('room line', 'room.movement'),
      msg('chat line', 'chat.say'),
      msg('command line', 'command.output'),
    ];

    it('offers one option per category domain', () => {
      render(<GameInfoPanel messages={everyDomain} />);
      const options = within(screen.getByRole('combobox')).getAllByRole('option');
      expect(options.map(o => o.getAttribute('value'))).toEqual([
        'all',
        'combat',
        'status',
        'system',
        'quest',
        'room',
        'chat',
        'command',
      ]);
      expect(options.map(o => o.textContent)).toEqual([
        'All Messages',
        'Combat',
        'Status',
        'System',
        'Quest',
        'Room',
        'Chat',
        'Commands',
      ]);
    });

    it('shows every domain under All', () => {
      render(<GameInfoPanel messages={everyDomain} />);
      for (const m of everyDomain) expect(screen.getByText(m.text)).toBeInTheDocument();
    });

    it.each([
      ['combat', 'combat line'],
      ['status', 'status line'],
      ['system', 'system line'],
      ['quest', 'quest line'],
      ['room', 'room line'],
      ['chat', 'chat line'],
      ['command', 'command line'],
    ])('filter %s leaves only the %s', (filter, visibleText) => {
      render(<GameInfoPanel messages={everyDomain} />);
      fireEvent.change(screen.getByRole('combobox'), { target: { value: filter } });
      expect(screen.getByText(visibleText)).toBeInTheDocument();
      for (const m of everyDomain.filter(x => x.text !== visibleText)) {
        expect(screen.queryByText(m.text)).not.toBeInTheDocument();
      }
    });

    it('groups every kind in a domain together (system.info, system.warning, system.error)', () => {
      const system = [msg('info', 'system.info'), msg('warn', 'system.warning'), msg('err', 'system.error')];
      render(<GameInfoPanel messages={[...system, msg('hit', 'combat.hit')]} />);
      fireEvent.change(screen.getByRole('combobox'), { target: { value: 'system' } });
      for (const text of ['info', 'warn', 'err']) expect(screen.getByText(text)).toBeInTheDocument();
      expect(screen.queryByText('hit')).not.toBeInTheDocument();
    });

    it('Clear Filters resets the dropdown to All', () => {
      render(<GameInfoPanel messages={everyDomain} />);
      fireEvent.change(screen.getByRole('combobox'), { target: { value: 'combat' } });
      fireEvent.click(screen.getByRole('button', { name: /clear filters/i }));
      expect(screen.getByRole('combobox')).toHaveValue('all');
      expect(screen.getByText('room line')).toBeInTheDocument();
    });
  });

  it('should filter messages by search query', () => {
    render(<GameInfoPanel messages={mockMessages} />);

    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'System' } });

    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.queryByText('Combat message')).not.toBeInTheDocument();
  });

  it('should show combat header affordances when inCombat is true', () => {
    render(<GameInfoPanel messages={mockMessages} inCombat />);
    expect(screen.getByTestId('game-info-combat-indicator')).toBeInTheDocument();
    expect(screen.getByTestId('game-info-combat-label')).toHaveTextContent('In combat');
  });

  it('should show local and say chat in Game Info for multiplayer E2E', () => {
    const chatMessages = [
      msg('ArkanWolfshade (local): Hello', 'chat.local', { channel: 'local' }),
      msg('ArkanWolfshade says: Hi', 'chat.say', { channel: 'say' }),
      msg('Party line', 'chat.party', { channel: 'party' }),
      msg('Global channel line', 'chat.global', { channel: 'global' }),
      msg('Whisper line', 'chat.whisper', { channel: 'whisper' }),
    ];
    render(<GameInfoPanel messages={chatMessages} />);
    expect(screen.getByText('ArkanWolfshade (local): Hello')).toBeInTheDocument();
    expect(screen.getByText('ArkanWolfshade says: Hi')).toBeInTheDocument();
    expect(screen.getByText('Party line')).toBeInTheDocument();
    expect(screen.queryByText('Global channel line')).not.toBeInTheDocument();
    expect(screen.queryByText('Whisper line')).not.toBeInTheDocument();
  });
});
