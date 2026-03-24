import { afterEach, describe, expect, it, vi } from 'vitest';
import { buildChatExportCSV, buildChatExportJSON, resolveChatExportPayload } from '../chatPanelExportFormat';
import {
  applyChatSearchFilters,
  buildChatExportHTML,
  buildChatExportPlainText,
  buildChatSearchHighlightHtml,
  buildChatSearchMatchIndices,
  computeUnreadChatCounts,
  escapeForChatHighlight,
  filterHistoryEligibleMessages,
  filterMessagesForChannelView,
  formatChatTimestampUtc,
  getChatPanelMessageClass,
} from '../chatPanelRuntimeUtils';

describe('chatPanelRuntimeUtils', () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  describe('formatChatTimestampUtc', () => {
    it('formats ISO timestamps as HH:MM:SS UTC', () => {
      expect(formatChatTimestampUtc('2024-01-01T10:05:07Z')).toBe('10:05:07');
    });

    it('returns original string when date is invalid', () => {
      expect(formatChatTimestampUtc('not-a-date')).toBe('not-a-date');
    });
  });

  describe('getChatPanelMessageClass', () => {
    it('uses messageType tailwind classes', () => {
      expect(getChatPanelMessageClass({ messageType: 'error' })).toContain('error');
    });

    it('honors hallucination tag', () => {
      expect(getChatPanelMessageClass({ tags: ['hallucination'] })).toContain('fuchsia');
    });
  });

  describe('filterMessagesForChannelView', () => {
    const base = [
      { text: 'hi', timestamp: 't', isHtml: false, messageType: 'chat' as const, channel: 'local' },
      { text: 'sys', timestamp: 't', isHtml: false, messageType: 'system' as const },
      { text: 'fight', timestamp: 't', isHtml: false, messageType: 'combat' as const },
      { text: 'log', timestamp: 't', isHtml: false, messageType: 'chat' as const, channel: 'game-log' },
    ];

    it('excludes system, combat, and game-log regardless of channel mode', () => {
      const out = filterMessagesForChannelView(base, 'all', true);
      expect(out).toHaveLength(1);
      expect(out[0].text).toBe('hi');
    });

    it('shows only matching channel when not all', () => {
      const msgs = [
        {
          text: '[local] A says: x',
          timestamp: 't',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
        {
          text: '[whisper] B whispers: y',
          timestamp: 't',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'whisper',
        },
      ];
      const localOnly = filterMessagesForChannelView(msgs, 'local', false);
      expect(localOnly).toHaveLength(1);
      expect(localOnly[0].channel).toBe('local');
    });
  });

  describe('filterHistoryEligibleMessages', () => {
    it('drops system messages', () => {
      const msgs = [
        { text: 'a', timestamp: 't', isHtml: false, messageType: 'chat' },
        { text: 'b', timestamp: 't', isHtml: false, messageType: 'system' },
      ];
      expect(filterHistoryEligibleMessages(msgs)).toHaveLength(1);
    });
  });

  describe('applyChatSearchFilters', () => {
    const msgs = [
      { text: 'alpha bravo', timestamp: 't', isHtml: false, messageType: 'chat', channel: 'local', rawText: 'alpha' },
      { text: '[whisper] hide', timestamp: 't', isHtml: false, messageType: 'whisper', channel: 'whisper' },
    ];

    it('filters by substring on rawText or text', () => {
      const out = applyChatSearchFilters(msgs, 'alpha', 'all', 'all');
      expect(out).toHaveLength(1);
    });

    it('filters by channel and type', () => {
      const out = applyChatSearchFilters(msgs, '', 'whisper', 'whisper');
      expect(out).toHaveLength(1);
    });
  });

  describe('buildChatSearchMatchIndices', () => {
    it('returns empty set when query blank', () => {
      expect(buildChatSearchMatchIndices([{ text: 'a', timestamp: 't', isHtml: false }], '').size).toBe(0);
    });

    it('marks indices of matches', () => {
      const msgs = [
        { text: 'one', timestamp: 't', isHtml: false },
        { text: 'two', timestamp: 't', isHtml: false },
      ];
      const s = buildChatSearchMatchIndices(msgs, 'two');
      expect(s.has(1)).toBe(true);
    });
  });

  describe('export builders', () => {
    const msgs = [
      {
        text: 'line',
        rawText: 'raw',
        timestamp: '2024-06-01T12:00:00Z',
        isHtml: false,
        channel: 'local',
        messageType: 'chat',
      },
    ];

    it('buildChatExportPlainText uses rawText when present', () => {
      expect(buildChatExportPlainText(msgs)).toContain('raw');
    });

    it('buildChatExportJSON is valid JSON array', () => {
      const parsed = JSON.parse(buildChatExportJSON(msgs)) as unknown[];
      expect(Array.isArray(parsed)).toBe(true);
      expect((parsed[0] as { text: string }).text).toBe('raw');
    });

    it('buildChatExportCSV escapes quotes in message body', () => {
      const row = buildChatExportCSV([
        {
          text: 'say "hi"',
          timestamp: '2024-06-01T12:00:00Z',
          isHtml: false,
          channel: 'say',
          messageType: 'chat',
        },
      ]);
      expect(row).toContain('""');
    });

    it('buildChatExportHTML escapes plain text angle brackets', () => {
      const html = buildChatExportHTML([
        {
          text: '<script>x</script>',
          timestamp: '2024-06-01T12:00:00Z',
          isHtml: false,
        },
      ]);
      expect(html).toContain('&lt;script&gt;');
      expect(html).not.toContain('<script>');
    });
  });

  describe('escapeForChatHighlight and buildChatSearchHighlightHtml', () => {
    it('escapeForChatHighlight encodes HTML metacharacters', () => {
      expect(escapeForChatHighlight(`<&>"'`)).toBe('&lt;&amp;&gt;&quot;&#39;');
    });

    it('buildChatSearchHighlightHtml wraps matches in mark', () => {
      const html = buildChatSearchHighlightHtml('hello world', 'world');
      expect(html).toContain('<mark');
      expect(html).toContain('world');
    });

    it('escapes regex metacharacters in user query (no thrown RegExp)', () => {
      expect(() => buildChatSearchHighlightHtml('price $10', '$')).not.toThrow();
    });
  });

  describe('computeUnreadChatCounts', () => {
    it('returns empty when all-channel view', () => {
      const msgs = [{ text: 'a', timestamp: 't', isHtml: false, messageType: 'chat' as const, channel: 'local' }];
      expect(computeUnreadChatCounts(msgs, 'local', {}, true)).toEqual({});
    });

    it('counts unread per channel when not on all', () => {
      const msgs = [
        { text: '[local] x', timestamp: 't', isHtml: false, messageType: 'chat' as const, channel: 'local' },
        { text: '[whisper] y', timestamp: 't', isHtml: false, messageType: 'chat' as const, channel: 'whisper' },
      ];
      const counts = computeUnreadChatCounts(msgs, 'local', {}, false);
      expect(counts.whisper).toBe(1);
    });
  });

  describe('resolveChatExportPayload', () => {
    const one = [{ text: 'hi', timestamp: '2024-01-01T00:00:00Z', isHtml: false, messageType: 'chat' }];

    it('selects txt by default', () => {
      const p = resolveChatExportPayload('txt', one);
      expect(p.mimeType).toBe('text/plain');
      expect(p.filename.endsWith('.txt')).toBe(true);
      expect(p.content).toContain('hi');
    });

    it('selects json when requested', () => {
      const p = resolveChatExportPayload('json', one);
      expect(p.mimeType).toBe('application/json');
      expect(JSON.parse(p.content)).toHaveLength(1);
    });
  });
});
