/**
 * Pure helpers for ChatPanelRuntime: channel filtering, search narrowing, and export payloads.
 * Agent-readable: keep behavior aligned with ChatPanelRuntime display rules.
 */
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { extractChannelFromMessage } from '../../utils/messageTypeUtils';
import { getChatPanelMessageClass } from './chatPanelMessageClass';

export { getChatPanelMessageClass };

export interface ChatPanelMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  aliasChain?: Array<{ original: string; expanded: string; alias_name: string }>;
  rawText?: string;
  tags?: string[];
}

/**
 * Stable-enough row key for React lists without server message ids (append-heavy chat log).
 * Agent-readable: avoids index keys so new messages at the end do not reshuffle identity.
 */
export function chatPanelMessageRowKey(message: ChatPanelMessage): string {
  const body = message.rawText ?? message.text;
  const channel = message.channel ?? '';
  const mt = message.messageType ?? '';
  let h = 0;
  for (let i = 0; i < body.length; i += 1) {
    h = (Math.imul(31, h) + body.charCodeAt(i)) | 0;
  }
  const hash = (h >>> 0).toString(36);
  return `${message.timestamp}\x1f${channel}\x1f${mt}\x1f${body.length}\x1f${hash}`;
}

export { filterMessagesForChannelView } from './chatPanelChannelFilter';
export { computeUnreadChatCounts } from './chatPanelUnreadCounts';

export function formatChatTimestampUtc(timestamp: string): string {
  const date = new Date(timestamp);
  if (Number.isNaN(date.getTime())) {
    return timestamp;
  }
  return `${date.getUTCHours().toString().padStart(2, '0')}:${date.getUTCMinutes().toString().padStart(2, '0')}:${date.getUTCSeconds().toString().padStart(2, '0')}`;
}

export function filterHistoryEligibleMessages(messages: ChatPanelMessage[]): ChatPanelMessage[] {
  return messages.filter(message => message.messageType !== 'system');
}

export function applyChatSearchFilters(
  baseMessages: ChatPanelMessage[],
  searchQuery: string,
  searchFilterChannel: string,
  searchFilterType: string
): ChatPanelMessage[] {
  let result = baseMessages;
  if (searchQuery.trim()) {
    const query = searchQuery.toLowerCase();
    result = result.filter(message => (message.rawText ?? message.text).toLowerCase().includes(query));
  }
  if (searchFilterChannel !== 'all') {
    result = result.filter(message => {
      const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
      return messageChannel === searchFilterChannel;
    });
  }
  if (searchFilterType !== 'all') {
    result = result.filter(message => message.messageType === searchFilterType);
  }
  return result;
}

export function buildChatSearchMatchIndices(messages: ChatPanelMessage[], searchQuery: string): Set<number> {
  if (!searchQuery.trim()) return new Set<number>();
  const query = searchQuery.toLowerCase();
  const matches = new Set<number>();
  messages.forEach((message, index) => {
    if ((message.rawText ?? message.text).toLowerCase().includes(query)) {
      matches.add(index);
    }
  });
  return matches;
}

export function buildChatExportPlainText(messagesToExport: ChatPanelMessage[]): string {
  return messagesToExport
    .map(msg => `[${formatChatTimestampUtc(msg.timestamp)}] ${msg.rawText ?? msg.text}`)
    .join('\n');
}

function escapeHtmlForPlainExport(text: string): string {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function formatExportMessageInnerHtml(msg: ChatPanelMessage): string {
  if (msg.isHtml) {
    return msg.isCompleteHtml ? msg.text : ansiToHtmlWithBreaks(msg.text);
  }
  return escapeHtmlForPlainExport(msg.rawText ?? msg.text);
}

function buildChatExportHtmlMessageBlock(msg: ChatPanelMessage): string {
  const text = formatExportMessageInnerHtml(msg);
  const ts = formatChatTimestampUtc(msg.timestamp);
  const cls = getChatPanelMessageClass(msg);
  return `<div class="message" style="margin-bottom: 1em;"><div style="font-size: 0.8em; color: #888;">[${ts}]</div><div class="${cls}">${text}</div></div>`;
}

export function buildChatExportHTML(messagesToExport: ChatPanelMessage[]): string {
  const htmlMessages = messagesToExport.map(buildChatExportHtmlMessageBlock).join('\n');
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Chat Export</title><style>body { font-family: monospace; background: #1a1a1a; color: #e0e0e0; padding: 20px; } .message { padding: 10px; border-bottom: 1px solid #333; }</style></head><body><h1>Chat Export</h1>${htmlMessages}</body></html>`;
}

export function escapeForChatHighlight(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function buildChatSearchHighlightHtml(text: string, query: string): string {
  if (!query.trim()) return text;
  const MAX_QUERY_LENGTH = 100;
  const safeQuery = query.length > MAX_QUERY_LENGTH ? query.substring(0, MAX_QUERY_LENGTH) : query;
  const escapedText = escapeForChatHighlight(text);
  const escapedQuery = safeQuery.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // nosemgrep: javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
  const regex = new RegExp(`(${escapedQuery})`, 'gi');
  // nosemgrep: typescript.lang.security.audit.xss.xss
  return escapedText.replace(regex, '<mark class="bg-yellow-500 text-black font-semibold">$1</mark>');
}
