import type { ChatPanelMessage } from './chatPanelRuntimeUtils';
import { buildChatExportHTML, buildChatExportPlainText, formatChatTimestampUtc } from './chatPanelRuntimeUtils';

export interface ChatExportPayload {
  content: string;
  filename: string;
  mimeType: string;
}

function chatMessageToExportJsonRecord(msg: ChatPanelMessage) {
  return {
    timestamp: msg.timestamp,
    text: msg.rawText ?? msg.text,
    channel: msg.channel,
    messageType: msg.messageType,
    tags: msg.tags,
  };
}

export function buildChatExportJSON(messagesToExport: ChatPanelMessage[]): string {
  return JSON.stringify(messagesToExport.map(chatMessageToExportJsonRecord), null, 2);
}

function buildChatExportCsvRow(msg: ChatPanelMessage): string {
  const text = (msg.rawText ?? msg.text).replace(/"/g, '""');
  return `"${formatChatTimestampUtc(msg.timestamp)}","${msg.channel || ''}","${msg.messageType || ''}","${text}"`;
}

export function buildChatExportCSV(messagesToExport: ChatPanelMessage[]): string {
  const headers = ['Timestamp', 'Channel', 'Type', 'Message'];
  const rows = messagesToExport.map(buildChatExportCsvRow);
  return [headers.map(h => `"${h}"`).join(','), ...rows].join('\n');
}

export function resolveChatExportPayload(
  exportFormat: string,
  messagesToExport: ChatPanelMessage[]
): ChatExportPayload {
  const dateSuffix = new Date().toISOString().split('T')[0];
  const baseName = `chat_export_${dateSuffix}`;
  switch (exportFormat) {
    case 'html':
      return {
        content: buildChatExportHTML(messagesToExport),
        filename: `${baseName}.html`,
        mimeType: 'text/html',
      };
    case 'json':
      return {
        content: buildChatExportJSON(messagesToExport),
        filename: `${baseName}.json`,
        mimeType: 'application/json',
      };
    case 'csv':
      return {
        content: buildChatExportCSV(messagesToExport),
        filename: `${baseName}.csv`,
        mimeType: 'text/csv',
      };
    default:
      return {
        content: buildChatExportPlainText(messagesToExport),
        filename: `${baseName}.txt`,
        mimeType: 'text/plain',
      };
  }
}
