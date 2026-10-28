/**
 * Segmented lines in the panels (#1025): NPC names get colour and weight only, the words never change, and
 * corruption decay wins over highlighting.
 */
import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ThemeProvider } from '../../../../contexts/ThemeContext';
import { SegmentedText } from '../../components/SegmentedText';
import type { ChatMessage } from '../../types';
import { ChatHistoryPanel } from '../ChatHistoryPanel';
import { GameInfoPanel } from '../GameInfoPanel';

const TEXT = 'you strike the pale Wretch hard now';
const SEGMENTS: NonNullable<ChatMessage['segments']> = [
  { text: 'you strike the pale ' },
  { text: 'Wretch', category: 'npc.aggressive_mob' },
  { text: ' hard now' },
];

const line = (timestamp: string, extra: Partial<ChatMessage> = {}): ChatMessage => ({
  text: TEXT,
  timestamp,
  isHtml: false,
  category: 'chat.say',
  channel: 'say',
  segments: SEGMENTS,
  ...extra,
});

describe('SegmentedText', () => {
  it('styles an npc span by disposition and renders the rest as bare text', () => {
    const { container } = render(<SegmentedText segments={SEGMENTS} />);
    expect(container.textContent).toBe(TEXT);
    const span = screen.getByText('Wretch');
    expect(span).toHaveClass('seg', 'seg-npc-aggressive_mob');
    expect(container.querySelectorAll('span')).toHaveLength(1);
  });

  it('puts no glyph/label class and no aria on a name: that belongs to the line, not every name', () => {
    render(<SegmentedText segments={SEGMENTS} />);
    const span = screen.getByText('Wretch');
    expect(span.className).not.toMatch(/\bcat\b/);
    expect(span.getAttributeNames()).toEqual(['class']);
  });

  it('renders a non-npc category as plain text rather than inventing a style', () => {
    const { container } = render(<SegmentedText segments={[{ text: 'hello', category: 'chat.say' }]} />);
    expect(container.querySelector('span')).toBeNull();
    expect(container.textContent).toBe('hello');
  });
});

describe('GameInfoPanel with segments', () => {
  it('colours the name and keeps the full line in data-message-text and search', () => {
    const message = line(new Date().toISOString(), { category: 'combat.hit' });
    const { container } = render(<GameInfoPanel messages={[message]} />);
    expect(screen.getByText('Wretch')).toHaveClass('seg-npc-aggressive_mob');
    expect(container.querySelector('[data-message-text]')?.getAttribute('data-message-text')).toBe(TEXT);
  });

  it('renders an ordinary line exactly as before when it has no segments', () => {
    render(<GameInfoPanel messages={[line(new Date().toISOString(), { segments: undefined })]} />);
    expect(screen.getByText(TEXT)).toBeInTheDocument();
  });
});

describe('ChatHistoryPanel with segments and corruption decay', () => {
  const renderPanel = (message: ChatMessage, corruption: number) =>
    render(
      <ThemeProvider>
        <ChatHistoryPanel messages={[message]} onSendChatMessage={vi.fn()} isConnected={true} corruption={corruption} />
      </ThemeProvider>
    );

  it('shows the highlighted name while the line is untouched', () => {
    const { container } = renderPanel(line(new Date().toISOString()), 100);
    expect(container.textContent).toContain(TEXT);
    expect(screen.getByText('Wretch')).toHaveClass('seg-npc-aggressive_mob');
  });

  it('falls back to the decayed plain text once decay has rewritten the line (corruption eats the highlighting)', () => {
    const old = new Date(Date.now() - 60 * 60 * 1000).toISOString(); // past the 30-minute full-age bucket
    const { container } = renderPanel(line(old), 100);
    expect(container.textContent).not.toContain(TEXT);
    expect(container.querySelector('.seg')).toBeNull();
  });

  it('does not decay, and so keeps the highlight, with no corruption at all', () => {
    const old = new Date(Date.now() - 60 * 60 * 1000).toISOString();
    renderPanel(line(old), 0);
    expect(screen.getByText('Wretch')).toHaveClass('seg-npc-aggressive_mob');
  });
});
